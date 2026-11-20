#pragma once
#include <vector>
#include <map>
#include <stdexcept>
#include <iostream>

template <typename T>
class Graph {
private:
    std::map<T, std::map<T, bool>> adj_matrix;
    int edge_count;

public:
    Graph() : edge_count(0) {}

    // --- Core Graph Methods ---
    bool has_vertex(const T& v) const {
        return adj_matrix.find(v) != adj_matrix.end();
    }

    bool has_edge(const T& u, const T& v) const {
        if (!has_vertex(u) || !has_vertex(v)) return false;
        return adj_matrix.at(u).at(v);
    }

    void add_vertex(const T& v) {
        if (!has_vertex(v)) {
            adj_matrix[v] = std::map<T, bool>();
            for (auto& pair : adj_matrix) {
                pair.second[v] = false;
            }
        }
    }

    void add_edge(const T& u, const T& v) {
        if (!has_vertex(u)) add_vertex(u);
        if (!has_vertex(v)) add_vertex(v);
        
        if (!adj_matrix[u][v]) {
            adj_matrix[u][v] = true;
            adj_matrix[v][u] = true;
            edge_count++;
        }
    }

    void remove_edge(const T& u, const T& v) {
        if (has_edge(u, v)) {
            adj_matrix[u][v] = false;
            adj_matrix[v][u] = false;
            edge_count--;
        }
    }

    void remove_vertex(const T& v) {
        if (!has_vertex(v)) return;
        
        for (auto& pair : adj_matrix) {
            if (pair.second[v]) edge_count--;
        }
        
        adj_matrix.erase(v);
        for (auto& pair : adj_matrix) {
            pair.second.erase(v);
        }
    }

    int vertex_count() const {
        return adj_matrix.size();
    }

    int get_edge_count() const {
        return edge_count;
    }

    int degree(const T& v) const {
        if (!has_vertex(v)) throw std::invalid_argument("Vertex not found");
        int count = 0;
        for (const auto& pair : adj_matrix.at(v)) {
            if (pair.second) count++;
        }
        return count;
    }

    int edge_degree(const T& u, const T& v) const {
        if (!has_edge(u, v)) throw std::invalid_argument("Edge not found");
        return 2;
    }

    std::vector<std::pair<T, T>> get_all_edges() const {
        std::vector<std::pair<T, T>> unique_edges;
        for (auto it = adj_matrix.begin(); it != adj_matrix.end(); ++it) {
            for (auto inner = it->second.begin(); inner != it->second.end(); ++inner) {
                if (inner->second && it->first < inner->first) {
                    unique_edges.push_back({it->first, inner->first});
                }
            }
        }
        return unique_edges;
    }

    // --- Vertex Iterator ---
    class VertexIterator {
    private:
        typename std::map<T, std::map<T, bool>>::iterator it;
    public:
        VertexIterator(typename std::map<T, std::map<T, bool>>::iterator i) : it(i) {}
        const T& operator*() const { return it->first; }
        VertexIterator& operator++() { ++it; return *this; }
        bool operator!=(const VertexIterator& other) const { return it != other.it; }
        bool operator==(const VertexIterator& other) const { return it == other.it; }
    };

    VertexIterator begin_vertices() { return VertexIterator(adj_matrix.begin()); }
    VertexIterator end_vertices() { return VertexIterator(adj_matrix.end()); }

    // --- Adjacent Vertex Iterator ---
    class AdjacentVertexIterator {
    private:
        typename std::map<T, bool>::iterator it;
        typename std::map<T, bool>::iterator end;
    public:
        AdjacentVertexIterator(typename std::map<T, bool>::iterator i, typename std::map<T, bool>::iterator e) : it(i), end(e) {}
        const T& operator*() const { return it->first; }
        AdjacentVertexIterator& operator++() {
            ++it;
            while (it != end && !it->second) ++it;
            return *this;
        }
        bool operator!=(const AdjacentVertexIterator& other) const { return it != other.it; }
        bool operator==(const AdjacentVertexIterator& other) const { return it == other.it; }
    };

    AdjacentVertexIterator begin_adjacent(const T& v) {
        if (!has_vertex(v)) throw std::invalid_argument("Vertex not found");
        auto it = adj_matrix.at(v).begin();
        while (it != adj_matrix.at(v).end() && !it->second) ++it;
        return AdjacentVertexIterator(it, adj_matrix.at(v).end());
    }

    AdjacentVertexIterator end_adjacent(const T& v) {
        if (!has_vertex(v)) throw std::invalid_argument("Vertex not found");
        return AdjacentVertexIterator(adj_matrix.at(v).end(), adj_matrix.at(v).end());
    }

    // --- Edge Iterator (Bulletproof Version) ---
    class EdgeIterator {
    private:
        Graph<T>* graph;
        size_t index;
    public:
        EdgeIterator(Graph<T>* g, size_t i) : graph(g), index(i) {}

        std::pair<T, T> operator*() const {
            auto edges = graph->get_all_edges();
            return edges[index];
        }

        EdgeIterator& operator++() {
            ++index;
            return *this;
        }

        bool operator!=(const EdgeIterator& other) const { return index != other.index; }
        bool operator==(const EdgeIterator& other) const { return index == other.index; }
    };

    EdgeIterator begin_edges() { return EdgeIterator(this, 0); }
    EdgeIterator end_edges() { return EdgeIterator(this, get_all_edges().size()); }
};