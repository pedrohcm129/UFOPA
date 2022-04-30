package UFOPA.programacao_orientada_a_objetos.Aula_5.Exercicio_5;

public class Main {
    public static void main(String[] args) {
        Cliente cli_1 = new Cliente("111111111-11", "João Batista", 'M', "12345");
	    Cliente cli_2 = new Cliente("222222222-22", "Paula Leite", 'F', "67890");
	    
		Conta c1 = new Conta(cli_1);
		Conta c2 = new Conta(cli_2);
		
		c1.depositar(1000);
		c2.depositar(100);
		c1.depositar(500);
       
        try {   
            c2.sacar(400);
        } catch (SaldoInsuficiente contaSaldoInsuficiente) {
            System.out.println("Saque não realizado!! | Nº Conta: " + contaSaldoInsuficiente.getConta().getNumero());
        } catch (ChequeEspecial contaChequeEspecial) {
            System.out.println("Cheque especial em uso ( Saque ) !! | Nº Conta: " +  contaChequeEspecial.getConta().getNumero());
        }
        
        try {   
            c1.sacar(800);
        } catch (SaldoInsuficiente contaSaldoInsuficiente) {
            System.out.println("Saque não realizado!! | Nº Conta: " + contaSaldoInsuficiente.getConta().getNumero());
        } catch (ChequeEspecial contaChequeEspecial) {
            System.out.println("Cheque especial em uso ( Saque ) !! | Nº Conta: " +  contaChequeEspecial.getConta().getNumero());
        }

		try {
            c1.transferir(c2, 200);
        } catch (SaldoInsuficiente contaSaldoInsuficiente) {
            System.out.println("Transferência não realizada!! | Nº Conta: " + contaSaldoInsuficiente.getConta().getNumero());
        } catch (ChequeEspecial contaChequeEspecial) {
            System.out.println("Cheque especial em uso ( Transferência ) !! | Nº Conta: " +  contaChequeEspecial.getConta().getNumero());
        }
		System.out.println("Conta #1");
		System.out.println(c1);

        System.out.println();
        
		System.out.println("Conta #2");
		System.out.println(c2);
    }
}