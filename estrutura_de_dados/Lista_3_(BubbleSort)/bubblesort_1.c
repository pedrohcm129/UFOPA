#include <stdlib.h>
#include <stdio.h>

int main(){
    int vetor[] = {1 ,-8 ,-9 ,-2 ,-15 ,-20};
    int memoria, troca, i, j, contTrocas = 0, contComparacoes = 0, contVarreduras = 0, tamanho = sizeof(vetor) / sizeof(vetor[0]);
	troca=1; 
	for(j=tamanho-1; (j>=1) && (troca==1); j--){
		troca=0; 
		contVarreduras += 1;
        for(i=0; i<j; i++){
                contComparacoes += 1;
                if(vetor[i]>vetor[i+1]){
					contTrocas += 1;
                    memoria=vetor[i];
					vetor[i]=vetor[i+1];
					vetor[i+1]=memoria;
					troca=1; 
                }
        }
        if (contVarreduras == 1) {
            printf("Trocas 1 interacao: %i\n", contTrocas);
        }
    }
    printf("%i\n", contTrocas);
    printf("%i\n", contComparacoes);
    printf("%i\n", contVarreduras);
    for (i = 0; i < tamanho; i++) {
        if (i < tamanho -1) {
            printf("%i ", vetor[i]); 
        } else {
            printf("%i\n", vetor[i]);
        }
    }

    return 0;
}