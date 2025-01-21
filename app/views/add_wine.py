import customtkinter as ctk
from src.models.wines import insert_wine
from src.utils import validate_required_fields

class AddWinePage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Título da página
        title_label = ctk.CTkLabel(self, text="Adicionar Vinho", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Campos de entrada para os detalhes do vinho
        self.name_entry = self.create_entry("Nome")
        self.price_entry = self.create_entry("Preço")
        label = ctk.CTkLabel(self, text="Tipo")
        label.pack(pady=5)
        self.type_combobox = ctk.CTkComboBox(self, values=["Mesa", "Exotico", "Reserva", "Signature"])
        self.type_combobox.pack(pady=5)
        self.alcohol_entry = self.create_entry("Alcool (%)")
        self.year_entry = self.create_entry("Ano (AAAA)")
        self.region_entry = self.create_entry("Região")
        self.description_entry = self.create_entry("Descrição")

        # Botão para adicionar o vinho
        add_button = ctk.CTkButton(
            self, 
            text="Adicionar Vinho", 
            command=self.add_wine, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        add_button.pack(pady=20)

        # Botão para voltar à página de gestão de produtos
        back_button = ctk.CTkButton(
            self, 
            text="Voltar à Gestão de Produtos", 
            command=self.app.router.show_product_management_page, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        back_button.pack(pady=10)

        # Label para mostrar o status
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)
        

    def create_entry(self, label_text):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self)
        entry.pack(pady=5)
        return entry

    def add_wine(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        type = self.type_combobox.get()
        alcohol = self.alcohol_entry.get()
        year = self.year_entry.get()
        region = self.region_entry.get()
        description = self.description_entry.get()

        if not validate_required_fields(name, price, type, alcohol, year, region, description):
            self.status_label.configure(text="Por favor, preencha todos os campos.", text_color="gray")
            return

        if not (self.validate_price(price) and self.validate_alcohol(alcohol) and self.validate_year(year)):
            return

        insert_wine('Rosa Negra', name, price, type, alcohol, year, region, description)
        self.clear_entries()
        self.status_label.configure(text="Vinho adicionado com sucesso!", text_color="gray")
        
    def validate_price(self, price):
        try:
            price = float(price)
            return True
        except ValueError:
            self.status_label.configure(text="Por favor, insira um valor válido para o preço.", text_color="gray")
            return False

    def validate_alcohol(self, alcohol):
        try:
            alcohol = float(alcohol)
            return True
        except ValueError:
            self.status_label.configure(text="Por favor, insira um valor válido para o teor alcoólico.", text_color="gray")
            return False

    def validate_year(self, year):
        try:
            year = int(year)
            if len(str(year)) != 4:
                raise ValueError("Year must be in YYYY format")
            return True
        except ValueError:
            self.status_label.configure(text="Por favor, insira um valor válido para o ano (YYYY).", text_color="gray")
            return False

    def clear_entries(self):
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.type_combobox.set('Mesa')
        self.alcohol_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.region_entry.delete(0, 'end')
        self.description_entry.delete(0, 'end')
