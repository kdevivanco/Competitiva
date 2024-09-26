// Se te dan tres dígitos  Dos de ellos son iguales, pero el tercero es diferente de los otros dos.

// Encuentra el valor que ocurre exactamente una vez.

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;


    // para cada numero leemos 3
    for (int i = 0; i < n; i++) {
        vector<int> input_nums(3);
        cin >> input_nums[0];
        cin >> input_nums[1];
        cin >> input_nums[2];

        

        sort(input_nums.begin(), input_nums.end());

        if(input_nums[1] == input_nums[0]){
            cout << input_nums[2] << endl;
        }
        else if(input_nums[1] == input_nums[2]){
            cout << input_nums[0] << endl;
        }
    }

}