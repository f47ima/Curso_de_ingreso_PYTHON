import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):

        ###Hacerlo con isdigit hace que se rompa si ponen negativos, en esta situacion no es necesario usarlo
        #numero= int(None)
        primer_numero = True #bandera
        while True:
            numero = prompt("Ingreso","Ingrese un numero")
            if numero is None or numero == "": #numero ==None or string vacio para que el okey tampoco de error 
                break #toda esta secuencia de numero intnone es para que el cancelar no te de error en la consola
            numero =int(numero) #aca vuelve al bucle para seguir con lo que si este escribiendo el usuario dentro del prompt
            """if primer_numero:
                maximo = numero
                minimo = numero 
                primer_numero = False #cambio de bandera para qeu ya no entre en esta parte del bucle 
            elif numero > maximo:
                maximo = numero
            elif numero < minimo:
                minimo = numero """
            
            if primer_numero or numero > maximo:
                maximo = numero 
            if primer_numero or numero > minimo:
                minimo = numero 
                primer_numero = False 

        self.txt_maximo.delete(0,"end")
        self.txt_minimo.delete(0,"end")

        if not primer_numero: #maximo != None 
            self.txt_minimo.insert(0,minimo)
            self.txt_maximo.insert(0,maximo)
        
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
