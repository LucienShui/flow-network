cmake_minimum_required(VERSION 3.17)
project(network_flows)

set(CMAKE_CXX_STANDARD 14)

add_executable(network_flows flow-network.cpp flow-network.h python-flow-network.h python-flow-network.cpp)
