//
// Created by 水清源 on 2020/10/5.
//

#ifndef NETWORK_FLOWS_PYTHON_FLOW_NETWORK_H
#define NETWORK_FLOWS_PYTHON_FLOW_NETWORK_H

#include "flow-network.h"

extern "C" {

void delete_ptr(void *ptr);

void *flow_network_new(int n);

void flow_network_add_edge(void *raw_flow_network, int u, int v, int flow);

void flow_network_run(void *raw_flow_network, int S, int T, int *result);

void *minimum_cost_flow_new(int n);

void minimum_cost_flow_add_edge(void *raw_minimum_cost_flow, int u, int v, int flow, int cost);

void minimum_cost_flow_run(void *raw_minimum_cost_flow, int S, int T, int *result);

}

#endif //NETWORK_FLOWS_PYTHON_FLOW_NETWORK_H
