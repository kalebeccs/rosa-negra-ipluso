import os
import customtkinter as ctk
from PIL import Image

class IndexPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        
        # Seção de imagem e texto
        main_content_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_content_frame.pack(pady=20, padx=40, fill="x")

        # Imagem no lado esquerdo
        image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner-index.jpg')
        image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(300, 200))
        image_label = ctk.CTkLabel(main_content_frame, image=image, text="")
        image_label.pack(side="left", padx=20, pady=10)

        # Texto no lado direito
        text_label = ctk.CTkLabel(
            main_content_frame,
            text=(
                "Cada taça de vinho é um convite para uma jornada sensorial."
                "Do aroma delicado das frutas ao corpo rico e persistente no paladar,"
                "nossos vinhos foram selecionados para transformar qualquer ocasião em uma celebração."
                "Explore nossa galeria e descubra o vinho perfeito para cada momento." 
                "Brindemos juntos à tradição, ao sabor e à arte de viver bem!"
            ),
            font=("Arial", 14),
            text_color="white",
            wraplength=500,
            justify="left",
        )
        text_label.pack(side="right", padx=20, pady=10)

        # Título da seção
        title_label = ctk.CTkLabel(
            self,
            text="As nossas linhas de vinhos",
            font=("Arial", 24, "bold"),
            text_color="white",
        )
        title_label.pack(pady=20)

        # Grade de categorias de vinhos
        categories_frame = ctk.CTkFrame(self, fg_color="transparent")
        categories_frame.pack(pady=20, padx=40, fill="x")

        categories = [
            {"name": "Signature", "image": "signature-tinto.png", "description": "Vinhos exclusivos e de alta qualidade."},
            {"name": "Reserva", "image": "reserva-tinto.png", "description": "Vinhos envelhecidos para um sabor único."},
            {"name": "Mesa", "image": "mesa-tinto.png", "description": "Vinhos para o dia a dia, acessíveis e saborosos."},
            {"name": "Exotico", "image": "exotic-branco.png", "description": "Vinhos com sabores exóticos e diferenciados."}
        ]

        for i, category in enumerate(categories):
            card = ctk.CTkFrame(categories_frame, width=200, height=250, fg_color="transparent", border_color="#C9A234", border_width=2)
            card.grid(row=0, column=i, padx=10, pady=10, sticky="n")

            image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', category["image"])
            image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(200, 200))
            image_label = ctk.CTkLabel(card, image=image, text="")
            image_label.pack(pady=0)  # No padding to remove any space

            card_label = ctk.CTkLabel(card, text=category["name"], font=("Arial", 18, "bold"))
            card_label.pack(pady=5)

            description_label = ctk.CTkLabel(card, text=category["description"], font=("Arial", 12), wraplength=180, justify="center")
            description_label.pack(pady=5)

        categories_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Botão para abrir a tela de vinhos
        wines_button = ctk.CTkButton(
            self, 
            text="Ver Vinhos", 
            command=self.app.router.show_product_page, 
            font=("Arial", 16, "bold"), 
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#242424"
        )
        wines_button.pack(pady=20)