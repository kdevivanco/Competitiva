
# int liebre(vector<int> vec, int k){
#     vector<int> dp(vec.size(), 1e9);
#     dp[0] = 0;
#     for(int i=0; i<vec.size(); i++){
#         for(int j=1; j<=k; j++){
#             if(i+j < vec.size()){
#                 dp[i+j] = min(dp[i+j], dp[i] + abs(vec[i+j] - vec[i]));
#             }
#         }
#     }
#     int tam = vec.size() -1;
#     return dp[tam];
# }

# int main(){
#     int n, k;
#     cin >> n >> k;
#     vector<int> vec(n);
#     for(int i=0; i<n; i++){
#         cin >> vec[i];
#     }
#     cout << liebre(vec, k) << endl;
# }

def liebre(L,k):
    dp = [1e9] * len(L)
    dp[0] = 0
    for i in range(len(L)):
        for j in range(1,k+1):
            if i+j < len(L):
                dp[i+j] = min(dp[i+j], dp[i] + abs(L[i+j] - L[i]))
    return dp[-1]


n, k = map(int, input().split())
L = list(map(int, input().split()))
print(liebre(L,k))


