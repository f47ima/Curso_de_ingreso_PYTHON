import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:fatima
apellido:gonzalez
---
Ejercicio: entrada_salida_06
---
Enunciado:
Al presionar el botón  'Sumar', se deberán obtener los valores contenidos en las cajas de texto (txt_operador_A y txt_operador_B), 
transformarlos en números enteros, realizar la suma y luego mostrar el resultado de la operación utilizando el Dialog Alert. 
Ej: "El resultado de la sumas es: 755" 
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
        self.btn_sumar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_sumar_on_click(self):
        #obtengo datos de op a y op b y creo una variable para identificarlos 
        operador_a = self.txt_operador_a.get()
        operador_b = self.txt_operador_b.get()

        #creo una variable para pasarlo a entero 
        operador_a_int = int(operador_a)
        operador_b_int = int(operador_b)
        
        resultado_int = operador_a_int + operador_b_int
        #paso el resultado a str para que se concatene con el mensaje del alert 
        resultado_str = str(resultado_int)

        #creo la variable para poner en message
        mensaje_resultado = "El resultado de la suma es: " + resultado_str

        
        alert(title = "Resultado" , message = mensaje_resultado)

        
        pass



    # TAmbien me gusto 
    # resultado= int(a) + int(b) pero ahora ya se que no se puede hacer eso 
    #entonces en 
    #53 alert (title="Resultado", message= "El resultado de la suma es: " + str(resultado))

     #alert("utn", f"tu resultado es {suma}")??? Raro, no se, todavia no.
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()