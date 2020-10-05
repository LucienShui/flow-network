cmake_minimum_required(VERSION 3.17)
project(network_flows)

set(CMAKE_CXX_STANDARD 14)

add_library(network_flows SHARED flow-network.cpp flow-network.h python-flow-network.h)
