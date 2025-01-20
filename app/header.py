import os
from PIL import Image
import customtkinter as ctk


class Header(ctk.CTkFrame):
    def __init__(self, master, router):
        # Define a cor de fundo fixa com fg_color
        super().__init__(master, height=50, fg_color="#242424")
        self.pack(side="top", fill="x", pady=16, padx=16)

        # Adicionando o logo
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
        logo_image = ctk.CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(210, 90))
        logo_label = ctk.CTkLabel(self, image=logo_image, text="", fg_color="#242424")
        logo_label.pack(side="left", padx=10)

        # Botões com cores relacionadas à logo
        button_frame = ctk.CTkFrame(self, fg_color="#242424")
        button_frame.pack(side="right", padx=10)

        # Cores principais
        button_color = "#C9A234"  # Dourado da logo
        button_hover = "#A88227"  # Tom mais escuro para hover

        home_button = ctk.CTkButton(
            button_frame, 
            text="Página Inicial", 
            command=router.show_index_page, 
            font=("Arial", 20, "bold"), 
            width=80, 
            height=40,
            fg_color=button_color, 
            hover_color=button_hover,
            text_color="#242424"
        )
        home_button.pack(side="left", padx=10, pady=10)

        wines_button = ctk.CTkButton(
            button_frame, 
            text="Garrafeira", 
            command=router.show_product_page, 
            font=("Arial", 20, "bold"), 
            width=80, 
            height=40,
            fg_color=button_color, 
            hover_color=button_hover,
            text_color="#242424"
        )
        wines_button.pack(side="left", padx=10, pady=10)

        # Ícone do Carrinho
        cart_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'cart-icon.png')
        cart_icon_image = ctk.CTkImage(light_image=Image.open(cart_icon_path), dark_image=Image.open(cart_icon_path), size=(24, 24))

        cart_button = ctk.CTkButton(
            button_frame, 
            image=cart_icon_image, 
            text="", 
            command=router.show_cart_page, 
            width=40, 
            height=40,
            fg_color=button_color, 
            hover_color=button_hover
        )
        cart_button.pack(side="left", padx=10, pady=10)

        # Ícone do Usuário
        user_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'user-icon.png')
        user_icon_image = ctk.CTkImage(light_image=Image.open(user_icon_path), dark_image=Image.open(user_icon_path), size=(24, 24))

        login_button = ctk.CTkButton(
            button_frame, 
            image=user_icon_image, 
            text="", 
            command=router.show_login_page, 
            width=40, 
            height=40,
            fg_color=button_color, 
            hover_color=button_hover
        )
        login_button.pack(side="left", padx=10, pady=10)
