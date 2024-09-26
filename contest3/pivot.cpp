

#include <iostream>

using namespace std;


void pivot(){
    int n;
    cin>>n; // how many numbers;
    vector<int> v(n);
    for ( int i=0; i<n; ++i ){
        cin>>v[i];
    }

    //usar puntero doble 
    int* p = &v[0];
    
    // int* q = &v[n-1];
    
}

def pivot():
    n= int(input())
    A = [int(x) for x in input().split()]
    pivots= []
    

    for i in range(len(A)-1):
        possible_pivot = A[i]
        # print(possible_pivot)
        
        left = [x for x in A[:i] if x < possible_pivot]
        if len(left) < len(A[:i]):
            continue

        # print(left)
        right = [x for x in A[i+1:] if x > possible_pivot]
        # print(right)
        if len(left) + len(right) == n - 1:
            # print("hollaaa")
            pivots.append(possible_pivot)
    maximum = max(A)
    # print(maximum)
    # print(A[-1])
    if A[-1] == maximum:
        pivots.append(maximum)
    
    # print(pivots)

    print(len(pivots) )

pivot()
    