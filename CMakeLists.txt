cmake_minimum_required(VERSION 3.17)
project(flow_network)

set(CMAKE_CXX_STANDARD 14)

add_library(network_flows SHARED flow_network/core/flow-network.cpp flow_network/core/flow-network.h flow_network/core/py-api.h flow_network/core/py-api.cpp)
