library: flow-network.h python-flow-network.h
	g++ -shared -W \
	-o flow_network/lib/flow-network.so \
	-std=c++14 \
	-fPIC flow-network.cpp python-flow-network.cpp
