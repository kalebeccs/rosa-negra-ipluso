import customtkinter as ctk

class ProfilePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Profile Page")
        label.pack(pady=20)
        # Adicione mais widgets e lógica aqui
