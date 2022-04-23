package UFOPA.programacao_orientada_a_objetos.Aula_4;

public class Titular {
    private String nome, cpf;

    // Construtor
    public Titular(String nome, String cpf) {
        this.nome = nome;
        this.cpf = cpf;
    }

    // Metodos Get e Set
    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return this.cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }
    
}