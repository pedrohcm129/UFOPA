package UFOPA.programacao_orientada_a_objetos.Aula_3.execicio_aula_3;

public class Eleicao {
    // Atribultos
    private String nomeDoCandidato;
    private int numeroDeVotos;
    // Metodo construtor
    public Eleicao(String nomeDoCandidato){
        this.nomeDoCandidato = nomeDoCandidato;
        this.numeroDeVotos = 0;
    }
    // Metodo votar
    public void votar() {
        this.numeroDeVotos += 1;
    }
    // Metodos Get e Set
    public String getNomeDoCandidato() {
        return this.nomeDoCandidato;
    }
    public int getNumeroDeVotos() {
        return this.numeroDeVotos;
    }
    public void setNomeDoCandidato(String nomeDoCandidato) {
        this.nomeDoCandidato = nomeDoCandidato;
    }
    public void setNumeroDeVotos(int quantidadeDeVotos) {
        this.numeroDeVotos = quantidadeDeVotos;
    }
    // Metodo toString
    public String toString() {
        return ("\nCandidato: " + this.nomeDoCandidato) + ("\nQuantidade de votos: " + this.numeroDeVotos);
    }
}   

