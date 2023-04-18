public class operadoresCondicionales {
    
    /**
     * @param args
     */
    public static void main(String args[]) {
        int a = 8;
        int valorMinimo = 0;
        int valorMaximo = 10;
        
        boolean resultado = a >= valorMinimo && a <= valorMaximo;
        if(resultado){
            System.out.println("Dentro de rango");
        }
        else{
            System.out.println("Fuera de rango");
        }
        
        boolean vacaciones = false;
        boolean diaDescanso = true;
        
        if( vacaciones || diaDescanso){
            System.out.println("Padre puede asisitir al juego del hijo");
        }
        else{
            System.out.println("El padre esta ocupado");
        }
        
    }
}
