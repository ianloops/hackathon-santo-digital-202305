import metodosLogica.MetodosLogica;

public class Main {
    public static void main(String[] args) {

        //Variável passada para teste do primeiro exercício
        Integer teste1 = 3;

        //Array passado para teste do segundo exercício
        Integer [] teste2 = {3, 8, 50, 5, 1, 18, 12};

        //Array passado para teste do terceiro exercício
        Integer [] teste3 = {1,2};

        System.out.println("Exercício 1, strings de asteriscos");
        System.out.println(MetodosLogica.stringAsteriscos(teste1));
        System.out.println("\nExercício 2, pares com menor diferença");
        System.out.println(MetodosLogica.menorDiferencaEntrePares(teste2));
        System.out.println("\nExercício 3, subconjuntos");
        System.out.println(MetodosLogica.getSubconjuntosPossiveis(teste3));
    }
}