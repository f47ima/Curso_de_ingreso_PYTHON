import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        suma_acumulada_negativos = 0
        suma_acumulada_positivos = 0
        cantidad_nro_positivo = 0
        cantidad_nro_negativo = 0
        cantidad_ceros = 0
        #diferencia == cantidad_nro_positivo - cantidad_nro_negativo

        
        while True:
            numero = prompt ("UTN","Ingrese un numero")
            
            if numero == None:
                break
            
            numero_int = int (numero)

            if numero_int > 0 :
                cantidad_nro_positivo = cantidad_nro_positivo +1
                suma_acumulada_positivos = suma_acumulada_positivos + numero_int

            elif numero_int < 0 :
                cantidad_nro_negativo = cantidad_nro_negativo +1
                suma_acumulada_negativos = suma_acumulada_negativos - numero_int
            
            else:
                cantidad_ceros = cantidad_ceros +1

            diferencia = cantidad_nro_positivo - cantidad_nro_negativo
        #mensaje = "Suma +: " + str(suma_acumulada_positivos) + "/Suma -:" + str(suma_acumulada_negativos) + "/Cantidad +: " + str(cantidad_nro_positivo) + "/Cantidad -: " + str(cantidad_nro_negativo) +  "/Diferencia entre estos: " + str(diferencia)
        mensaje = "Suma +: {0} \nSuma -: {1} Cantidad +: {2} ".format(suma_acumulada_positivos, suma_acumulada_negativos, cantidad_nro_positivo)
        alert("Informe",message=mensaje)
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
