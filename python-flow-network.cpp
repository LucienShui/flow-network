//
// Created by 水清源 on 2020/10/5.
//

#include "python-flow-network.h"

extern "C" {

flow_network::FlowNetwork flow_network_new(int n) {
    return flow_network::FlowNetwork(n);
}

void flow_network_add_edge(flow_network::FlowNetwork *flow_network, int u, int v, int flow) {
    flow_network->graph.add_edge(u, v, flow);
}

void flow_network_run(flow_network::FlowNetwork *flow_network, int S, int T, int *result) {
    result[0] = flow_network->run(S, T);
}

flow_network::MinimumCostFlow minimum_cost_flow_new(int n) {
    return flow_network::MinimumCostFlow(n);
}

void minimum_cost_flow_add_edge(flow_network::MinimumCostFlow *minimum_cost_flow, int u, int v, int flow, int cost) {
    minimum_cost_flow->graph.add_edge(u, v, flow, cost);
}

void minimum_cost_flow_run(flow_network::MinimumCostFlow *minimum_cost_flow, int S, int T, int *result) {
    std::pair<int, int> answer = minimum_cost_flow->run(S, T);
    result[0] = answer.first;
    result[1] = answer.second;
}

}