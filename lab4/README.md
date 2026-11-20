# Lab 4: Generic Programming - Sorting and Graphs

## Task 1: Sorting Algorithms
- **Bubble Sort:** A generic `template <typename T>` function that sorts `std::vector` and C-style arrays.
- **Patience Sort:** A generic algorithm using piles.
- **Demonstration:** Sorts both built-in types (`int`) and custom objects (`Person`).

## Task 2: Undirected Graph (Adjacency Matrix)
- **Generic Container:** `Graph<T>` uses a `std::map<T, std::map<T, bool>>` for the adjacency matrix.
- **Core Methods:** `add_vertex`, `add_edge`, `remove_vertex`, `remove_edge`, `has_vertex`, `has_edge`, `vertex_count`, `get_edge_count`, `degree`.
- **Iterators:** Custom iterators for vertices, edges, and adjacent vertices.

## How to Build and Run
```bash
g++ src/main_sorting.cpp -o task1.exe -I include
g++ src/main_graph.cpp -o task2.exe -I include
./task1.exe
./task2.exe