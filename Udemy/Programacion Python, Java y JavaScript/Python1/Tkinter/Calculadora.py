import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.resizable(0,0)
        self.resultado = ""
        master.iconbitmap('Udemy/Programacion Python, Java y JavaScript/Python1/Tkinter/calculadora.ico')
        

        # Crear etiqueta de resultado
        self.resultado_label = tk.Label(master, text="", font=("Arial", 12))
        self.resultado_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Crear botones numéricos
        numeros = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
        self.botones_numeros = []
        for i, num in enumerate(numeros):
            boton = tk.Button(master, text=num, width=5, height=2, command=lambda num=num: self.agregar_num(num))
            boton.grid(row=i//3+1, column=i%3, padx=5, pady=5)
            self.botones_numeros.append(boton)

        # Crear botones de operaciones
        operaciones = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3), ("=", 4, 2), ("C", 4, 1)]
        self.botones_operaciones = []
        for operacion in operaciones:
            boton = tk.Button(master, text=operacion[0], width=5, height=2, command=lambda op=operacion[0]: self.agregar_op(op))
            boton.grid(row=operacion[1], column=operacion[2], padx=5, pady=5)
            self.botones_operaciones.append(boton)

    def agregar_num(self, num):
        self.resultado += str(num)
        self.resultado_label.config(text=self.resultado)

    def agregar_op(self, op):
        if op == "C":
            self.resultado = ""
        elif op == "=":
            try:
                self.resultado = str(eval(self.resultado))
            except:
                self.resultado = "Error"
        else:
            self.resultado += " " + str(op) + " "
        self.resultado_label.config(text=self.resultado)

# Crear ventana principal
ventana = tk.Tk()
# Crear instancia de calculadora
calc = Calculadora(ventana)
# Ejecutar ventana principal
ventana.mainloop()