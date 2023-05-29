package metodosLogica;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public abstract class MetodosLogica {
    public static ArrayList<String> stringAsteriscos(Integer n){
        ArrayList<String> strings = new ArrayList<>();
        for (int i = 1; i<=n; i++){
            StringBuilder asteriscos = new StringBuilder();
            for (int j = 1; j<=i; j++){
                asteriscos.append("*");
            }
            strings.add(asteriscos.toString());
        }
        return strings;
    }

    public static ArrayList<String> menorDiferencaEntrePares(Integer[] lista){
        ArrayList<String> pares = new ArrayList<>();
        //Utilizando ArrayList para uso dos métodos sort() e indexOf(). A operação é facilitada com o array ordenado
        //Array original mantido para que os valores fossem retornados na ordem original, semelhante ao exemplo
        ArrayList<Integer> listaOrdenada = new ArrayList<>(Arrays.asList(lista));
        ArrayList<Integer> listaOriginal = new ArrayList<>(Arrays.asList(lista));

        Collections.sort(listaOrdenada);
        int menorDiferenca = Integer.MAX_VALUE;

        for (int i = 1; i < listaOrdenada.size(); i++) {
            int diferenca = listaOrdenada.get(i) - listaOrdenada.get(i - 1);
            String par = "(" + listaOriginal.get(listaOriginal.indexOf(listaOrdenada.get(i))) + ","
                             + listaOriginal.get(listaOriginal.indexOf(listaOrdenada.get(i-1))) + ")";

            if (diferenca==menorDiferenca){
                pares.add(par);
            }

            if (diferenca<menorDiferenca){
                pares.clear();
                pares.add(par);
                menorDiferenca=diferenca;
            }
        }

        return pares;
    }

    public static List<List<Integer>> getSubconjuntosPossiveis(Integer[] conjuntoOriginal) {
        List<List<Integer>> subconjuntos = new ArrayList<>();
        criaSubconjuntos(conjuntoOriginal, 0, new ArrayList<>(), subconjuntos);
        return subconjuntos;
    }

    private static void criaSubconjuntos(Integer[] conjuntoOriginal, int i, List<Integer> subconjuntoAtual, List<List<Integer>> subconjuntos) {
        if (i == conjuntoOriginal.length) {
            subconjuntos.add(new ArrayList<>(subconjuntoAtual));
            System.out.println(subconjuntoAtual);
            return;
        }

        // Inclui o elemento atual no subconjunto e efetua uma chamada recursiva
        subconjuntoAtual.add(conjuntoOriginal[i]);
        criaSubconjuntos(conjuntoOriginal, i+1, subconjuntoAtual, subconjuntos);

        // Exclui o elemento atual do subconjunto efetua uma chamada recursiva
        subconjuntoAtual.remove(subconjuntoAtual.size() - 1);
        criaSubconjuntos(conjuntoOriginal, i+1, subconjuntoAtual, subconjuntos);
    }
}
