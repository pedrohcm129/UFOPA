// 4

#include <stdio.h>
#include <stdlib.h>

int main() {
    int vetor[8], x, y, i;

    for (i = 0; i < 8; i++) {
        printf("Entrada de valor do vetor na posicao %i: ", i + 1); scanf("%i", &vetor[i]);
    }

    printf("X: ") ;scanf("%i", &x); printf("Y: "); scanf("%i", &y);
    printf("Soma: %i", vetor[x - 1] + vetor[y - 1]);

    return 0;
}
