#include "base_network.h"

namespace flow_network {
    BaseNetwork::BaseNetwork(int n) : dist(new int[n]), n(n), graph(n) {}
}

