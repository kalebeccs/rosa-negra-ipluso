import customtkinter as ctk

class IndexPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        banner_image = ctk.CTkLabel(self, text="Banner Image", width=master.winfo_screenwidth(), height=200)
        banner_image.pack(pady=10)

        wine_frame = ctk.CTkFrame(self)
        wine_frame.pack(pady=20)

        for wine in ["Vinho 1", "Vinho 2", "Vinho 3"]:
            wine_card = ctk.CTkFrame(wine_frame, width=200, height=300)
            wine_card.pack(side="left", padx=10)
            wine_label = ctk.CTkLabel(wine_card, text=wine)
            wine_label.pack(pady=10)
