import tkinter as tk
from tkinter import messagebox
from Client import Client
from Product import Product
from Category import Category
from Order import Order
from OrderManager import OrderManager
from TruckManager import TruckManager
from Inventory import Inventory


class MainWindow:

    def __init__(self):

        # ===== SISTEMA =====
        self.inventory = Inventory(3, 3)
        self.orderManager = OrderManager()
        self.truckManager = TruckManager(1, 50)

        self.clients = []
        self.products = []

        self.clientCounter = 1
        self.productCounter = 1
        self.orderCounter = 1

        # ===== ROOT =====
        self.root = tk.Tk()
        self.root.title("Amazon Hub - Sistema Logístico")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e2f")

        self.createMenu()
        self.createMainPanel()

        self.root.mainloop()


    # =====================================================
    # ===================== MENÚ ==========================
    # =====================================================

    def createMenu(self):

        menuBar = tk.Menu(self.root)

        # ----- Cliente -----
        menuBar.add_command(label="Crear Cliente", command=self.openClientWindow)

        # ----- Producto -----
        menuBar.add_command(label="Crear Producto", command=self.openProductWindow)

        # ----- Pedido -----
        menuBar.add_command(label="Crear Pedido", command=self.createOrder)
        menuBar.add_command(label="Procesar Pedido (Cola → Camión)", command=self.processOrder)
        menuBar.add_command(label="Entregar Pedido (LIFO)", command=self.deliverOrder)

        self.root.config(menu=menuBar)


    # =====================================================
    # ================= PANEL PRINCIPAL ===================
    # =====================================================

    def createMainPanel(self):

        title = tk.Label(
            self.root,
            text="SIMULADOR AMAZON HUB",
            font=("Arial", 22, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title.pack(pady=20)

        self.output = tk.Text(self.root, width=100, height=20)
        self.output.pack(pady=20)


    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)


    # =====================================================
    # ================= VENTANA CLIENTE ===================
    # =====================================================

    def openClientWindow(self):

        window = tk.Toplevel(self.root)
        window.title("Crear Cliente")
        window.geometry("400x300")
        window.configure(bg="#2e2e48")

        tk.Label(window, text="Nombre", bg="#2e2e48", fg="white").pack(pady=5)
        entryName = tk.Entry(window)
        entryName.pack()

        tk.Label(window, text="Teléfono", bg="#2e2e48", fg="white").pack(pady=5)
        entryPhone = tk.Entry(window)
        entryPhone.pack()

        tk.Label(window, text="Dirección", bg="#2e2e48", fg="white").pack(pady=5)
        entryAddress = tk.Entry(window)
        entryAddress.pack()

        def createClient():

            name = entryName.get()
            phone = entryPhone.get()
            address = entryAddress.get()

            if not name or not phone or not address:
                messagebox.showerror("Error", "Completa todos los campos")
                return

            client = Client(self.clientCounter, name, phone, address)
            self.clients.append(client)
            self.clientCounter += 1

            self.log(f"Cliente creado: {client.name}")
            window.destroy()

        tk.Button(
            window,
            text="Guardar Cliente",
            bg="#4CAF50",
            fg="white",
            command=createClient
        ).pack(pady=15)


    # =====================================================
    # ================= VENTANA PRODUCTO ==================
    # =====================================================

    def openProductWindow(self):

        window = tk.Toplevel(self.root)
        window.title("Crear Producto")
        window.geometry("400x400")
        window.configure(bg="#2e2e48")

        tk.Label(window, text="Nombre", bg="#2e2e48", fg="white").pack(pady=5)
        entryName = tk.Entry(window)
        entryName.pack()

        tk.Label(window, text="Precio", bg="#2e2e48", fg="white").pack(pady=5)
        entryPrice = tk.Entry(window)
        entryPrice.pack()

        tk.Label(window, text="Categoría", bg="#2e2e48", fg="white").pack(pady=5)

        categoryVar = tk.StringVar()
        categoryVar.set("ELECTRONICS")

        tk.OptionMenu(window, categoryVar, *[c.name for c in Category]).pack()

        tk.Label(window, text="Fila (0-2)", bg="#2e2e48", fg="white").pack(pady=5)
        entryRow = tk.Entry(window)
        entryRow.pack()

        tk.Label(window, text="Columna (0-2)", bg="#2e2e48", fg="white").pack(pady=5)
        entryCol = tk.Entry(window)
        entryCol.pack()

        def createProduct():

            try:
                name = entryName.get()
                price = float(entryPrice.get())
                category = Category[categoryVar.get()]
                row = int(entryRow.get())
                col = int(entryCol.get())

                product = Product(self.productCounter, name, price, category)

                if self.inventory.addProduct(product, row, col):
                    self.products.append(product)
                    self.productCounter += 1
                    self.log(f"Producto agregado en [{row},{col}]")
                    window.destroy()
                else:
                    messagebox.showerror("Error", "Posición inválida")

            except:
                messagebox.showerror("Error", "Datos inválidos")

        tk.Button(
            window,
            text="Guardar Producto",
            bg="#2196F3",
            fg="white",
            command=createProduct
        ).pack(pady=15)


    # =====================================================
    # =================== PEDIDOS =========================
    # =====================================================

    def createOrder(self):

        if not self.clients or not self.products:
            messagebox.showerror("Error", "Necesitas clientes y productos")
            return

        client = self.clients[-1]
        order = Order(self.orderCounter, client)

        for product in self.products:
            order.addProduct(product, 2)

        self.orderManager.addOrder(order)
        self.orderCounter += 1

        self.log(f"Pedido {order.orderId} agregado a la cola")


    def processOrder(self):

        if self.orderManager.isEmpty():
            self.log("No hay pedidos en cola")
            return

        order = self.orderManager.removeOrder()

        if self.truckManager.loadOrder(order):
            self.log(f"Pedido {order.orderId} cargado al camión")
        else:
            self.log("Camión sin capacidad")


    def deliverOrder(self):

        if self.truckManager.isEmpty():
            self.log("No hay pedidos en el camión")
            return

        order = self.truckManager.deliverOrder()
        self.log(f"Pedido {order.orderId} entregado (LIFO)")