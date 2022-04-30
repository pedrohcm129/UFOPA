package UFOPA.programacao_orientada_a_objetos.Aula_5.Exercicio_5;

public class ChequeEspecial extends Exception{
    Conta conta;

    public ChequeEspecial(Conta conta) {
        super("Cheque especial em uso!!");
        this.conta = conta;
    }

    public Conta getConta() {
        return this.conta;
    }
}