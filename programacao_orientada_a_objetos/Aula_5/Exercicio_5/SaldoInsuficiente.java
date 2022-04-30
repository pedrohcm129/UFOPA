package UFOPA.programacao_orientada_a_objetos.Aula_5.Exercicio_5;

public class SaldoInsuficiente extends Exception {
    Conta conta;

    public SaldoInsuficiente(Conta conta) {
        super("Saldo Insuficiente");
        this.conta = conta;
    }

    public Conta getConta() {
        return this.conta;
    }
}