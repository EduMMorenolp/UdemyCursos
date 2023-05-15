/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apicollections;

import java.util.*;

/**
 *
 * @author no_de
 */
public class APICollections {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        List miLista = new ArrayList();

        miLista.add("Lunes");
        miLista.add("Martes");
        miLista.add("Miercoles");
        miLista.add("Jueves");
        miLista.add("Viernes");

        // Ciclo for Each 
        for (Object elemento : miLista) {
            System.out.println(elemento);
        }

        // Funcion LAMBA o FLECHA
        miLista.forEach((elemento) -> {
            System.out.println(elemento);
        });
        
        System.out.println("-------------------------");
        
        miLista.add("Viernes"); // Se puede agregar duplicados.
        imprimir(miLista);
        
        System.out.println("-------------------------");

        Set miSet = new HashSet();
        
        miSet.add("Lunes");
        miSet.add("Martes");
        miSet.add("Miercoles");
        miSet.add("Jueves");
        miSet.add("Viernes");
        miSet.add("Viernes"); // No se Agregan los duplicados
        imprimir(miSet);
        
        System.out.println("-------------------------");
        
        Map miMapa = new HashMap();
        
        miMapa.put("Valor1", "Juan");
        miMapa.put("Valor2", "Karla");
        miMapa.put("Valor3", "Rosario");
        
       String elemento = (String) miMapa.get("Valor1");
        System.out.println("elemento = " + elemento);
        
        System.out.println("LLAVES MAP :");
        imprimir(miMapa.keySet());
        System.out.println(" VALORES MAP : ");
       imprimir(miMapa.values());
        
        
    }
    
    
    public static void imprimir(Collection colleccion){
        colleccion.forEach((object) -> {
            System.out.println("Elemento = " + object);
        });
    }

}
