package UFOPA.programacao_orientada_a_objetos.Aula_2;

public class Triangulo {
    // Atribulto da classe Triângulo
    private double area;
    // 'Private' impede que se utilize os atribultos no Main //

    // Metodo construtor //
    public Triangulo(double a, double b, double c) {
        double semiperimetro = (a + b + c) / 2;
        this.area = Math.sqrt(semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c));
    }
    
    // Metodo Get para acesso do valor de area no Main //
    public double getArea() {
        return this.area;
    }
}   