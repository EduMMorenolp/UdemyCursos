

import Clase.Clase;

public class MainClase {
    public static void main(String[] args) throws Exception {
        System.out.println("Hola Mundo! Desde el Main ");

        Clase.print(); // LLAMAMOS LA FUNCION DE CLASE PRINT

        Clase persona1 =  new Clase(); 
        persona1.nombre = "Juan";
        persona1.apellido = "Perez";
        persona1.desplegarInformacion();
        
        Clase persona2 = new Clase();
        
        System.out.println("persona1 = " + persona1);
        System.out.println("persona2 = " + persona2);
        
        persona2.desplegarInformacion(); // Verificamos que la nueva persona esta VACIO o NULO
        persona2.nombre = "Karla";
        persona2.apellido = "Lara";
        persona2.desplegarInformacion();

    }
}
