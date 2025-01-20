import customtkinter as ctk
from src.models.users import insert_user
import re

class RegisterPage(ctk.CTkFrame):
    def __init__(self, master, app):
        """
        Initialize the RegisterPage frame.

        Args:
            master: The parent widget.
            app: The application instance.
        """
        super().__init__(master)
        self.app = app

        # Configurar layout em 2 colunas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Primeira coluna - Conteúdo de registro
        register_frame = ctk.CTkFrame(self)
        register_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Título da página
        title_label = ctk.CTkLabel(register_frame, text="Pagina de registro", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Campo de entrada para o nome
        name_label = ctk.CTkLabel(register_frame, text="Nome")
        name_label.pack(pady=5)
        self.name_entry = ctk.CTkEntry(register_frame)
        self.name_entry.pack(pady=5)

        # Campo de entrada para o email
        email_label = ctk.CTkLabel(register_frame, text="Email")
        email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(register_frame)
        self.email_entry.pack(pady=5)

        # Campo de entrada para a data de nascimento
        dob_label = ctk.CTkLabel(register_frame, text="Data de nascimento (YYYY-MM-DD)")
        dob_label.pack(pady=5)
        self.dob_entry = ctk.CTkEntry(register_frame)
        self.dob_entry.pack(pady=5)

        # Campo de entrada para a senha
        password_label = ctk.CTkLabel(register_frame, text="Senha")
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(register_frame, show="*")
        self.password_entry.pack(pady=5)

        # Botão de registro
        register_button = ctk.CTkButton(
            register_frame, 
            text="Registrar", 
            command=self.register_user, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        register_button.pack(pady=20)

        # Label para status do registro
        self.status_label = ctk.CTkLabel(register_frame, text="")
        self.status_label.pack(pady=5)

        # Segunda coluna - Botão de voltar para o login
        back_frame = ctk.CTkFrame(self)
        back_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Centralizar conteúdo da segunda coluna
        back_frame.grid_columnconfigure(0, weight=1)
        back_frame.grid_rowconfigure(0, weight=1)
        back_frame.grid_rowconfigure(1, weight=1)
        back_frame.grid_rowconfigure(2, weight=1)
        back_frame.grid_rowconfigure(3, weight=1)

        # Frase "Já tem uma conta?"
        question_label = ctk.CTkLabel(back_frame, text="Já tem uma conta?", font=("Arial", 14))
        question_label.grid(row=1, column=0, pady=10)

        # Botão para voltar à tela de login
        back_button = ctk.CTkButton(
            back_frame, 
            text="Voltar ao Login", 
            command=self.back_to_login, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        back_button.grid(row=2, column=0, pady=10)

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        dob = self.dob_entry.get()
        password = self.password_entry.get()

        # Verificar se todos os campos foram preenchidos
        if not name or not email or not dob or not password:
            self.status_label.configure(text="Todos os campos devem ser preenchidos!", text_color="gray")
            return

        # Validar o formato do email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            self.status_label.configure(text="Email inválido!", text_color="gray")
            return

        # Validar o formato da data de nascimento
        dob_regex = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(dob_regex, dob):
            self.status_label.configure(text="Data de nascimento inválida! Use YYYY-MM-DD.", text_color="gray")
            return

        # Aqui você pode adicionar a lógica para registrar o usuário, por exemplo, chamando uma função para inserir os dados no banco de dados
        insert_user(name, dob, email, password, role="user")

        # Limpar os campos de entrada após o registro
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.dob_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

        # Exibir uma mensagem de sucesso
        self.status_label.configure(text="Usuário registrado com sucesso!", text_color="gray")

    def back_to_login(self):
        self.app.router.show_login_page()