import customtkinter as ctk

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Register Page")
        label.pack(pady=20)
        # Adicione mais widgets e lógica aqui
