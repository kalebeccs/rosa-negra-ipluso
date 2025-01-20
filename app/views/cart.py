import customtkinter as ctk
from app.global_state import get_current_user_cart, remove_from_cart

class CartPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Título da página
        title_label = ctk.CTkLabel(self, text="Carrinho de Compras", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Frame para exibir os itens do carrinho
        self.cart_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cart_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Botão para finalizar a compra
        checkout_button = ctk.CTkButton(
            self, 
            text="Finalizar Compra", 
            command=self.checkout,
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        checkout_button.pack(pady=20)

        # Exibir os itens do carrinho
        self.display_cart_items()

    def display_cart_items(self):
        # Limpar o frame do carrinho antes de exibir os itens
        for widget in self.cart_frame.winfo_children():
            widget.destroy()

        cart_items = get_current_user_cart()
        if not cart_items:
            empty_label = ctk.CTkLabel(self.cart_frame, text="Seu carrinho está vazio.", font=("Arial", 16))
            empty_label.pack(pady=10)
        else:
            for cart_item in cart_items:
                item = cart_item['item']
                quantity = cart_item['quantity']
                item_frame = ctk.CTkFrame(self.cart_frame, fg_color="#242424")
                item_frame.pack(pady=5, padx=10, fill="x")

                item_info = (
                    f"Nome: {item['name']}\n"
                    f"Preço: ${item['price']:.2f}\n"
                    f"Quantidade: {quantity}\n"
                )
                item_label = ctk.CTkLabel(item_frame, text=item_info, font=("Arial", 16), justify="left", text_color="white")
                item_label.pack(side="left", padx=10, pady=5)

                remove_button = ctk.CTkButton(item_frame, text="Remover", command=lambda i=item: self.remove_item(i))
                remove_button = ctk.CTkButton(
                    item_frame, 
                    text="Remover", 
                    command=lambda i=item: self.remove_item(i),
                    font=("Arial", 12, "bold"),
                    fg_color="#C9A234",
                    hover_color="#A88227",
                    text_color="#292929"
                )
                remove_button.pack(side="right", padx=10, pady=5)

    def remove_item(self, item):
        remove_from_cart(item)
        self.display_cart_items()
        
    def update_cart(self):
        self.display_cart_items()

    def checkout(self):
        # Lógica para finalizar a compra
        pass
