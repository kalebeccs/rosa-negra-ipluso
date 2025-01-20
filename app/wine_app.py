import os
import customtkinter as ctk

from app.router import Router
from app.header import Header
from app.footer import Footer

class WineApp(ctk.CTk):
    def __init__(self, appearance_mode="dark", color_theme="dark-blue"):
        super().__init__()
        self.setup_window()
        self.setup_appearance(appearance_mode, color_theme)
        self.create_router()
        self.create_layout()
        self.initialize_pages()
        self.show_index_page()

    def setup_window(self):
        """Set up the main window properties."""
        self.geometry("1280x720")
        self.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico'))
        self.title("Home - Rosa Negra")

    def setup_appearance(self, appearance_mode, color_theme):
        """Set up the appearance mode and color theme."""
        ctk.set_appearance_mode(appearance_mode)
        ctk.set_default_color_theme(color_theme)
        
    def create_layout(self):
        """Create the layout including header, content frame, and footer."""
        self.header = Header(self, self.router)
        self.header.pack(side="top", fill="x")

        self.content = ctk.CTkScrollableFrame(self)
        self.content.pack(side="top", fill="both", expand=True)

        self.footer = Footer(self)
        self.footer.pack(side="bottom", fill="x")

    def create_content_frame(self):
        """Create the main content frame for the application."""
        self.content = ctk.CTkFrame(self)
        self.content.pack(side="top", fill="both", expand=True)

    def create_router(self):
        """Create the router."""
        self.router = Router(self)

    def initialize_pages(self):
        """Initialize the pages."""
        self.router.initialize_pages()

    def show_index_page(self):
        """Show the index page."""
        self.router.show_index_page()

    def create_header(self):
        """Create the header."""
        self.header = Header(self, self.router)

    def create_footer(self):
        """Create the footer."""
        self.footer = Footer(self)

    def clear_frame(self):
        """Clear all widgets from the content frame."""
        for widget in self.content.winfo_children():
            widget.pack_forget()


def create_app():
    """Create and return an instance of WineApp."""
    return WineApp()
