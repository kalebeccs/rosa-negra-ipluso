import customtkinter as ctk
from src.models.wines import get_wines_by_type

class ProductPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Título da página
        title_label = ctk.CTkLabel(self, text="Product Page", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Frame para vinhos de mesa
        table_wines_frame = ctk.CTkFrame(self, fg_color="transparent")
        table_wines_frame.pack(pady=10, padx=20, fill="x")
        table_wines_label = ctk.CTkLabel(table_wines_frame, text="Vinhos de Mesa", font=("Arial", 20, "bold"))
        table_wines_label.pack(anchor="w")
        table_wines = get_wines_by_type("Mesa")
        self.add_products(table_wines_frame, table_wines)

        # Frame para vinhos exóticos
        exotic_wines_frame = ctk.CTkFrame(self, fg_color="transparent")
        exotic_wines_frame.pack(pady=10, padx=20, fill="x")
        exotic_wines_label = ctk.CTkLabel(exotic_wines_frame, text="Vinhos Exóticos", font=("Arial", 20, "bold"))
        exotic_wines_label.pack(anchor="w")
        exotic_wines = get_wines_by_type("Exotico")
        self.add_products(exotic_wines_frame, exotic_wines)

        # Frame para vinhos reserva
        reserve_wines_frame = ctk.CTkFrame(self, fg_color="transparent")
        reserve_wines_frame.pack(pady=10, padx=20, fill="x")
        reserve_wines_label = ctk.CTkLabel(reserve_wines_frame, text="Vinhos Reserva", font=("Arial", 20, "bold"))
        reserve_wines_label.pack(anchor="w")
        reserve_wines = get_wines_by_type("Reserva")
        self.add_products(reserve_wines_frame, reserve_wines)

        # Frame para vinhos signature
        signature_wines_frame = ctk.CTkFrame(self, fg_color="transparent")
        signature_wines_frame.pack(pady=10, padx=20, fill="x")
        signature_wines_label = ctk.CTkLabel(signature_wines_frame, text="Vinhos Signature", font=("Arial", 20, "bold"))
        signature_wines_label.pack(anchor="w")
        signature_wines = get_wines_by_type("Signature")
        self.add_products(signature_wines_frame, signature_wines)

    def add_products(self, frame, products):
        for product in products:
            product_info = (
                f"Brand: {product['brand']}\n"
                f"Name: {product['name']}\n"
                f"Price: ${product['price']:.2f}\n"
                f"Type: {product['type']}\n"
                f"Alcohol: {product['alcohol']}%\n"
                f"Year: {product['year']}\n"
                f"Region: {product['region']}\n"
                f"Description: {product['description']}\n"
            )
            product_label = ctk.CTkLabel(frame, text=product_info, font=("Arial", 16), justify="left")
            product_label.pack(anchor="w", padx=10, pady=5)