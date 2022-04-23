// 2

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

typedef struct {
    char nome[20];
    float altura;
    float massa;
    char cpf[12];
    char sexo;
} Cadastro;

Cadastro cadastrar(char nome[50], float altura, float massa, char cpf[12], char sexo) {
    Cadastro informacoesUsuario;
    strcpy(informacoesUsuario.nome, nome);
    informacoesUsuario.altura = altura;
    informacoesUsuario.massa = massa;
    strcpy(informacoesUsuario.cpf, cpf);
    informacoesUsuario.sexo = sexo;
    return informacoesUsuario;
}

int main() {
    Cadastro bancoDeDadosUsuarios[4];
    Cadastro usuarioUm;
    Cadastro usuarioDois;
    Cadastro usuarioTres;
    Cadastro usuarioQuatro;
    char cpfProcurado[12];
    int i;

    usuarioUm = cadastrar("Pedro Henrique Costa Menezes", 1.77, 68.0, "99933344466", 'M');
    usuarioDois = cadastrar("Fernanda Berlineta", 1.56, 47, "11100333222", 'F');
    usuarioTres = cadastrar("Henrique Freitas da Silva", 1.79, 73, "00022233344", 'M');
    usuarioQuatro = cadastrar("Debora Santos Pontes", 1.67, 78, "00011100022", 'F');

    bancoDeDadosUsuarios[0] = usuarioUm;
    bancoDeDadosUsuarios[1] = usuarioDois;
    bancoDeDadosUsuarios[2] = usuarioTres;
    bancoDeDadosUsuarios[3] = usuarioQuatro;

    printf("CPF: "); scanf("%s", cpfProcurado);

    for (i = 0; i < 4; i++) {
        if (strcmp(cpfProcurado, bancoDeDadosUsuarios[i].cpf) == 0) {
            printf("Nome: %s", bancoDeDadosUsuarios[i].nome);
            printf("\nIMC: %.2f", bancoDeDadosUsuarios[i].massa / pow(bancoDeDadosUsuarios[i].altura, 2));
        }
    }

    return 0;
}