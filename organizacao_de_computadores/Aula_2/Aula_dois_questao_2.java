package UFOPA.organizacao_de_computadores.Aula_2;

public class Aula_dois_questao_2 {
    public static void main(String[] args) {
        int vetor[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, contador, soma = 0; int vetorCopia[] = new int[10];
        // Copiando os valores de 'vetor' para 'vetorCopia'.
        for (contador = 0; contador < 10; contador++) {
            vetorCopia[contador] = vetor[contador];
        }
        // Inversão dos valores do 'vetor',impressão deles, verificação dos indicies pares e soma dos valores de indice par.
        for (contador = 0; contador < 10; contador++) {
            vetor[contador] = vetorCopia[9 - contador];
            System.out.print(" " + vetor[contador]);
            if (contador % 2 == 0) {
                soma += vetor[contador];
            } else {
                continue;
            }
        }
        System.out.print("\n A soma dos valores de indice par: " + soma);


    }
}