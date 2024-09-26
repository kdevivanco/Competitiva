#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
   
    vector<char> cola(N);
    ///read cola
    for (int i = 0; i < N; ++i) {
        cin >> cola[i];
    }

    int veces = 0;
    
    // while ocelote:
    while (true) {
        // ocelote mas abajo:
        int index = -1;
        for (int i = N-1; i >= 0; --i) {
            if (cola[i] == 'O') {
                index = i;
                break;
            }
        }
        
        if (index == -1) {
            break;
        }

        veces += (index + 1);
        cola[index] = 'Z';

        for (int i = index - 1; i >= 0; --i) {
            if (cola[i] == 'Z') {
                cola[i] = 'O';
            }
        }
    }
    veces = veces - 1; //jeje
    cout << veces << endl;
}
