#define CATCH_CONFIG_MAIN
#include "../include/catch.hpp"
#include "../include/sorting.hpp"
#include "../include/graph.hpp"

// --- Sorting Tests ---
TEST_CASE("Bubble sort integers") {
    std::vector<int> v = {3, 1, 2};
    bubble_sort(v);
    REQUIRE(v == std::vector<int>{1, 2, 3});
}

TEST_CASE("Patience sort integers") {
    std::vector<int> v = {5, 3, 8, 1};
    patience_sort(v);
    REQUIRE(v == std::vector<int>{1, 3, 5, 8});
}

// --- Custom class for testing ---
class Person {
public:
    std::string name;
    int age;
    Person(std::string n, int a) : name(n), age(a) {}
    bool operator<(const Person& other) const { return age < other.age; }
    bool operator>(const Person& other) const { return age > other.age; }
};

TEST_CASE("Bubble sort custom objects") {
    std::vector<Person> people = {Person("Alice", 30), Person("Bob", 25)};
    bubble_sort(people);
    REQUIRE(people[0].name == "Bob");
}

// --- Graph Tests ---
TEST_CASE("Graph add vertices and edges") {
    Graph<int> g;
    g.add_vertex(1);
    g.add_vertex(2);
    g.add_edge(1, 2);
    
    REQUIRE(g.vertex_count() == 2);
    REQUIRE(g.get_edge_count() == 1);
    REQUIRE(g.has_vertex(1) == true);
}
TEST_CASE("Bubble sort C-style array") {
    int arr[] = {3, 1, 2};
    bubble_sort(arr, 3);
    REQUIRE(arr[0] == 1);
    REQUIRE(arr[1] == 2);
    REQUIRE(arr[2] == 3);
}

TEST_CASE("Comparison with std::sort") {
    std::vector<int> v1 = {5, 2, 8, 1};
    std::vector<int> v2 = {5, 2, 8, 1};
    
    bubble_sort(v1);
    std::sort(v2.begin(), v2.end());
    
    REQUIRE(v1 == v2); // Bubble sort produces the same result
}