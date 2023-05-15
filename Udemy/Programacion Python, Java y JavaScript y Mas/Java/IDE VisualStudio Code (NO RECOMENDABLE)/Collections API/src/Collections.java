import java.util.*;

public class Collections {
    public static void main(String[] args) throws Exception {
        
        List miLista = new ArrayList();

        miLista.add("Lunes");
        miLista.add("Martes");
        miLista.add("Miercoles");
        miLista.add("Jueves");
        miLista.add("Viernes");

        for (Object elemento : miLista) {
            System.out.println(elemento);
        }

        
    }
}
