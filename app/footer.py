import customtkinter as ctk

class Footer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=50)
        self.pack(side="bottom", fill="x")
        footer_label = ctk.CTkLabel(self, text="© Rosa Negra - 2025")
        footer_label.pack(pady=10)
