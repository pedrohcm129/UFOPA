package UFOPA.programacao_orientada_a_objetos.Aula_1;

import java.util.Scanner;

public class AulaUm {
    public static void main(String[] args) {
        Scanner variavel = new Scanner(System.in);
        System.out.println("________________________");
        System.out.println("Triângulo X");
        System.out.println("________________________");
        System.out.print("1° Lado: ");
        double xLadoUm = variavel.nextDouble();
        System.out.print("2° Lado: ");
        double xLadoDois = variavel.nextDouble();
        System.out.print("3° Lado: ");
        double xLadoTres = variavel.nextDouble();
        double semiperimetroX = (xLadoDois + xLadoUm + xLadoTres) / 2;
        double xArea = Math.sqrt(semiperimetroX * (semiperimetroX - xLadoUm) * (semiperimetroX - xLadoDois) * (semiperimetroX - xLadoTres));
        System.out.printf("Área de X: %.4f", xArea);

        System.out.println("\n________________________");
        System.out.println("Triângulo Y");
        System.out.println("________________________");
        System.out.print("1° Lado: ");
        double yLadoUm = variavel.nextDouble();
        System.out.print("2° Lado: ");
        double yLadoDois = variavel.nextDouble();
        System.out.print("3° Lado: ");
        double yLadoTres = variavel.nextDouble();
        double semiperimetroY = (yLadoDois + yLadoUm + yLadoTres) / 2;
        double yArea = Math.sqrt(semiperimetroY * (semiperimetroY - yLadoUm) * (semiperimetroY - yLadoDois) * (semiperimetroY - yLadoTres));
        System.out.printf("Área de X: %.4f", yArea);
        
        System.out.println("\n________________________");

        if (xArea == yArea) {
            System.out.print("Ambos triângulos são iguais.");
            System.out.println("________________________");
        } else if (xArea > yArea) {
            System.out.println("O maior triângulo é X");
            System.out.println("________________________");
        } else {
            System.out.println("O maior triângulo é y");
            System.out.println("________________________");
        }
        variavel.close();
    
    }

}