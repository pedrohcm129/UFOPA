package UFOPA.programacao_orientada_a_objetos.Aula_5.Exercicio_5;

public class Conta {
    private static int prox_num = 1;
    private String numero;
    private Cliente titular;
    private double saldo;
    
    public Conta(Cliente titular) {
        this.titular = titular;
        this.numero = String.valueOf(prox_num++);
        this.saldo = 0;
    }
    
    public void depositar(double valor_deposito) {
        this.saldo += valor_deposito;
    }
    
    public void sacar(double valor_saque) throws SaldoInsuficiente, ChequeEspecial {
        if (valor_saque <= saldo) {
            this.saldo -= valor_saque;
        } else if (valor_saque > saldo){
            if (saldo - valor_saque >= -1000) {
                this.saldo -= valor_saque;
                throw new ChequeEspecial(this);
            } else {
                throw new SaldoInsuficiente(this);
            }
        } else {
            throw new SaldoInsuficiente(this);
        }
    }
    
    public void transferir(Conta destino, double valorTransferir) throws SaldoInsuficiente, ChequeEspecial{
        if (valorTransferir > saldo && saldo - valorTransferir >= -1000) {
            destino.depositar(valorTransferir);
            sacar(valorTransferir);
        } else {
            sacar(valorTransferir);
            destino.depositar(valorTransferir);;
        }
    }
    
    public void setNumero(String numero) {
        this.numero = numero;
    }
    
    public String getNumero() {
        return this.numero;
    }
    
    public void setTitular(Cliente titular) {
        this.titular = titular;
    }
    
    public Cliente getTitular() {
        return this.titular;
    }
    
    public void setSaldo(double saldo) {
        this.saldo = saldo;    
    }
    
    public double getSaldo() {
        return this.saldo;
    }
    
    public int getProximoNumero() {
        return Conta.prox_num;
    }
    
    public String toString() {
        return ("\nNumero.: " + this.numero) + ("\nTitular: " + this.titular.getCpf()) + ("\nSaldo..: " + this.saldo);
    }
}