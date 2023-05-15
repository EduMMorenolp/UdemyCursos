public class operadoresAritmeticos {
    
    public static void main(String args[]) {
        int a=3, b=2;
        int resultado = a + b;
        System.out.println("resultado suma = " + resultado);
        
        resultado = a - b;
        System.out.println("resultado resta = " + resultado);
        
        resultado = a * b;
        System.out.println("resultado multiplicacion = " + resultado);
        
        double resultado2 = 3D / b;
        System.out.println("resultado division = " + resultado2);
        
        resultado = a % b;
        System.out.println("resultado modulo = " + resultado);
        
        if( b % 2 == 0)
            System.out.println("Es numero par");
        else
            System.out.println("Es numero impar");
    }
}