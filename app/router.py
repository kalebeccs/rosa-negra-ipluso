from app.views.index import IndexPage
from app.views.product import ProductPage
from app.views.cart import CartPage
from app.views.login import LoginPage
from app.views.register import RegisterPage
from app.views.profile import ProfilePage
from app.views.dashboard import DashboardPage
from app.views.product_management import ProductManagementPage
from app.views.user_management import UserManagementPage
from app.views.purchase_management import PurchaseManagementPage

class Router:
    def __init__(self, app):
        self.app = app
        self.pages = {}
        
    def initialize_pages(self):
        # Inicializar as páginas
        self.pages = {
            "index": IndexPage(self.app.content),
            "product": ProductPage(self.app.content),
            "cart": CartPage(self.app.content),
            "login": LoginPage(self.app.content),
            "register": RegisterPage(self.app.content),
            "profile": ProfilePage(self.app.content),
            "dashboard": DashboardPage(self.app.content),
            "product_management": ProductManagementPage(self.app.content),
            "user_management": UserManagementPage(self.app.content),
            "purchase_management": PurchaseManagementPage(self.app.content),
        }

    def navigate_to(self, page_name):
        """
        Exibe a página solicitada pelo nome.
        """
        if page_name not in self.pages:
            raise ValueError(f"Page '{page_name}' does not exist.")
        
        self.app.clear_frame()  # Limpar o conteúdo atual
        self.app.title(f"{page_name.capitalize()} - Rosa Negra")  # Atualizar título
        self.pages[page_name].pack(fill="both", expand=True)

    # Métodos específicos para facilitar o acesso a páginas principais
    def show_index_page(self):
        self.navigate_to("index")

    def show_product_page(self):
        self.navigate_to("product")

    def show_cart_page(self):
        self.navigate_to("cart")

    def show_login_page(self):
        self.navigate_to("login")

    def show_register_page(self):
        self.navigate_to("register")

    def show_profile_page(self):
        self.navigate_to("profile")

    def show_dashboard_page(self):
        self.navigate_to("dashboard")

    def show_product_management_page(self):
        self.navigate_to("product_management")

    def show_user_management_page(self):
        self.navigate_to("user_management")

    def show_purchase_management_page(self):
        self.navigate_to("purchase_management")
