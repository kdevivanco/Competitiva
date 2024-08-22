#include <iostream>
#include <vector>
#include <string>

void cardgame() {
    int it;
    std::cin >> it;
    std::vector<int> cards;
    std::vector<int> results;

    for (int i = 0; i < it; ++i) {
        for (int j = 0 ; j < 4 ; i++){
            std::cin >> n;
            cards.push_back(n);
        }
        int a1 = cards[0]
        int a2 = cards[1]
        int b1 = cards[2]
        int b2 = cards[3]
        // todas mayores:
        if(a1 > b1 && a1 > b2 && a2 > b1  && a2 > b2 ){
            int ways = 4 
        }
        // two cards greater than 
        if((a1 > b1 && a2 > b2) || (a2>b1 && a1 > b1)) {
            int ways = 2
        }
        
        

    }

    for (int r : results) {
        std::cout << r << std::endl;
    }
}

int main() {
    sumab();
    return 0;
}