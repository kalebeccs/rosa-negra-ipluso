import customtkinter as ctk

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        label = ctk.CTkLabel(self, text="Dashboard Page")
        label.pack(pady=20)
        # Adicione mais widgets e lógica aqui
