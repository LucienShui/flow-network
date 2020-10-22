%module core

%include "std_vector.i"
%include "std_pair.i"

%{

#include "common.h"
#include "graph.h"
#include "base_network.h"
#include "maximum_flow.h"
#include "minimum_cost_flow.h"

%}

%template(EdgeVector) std::vector<flow_network::Edge>;
%template(IntVector) std::vector<int>;
%template(IntIntPair) std::pair<int, int>;

%include "common.h"
%include "graph.h"
%include "base_network.h"
%include "maximum_flow.h"
%include "minimum_cost_flow.h"
