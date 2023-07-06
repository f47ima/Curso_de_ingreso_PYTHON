import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: fatima
apellido: gonzalez 
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        #obtengo datos de op a y op b y creo una variable para identificarlos 
        operador_a = self.txt_operador_a.get()
        operador_b = self.txt_operador_b.get()

        #creo una variable para pasarlo a entero 
        operador_a_int = int(operador_a)
        operador_b_int = int(operador_b)
        
        suma = operador_a_int + operador_b_int
        #paso el resultado a str para que se concatene con el mensaje del alert 
        suma_str = str(suma)

        #creo la variable para poner en message
        mensaje_resultado_suma = "El resultado de la suma es: " + suma_str
        
        alert(title = "Suma" , message = mensaje_resultado_suma)
        pass

    def btn_restar_on_click(self):
        #Cada vez que se hace un nuevo boton se debe poner otra vez la variable de los operadores.
        #No sabemos aun porque, pero monkey see, monkey do.

        #Obtengo datos de op a y op b y creo una variable para identificarlos 
        operador_a = self.txt_operador_a.get()
        operador_b = self.txt_operador_b.get()

        #creo una variable para pasarlo a entero 
        operador_a_int = int(operador_a)
        operador_b_int = int(operador_b)
        
        resta = operador_a_int - operador_b_int
        #paso el resultado a str para que se concatene con el mensaje del alert 
        resta_str = str(resta)

        #creo la variable para poner en message
        mensaje_resultado_resta = "El resultado de la resta es: " + resta_str

        
        alert(title = "Resta" , message = mensaje_resultado_resta)
        pass

    def btn_multiplicar_on_click(self):
        #Obtengo datos de op a y op b y creo una variable para identificarlos 
        operador_a = self.txt_operador_a.get()
        operador_b = self.txt_operador_b.get()

        #creo una variable para pasarlo a entero 
        operador_a_int = int(operador_a)
        operador_b_int = int(operador_b)
        
        multiplicacion = operador_a_int * operador_b_int
        #paso el resultado a str para que se concatene con el mensaje del alert 
        multiplicacion_str = str(multiplicacion)

        #creo la variable para poner en message
        mensaje_resultado_multiplicacion = "El resultado de la multiplicación es: " + multiplicacion_str

        
        alert(title = "Multiplicación" , message = mensaje_resultado_multiplicacion)
        pass

    def btn_dividir_on_click(self):
        #Obtengo datos de op a y op b y creo una variable para identificarlos 
        operador_a = self.txt_operador_a.get()
        operador_b = self.txt_operador_b.get()

        #creo una variable para pasarlo a entero 
        operador_a_int = int(operador_a)
        operador_b_int = int(operador_b)
        
        division = operador_a_int / operador_b_int
        #paso el resultado a str para que se concatene con el mensaje del alert 
        division_str = str(division)

        #creo la variable para poner en message
        mensaje_resultado_division = "El resultado de la división es: " + division_str

        
        alert(title = "División" , message = mensaje_resultado_division)
        pass
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()