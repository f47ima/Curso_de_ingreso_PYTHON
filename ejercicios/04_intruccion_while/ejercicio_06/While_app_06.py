import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        acumulador = 0
        contador = 0 #inicializar variable de control
        numero = "" #esta variable se modificara en la linea 39 
        while(contador < 5) :#condicion que se evalua 
            numero = prompt(title="EJ06", prompt= "Ingrese un numero ")
            if numero != None and numero != "":
                numero = int(numero)
                contador = contador + 1 #cambiar la condicion de la variable de control
                acumulador = acumulador + numero
            else: 
                numero = 0
                break
        if contador != 0:
            promedio= acumulador / contador
        else:
            promedio = "No se ingresaron datos"
            
        self.txt_suma_acumulada.delete(0,1000000000)
        self.txt_suma_acumulada.insert(0,acumulador)
        self.txt_promedio.delete(0,100000000)
        self.txt_promedio.insert(0,promedio)
        pass
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
