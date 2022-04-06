package UFOPA.programacao_orientada_a_objetos.Aula_3;

public class Conta {
    private String titularConta,  numeroConta;
    private double saldo;
    

    // Construtor
    public Conta(String titularConta, String numeroConta) {
        this.titularConta = titularConta;
        this.numeroConta = numeroConta;
        this.saldo = 0;
    }
    // Metodos 'depositar' e 'sacar'
    public void depositar(double valorDeposito) {
        this.saldo += valorDeposito;
    }
    
    public void sacar(double valorSaque) {
        this.saldo -= valorSaque;
    }
    // Metodos de retorno e set
    public String getTitularConta() {
        return this.titularConta;
    }

    public String getNumeroConta () {
        return this.numeroConta;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getSaldo() {
        return this.saldo;
    }
    // Usado para imprimir ,em Main, o próprio objeto
    public String toString() {
        return ("Número da Conta: " + this.numeroConta) + ("\nTitular: " + this.titularConta) + ("\nSaldo: " + this.saldo);
    }
}


