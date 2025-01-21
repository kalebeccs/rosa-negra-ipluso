import customtkinter as ctk
import logging
from app.global_state import add_to_cart
from src.models.wines import get_wines_by_type

class ProductPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Frame principal para centralizar tudo
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(expand=True, fill="both")

        # Título da página
        title_label = ctk.CTkLabel(
            main_frame, 
            text="Página de Produtos", 
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        title_label.pack(pady=20)

        # Criar as seções de produtos
        self.create_section(main_frame, "Vinhos de Mesa", "Mesa")
        self.create_section(main_frame, "Vinhos Exóticos", "Exotico")
        self.create_section(main_frame, "Vinhos Reserva", "Reserva")
        self.create_section(main_frame, "Vinhos Signature", "Signature")

    def create_section(self, parent, section_title, wine_type):
        # Frame da seção
        section_frame = ctk.CTkFrame(parent, fg_color="transparent")
        section_frame.pack(pady=20, padx=20, fill="x")

        # Título da seção
        section_label = ctk.CTkLabel(
            section_frame,
            text=section_title,
            font=("Arial", 22, "bold"),
            text_color="#FFFFFF",
        )
        section_label.pack(anchor="center", pady=10)  # Centralizar o título

        # Frame para os produtos
        products_frame = ctk.CTkFrame(section_frame, fg_color="transparent")
        products_frame.pack(anchor="center", padx=10, pady=10)

        # Adicionar os produtos em uma grade
        self.add_products(products_frame, wine_type)

    def add_products(self, frame, wine_type):
        # Configurar grade
        products = get_wines_by_type(wine_type)
        columns = 3  # Número de colunas na grade
        for i, product in enumerate(products):
            # Frame para cada produto
            product_frame = ctk.CTkFrame(
                frame, 
                fg_color="#242424", 
                corner_radius=10, 
                border_width=2, 
                border_color="#C9A234",
                width=300,  # Largura do frame
                height=400  # Altura do frame
            )
            product_frame.grid(row=i // columns, column=i % columns, padx=20, pady=20, sticky="nsew")
            product_frame.grid_propagate(False)  # Desativa ajuste automático de tamanho

            # Informações do produto (incluindo descrição)
            product_info = (
                f"{product['name']}\n"
                f"€{product['price']:.2f}\n"
                f"{product['alcohol']}\n"
                f"{product['region']}\n"
                f"\n"
                f"{product['description']}\n"
            )
            product_label = ctk.CTkLabel(
                product_frame,
                text=product_info,
                font=("Arial", 15),
                justify="center",  # Centralizar texto
                text_color="#FFFFFF",
                wraplength=280  # Quebra de linha para caber no frame
            )
            product_label.pack(expand=True, padx=15, pady=15)  # Adicionado padding interno

            # Botão "Adicionar ao Carrinho"
            add_to_cart_button = ctk.CTkButton(
                product_frame, 
                text="Adicionar ao carrinho", 
                command=lambda p=product: self.add_to_cart(p),
                font=("Arial", 12, "bold"),
                fg_color="#C9A234",
                hover_color="#A88227",
                text_color="#292929"
            )
            add_to_cart_button.pack(pady=10)  # Espaçamento abaixo do texto

        # Ajustar as colunas para expandirem uniformemente
        for col in range(columns):
            frame.grid_columnconfigure(col, weight=1)

    def add_to_cart(self, product):
        add_to_cart(product, 1)
        logging.info(f"Adicionado ao carrinho: {product['type']} {product['name']}")
