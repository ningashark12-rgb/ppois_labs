#include "../include/graph.hpp"
#include <iostream>

void print_graph_info(Graph<int>& g) {
    std::cout << "\n--- Graph Information ---" << std::endl;
    std::cout << "Vertices: " << g.vertex_count() << std::endl;
    std::cout << "Edges: " << g.get_edge_count() << std::endl;
    
    std::cout << "\nVertices: ";
    for (auto it = g.begin_vertices(); it != g.end_vertices(); ++it) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Edges: ";
    for (auto it = g.begin_edges(); it != g.end_edges(); ++it) {
        auto edge = *it;
        std::cout << "(" << edge.first << "," << edge.second << ") ";
    }
    std::cout << std::endl;
}

int main() {
    Graph<int> g;
    
    // Add some sample vertices and edges
    g.add_vertex(1);
    g.add_vertex(2);
    g.add_vertex(3);
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    
    int choice;
    do {
        std::cout << "\n=== Task 2: Undirected Graph ===" << std::endl;
        std::cout << "1. Show Graph Info" << std::endl;
        std::cout << "2. Add Vertex" << std::endl;
        std::cout << "3. Add Edge" << std::endl;
        std::cout << "4. Check Adjacent Vertices of a Vertex" << std::endl;
        std::cout << "5. Vertex Degree" << std::endl;
        std::cout << "0. Exit" << std::endl;
        std::cout << "Choose: ";
        std::cin >> choice;
        
        if (choice == 1) {
            print_graph_info(g);
        } else if (choice == 2) {
            int v; std::cout << "Vertex ID: "; std::cin >> v;
            g.add_vertex(v);
            std::cout << "Vertex " << v << " added." << std::endl;
        } else if (choice == 3) {
            int u, v;
            std::cout << "Vertex U: "; std::cin >> u;
            std::cout << "Vertex V: "; std::cin >> v;
            g.add_edge(u, v);
            std::cout << "Edge (" << u << "," << v << ") added." << std::endl;
        } else if (choice == 4) {
            int v; std::cout << "Vertex ID: "; std::cin >> v;
            if (!g.has_vertex(v)) {
                std::cout << "Vertex not found." << std::endl;
                continue;
            }
            std::cout << "Neighbors of " << v << ": ";
            for (auto it = g.begin_adjacent(v); it != g.end_adjacent(v); ++it) {
                std::cout << *it << " ";
            }
            std::cout << std::endl;
        } else if (choice == 5) {
            int v; std::cout << "Vertex ID: "; std::cin >> v;
            try {
                std::cout << "Degree of " << v << ": " << g.degree(v) << std::endl;
            } catch (const std::exception& e) {
                std::cout << e.what() << std::endl;
            }
        } else if (choice == 0) {
            std::cout << "Goodbye!" << std::endl;
        } else {
            std::cout << "Invalid choice." << std::endl;
        }
    } while (choice != 0);
    
    return 0;
}