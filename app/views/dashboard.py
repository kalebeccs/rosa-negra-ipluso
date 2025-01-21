import customtkinter as ctk
from tkinter import ttk
from src.models.purchases import get_top_revenue_wines, get_top_selling_wines

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Título da página
        title_label = ctk.CTkLabel(self, text="Dashboard de Vendas", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Frame para a tabela de vendas
        self.sales_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.sales_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Tabela de vendas
        self.sales_table = ttk.Treeview(self.sales_frame, columns=("Type", "Name", "Quantity", "Total Value"), show="headings")
        self.sales_table.heading("Type", text="Tipo")
        self.sales_table.heading("Name", text="Nome")
        self.sales_table.heading("Quantity", text="Quantidade Vendida")
        self.sales_table.heading("Total Value", text="Valor Total")
        self.sales_table.pack(fill="both", expand=True)

        # Carregar os dados de vendas na tabela
        self.load_sales_data(get_top_selling_wines)

        # Frame para os botões
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10, padx=20, fill="x")

        # Botão para ir para a tela de gerenciamento de produtos
        manage_products_button = ctk.CTkButton(
            button_frame, 
            text="Gerir Vinhos", 
            command=self.app.router.show_product_management_page, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        manage_products_button.pack(side="right", padx=5)

        # Botão para atualizar a tabela com os vinhos de maior receita
        top_revenue_button = ctk.CTkButton(
            button_frame, 
            text="Top Vinhos por Receita", 
            command=lambda: self.load_sales_data(get_top_revenue_wines), 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        top_revenue_button.pack(side="right", padx=5)
        
        # Botão para atualizar a tabela com os vinhos mais vendidos
        top_selling_button = ctk.CTkButton(
            button_frame, 
            text="Top Vinhos Vendidos", 
            command=lambda: self.load_sales_data(get_top_selling_wines), 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        top_selling_button.pack(side="right", padx=5)

    def load_sales_data(self, data_function):
        sales_data = data_function()
        self.sales_table.delete(*self.sales_table.get_children())
        for sale in sales_data:
            total_value_sold = f"{sale['total_value_sold']:.2f}"
            self.sales_table.insert("", "end", values=(sale['wine_type'], sale['wine_name'], sale['total_quantity_sold'], total_value_sold))