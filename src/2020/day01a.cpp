#include <chrono>
#include <iostream>
#include <string>
#include <vector>

void log(std::string msg) { std::cout << msg << std::endl; }

int main() {
    int n;
    std::vector<int> v;

    while (std::cin >> n) {
        log("n loaded as " + std::to_string(n));
        v.push_back(n);
    }

    auto startTime = std::chrono::high_resolution_clock::now();

    // Run algorithm

    auto finishTime = std::chrono::high_resolution_clock::now();
    double executionTime = std::chrono::duration_cast<std::chrono::nanoseconds>(
                               finishTime - startTime)
                               .count();
    std::cout << std::endl
              << "Execution time: " << executionTime << " ns" << std::endl;

    return 0;
}
