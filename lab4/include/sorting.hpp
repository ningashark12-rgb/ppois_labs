#pragma once
#include <vector>
#include <algorithm>

// Generic Bubble Sort
template <typename T>
void bubble_sort(std::vector<T>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// Generic Patience Sort (Simplified)
template <typename T>
void patience_sort(std::vector<T>& arr) {
    if (arr.empty()) return;
    
    std::vector<std::vector<T>> piles;
    for (const T& item : arr) {
        bool placed = false;
        for (auto& pile : piles) {
            if (item < pile.back()) {
                pile.push_back(item);
                placed = true;
                break;
            }
        }
        if (!placed) {
            piles.push_back({item});
        }
    }
    
    arr.clear();
    for (const auto& pile : piles) {
        for (const T& item : pile) {
            arr.push_back(item);
        }
    }
    bubble_sort(arr);
}
// Overload for C-style arrays
template <typename T>
void bubble_sort(T arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < size - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}