#include <stdio.h>
#include <stdlib.h>

void insertionSort(int *a, int tamanho)
{
 int i, j, tmp;
  
 for(i = 1; i < tamanho; i++)
 {
  tmp = a[i];
  for(j = i-1; j >= 0 && tmp < a[j]; j--)
  {
   a[j+1] = a[j];
  }
  a[j+1] = tmp;
 }
}

int pesquisaSequencial(int vetor[], int valorPesquisa, int tamanhoVetor) {
    int i, contComparacoes = 0;
    for (i = 0; i < tamanhoVetor; i++) {
        contComparacoes += 1;
        if (vetor[i] == valorPesquisa) {
            break;
        }
    }
    return (contComparacoes);
}

int pesquisaBinaria (int vet[], int chave, int tamanhoVetor) {
    int inf = 0;     // limite inferior (o primeiro índice de vetor em C é zero          )
    int sup = tamanhoVetor-1; // limite superior (termina em um número a menos. 0 a 9 são 10 números)
    int meio;
    int contComparacao = 0;
    insertionSort(vet, tamanhoVetor);
    while (inf != sup) {
        meio = (inf + sup)/2;
        printf("%i ", meio + 1);
        contComparacao++;
        if (chave == vet[meio]) {
            return contComparacao;
        }
        if (chave < vet[meio]) {
            sup = meio;
        }
        else {
            inf = meio;
        }
        if (inf + 1 == sup) {
            return contComparacao;
        } 
    }
}

int main() {
    int vetor[16] = {0, 1, 2, 3, 4, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    int i;
    int tamanhoVetor;
    int chave = 75;
    tamanhoVetor = sizeof(vetor) / sizeof(vetor[0]);
    printf("\n%i comparacoes (PS):\n", pesquisaSequencial(vetor, chave, tamanhoVetor));
    printf("%i comparacoes (PB):\n", pesquisaBinaria(vetor, chave, tamanhoVetor));
    printf(" ");
    
    return 0;
}