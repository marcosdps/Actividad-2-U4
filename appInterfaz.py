from tkinter import *
from tkinter import ttk

class Interfaz:
    __ventana = None
    __precio= None
    __elegido=None
    __IVAelegido = None
    __precioConImpuesto = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("300x240")
        self.__ventana.title("Calculadora de IVA")
        self.labelsYrecuadros()
        self.botones()
        self.ingresoDatos()

    def labelsYrecuadros(self):
        padxy = {"padx":10, "pady":10}
        ttk.Label(self.__ventana, text="Calculo de IVA", background="lightblue", anchor="center").grid(row=0, column=0, columnspan=2,rowspan=2, sticky="ewns")
        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.columnconfigure(1, weight=1)
        ttk.Label(self.__ventana, text="Precio sin IVA").grid(row=2, column=0,padx=15, pady=15)
        ttk.Label(self.__ventana, text="IVA").grid(row=7, column=0, **padxy)
        ttk.Label(self.__ventana, text="Precio con IVA").grid(row=8, column=0, **padxy)
        self.__IVAelegido = StringVar()
        self.__precioConImpuesto = StringVar()
        Entry(self.__ventana, textvariable=self.__IVAelegido).grid(row=7, column=1)
        Entry(self.__ventana, textvariable=self.__precioConImpuesto).grid(row=8, column=1)
        
    
    def botones(self):
        style=ttk.Style()
        style.configure("Red.TButton", background="red")
        style.configure("Green.TButton", background="green")
        salir = ttk.Button(self.__ventana, text = "Salir", command=self.__ventana.destroy, style= "Red.TButton")
        calcular = ttk.Button(self.__ventana, text = "Calcular", command= self.calcular, style="Green.TButton")
        calcular.grid(row=9, column=0)
        salir.grid(row=9, column=1)
        self.__elegido = IntVar()
        Radiobutton(self.__ventana, text="IVA 21%  ", variable=self.__elegido, value=21).grid(row=5, column=0)
        Radiobutton(self.__ventana, text="IVA 10.5%", variable=self.__elegido, value=10).grid(row=6, column=0)



    def ingresoDatos(self):
        self.__precio = ttk.Entry(self.__ventana, width=10)
        self.__precio.grid(row=2, column=1)
    
    def calcular(self):
        try: 
            valor = int(self.__elegido.get())
            if valor == 21:
                self.__precioConImpuesto.set(float(self.__precio.get()) * 1.21)
                self.__IVAelegido.set(21)
            elif valor == 10:#tengo que poner 10 y no 10.5 porque al momento de comparar, me genera conflictos el num flotante, no encontré la solucion
                self.__precioConImpuesto.set(float(self.__precio.get()) * 1.105)
                self.__IVAelegido.set(10.5)
        except ValueError:
            print("Ingrese primero el precio")  


    def ejecutar(self):
        self.__ventana.mainloop()
