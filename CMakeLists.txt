cmake_minimum_required(VERSION 3.17)
project(network_flows)

set(CMAKE_CXX_STANDARD 14)

add_executable(network_flows flow_network/core/flow-network.cpp flow_network/core/flow-network.h flow_network/core/pyapi.h flow_network/core/pyapi.cpp)
