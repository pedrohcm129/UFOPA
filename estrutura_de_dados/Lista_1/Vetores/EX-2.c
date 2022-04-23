// 2
#include <stdio.h>
#include <stdlib.h>

int main() {
    int i, vetor[6];
    
    for (i = 0; i < 6; i++) {
        printf("Entrada: "); scanf("%i", &vetor[i]);
    }

    for (i = 0; i < 6; i++) {
        printf("Saida: %i\n", vetor[i]);
    }
    return 0;
}
