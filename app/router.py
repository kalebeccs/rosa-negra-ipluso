import logging

from app.views.index import IndexPage
from app.views.products import ProductPage
from app.views.cart import CartPage
from app.views.login import LoginPage
from app.views.register import RegisterPage
from app.views.profile import ProfilePage
from app.views.dashboard import DashboardPage
from app.views.product_management import ProductManagementPage
from app.views.add_wine import AddWinePage 

class Router:
    """
    Router class to manage navigation between different pages of the application.

    Attributes:
        app (WineApp): Instance of the main application.
        pages (dict): Dictionary containing instances of the pages.

    Methods:
        initialize_pages(): Initializes all pages and stores them in the pages dictionary.
        navigate_to(page_name): Displays the requested page by name.
        show_index_page(): Displays the index page.
        show_product_page(): Displays the product page.
        show_cart_page(): Displays the cart page.
        show_login_page(): Displays the login page.
        show_register_page(): Displays the register page.
        show_profile_page(): Displays the profile page.
        show_dashboard_page(): Displays the dashboard page.
        show_product_management_page(): Displays the product management page.
    """
    def __init__(self, app):
        self.app = app
        self.pages = {}
        
    def initialize_pages(self):
        self.pages = {
            "index": IndexPage(self.app.content, self.app),
            "product": ProductPage(self.app.content),
            "cart": CartPage(self.app.content, self.app),
            "login": LoginPage(self.app.content, self.app),
            "register": RegisterPage(self.app.content, self.app),
            "profile": ProfilePage(self.app.content, self.app),
            "dashboard": DashboardPage(self.app.content, self.app),
            "product_management": ProductManagementPage(self.app.content, self.app),
            "add_wine": AddWinePage(self.app.content, self.app),
        }

    def navigate_to(self, page_name):
        """
        Displays the requested page by name.

        :param page_name: Name of the page to be displayed.
        """
        if page_name not in self.pages:
            logging.error(f"Page '{page_name}' does not exist.")
        
        self.app.clear_frame()
        self.app.title(f"{page_name.capitalize()} - Rosa Negra")
        self.pages[page_name].pack(fill="both", expand=True)
        
        if page_name == "cart":
            self.pages[page_name].update_cart()
        elif page_name == "profile":
            self.pages[page_name].load_user_details()
        
        

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
        
    def show_add_wine_page(self):
        self.navigate_to("add_wine")
