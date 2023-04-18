import tkinter as tk
from tkinter import ttk, messagebox, Menu


# Función para mostrar ventana informativa con datos de inicio de sesión
def mostrar_datos():
    usuario = usuario_entry.get()
    contrasena = password_entry.get()
    mensaje = f"Los datos ingresados son:\nUsuario: {usuario}\nContraseña: {contrasena}"
    tk.messagebox.showinfo("Datos de inicio de sesión", mensaje)

# Crear ventana
ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("250x110")
ventana.resizable(0,0) # No se puede modificar la ventana 

# Crear etiquetas y campos de entrada
usuario_label = tk.Label(ventana, text="Usuario:")
usuario_label.grid(row=0, column=0, padx=6, pady=6, sticky=tk.E)
usuario_entry = tk.Entry(ventana)
usuario_entry.grid(row=0, column=1,sticky=tk.W, padx=6, pady=6)

password_label = tk.Label(ventana, text="Contraseña:")
password_label.grid(row=1, column=0, padx=6, pady=6, sticky=tk.E)
password_entry = tk.Entry(ventana, show="*")
password_entry.grid(row=1, column=1, padx=6, pady=6 , sticky=tk.W)

# Agregar botón de inicio de sesión
login_button = tk.Button(ventana, text="Iniciar sesión", command=mostrar_datos)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5 )

# Ejecutar ventana
ventana.mainloop()