library: flow-network.h python-flow-network.h
	g++ -shared -W \
	-o flow-network.so \
	-std=c++14 \
	-fPIC flow-network.cpp
