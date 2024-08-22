#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> input_nums(n-1);
    
    // Leer los valores de entrada
    for (int i = 0; i < n-1; i++) {
        cin >> input_nums[i];
    }

    int missing_number = -1;

    // Buscar el número faltante usando un doble for
    for (int i = 1; i <= n; i++) {
        bool found = false;
        for (int j = 0; j < n-1; j++) {
            if (input_nums[j] == i) {
                found = true;
                break;
            }
        }
        if (!found) {
            missing_number = i;
            break;
        }
    }

    cout << missing_number << endl;

    return 0;
}
