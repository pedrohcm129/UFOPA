package UFOPA.programacao_orientada_a_objetos.Aula_3;

public class Main {
    public static void main(String[] agrs) {
        Conta c1 = new Conta("Pedro", "3422-5");
        Conta c2 = new Conta("Rebeca", "7354-2");


        System.out.println("1ª Conta");
        // Impressão do objeto
        System.out.print(c1);

        System.out.println("______________");

        System.out.println("2ª Conta");
        System.out.println("Nº da Conta: " + c2.getNumeroConta());
        System.out.println("Titular: " + c2.getTitularConta());
        System.out.println("Saldo: R$" + c2.getSaldo());
    }
}