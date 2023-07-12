import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % 
        y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y 
        si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas”
          se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):

        #CUANDO TERMINES ACORDATE DE PONERLE BIEN EL MENSAJE A LOS MENSAJES
         
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio_final= 800

        #A) Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
        if cantidad >= 6:
            precio_a = precio_final * 0.5 * cantidad
            mensaje = "El precio total de su compra es de precio a "

        #B) Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % 
       # y si es de otra marca el descuento es del 30%.
        elif cantidad == 5 and marca == "ArgentinaLuz":
            precio_b_argentina = precio_final * 0.6 * cantidad
            mensaje = "El precio total de su compra es de precio b argentina"
        elif cantidad == 5:
            precio_b = precio_final * 0.7 * cantidad
            mensaje = "El precio total de su compra es de precio b"
        
        #C) Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y 
        #si es de otra marca el descuento es del 20%.
	
        elif cantidad == 4 and (marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
            precio_c_arg_feli = precio_final * 0.75 * cantidad
            mensaje = "El precio total de su compra es de precio c arg feliz "
        elif cantidad == 4 :
            precio_c = precio_final * 0.8 * cantidad
            mensaje = "El precio total de su compra es de precio c "

        #D) Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, 
        # si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
        elif cantidad == 3 and marca == "AgentinaLuz":
            precio_d_arg = precio_final * 0.85 * cantidad
            mensaje = "El precio total de su compra es de precio_d_arg "
        elif cantidad == 3 and marca == "FelipeLamparas":
            precio_d_feli = precio_final * 0.90 * cantidad
            mensaje = "El precio total de su compra es de precio_d_feli"
        elif cantidad == 3:
            precio_d = precio_final * 0.95 * cantidad
            mensaje = "El precio total de su compra es de precio_d"

        #E) Si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%

        alert("Probando", mensaje)
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()