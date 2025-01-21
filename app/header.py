import os
from PIL import Image
import customtkinter as ctk
from app.global_state import is_user_logged_in, logout_user, is_user_admin

class Header(ctk.CTkFrame):
    def __init__(self, master, router):
        # Define a cor de fundo fixa com fg_color
        super().__init__(master, height=50, fg_color="#242424")
        self.router = router
        self.pack(side="top", fill="x", pady=16, padx=16)

        # Adicionando o logo
        logo_path = os.path.join(os.path.dirname(__file__), 'assets', 'logo.png')
        logo_image = ctk.CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(210, 90))
        logo_label = ctk.CTkLabel(self, image=logo_image, text="", fg_color="#242424")
        logo_label.pack(side="left", padx=10)

        # Frame para os botões
        self.button_frame = ctk.CTkFrame(self, fg_color="#242424")
        self.button_frame.pack(side="right", padx=10)

        # Cores principais
        self.button_color = "#C9A234"  # Dourado da logo
        self.button_hover = "#A88227"  # Tom mais escuro para hover

        self.update_header()

    def update_header(self):
        # Ícone do Usuário
        user_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'user-icon.png')
        user_icon_image = ctk.CTkImage(light_image=Image.open(user_icon_path), dark_image=Image.open(user_icon_path), size=(24, 24))
        
        # Ícone de Logout
        logout_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'logout-icon.png')
        logout_icon_image = ctk.CTkImage(light_image=Image.open(logout_icon_path), dark_image=Image.open(logout_icon_path), size=(24, 24))
        # Ícone de Admin
        admin_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'admin-icon.png')
        admin_icon_image = ctk.CTkImage(light_image=Image.open(admin_icon_path), dark_image=Image.open(admin_icon_path), size=(24, 24))
        # Limpar o frame dos botões antes de adicionar novos botões
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        home_button = ctk.CTkButton(
            self.button_frame, 
            text="HOME", 
            command=self.router.show_index_page, 
            font=("Arial", 20, "bold"), 
            width=80, 
            height=40,
            fg_color=self.button_color, 
            hover_color=self.button_hover,
            text_color="#242424"
        )
        home_button.pack(side="left", padx=10, pady=10)

        wines_button = ctk.CTkButton(
            self.button_frame, 
            text="WINES", 
            command=self.router.show_product_page, 
            font=("Arial", 20, "bold"), 
            width=80, 
            height=40,
            fg_color=self.button_color, 
            hover_color=self.button_hover,
            text_color="#242424"
        )
        wines_button.pack(side="left", padx=10, pady=10)
        
        # Ícone do Carrinho
        cart_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'cart-icon.png')
        cart_icon_image = ctk.CTkImage(light_image=Image.open(cart_icon_path), dark_image=Image.open(cart_icon_path), size=(24, 24))

        cart_button = ctk.CTkButton(
            self.button_frame, 
            image=cart_icon_image, 
            text="", 
            command=self.router.show_cart_page, 
            width=40, 
            height=40,
            fg_color=self.button_color, 
            hover_color=self.button_hover
        )
        cart_button.pack(side="left", padx=10, pady=10)

        # Botão de login/logout
        if is_user_logged_in():
            login_button = ctk.CTkButton(
                self.button_frame, 
                image=logout_icon_image,
                text="", 
                command=self.logout_user, 
                font=("Arial", 20, "bold"), 
                width=40, 
                height=40,
                fg_color=self.button_color, 
                hover_color=self.button_hover,
                text_color="#242424"
            )
        else:
            login_button = ctk.CTkButton(
                self.button_frame, 
                image=user_icon_image,
                text="", 
                command=self.router.show_login_page, 
                font=("Arial", 20, "bold"), 
                width=40, 
                height=40,
                fg_color=self.button_color, 
                hover_color=self.button_hover,
                text_color="#242424"
            )
        login_button.pack(side="left", padx=10, pady=10)

        # Botão de administração (visível apenas para administradores)
        if is_user_logged_in():
            if is_user_admin():
                admin_button = ctk.CTkButton(
                    self.button_frame, 
                    image=admin_icon_image,
                    text="", 
                    command=self.router.show_dashboard_page, 
                    font=("Arial", 20, "bold"), 
                    width=40, 
                    height=40,
                    fg_color=self.button_color, 
                    hover_color=self.button_hover,
                    text_color="#242424"
                )
                admin_button.pack(side="left", padx=10, pady=10)
            else:
                profile_button = ctk.CTkButton(
                    self.button_frame, 
                    image=user_icon_image,
                    text="", 
                    command=self.router.show_profile_page, 
                    font=("Arial", 20, "bold"), 
                    width=40, 
                    height=40,
                    fg_color=self.button_color, 
                    hover_color=self.button_hover,
                    text_color="#242424"
                )
                profile_button.pack(side="left", padx=10, pady=10)

    def logout_user(self):
        logout_user()
        self.router.show_index_page()
        self.update_header()