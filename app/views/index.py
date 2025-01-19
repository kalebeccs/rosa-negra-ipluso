import customtkinter as ctk

class IndexPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        banner_frame = ctk.CTkFrame(self, height=80, fg_color="lightgray", corner_radius=0)
        banner_frame.pack(fill="x")

        logo_label = ctk.CTkLabel(
            banner_frame, text="Rosa Negra\nVinhos - Garrafeira", font=("Arial", 14, "bold")
        )
        logo_label.place(relx=0.02, rely=0.5, anchor="w")

        nav_button_home = ctk.CTkButton(banner_frame, text="Home", width=100, command=self.go_home)
        nav_button_home.place(relx=0.7, rely=0.5, anchor="center")

        nav_button_garrafeira = ctk.CTkButton(
            banner_frame, text="Garrafeira", width=100, command=self.go_garrafeira
        )
        nav_button_garrafeira.place(relx=0.8, rely=0.5, anchor="center")

        icon_label = ctk.CTkLabel(
            banner_frame, text="Ícone", font=("Arial", 14), text_color="gray"
        )
        icon_label.place(relx=0.95, rely=0.5, anchor="e")

        # Seção de imagem e texto
        main_content_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_content_frame.pack(pady=20, padx=40, fill="x")

        # Imagem no lado esquerdo
        image_placeholder = ctk.CTkLabel(
            main_content_frame, text="IMAGEM", font=("Arial", 18, "bold"), width=300, height=200, fg_color="lightgray"
        )
        image_placeholder.grid(row=0, column=0, padx=20, pady=10)

        # Texto no lado direito
        text_label = ctk.CTkLabel(
            main_content_frame,
            text=(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu diam lacus, "
                "in hac habitasse platea dictumst. Suspendisse cursus efficitur mauris quis placerat. "
                "Nam vitae dui sit amet lacus tempus porttitor eu quis odio. Donec diam turpis, "
                "venenatis id odio nec, ullamcorper ornare nibh."
            ),
            font=("Arial", 14),
            text_color="black",
            wraplength=500,
            justify="left",
        )
        text_label.grid(row=0, column=1, padx=20, pady=10)

        # Título da seção
        title_label = ctk.CTkLabel(
            self,
            text="As nossas linhas de vinhos",
            font=("Arial", 24, "bold"),
            text_color="black",
        )
        title_label.pack(pady=20)

        # Grade de categorias de vinhos
        categories_frame = ctk.CTkFrame(self, fg_color="transparent")
        categories_frame.pack(pady=20, padx=40, fill="x")

        categories = ["Signature", "Reserva", "Mesa", "Exotic"]
        descriptions = [
            "Tinto, Branco.",
            "Tinto.",
            "Tinto, Branco.",
            "Branco Frisante, Rosé, Verde.",
        ]

        for index, (category, desc) in enumerate(zip(categories, descriptions)):
            category_frame = ctk.CTkFrame(
                categories_frame,
                width=200,
                height=150,
                corner_radius=10,
                fg_color="white",
            )
            category_frame.grid(row=0, column=index, padx=20, pady=10)

            # Título da categoria
            category_label = ctk.CTkLabel(
                category_frame, text=category, font=("Arial", 16, "bold"), text_color="darkblue"
            )
            category_label.pack(pady=(10, 5))

            # Descrição da categoria
            category_desc = ctk.CTkLabel(
                category_frame,
                text=desc,
                font=("Arial", 12),
                text_color="gray",
                wraplength=180,
                justify="center",
            )
            category_desc.pack(pady=(5, 10))

        # Botão final
        view_button = ctk.CTkButton(
            self, text="Ver Garrafeira", font=("Arial", 16, "bold"), width=200, command=self.view_garrafeira
        )
        view_button.pack(pady=30)

    def go_home(self):
        print("Navegar para Home.")

    def go_garrafeira(self):
        print("Navegar para Garrafeira.")

    def view_garrafeira(self):
        print("Ver Garrafeira.")

