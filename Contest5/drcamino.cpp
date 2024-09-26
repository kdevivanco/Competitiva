

//  Considera una n×n cuadrícula cuyos cuadrados pueden tener trampas. 
//  No se permite moverse a un cuadrado con una trampa. 
//  
//  Tu tarea es calcular el número de caminos desde el cuadrado superior izquierdo hasta el cuadrado inferior derecho.
//  Solo puedes moverte hacia la derecha o hacia abajo. 
//  
//  Entrada:
//  La primera línea de entrada tiene un entero n: el tamaño de la cuadrícula. 
//  Después de esto, hay n líneas que describen la cuadrícula. 
//  Cada línea tiene  n caracteres: . denota una celda vacía, y * denota una trampa. 
//  
//  Salida: Imprime el número de caminos módulo 10^9 + 7 
//  Restricciones 1 ≤ n ≤ 1000 1≤n≤1000 
//  
//  Ejemplo:
//  input  : 
//  4
//  ....
//  .*..
//  ...*
//  *...

//  output :
//  3

// Ejemplo en puthon: 
// MOD = 1000000007
// n = int(input())
// def solucion_doble_for(n):
//     grid = [input() for elem in range(n)] #caminos
//     dp = [[0] * n for elem in range(n)] #Matriz dp 
//     dp[0][0] = 1
//     for i in range(n):
//         for j in range(n):
//             if grid[i][j] == '*':
//                 continue
//             if i > 0:
//                 dp[i][j] += dp[i - 1][j]
//             if j > 0:
//                 dp[i][j] += dp[i][j - 1]
//             dp[i][j] %= MOD

//     print(dp[n - 1][n - 1])

#include <iostream>
#include <vector>

using namespace std;

// implementacion en c++ 

int MOD = 1000000007;
int n;
vector<string> grid;
vector<vector<int>> dp;

void drcamino(){
    if (grid[0][0]== 0){
        cout << 0 <<endl;
        
    }
    else{
    dp = vector<vector<int>>(n, vector<int>(n, 0));
    dp[0][0] = 1;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (grid[i][j] == '*'){
                continue;
            }
            if (i > 0){
                dp[i][j] += dp[i - 1][j];
            }
            if (j > 0){
                dp[i][j] += dp[i][j - 1];
            }
            dp[i][j] %= MOD;
        }
    }
    cout << dp[n - 1][n - 1] << endl;
    }
}

int main(){
    cin >> n;
    grid = vector<string>(n);
    for (int i = 0; i < n; i++){
        cin >> grid[i];
    }
    drcamino();
    return 0;
}
