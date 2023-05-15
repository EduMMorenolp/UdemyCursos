public class operadoresRelacionEigualdad {

    /**
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        
        int a = 3;
        int b = 2;

        Boolean c = (a == b);
        System.out.println("c = " + c);

        Boolean d = a != b;
        System.out.println("d = " + d);

        String cadena = "Hola";
        String cadena2 = "Hola";
        Boolean e = cadena == cadena2;//compara referencias de objetos
        System.out.println("e = " + e);

        Boolean f = cadena.equals(cadena2);//comparamos contenido de cadenas
        System.out.println("f = " + f);

        boolean g = a >= b;//mayor  que > o el mayor o igual >=
        System.out.println("g = " + g);

        if (a % 2 == 0) {
            System.out.println("Es numero par");
        } else {
            System.out.println("Es numero impar");
        }
        
        int edad = 10;
        int adulto = 18;
        if(edad >= adulto){
            System.out.println("Es un adulto");
        }
        else{
            System.out.println("Es menor de edad");
        }

    }
    }