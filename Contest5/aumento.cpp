// def get_subsequence(a, dp):
//     n = len(a)
//     max_length = max(dp)
//     index = dp.index(max_length)
    
//     elemnt = [i for i in range(n) if dp[i] == max_length]


//     index = elemnt[0]
//     for i in elemnt:
//         if a[i] < a[index]:
//             index = i

//     sequence = [a[index]]
//     max_length -= 1
    
//     for i in range(index - 1, -1, -1):
//         if dp[i] == max_length and a[i] < a[index]:
//             sequence.append(a[i])
//             index = i
//             max_length -= 1
    
//     return sequence[::-1]


// def longest_increasing_subsequence(n, a):
//     dp = [1] * n
    
//     for i in range(n):
//         for j in range(i):
//             if a[j] < a[i]:
//                 dp[i] = max(dp[i], dp[j] + 1)
    
//     subsequence = get_subsequence(a, dp)
//     string_subsequence = ' '.join(map(str, subsequence))
//     print(f'{max(dp)} {string_subsequence} ')



// n, *a = map(int, input().split())

// longest_increasing_subsequence(n, a)


#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    vector<int> dp(n, 1);
    for (int i = 0; i < n; i++){
        for (int j = 0; j < i; j++){
            if (a[j] < a[i]){
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    int max_length = *max_element(dp.begin(), dp.end());
    vector<int> sequence;
    int index = max_element(dp.begin(), dp.end()) - dp.begin();
    sequence.push_back(a[index]);
    max_length -= 1;
    for (int i = index - 1; i >= 0; i--){
        if (dp[i] == max_length && a[i] < a[index]){
            sequence.push_back(a[i]);
            index = i;
            max_length -= 1;
        }
    }
    reverse(sequence.begin(), sequence.end());
    cout << sequence.size() << " ";
    for (int i = 0; i < sequence.size(); i++){
        cout << sequence[i] << " ";
    }
    cout << endl;
    return 0;
}