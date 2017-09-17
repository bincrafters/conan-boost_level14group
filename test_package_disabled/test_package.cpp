#include <vector>
#include <boost/bimap.hpp>
#include <boost/pending/disjoint_sets.hpp>
#include <boost/property_map/vector_property_map.hpp>
#include <boost/graph/undirected_graph.hpp>
#include <boost/graph/accounting.hpp>

int main()
{
	std::vector<int>  rank (100);
	std::vector<int>  parent (100);
	
	boost::disjoint_sets<int*,int*> ds(&rank[0], &parent[0]);
	boost::bimap<int, int> test;
	boost::vector_property_map<std::string> m;
	boost::undirected_graph<int> g;
	boost::graph::accounting::print_time(1000);
}


