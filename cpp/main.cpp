// Grupo 13
// Trabajo 2

#include <iostream>
#include <string>
#include <vector>
#include <assert.h>
#include <limits.h>

using namespace std;

#define push push_back
#define pop  pop_back

typedef unsigned long long ll;

const char chars[] = "BEA";

// Genera las combinaciones con repetición de los caracteres "ABE" recursivamente
void generar(vector<string> &arr, long long a1, long long a2, string &acc, long long diff, long long vivosB) {
    if (a1 <= acc.size() && vivosB == 0) { // Caso Base (Condicion 3: A + E < m)
        arr.push(acc);
        return;
    }
    if (acc.size() == a2) // Caso Base
        return;
    if (vivosB < 0) // Poda
        return;
    
    for (int i = 0; i < 3; ++i) {
        diff += i-1;
        if (diff >= 0) { // Condicion 2
            vivosB -= i > 0;
            acc.push(chars[i]);
            generar(arr, a1, a2, acc, diff, vivosB);
            acc.pop();
            vivosB += i > 0;
        }
        diff -= i-1;
    }
}

void generar(vector<string> &arr, long long a1, long long a2) {
    string str = "";
    str.reserve(a2);
    generar(arr, a1, a2, str, 0, a1);
}

ll T(ll k, ll n) {
    if (n == 0)
        return 1;
    else if (k == n)
        return T(k, n-1) + T(k-1, n-1);
    else
        return T(k, n-1) + T(k-1, n-1) + T(k-1, n);
}

ll T(ll m) {
    return T(m, m);
}

ll T_tabulacion(ll m) {
    vector<vector<ll>> tabla(2, vector<ll>(m+1));
    tabla[0][0] = 1;
    tabla[1][0] = 1;
    for (ll k = 1; k <= m; ++k) {
        for (ll n = 1; n < k; ++n)
            tabla[1][n] = tabla[0][n-1] + tabla[1][n-1] + tabla[0][n];
        tabla[1][k] = tabla[0][k-1] + tabla[1][k-1];
        swap(tabla[0], tabla[1]);
    }
    return tabla[0][m];
}

void parteB() {
    vector<string> combinaciones;

    // Input
    long long a1, a2, m;
    cin >> m;
    a1 = m;
    a2 = 2 * m - 1;

    // Process
    generar(combinaciones, a1, a2);

    // Output
    cout << "Existen: " << combinaciones.size()  << " combinaciones validas" << '\n';
}

int main() {
    ios::sync_with_stdio(0); cin.tie(0);

    ll mm = 10000;
    ll ans;
    //ans = T(mm);
    //ans = T_memoizacion(mm);
    ans = T_tabulacion(mm);

    cout << ans << '\n';

    return 0;
}
