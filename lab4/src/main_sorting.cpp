#include "../include/sorting.hpp"
#include <iostream>
#include <string>
#include <vector>

class Person {
public:
    std::string name;
    int age;
    Person(std::string n, int a) : name(n), age(a) {}
    bool operator<(const Person& other) const { return age < other.age; }
    bool operator>(const Person& other) const { return age > other.age; }
    friend std::ostream& operator<<(std::ostream& os, const Person& p) {
        return os << p.name << "(" << p.age << ")";
    }
};

template <typename T>
void print_vector(const std::vector<T>& v) {
    for (const auto& item : v) {
        std::cout << item << " ";
    }
    std::cout << std::endl;
}

void demo_integers() {
    std::cout << "\n--- Sorting Integers ---" << std::endl;
    std::vector<int> v = {5, 2, 8, 1, 9, 3};
    
    std::cout << "Original: ";
    print_vector(v);
    
    bubble_sort(v);
    std::cout << "Bubble sorted: ";
    print_vector(v);
    
    v = {5, 2, 8, 1, 9, 3};
    patience_sort(v);
    std::cout << "Patience sorted: ";
    print_vector(v);
}

void demo_custom_objects() {
    std::cout << "\n--- Sorting Custom Objects (Person by age) ---" << std::endl;
    std::vector<Person> people = {
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("Dave", 20)
    };
    
    std::cout << "Original: ";
    print_vector(people);
    
    bubble_sort(people);
    std::cout << "Bubble sorted: ";
    print_vector(people);
    
    people = {
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 35),
        Person("Dave", 20)
    };
    patience_sort(people);
    std::cout << "Patience sorted: ";
    print_vector(people);
}

void demo_c_arrays() {
    std::cout << "\n--- Sorting C-Style Arrays ---" << std::endl;
    int arr[] = {5, 2, 8, 1, 9, 3};
    int size = 6;
    
    std::cout << "Original: ";
    for (int i = 0; i < size; ++i) std::cout << arr[i] << " ";
    std::cout << std::endl;
    
    bubble_sort(arr, size);
    std::cout << "Bubble sorted: ";
    for (int i = 0; i < size; ++i) std::cout << arr[i] << " ";
    std::cout << std::endl;
}

int main() {
    int choice;
    do {
        std::cout << "\n=== Task 1: Generic Sorting ===" << std::endl;
        std::cout << "1. Sort Integers" << std::endl;
        std::cout << "2. Sort Custom Objects (Person)" << std::endl;
        std::cout << "3. Sort C-Style Array" << std::endl;
        std::cout << "0. Exit" << std::endl;
        std::cout << "Choose: ";
        std::cin >> choice;
        
        switch (choice) {
            case 1: demo_integers(); break;
            case 2: demo_custom_objects(); break;
            case 3: demo_c_arrays(); break;
            case 0: std::cout << "Goodbye!" << std::endl; break;
            default: std::cout << "Invalid choice." << std::endl;
        }
    } while (choice != 0);
    
    return 0;
}