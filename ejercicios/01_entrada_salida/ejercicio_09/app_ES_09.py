import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: fatima
apellido: gonzalez
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo = (self.txt_sueldo.get())
        incremento = (self.txt_incremento.get())
        
        #paso a float 
        sueldo_float = float (sueldo)
        incremento_float = float (incremento)
        
        resultado = (sueldo_float * incremento_float / 100) + sueldo_float

        alert(title = "Actualización", message = resultado)
        pass


    
    #preguntar porque la caja de texto no permite la coma del
    #escritorio como entrada de datos, solo el punto. Because it is in English, stupid bitch.
    #En un principio puse int y en el alert me puso un resultado 
    # redondo con .0 como si fuera un float, porque? Porque al trabajar con dinero 
    # es necesario el .0 para no perder informacion 
    
    # recorda que 10/100= 0.10 
    # para hacer un AUMENTOS en vez de hacer (x*incremento/100)+x
    # puedo hacer x*1.incremento para tener el total
    # es decir el total x+ el incremento
    # ej incremento=10 entonces x*1.10
    
    # para hacer un DESCUENTOS en vez de hacer x-(x*dto/100)
    # puedo hacer 100-dto= que me da el porcentaje de descuento
    #ej 100-10=90, necesito saber el 90% del precio,
    # para que ya se reste directamente el dto del precio total
    # entonces x *0.90, es el total del precio - dto 


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()