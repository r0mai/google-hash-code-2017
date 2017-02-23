#include <iostream>
#include <vector>
#include <unordered_map>

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

int main() {
    Data data = parse();
}
