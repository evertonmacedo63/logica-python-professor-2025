#include <iostream>

using namespace std;

int main() {
    int V;
    // Lendo o valor inicial V
    cin >> V;

    // O vetor N terá 10 posições
    int N[10];

    // N[0] recebe o valor de Vrec
    N[0] = V;

    // Imprime N[0] imediatamente
    cout << "N[0] = " << N[0] << endl;

    // Loop para preencher e imprimir de N[1] até N[9]
    for (int i = 1; i < 10; ++i) {
        // Cada posição é o dobro da anterior
        N[i] = N[i - 1] * 2;
        // Imprime o resultado
        cout << "N[" << i << "] = " << N[i] << endl;
    }

    return 0;
}
