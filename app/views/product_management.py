import customtkinter as ctk
from tkinter import messagebox, ttk
from src.models.wines import delete_wine, get_all_wines, get_wine_by_id, update_wine

class ProductManagementPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Título da página
        title_label = ctk.CTkLabel(self, text="Gestão de Produtos", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Frame para a tabela de vinhos
        self.table_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Tabela de vinhos
        self.wine_table = ttk.Treeview(self.table_frame, columns=("ID", "Brand", "Name", "Price", "Type", "Alcohol", "Year", "Region", "Description"), show="headings")
        self.wine_table.heading("ID", text="ID")
        self.wine_table.heading("Brand", text="Brand")
        self.wine_table.heading("Name", text="Name")
        self.wine_table.heading("Price", text="Price")
        self.wine_table.heading("Type", text="Type")
        self.wine_table.heading("Alcohol", text="Alcohol")
        self.wine_table.heading("Year", text="Year")
        self.wine_table.heading("Region", text="Region")
        self.wine_table.heading("Description", text="Description")
        self.wine_table.pack(fill="both", expand=True)

        # Bind para selecionar uma linha da tabela
        self.wine_table.bind("<<TreeviewSelect>>", self.on_row_select)

        # Campos individuais para editar os detalhes do vinho
        self.fields_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.fields_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.brand_entry = self.create_entry("Brand")
        self.name_entry = self.create_entry("Name")
        self.price_entry = self.create_entry("Price")
        self.type_entry = self.create_entry("Type")
        self.alcohol_entry = self.create_entry("Alcohol")
        self.year_entry = self.create_entry("Year")
        self.region_entry = self.create_entry("Region")
        self.description_entry = self.create_entry("Description")

        # Botão para salvar as alterações
        save_button = ctk.CTkButton(
            self, 
            text="Salvar Alterações", 
            command=self.save_changes, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        save_button.pack(pady=20)
        
        # Botão para excluir o vinho selecionado
        delete_button = ctk.CTkButton(
            self, 
            text="Excluir Vinho", 
            command=self.delete_wine, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        delete_button.pack(pady=10)
        
        # Botão para adicionar um novo vinho
        add_button = ctk.CTkButton(
            self, 
            text="Adicionar Novo Vinho", 
            command=self.app.router.show_add_wine_page, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        add_button.pack(pady=10)
        
        # Botão para voltar à página de dashboard
        back_button = ctk.CTkButton(
            self, 
            text="Voltar ao Dashboard", 
            command=self.app.router.show_dashboard_page, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        back_button.pack(pady=10)
        
        # Carregar os dados dos vinhos na tabela
        self.load_wine_data()

    def create_entry(self, label_text):
        label = ctk.CTkLabel(self.fields_frame, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self.fields_frame)
        entry.pack(pady=5)
        return entry

    def load_wine_data(self):
        wines = get_all_wines()
        for wine in wines:
            self.wine_table.insert("", "end", values=(wine['pk_wine'], wine['brand'], wine['name'], wine['price'], wine['type'], wine['alcohol'], wine['year'], wine['region'], wine['description']))

    def clear_table(self):
        for item in self.wine_table.get_children():
            self.wine_table.delete(item)

    def on_row_select(self, event):
        if not self.wine_table.selection():
            return
        selected_item = self.wine_table.selection()[0]
        wine_id = self.wine_table.item(selected_item, "values")[0]
        wine = get_wine_by_id(wine_id)
        if wine:
            self.brand_entry.delete(0, 'end')
            self.brand_entry.insert(0, wine['brand'])
            self.name_entry.delete(0, 'end')
            self.name_entry.insert(0, wine['name'])
            self.price_entry.delete(0, 'end')
            self.price_entry.insert(0, wine['price'])
            self.type_entry.delete(0, 'end')
            self.type_entry.insert(0, wine['type'])
            self.alcohol_entry.delete(0, 'end')
            self.alcohol_entry.insert(0, wine['alcohol'])
            self.year_entry.delete(0, 'end')
            self.year_entry.insert(0, wine['year'])
            self.region_entry.delete(0, 'end')
            self.region_entry.insert(0, wine['region'])
            self.description_entry.delete(0, 'end')
            self.description_entry.insert(0, wine['description'])

    def save_changes(self):
        if not self.wine_table.selection():
            return
        selected_item = self.wine_table.selection()[0]
        wine_id = self.wine_table.item(selected_item, "values")[0]
        update_wine(
            pk_wine=wine_id,
            brand=self.brand_entry.get(),
            name=self.name_entry.get(),
            price=self.price_entry.get(),
            type=self.type_entry.get(),
            alcohol=self.alcohol_entry.get(),
            year=self.year_entry.get(),
            region=self.region_entry.get(),
            description=self.description_entry.get()
        )
        self.wine_table.selection_remove(selected_item)
        self.clear_table()
        self.load_wine_data()

    def delete_wine(self):
        if not self.wine_table.selection():
            return
        selected_item = self.wine_table.selection()[0]
        wine_id = self.wine_table.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Confirmação", "Tem certeza de que deseja excluir este vinho?")
        if confirm:
            delete_wine(wine_id)
            self.clear_table()
            self.load_wine_data()