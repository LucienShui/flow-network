//
// Created by 水清源 on 2020/10/5.
//

#include "pyapi.h"
#include <new>

extern "C" {

void delete_flow_network_ptr(void *raw_flow_network) {
    auto *flow_network = reinterpret_cast<flow_network::FlowNetwork *>(raw_flow_network);
#ifndef NDEBUG
    printf("get ptr = %p, ready to delete\n", flow_network);
#endif
    delete flow_network;
}

void delete_minimum_cost_flow_ptr(void *raw_minimum_cost_flow) {
    auto minimum_cost_flow = reinterpret_cast<flow_network::MinimumCostFlow *>(raw_minimum_cost_flow);
#ifndef NDEBUG
    printf("get ptr = %p, ready to delete\n", minimum_cost_flow);
#endif
    delete minimum_cost_flow;
}

void *flow_network_new(int n) {
    auto *flow_network_ptr = new flow_network::FlowNetwork(n);
#ifndef NDEBUG
    printf("create ptr = %p, n = %d\n", flow_network_ptr, n);
#endif
    return flow_network_ptr;
}

void flow_network_add_edge(void *raw_flow_network, int u, int v, int flow) {
    auto *flow_network = reinterpret_cast<flow_network::FlowNetwork *>(raw_flow_network);
#ifndef NDEBUG
    printf("get ptr = %p, u = %d, v = %d, flow = %d\n", flow_network, u, v, flow);
#endif
    flow_network->graph.add_edge(u, v, flow);
}

void flow_network_run(void *raw_flow_network, int S, int T, int *result, int *edge_flows) {
    auto *flow_network = reinterpret_cast<flow_network::FlowNetwork *>(raw_flow_network);
#ifndef NDEBUG
    printf("get ptr = %p, S = %d, T = %d\n", flow_network, S, T);
#endif
    result[0] = flow_network->run(S, T);

    int edge_number = flow_network->graph.edge.size();
    for (int i = 0; i < edge_number; i++) {
        edge_flows[i] = flow_network->graph.edge[i].flow;
    }
}

void *minimum_cost_flow_new(int n) {
    auto *flow_network_ptr = new flow_network::MinimumCostFlow(n);
#ifndef NDEBUG
    printf("create ptr = %p, n = %d\n", flow_network_ptr, n);
#endif
    return flow_network_ptr;
}

void minimum_cost_flow_add_edge(void *raw_minimum_cost_flow, int u, int v, int flow, int cost) {
    auto minimum_cost_flow = reinterpret_cast<flow_network::MinimumCostFlow *>(raw_minimum_cost_flow);
#ifndef NDEBUG
    printf("get ptr = %p, u = %d, v = %d, flow = %d, cost = %d\n", minimum_cost_flow, u, v, flow, cost);
#endif
    minimum_cost_flow->graph.add_edge(u, v, flow, cost);
}

void minimum_cost_flow_run(void *raw_minimum_cost_flow, int S, int T, int *result, int *edge_flows) {
    auto minimum_cost_flow = reinterpret_cast<flow_network::MinimumCostFlow *>(raw_minimum_cost_flow);
#ifndef NDEBUG
    printf("get ptr = %p, S = %d, T = %d\n", minimum_cost_flow, S, T);
#endif
    std::pair<int, int> answer = minimum_cost_flow->run(S, T);
    result[0] = answer.first;
    result[1] = answer.second;

    int edge_number = minimum_cost_flow->graph.edge.size();
    for (int i = 0; i < edge_number; i++) {
        edge_flows[i] = minimum_cost_flow->graph.edge[i].flow;
    }
}

}