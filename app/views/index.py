import os
import customtkinter as ctk
from PIL import Image

class IndexPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        
        # Seção de imagem e texto
        main_content_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_content_frame.pack(pady=20, padx=5, fill="x")

        # Imagem no lado esquerdo
        image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'banner-index.jpg')
        image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(450, 350))
        image_label = ctk.CTkLabel(main_content_frame, image=image, text="")
        image_label.pack(side="left", padx=(0,10), pady=5)

        # Texto no lado direito
        text_label = ctk.CTkLabel(
            main_content_frame,
            text=(
                "O vinho é muito mais do que uma bebida: é uma expressão de história, "
                "cultura e paixão. Cada garrafa carrega consigo a alma do terroir de onde foi produzida, "
                "combinando a riqueza do solo, o clima único e o cuidado dos viticultores que transformam "
                "uvas em verdadeiras obras de arte. "
                "Nosso catálogo celebra a diversidade dos vinhos, abrangendo desde os clássicos tintos encorpados "
                "até os delicados brancos e os vibrantes rosés. Além disso, oferecemos opções exclusivas de vinhos frizantes, "
                "verdes e reservas, cada um cuidadosamente selecionado para proporcionar uma experiência sensorial única."
            ),
            font=("Arial", 14),
            text_color="white",
            wraplength=500,
            justify="left",
        )
        text_label.pack(side="left", padx=(10,0), pady=5)

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
            {"image": "card-signature.png", "description": "Vinhos autorais, refinados e exclusivos, ideais para aqueles que buscam sofisticação."},
            {"image": "card-reserva.png", "description": "Produzidos com as melhores uvas e envelhecidos com perfeição, entregando sabor e complexidade excepcionais."},
            {"image": "card-mesa.png", "description": "Versáteis e acessíveis, perfeitos para acompanhar os momentos do dia a dia."},
            {"image": "card-exotic.png", "description": "Opções inusitadas, como verdes e frizantes, que surpreendem o paladar com frescor e originalidade."}
        ]

        # Cores para as bordas, na ordem desejada
        border_colors = ["#000000", "#5b0202", "#736055", "#fbf8e3"]

        for i, category in enumerate(categories):
            card = ctk.CTkFrame(
                categories_frame, 
                width=320, 
                height=250, 
                fg_color="transparent", 
                border_color=border_colors[i % len(border_colors)],  # Alternar as cores na ordem especificada
                border_width=4
            )
            card.grid(row=0, column=i, padx=10, pady=10, sticky="n")

            image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', category["image"])
            image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(200, 200))
            image_label = ctk.CTkLabel(card, image=image, text="")
            image_label.pack(pady=0)  # No padding to remove qualquer espaço

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
