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
        #self.txt_operador_a 
        #self.txt_operador_b
        #obtengo datos de op a y op b y creo una variable para identificarlos 
        a=self.txt_operador_a.get()
        b=self.txt_operador_b.get()
        #convierto los datos de los operadores en enteros con el int y los sumo en una unica variable- resultado
        resultado_suma= int(a) + int(b)
        #creo el dialog alert y convierto el resultado en str para que se pueda concatenar en el mensaje 
        alert(title="Suma" ,message="El resultado de la suma es: "+ str(resultado_suma))
        pass

    def btn_restar_on_click(self):
        #Cada vez que se hace un nuevo boton se debe poner otra vez la variable de los operadores.
        # No sabemos aun porque, pero monkey see, monkey do.
        a=self.txt_operador_a.get()
        b=self.txt_operador_b.get()
        resultado_resta= int(a) - int(b)
        alert(title="Resta",message="El resultado de la resta es: "+ str(resultado_resta))
        pass

    def btn_multiplicar_on_click(self):
        a=self.txt_operador_a.get()
        b=self.txt_operador_b.get()
        resultado_multiplicacion= int(a) * int(b)
        alert(title="Multiplicación",message="El resultado de la multiplicación es: "+ str(resultado_multiplicacion))
        pass

    def btn_dividir_on_click(self):
        a=self.txt_operador_a.get()
        b=self.txt_operador_b.get()
        resultado_division= int(a) - int(b)
        alert(title="División",message="El resultado de la división es: "+ str(resultado_division))
        pass
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()