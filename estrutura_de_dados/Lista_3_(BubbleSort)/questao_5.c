#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void bubble_sort_1(){

    int vetor[]= {9, 2, 7, 6, 1, 3, 5, 4, 8};
    int n, k;
    bool swapped = true;

    for (n = sizeof(vetor) / sizeof(vetor[0]); swapped && n > 0; n--) {
        swapped = false;
        for (int va=0; va < n; va++) {
            if (vetor[va] > vetor[va+1]) {
                int swap = vetor[va];
                vetor[va] = vetor[va+1];
                vetor[va+1] = swap;
                swapped=true;
            }
        }
    }
    for (k = 1; k < n; k++) {
        printf("\n [%d]=%d ", k,vetor[k]);
    }
}

void bubble_sort_2() {

    int vetor[] = {9, 2, 7, 6, 1, 3, 5, 4, 8};
    int n = sizeof(vetor) / sizeof(vetor[0]);
    int k, j, aux;

    for (k = 1; k < n; k++) {
        for (j = 0; j < n - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
    for (k = 1; k < n; k++) {
        printf("\n [%d]=%d ", k, vetor[k]);
    }
}

void bubble_sort_3 () {
    
    int vetor[] = {9, 2, 7, 6, 1, 3, 5, 4, 8};
    int n = sizeof(vetor) / sizeof(vetor[0]);
    int k, j, aux;

    for (k = 1; k < n; k++) {
        for (j = 0; j < n - k; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux = vetor[j];
                vetor[j]= vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
        }
    for (k = 1; k < n; k++) {
    printf("\n [%d]=%d ", k,vetor[k]);
    }
}

int main() {
    
    clock_t inicio, fim;

    inicio = clock();
    bubble_sort_1();
    fim = clock();
    printf("\nbubble_sort_1: %f\n", ((double)(fim - inicio) / CLOCKS_PER_SEC));

    inicio = clock();
    bubble_sort_2();
    fim = clock();
    printf("\nbubble_sort_2: %f\n", ((double)(fim - inicio) / CLOCKS_PER_SEC));

    inicio = clock();
    bubble_sort_3();
    fim = clock();
    printf("\nbubble_sort_3: %f\n", ((double)(fim - inicio) / CLOCKS_PER_SEC));
    
    return 0;
}
