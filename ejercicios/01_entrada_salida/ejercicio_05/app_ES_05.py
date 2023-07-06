import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: fatima 
apellido: gonzalez 
---
Ejercicio: entrada_salida_05
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener tanto el nombre como la edad contenida en 
las cajas de texto correspondientes y luego mostrarlo concatenados utilizando el Dialog Alert. 
Ej: "Usted se llama José y su edad es 66 años"
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #self.txt_nombre
        #self.txt_edad
        #tomo el nombre del usuario
        nombre= self.txt_nombre.get()
        #tomo la edad del usuario
        edad= self.txt_edad.get()
        #programo el alert
        saludo= "Hola " + nombre +","+ " tienes " + edad + " años de edad."
        alert (title= "Bienvenid@", message=saludo)   

        #existe otra forma 
        # (52) message= "Hola " + nombre +","+ " tienes " + edad + " años de edad." 
        # Tambien se puede aplicar dentro de message cualquiera de las dos de abajo:
        # usando f (51) saludo= f"Hola {nombre}, tienes {edad} años de edad "
        # usando format (51) saludo= "Hola {0}, tienes {1} años de edad" .format(nombre,edad)    
                
        pass


        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()