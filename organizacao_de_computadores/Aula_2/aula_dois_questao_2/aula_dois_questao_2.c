#include <stdio.h>
#include <stdlib.h>


int main() {
    int vetor[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, vetorCopia[10], contador, soma = 0;
    for (contador = 0; contador < 10; contador++) {
        vetorCopia[contador] = vetor[contador];
    }
    for (contador = 0; contador < 10; contador++) {
        vetor[contador] = vetorCopia[9 - contador];
        printf("%d ", vetor[contador]);
        if (contador % 2 == 0) {
            soma = soma + vetor[contador];
        }
    }
    printf("\nA soma dos valores de indice par: %d", soma);
    return 0;
}