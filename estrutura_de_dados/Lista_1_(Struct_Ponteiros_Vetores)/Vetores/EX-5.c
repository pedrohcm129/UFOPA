// 5
#include <stdio.h>
#include <stdlib.h>

int main() {
    int vetor[10], i, maior = 0, menor = 0;
    for (i = 0; i < 10; i++) {
        printf("Entrada %i: ", i + 1); scanf("%i", &vetor[i]);
    }
    for (i = 0; i < 10; i++) {
        if (i != 0) {
            if (maior < vetor[i]) {
                maior = vetor[i];
            }
            if (menor > vetor[i]) {
                menor = vetor[i];
            }
        } else {
            maior = vetor[i];
            menor = vetor[i];
        }
    
    }
    printf("MAIOR: %d\n", maior);
    printf("MENOR: %d", menor);

    return 0;
}
