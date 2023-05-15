public class operadoresTernario {
    /**
     * @param args
     * @param resultado
     */
    public static void main(String args[]) {
        //String resultado = (3 < 2) ? "verdadero" : "falso";        
        //System.out.println("resultado = " + resultado);
        
        int numero = 9;
        String resultado = (numero % 2 == 0) ? "numero par" : "numero impar";
        System.out.println("resultado = " + resultado);
}
}