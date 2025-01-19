import customtkinter as ctk

class UserManagementPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        label_titulo = ctk.CTkLabel(self, text="User Management Page", font = ("Arial", 24))
        label_titulo.pack(pady=20)
        # Adicione mais widgets e lógica aqui
