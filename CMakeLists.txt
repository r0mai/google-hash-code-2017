cmake_minimum_required(VERSION 3.1)

add_executable(hashcode
    src/main.cpp
)

set_property(TARGET hashcode PROPERTY CXX_STANDARD 14)
