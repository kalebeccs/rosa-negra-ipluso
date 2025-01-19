import customtkinter as ctk
import os
from PIL import Image, ImageTk
from app.views.index import IndexPage
from app.views.products import ProductPage
from app.views.cart import CartPage
from app.views.login import LoginPage
from app.views.register import RegisterPage
from app.views.profile import ProfilePage
from app.views.dashboard import DashboardPage
from app.views.product_management import ProductManagementPage
from app.views.user_management import UserManagementPage
from app.views.purchase_management import PurchaseManagementPage

class WineApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico'))
        self.title("Tela Inicial - Rosa Negra")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_header()
        self.create_footer()

        self.content = ctk.CTkFrame(self)
        self.content.pack(side="top", fill="both", expand=True)

        self.show_index_page()

    def create_header(self):
        self.header = ctk.CTkFrame(self, height=50)
        self.header.pack(side="top", fill="x", pady=16, padx=16)

        title_label = ctk.CTkLabel(self.header, text="Rosa Negra", font=("Arial", 32))
        title_label.pack(side="left", padx=10)

        button_frame = ctk.CTkFrame(self.header)
        button_frame.pack(side="right", padx=10)

        home_button = ctk.CTkButton(button_frame, text="Home", command=self.show_index_page, font=("Arial", 16, "bold"), width=48)
        home_button.pack(side="left", padx=5)

        wines_button = ctk.CTkButton(button_frame, text="Vinhos", command=self.show_product_page, font=("Arial", 16, "bold"), width=48)
        wines_button.pack(side="left", padx=5)

        cart_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'cart-icon.png')
        cart_icon_image = ImageTk.PhotoImage(Image.open(cart_icon_path).resize((20, 20)))
        
        cart_button = ctk.CTkButton(button_frame, image=cart_icon_image, text="", command=self.show_cart_page, width=30)
        cart_button.image = cart_icon_image
        cart_button.pack(side="left", padx=5)
        
        user_icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'user-icon.png')
        user_icon_image = ImageTk.PhotoImage(Image.open(user_icon_path).resize((20, 20)))

        login_button = ctk.CTkButton(button_frame, image=user_icon_image, text="", command=self.show_login_page, width=30)
        login_button.image = user_icon_image
        login_button.pack(side="left", padx=5)

    def create_footer(self):
        self.footer = ctk.CTkFrame(self, height=50)
        self.footer.pack(side="bottom", fill="x")
        footer_label = ctk.CTkLabel(self.footer, text="© Rosa Negra - 2025")
        footer_label.pack(pady=10)

    def show_index_page(self):
        self.clear_frame()
        IndexPage(self.content).pack(fill="both", expand=True)

    def show_product_page(self):
        self.clear_frame()
        ProductPage(self.content).pack(fill="both", expand=True)

    def show_cart_page(self):
        self.clear_frame()
        CartPage(self.content).pack(fill="both", expand=True)

    def show_login_page(self):
        self.clear_frame()
        LoginPage(self.content).pack(fill="both", expand=True)

    def show_register_page(self):
        self.clear_frame()
        RegisterPage(self.content).pack(fill="both", expand=True)

    def show_profile_page(self):
        self.clear_frame()
        ProfilePage(self.content).pack(fill="both", expand=True)

    def show_dashboard_page(self):
        self.clear_frame()
        DashboardPage(self.content).pack(fill="both", expand=True)

    def show_product_management_page(self):
        self.clear_frame()
        ProductManagementPage(self.content).pack(fill="both", expand=True)

    def show_user_management_page(self):
        self.clear_frame()
        UserManagementPage(self.content).pack(fill="both", expand=True)

    def show_purchase_management_page(self):
        self.clear_frame()
        PurchaseManagementPage(self.content).pack(fill="both", expand=True)

    def clear_frame(self):
        for widget in self.content.winfo_children():
            widget.destroy()

def create_app():
    return WineApp()