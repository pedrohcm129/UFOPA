// 3
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int i;
    float vetorInicial[10], vetorQuadrado[10];

    for (i = 0; i < 10; i++) {
        printf("Entrada %i: ", i + 1); scanf("%f", &vetorInicial[i]);
        vetorQuadrado[i] = pow(vetorInicial[i], 2);
    }
    
    for (i = 0; i < 10; i++) {
        printf("%.2f ", vetorInicial[i]);
    }
    printf("\n");

    for (i = 0; i < 10; i++) {
        printf("%.2f ", vetorQuadrado[i]);
    }

    
    

    return 0;
}
