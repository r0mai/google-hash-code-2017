#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>

#include <boost/container/flat_map.hpp>

struct EndPoint {
    int data_center_latency;
    std::unordered_map<int, int> latencies; // end_point index -> latency in ms
};

struct Request {
    int end_point;
    int count; // request count
    int video_index;
};

struct Data {
    std::vector<int> video_sizes;
    std::vector<EndPoint> end_points;
    std::vector<Request> requests;
    int cache_server_count;
    int cache_size; // in MB
};

struct Result {
    std::vector<std::vector<int>> videos_in_cache;
};

struct Edge {
    int video_index;
    int cache_index;
    bool operator<(const Edge& rhs) const {
        return std::tie(video_index, cache_index) <
               std::tie(rhs.video_index, rhs.cache_index);
    }
    bool operator==(const Edge& rhs) const {
        return std::tie(video_index, cache_index) ==
               std::tie(rhs.video_index, rhs.cache_index);
    }
};

namespace std {
template<>
struct hash<Edge> {
    std::size_t operator()(const Edge& edge) const {
        return edge.video_index*1000000 + edge.cache_index;
    }
};
}


Data parse() {
    Data data;

    int video_count;
    int endpoint_count;
    int request_count;

    std::cin >> video_count >> endpoint_count >>
        request_count >> data.cache_server_count >>
        data.cache_size;

    data.video_sizes.resize(video_count);
    for (int i = 0; i < video_count; ++i) {
        std::cin >> data.video_sizes[i];
    }

    data.end_points.resize(endpoint_count);
    for (int i = 0; i < endpoint_count; ++i) {
        int connection_count;
        std::cin >> data.end_points[i].data_center_latency >> connection_count;
        for (int j = 0; j < connection_count; ++j) {
            int cache_index;
            int latency;
            std::cin >> cache_index >> latency;
            data.end_points[i].latencies[cache_index] = latency;
        }
    }

    data.requests.resize(request_count);
    for (int i = 0; i < request_count; ++i) {
        std::cin >> data.requests[i].video_index >>
            data.requests[i].end_point >>
            data.requests[i].count;
    }

    return data;
}

void output(const Result& result) {
    std::cout << result.videos_in_cache.size() << '\n';
    for (int i = 0; i < int(result.videos_in_cache.size()); ++i) {
        std::cout << i << ' ';
        for (int j = 0; j < int(result.videos_in_cache[i].size()); ++j) {
            std::cout << result.videos_in_cache[i][j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << std::flush;
}

struct Weight {
    int value = 0;
    std::vector<int> requests;
};

template<typename K, typename V>
using Map = std::unordered_map<K, V>;

Map<Edge, Weight> generateEdges(const Data& data) {
    Map<Edge, Weight> result;

    size_t count = 0;
    for (const auto& req : data.requests) {
        const auto& end_point = data.end_points[req.end_point];
        count += end_point.latencies.size();
    }
    std::cout << count << std::endl;

    std::size_t iterations = 0;
    std::cerr << "iterations to go: " << count << std::endl;
    std::cerr << "requests: " << data.requests.size() << std::endl;

    for (const auto& req : data.requests) {
        auto index = &req - &data.requests[0];
        ++iterations;
        const auto& end_point = data.end_points[req.end_point];

        if (iterations % 1000 == 0) {
            std::cerr << iterations << std::endl;
        }

        for (const auto& lt : end_point.latencies) {
            Edge edge;
            edge.video_index = req.video_index;
            edge.cache_index = lt.first;

            auto delta = (end_point.data_center_latency - lt.second);
            Weight& weight = result[edge];
            weight.value += req.count * delta;
            weight.requests.push_back(index);
        }
    }
    return result;
}

std::vector<std::pair<Edge, Weight>> sortEdges(
        const Map<Edge, Weight>& edges,
        const Data& data) {
    std::vector<std::pair<Edge, Weight>> result;
    result.reserve(edges.size());
    for (const auto& edge : edges) {
        result.push_back(std::pair<Edge, Weight>{edge.first, edge.second});
    }

    auto getWeight = [&data](const auto& e) {
        const auto& size = data.video_sizes[e.first.video_index];
        return static_cast<int>(
                std::round(e.second.value / static_cast<double>(size)));
    };

    auto comparator = [&getWeight](const auto& l, const auto& r) {
        return getWeight(l) > getWeight(r);
    };
    std::sort(result.begin(), result.end(), comparator);
    return result;
}


void insert_video_if_can_and_isnt_in_already(const Data& data, Result& result,
        int video,
        int cache) {
    auto& cache_vec = result.videos_in_cache[cache];
    auto it = std::find(cache_vec.begin(), cache_vec.end(), video);
    if (it != cache_vec.end()) {
        return;
    }
    int used = std::accumulate(cache_vec.begin(), cache_vec.end(), 0,
            [&data](int total, int video) {
                return total + data.video_sizes[video];
            });
    int remaining = data.cache_size - used;
    // TODO: Can we always fully pack a cache?
    if (data.video_sizes[video] <= remaining) {
        cache_vec.push_back(video);
    }
}

Result getResult(const Data& data) {
    const auto& edges = generateEdges(data);
    std::cerr << "After generate" << std::endl;
    const auto& sortedEdges = sortEdges(edges, data);

    Result result;
    result.videos_in_cache.resize(data.cache_server_count);
    for (const auto& edge : sortedEdges) {
        const auto& video = edge.first.video_index;
        const auto& cache = edge.first.cache_index;
        insert_video_if_can_and_isnt_in_already(data, result, video, cache);
    }

    return result;
    ;
}

int main() {
    Data data = parse();
    output(getResult(data));
}
