cmake_minimum_required(VERSION 3.1)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(hashcode
    src/main.cpp
)

set_property(TARGET hashcode PROPERTY CXX_STANDARD 14)
