int main() {   
    int a[13] = {12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5, 33, 42};
    int flag = 1;
    int i, j, contVarreduras = 0, contComparacoes = 0, contTrocas = 0;
    for (i = 0; i < n - 1 && flag == 1; i++) {
        flag = 0; //quando não há trocas, flag continuará 0
        contVarreduras += 1;
        for (j = 0; j < n - i - 1; j++) {
            contComparacoes += 1;
            if (a[j] > a[j + 1]) {
                contTrocas += 1;
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
                flag = 1; //troca realizada, flag = 1
                }
        }
    }
    printf("%i\n", contTrocas);
    printf("%i\n", contComparacoes);
    printf("%i\n", contVarreduras);
    for (i = 0; i < tamanho; i++) {
        printf("%i ", a[i]);
    }
    return 0;
}

