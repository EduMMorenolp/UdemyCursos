

public class IfElse {

    public static void main(String args[]) {
        boolean condicion = true;

        if (condicion) {
            System.out.println("Condicion verdadera");
        } else {
            System.out.println("Condicion falsa");
        }

        int numero = 5;
        String numeroTexto = "Numero Texto";
    
        if( numero == 1 ){ // SI
            numeroTexto = "Numero uno";
        } 
        else if( numero == 2 ){ // Sino Si
            numeroTexto = "Numero dos";
        }    
        else if( numero == 3 ){
            numeroTexto = "Numero tres";
        }
        else if( numero == 4){
            numeroTexto = "Numero cuatro";
        }
        else{ // Sino
            numeroTexto = "Numero no encontrado";
        }
        
        System.out.println("numeroTexto = " + numeroTexto);
    }
}