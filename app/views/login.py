import customtkinter as ctk

from app.global_state import login_user
from src.models.users import get_user_details, verify_user_credentials

class LoginPage(ctk.CTkFrame):
    def __init__(self, master, app):
        """
        Initialize the LoginPage frame.

        Args:
            master: The parent widget.
            app: The application instance.
        """
        super().__init__(master)
        self.app = app

        # Configurar layout em 2 colunas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Primeira coluna - Conteúdo de login
        login_frame = ctk.CTkFrame(self)
        login_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Título da página
        title_label = ctk.CTkLabel(login_frame, text="Entrar", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Campo de entrada para o email
        email_label = ctk.CTkLabel(login_frame, text="Email")
        email_label.pack(pady=5)
        self.email_entry = ctk.CTkEntry(login_frame)
        self.email_entry.pack(pady=5)

        # Campo de entrada para a senha
        password_label = ctk.CTkLabel(login_frame, text="Senha")
        password_label.pack(pady=5)
        self.password_entry = ctk.CTkEntry(login_frame, show="*")
        self.password_entry.pack(pady=5)

        # Botão de login
        login_button = ctk.CTkButton(
            login_frame, 
            text="Entrar", 
            command=self.login_user, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        login_button.pack(pady=20)

        # Label para mensagens de status
        self.status_label = ctk.CTkLabel(login_frame, text="")
        self.status_label.pack(pady=5)

        # Segunda coluna - Botão de registro e frase
        register_frame = ctk.CTkFrame(self)
        register_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Centralizar conteúdo da segunda coluna
        register_frame.grid_columnconfigure(0, weight=1)
        register_frame.grid_rowconfigure(0, weight=1)
        register_frame.grid_rowconfigure(1, weight=1)
        register_frame.grid_rowconfigure(2, weight=1)

        # Frase
        phrase_label = ctk.CTkLabel(register_frame, text="Ainda não tem uma conta?")
        phrase_label.grid(row=1, column=0, pady=20)

        # Botão para ir para a página de registro
        register_button = ctk.CTkButton(
            register_frame, 
            text="Registe-se", 
            command=self.go_to_register, 
            font=("Arial", 12, "bold"),
            fg_color="#C9A234",
            hover_color="#A88227",
            text_color="#292929"
        )
        register_button.grid(row=2, column=0, pady=10)

    def login_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Verificar as credenciais do usuário
        if verify_user_credentials(email, password):
            user_details = get_user_details(email)
            login_user(user_details['id'], email, password, user_details['role'])
            # Navegar para a página inicial ou outra página após o login
            self.app.router.show_index_page()
        else:
            self.status_label.configure(text="Email ou senha invalido!", text_color="gray")

        # Limpar os campos de entrada após o login
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')

    def go_to_register(self):
        self.app.router.show_register_page()