// 1
#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char nome[20];
    int matricula;
    float notaUm, notaDois;
} Alunos;

Alunos cadastrar(char nome[20], int matricula, float notaUm, float notaDois) {
    Alunos aluno;
    strcpy(aluno.nome, nome);
    aluno.matricula = matricula;
    aluno.notaUm = notaUm;
    aluno.notaDois = notaDois;
    return aluno;
}

void mostrarAlunos(Alunos aluno) {
    printf("---------------------------------\n");
    printf("Matricula: %i\n",aluno.matricula);
    printf("---------------------------------\n");
    printf("Nome: %s\n",aluno.nome);
    printf("Media: %.2f\n", (aluno.notaUm + aluno.notaDois) / 2);;
    printf("---------------------------------\n");
}



int main() {
    Alunos Pedro;
    Alunos Rebeca;
    Alunos Henrique;

    Pedro = cadastrar("Pedro", 20034456, 9.5, 9.3);
    mostrarAlunos(Pedro);

    Rebeca = cadastrar("Rebeca", 20054633, 9.9, 10);
    mostrarAlunos(Rebeca);

    Henrique = cadastrar("Henrique", 20045612, 9.8, 9.9);
    mostrarAlunos(Henrique);
    
    return 0;
}