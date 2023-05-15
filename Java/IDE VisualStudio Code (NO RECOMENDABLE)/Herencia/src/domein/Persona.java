package domein;

public class Persona {
    
    protected String nombre;
    protected char genero;
    protected int edad;
    protected String direccion;


    public Persona() {
        
    }
    public Persona(String nombre){
        this.nombre = nombre;
    }
    public Persona(char genero, int edad, String direccion, String nombre){
        this.direccion = direccion;
        this.edad = edad;
        this.genero = genero;
        this.nombre = nombre;
    }


    public String getDireccion() {
        return this.direccion;
    }    
    public int getEdad() {
        return this.edad;
    }
    public char getGenero() {
        return this.genero;
    }
    public String getNombre() {
        return this.nombre;
    }
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public void setGenero(char genero) {
        this.genero = genero;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }



}
