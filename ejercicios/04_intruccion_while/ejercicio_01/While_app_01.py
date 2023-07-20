import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''nombre = Fatima
apellido= Gonzalez
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        numero = 1 #inicializacion de mi variabe de control
        while (numero <=10) : #condicion para controlar cuantas veces se debe iterar 
            alert(message=str(numero))
            numero = numero +1 #le sumo 1 
            #sali del while
        """numero = 0
        while (numero < 10): ene ste caso no va el igual porqeu si no me mostraria el 11
            numero = numero +1 y se pone antes esta linea porqeu si no arracnaria en 0
            alert (message = str(numero))"""
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()