package UFOPA.programacao_orientada_a_objetos.Aula_3.execicio_aula_3;

public class Main {
    public static void main(String[] args) {
        System.out.print("----Eleições----");
        // Objetos
        Eleicao pedro = new Eleicao("Pedro");
        Eleicao rebeca = new Eleicao("Rebeca");
        Eleicao henrique = new Eleicao("Henrique");

        pedro.votar();
        pedro.votar();
        rebeca.votar();
        rebeca.votar();
        rebeca.votar();
        rebeca.votar();
        henrique.votar();

        System.out.println(pedro);
        System.out.println(rebeca);
        System.out.println(henrique);
    }
}
