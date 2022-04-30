// 1
#include <stdio.h>
#include <stdlib.h>

int main() {
    int vetor[6] = {1, 0, 5, -2, -5, 7}, i, soma;
    soma = vetor[0] + vetor[5] + vetor[1];
    vetor[4] = 100;
    for (i = 0; i < 6; i++) {
        printf("%d\n", vetor[i]);
    }
    return 0;
}
