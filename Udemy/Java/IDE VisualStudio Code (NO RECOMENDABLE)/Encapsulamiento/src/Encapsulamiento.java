

import dominio.Persona;

public class Encapsulamiento {

    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 5000.00, false);
//        System.out.println("persona1 nombre:" + persona1.getNombre());
        System.out.println("persona1: " + persona1.toString());
        persona1.setNombre("Juan Carlos");
//        persona1.nombre = "Juan Carlos";
//        System.out.println("nombre:" + persona1.nombre);
        System.out.println("persona1 nombre con cambio:" + persona1.getNombre());
        System.out.println("persona1 sueldo: " + persona1.getSueldo());
        System.out.println("persona1 eliminado:" + persona1.isEliminado());
        System.out.println("persona1: " + persona1); // Cuando se usa un Print no es requerido usar el .toString()
    }
}
