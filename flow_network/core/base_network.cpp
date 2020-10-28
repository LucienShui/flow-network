#include "base_network.h"

namespace flow_network {
    BaseNetwork::BaseNetwork(int n) : n(n), dist(new int[n]), graph(n) {}

    BaseNetwork::~BaseNetwork() {
    }
}

