#include <iostream>
#include <vector>
#include <string>

void sumab() {
    int it;
    std::cin >> it;

    std::vector<int> results;

    for (int i = 0; i < it; ++i) {
        std::string n;
        std::cin >> n;

        int a = n[0] - '0';  // Convert first character to integer
        int b = n[1] - '0';  // Convert second character to integer

        results.push_back(a + b);
    }

    for (int r : results) {
        std::cout << r << std::endl;
    }
}

int main() {
    sumab();
    return 0;
}