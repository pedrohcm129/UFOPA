package UFOPA.programacao_orientada_a_objetos.Aula_4;

public class CadastroCarro {
    private Carro veiculo;
    private Titular dono;

    public CadastroCarro(Carro veiculo, Titular dono) {
        this.veiculo = veiculo;
        this.dono = dono;
    }

    public String toString() {
        return ("--------------------" + "\nTitular: " + this.dono.getNome()) + ("\nCPF: " + this.dono.getCpf()) + ("\nTipo: " + this.veiculo.getTipo()) + ("\nMarca: " + this.veiculo.getMarca()) + ("\nCor: " + this.veiculo.getCor()) + ("\nAno: " + this.veiculo.getAno());
    }
}