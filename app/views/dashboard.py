import customtkinter as ctk
from src.models.purchases import get_all_purchases

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

        # Exibir a tabela de vendas
        self.display_sales_table()

    def display_sales_table(self):
        sales_data = get_all_purchases()

        if not sales_data:
            empty_label = ctk.CTkLabel(self.sales_frame, text="Nenhuma venda encontrada.", font=("Arial", 16))
            empty_label.pack(pady=10)
        else:
            # Cabeçalhos da tabela
            headers = ["ID", "Usuário", "Valor Total", "Itens", "Data"]
            for col, header in enumerate(headers):
                header_label = ctk.CTkLabel(self.sales_frame, text=header, font=("Arial", 16, "bold"))
                header_label.grid(row=0, column=col, padx=10, pady=5)

            # Dados da tabela
            for row, sale in enumerate(sales_data, start=1):
                sale_id = sale['purchase_id']
                user_id = sale['user_id']
                total_value = sale['total_value']
                items = ", ".join([f"{item['wine_id']} (x{item['quantity']})" for item in sale['items']])
                date = sale.get('date', 'N/A')  # Adicione a data se disponível

                ctk.CTkLabel(self.sales_frame, text=sale_id, font=("Arial", 14)).grid(row=row, column=0, padx=10, pady=5)
                ctk.CTkLabel(self.sales_frame, text=user_id, font=("Arial", 14)).grid(row=row, column=1, padx=10, pady=5)
                ctk.CTkLabel(self.sales_frame, text=f"€{total_value:.2f}", font=("Arial", 14)).grid(row=row, column=2, padx=10, pady=5)
                ctk.CTkLabel(self.sales_frame, text=items, font=("Arial", 14)).grid(row=row, column=3, padx=10, pady=5)
                ctk.CTkLabel(self.sales_frame, text=date, font=("Arial", 14)).grid(row=row, column=4, padx=10, pady=5)