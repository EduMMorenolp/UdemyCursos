public class BreakYContinue {
    

    public static void main(String args[]) {
        
        for( int contador1 = 0 ; contador1 < 6 ; contador1++ ){
            if( contador1 % 2 != 0){ // si el numero no es par
                continue; // ir a la siguiente iteracion
            }   
            System.out.println("contador continue = " + contador1);
        }
        
       for( int contador = 0 ; contador < 6 ; contador++ ){
            if( contador % 2 == 0){ // si el numero es par
               System.out.println("contador break = " + contador);
               break; // rompe el ciclo y lo termina 
            }
        }

        // NO ES RECOMENDABLE USAR ESTA FORMA 
        inicio:
        for( int contador3 = 0 ; contador3 < 6 ; contador3++ ){
            if( contador3 % 2 != 0){
                continue inicio;//ir a la linea de codigo de la etiqueta, tmb funciona con break 
            }   
            System.out.println("contador continue etiqueta = " + contador3);
        }
    }
}