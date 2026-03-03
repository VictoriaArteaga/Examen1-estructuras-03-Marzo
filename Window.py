import customtkinter as ctk

class Window(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Amazon Hub Simulator")
        self.geometry("600x500")

        self.orderManager = OrderManager()
        self.truck = TruckManager(1)

        self.createWidgets()

    def createWidgets(self):

        self.btnAddOrder = ctk.CTkButton(self, text="Agregar Pedido", command=self.addOrder)
        self.btnAddOrder.pack(pady=10)

        self.btnLoadTruck = ctk.CTkButton(self, text="Cargar en Camión", command=self.loadTruck)
        self.btnLoadTruck.pack(pady=10)

        self.output = ctk.CTkTextbox(self, width=400, height=200)
        self.output.pack(pady=20)