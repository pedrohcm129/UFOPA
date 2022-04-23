package UFOPA.programacao_orientada_a_objetos.Aula_4;

public class Main {
    public static void main(String[] args) {
        Titular donoUm = new Titular("Sr. Matheus", "023864094-34");
        Carro veiculoUmUm = new Carro("Carro", "Fiat", "Argo", "Prata", "2020");
        Carro veiculoUmDois = new Carro("Moto", "BMW", "CB-1000", "Branco", "2019");
        CadastroCarro cadastroUmUm = new CadastroCarro(veiculoUmUm, donoUm);
        CadastroCarro cadastroUmDois = new CadastroCarro(veiculoUmDois, donoUm);

        Titular donoDois = new Titular("Sara Lima", "845239509-09");
        Carro veiculoDois = new Carro("Moto", "Honda", "CB-500F", "Chumbo", "2022");
        CadastroCarro cadastroDois = new CadastroCarro(veiculoDois, donoDois);

        Titular donoTres = new Titular("Algusto César", "349523569-23");
        Carro veiculoTres = new Carro("Carro", "Volkswagen", "Fusca", "Azul", "1996");
        CadastroCarro cadastroTres = new CadastroCarro(veiculoTres, donoTres);

        System.out.println(cadastroUmUm);
        System.out.println(cadastroUmDois);
        System.out.println(cadastroDois);
        System.out.println(cadastroTres);
        
    }
}