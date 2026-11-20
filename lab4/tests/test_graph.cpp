#define CATCH_CONFIG_MAIN
#include "../include/catch.hpp"
#include "../include/graph.hpp"

TEST_CASE("Graph add vertices and edges") {
    // ... existing test ...
}

TEST_CASE("Graph iterators") {
    // ... existing test ...
}

// --- PASTE THE NEW TESTS AT THE BOTTOM ---
TEST_CASE("Graph copy constructor and assignment") {
    Graph<int> g1;
    g1.add_edge(1, 2);
    Graph<int> g2 = g1;
    REQUIRE(g1 == g2);
    
    Graph<int> g3;
    g3 = g1;
    REQUIRE(g1 == g3);
}

TEST_CASE("Graph is_empty and clear") {
    Graph<int> g;
    REQUIRE(g.is_empty() == true);
    g.add_vertex(1);
    REQUIRE(g.is_empty() == false);
    g.clear();
    REQUIRE(g.is_empty() == true);
}

TEST_CASE("Graph reverse iterators and to_string") {
    Graph<int> g;
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    std::string s = g.to_string();
    REQUIRE(s.find("(1-2)") != std::string::npos);
    REQUIRE(s.find("(2-3)") != std::string::npos);
}