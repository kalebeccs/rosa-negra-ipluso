import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Login Page")
        label.pack(pady=20)
        # Adicione mais widgets e lógica aqui
