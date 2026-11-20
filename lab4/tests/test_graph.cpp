#define CATCH_CONFIG_MAIN
#include "../include/catch.hpp"
#include "../include/graph.hpp"

TEST_CASE("Graph add vertices and edges") {
    Graph<int> g;
    g.add_vertex(1);
    g.add_vertex(2);
    g.add_edge(1, 2);
    
    REQUIRE(g.vertex_count() == 2);
    REQUIRE(g.get_edge_count() == 1);
    REQUIRE(g.has_vertex(1) == true);
    REQUIRE(g.has_edge(1, 2) == true);
}

TEST_CASE("Graph iterators") {
    Graph<int> g;
    g.add_edge(1, 2);
    g.add_edge(2, 3);

    std::vector<int> vertices;
    for (auto it = g.begin_vertices(); it != g.end_vertices(); ++it) {
        vertices.push_back(*it);
    }
    REQUIRE(vertices.size() == 3);

    std::vector<int> neighbors;
    for (auto it = g.begin_adjacent(2); it != g.end_adjacent(2); ++it) {
        neighbors.push_back(*it);
    }
    REQUIRE(neighbors.size() == 2);
}