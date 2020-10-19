//
// Created by 水清源 on 2020/10/5.
//

#ifndef NETWORK_FLOWS_PYAPI_H
#define NETWORK_FLOWS_PYAPI_H

#include "flow-network.h"

extern "C" {

/**
 * 删除朴素网络流对象
 * @param ptr 对象指针
 */
void delete_flow_network_ptr(void *ptr);

/**
 * 删除费用流对象
 * @param ptr 对象指针
 */
void delete_minimum_cost_flow_ptr(void *ptr);

/**
 * 创建朴素网络流对象
 * @param n 网络中点的数量
 * @return void * 格式的对象指针
 */
void *flow_network_new(int n);

/**
 * 添加一条从 u 到 v 的边
 * @param raw_flow_network void * 格式的对象指针
 * @param u 点的下标
 * @param v 点的下标
 * @param flow 边的容量
 */
void flow_network_add_edge(void *raw_flow_network, int u, int v, int flow);

/**
 * 运行网络流算法
 * @param raw_flow_network void * 格式的对象指针
 * @param S 源点的下标
 * @param T 汇点的下标
 * @param result 算法结果，长度约定为 1，result[0] = 最大流
 * @param edge_flows 边的流量
 */
void flow_network_run(void *raw_flow_network, int S, int T, int *result, int *edge_flows);

/**
 * 创建费用流对象
 * @param n 网络中点的数量
 * @return void * 格式的对象指针
 */
void *minimum_cost_flow_new(int n, int m);

/**
 * 添加一条从 u 到 v 的边
 * @param raw_minimum_cost_flow void * 格式的对象指针
 * @param u 点的下标
 * @param v 点的下标
 * @param flow 边的容量
 * @param cost 单位流量的花费
 */
void minimum_cost_flow_add_edge(void *raw_minimum_cost_flow, int u, int v, int flow, int cost);

/**
 * 运行费用流算法
 * @param raw_minimum_cost_flow void * 格式的对象指针
 * @param S 源点的下标
 * @param T 汇点的下标
 * @param result 算法结果，长度约定为 2，result[0] = 最大流，result[1] = 费用
 * @param edge_flows 边的流量
 */
void minimum_cost_flow_run(void *raw_minimum_cost_flow, int S, int T, int *result, int *edge_flows);

}

#endif //NETWORK_FLOWS_PYAPI_H
