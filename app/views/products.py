import customtkinter as ctk
import logging
from app.global_state import add_to_cart
from src.models.wines import get_wines_by_type

class ProductPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Título da página
        title_label = ctk.CTkLabel(self, text="Página de produtos", font=("Arial", 24, "bold"))
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
            product_frame = ctk.CTkFrame(frame, fg_color="#242424", corner_radius=10)
            product_frame.pack(fill="x", padx=10, pady=5)

            product_info = (
                f"Marca: {product['brand']}\n"
                f"Nome: {product['name']}\n"
                f"Valor: €{product['price']:.2f}\n"
                f"Tipo: {product['type']}\n"
                f"Álcool: {product['alcohol']}\n"
                f"Ano: {product['year']}\n"
                f"Região: {product['region']}\n"
                f"Descrição: {product['description']}\n"
            )
            product_label = ctk.CTkLabel(product_frame, text=product_info, font=("Arial", 16), justify="left")
            product_label.pack(anchor="w", padx=10, pady=5)

            add_to_cart_button = ctk.CTkButton(
                product_frame, 
                text="Adicionar ao carrinho", 
                command=lambda p=product: self.add_to_cart(p),
                font=("Arial", 12, "bold"),
                fg_color="#C9A234",
                hover_color="#A88227",
                text_color="#292929"
            )
            add_to_cart_button.pack(anchor="e", padx=10, pady=5)

    def add_to_cart(self, product):
        add_to_cart(product, 1)
        logging.info(f"Added to cart: {product['type']} {product['name']}")
