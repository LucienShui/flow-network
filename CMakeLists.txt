cmake_minimum_required(VERSION 3.17)
project(flow-network)

set(CMAKE_CXX_STANDARD 14)

add_executable(flow-network flow_network/core/minimum_cost_flow.cpp flow_network/core/minimum_cost_flow.h main.cpp flow_network/core/graph.cpp flow_network/core/graph.h flow_network/core/maximum_flow.cpp flow_network/core/maximum_flow.h flow_network/core/common.h flow_network/core/base_network.h flow_network/core/base_network.cpp)
