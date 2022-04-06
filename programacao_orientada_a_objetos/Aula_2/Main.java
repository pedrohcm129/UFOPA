package UFOPA.programacao_orientada_a_objetos.Aula_2;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner saida = new Scanner(System.in);
        double a, b, c;
        // Entrada dos dados do Triangulo X //
        System.out.println("________________________");
        System.out.println("Triângulo X");
        System.out.println("________________________");
        System.out.print("1° Lado: ");
        a = saida.nextDouble();
        System.out.print("2° Lado: ");
        b = saida.nextDouble();
        System.out.print("3° Lado: ");
        c = saida.nextDouble();
        Triangulo x = new Triangulo(a, b, c);
        System.out.printf("Área x: %.4f\n", x.getArea());

        // Entrada de dados do triângulo Y
        System.out.println("________________________");
        System.out.println("Triângulo Y");
        System.out.println("________________________");
        System.out.print("1° Lado: ");
        a = saida.nextDouble();
        System.out.print("2° Lado: ");
        b = saida.nextDouble();
        System.out.print("3° Lado: ");
        c = saida.nextDouble();
        Triangulo y = new Triangulo(a, b, c);
        System.out.printf("Área Y: %.4f\n", y.getArea());
        System.out.println("________________________");

        if (x.getArea() == y.getArea()) {
            System.out.println("SÃO IGUAIS");
        } else if (x.getArea() > y.getArea()) {
            System.out.println("TRIÃNGULO MAIOR: X");
        } else {
            System.out.println("TRIÃNGULO MAIOR: Y");
        }
        System.out.println("________________________");

        saida.close();
    }
}
// void --> Signigica que não tem retorno.