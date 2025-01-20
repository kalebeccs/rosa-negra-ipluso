import customtkinter as ctk
from app.global_state import get_current_user_id, get_current_user_email, get_current_user_password, get_current_user_role
from src.models.users import get_user_details_by_id, update_user_details

class ProfilePage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app

        # Título da página
        title_label = ctk.CTkLabel(self, text="Perfil do Usuário", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Campos de entrada para as informações do usuário
        self.name_entry = self.create_entry("Nome")
        self.dob_entry = self.create_entry("Data de Nascimento (YYYY-MM-DD)")
        self.email_entry = self.create_entry("Email")
        self.password_entry = self.create_entry("Senha", show="*")
        self.vat_number_entry = self.create_entry("Número de NIF")
        self.address_1_entry = self.create_entry("Endereço 1")
        self.address_2_entry = self.create_entry("Endereço 2")

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

        # Carregar as informações do usuário
        self.load_user_details()

    def create_entry(self, label_text, show=None):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self, show=show)
        entry.pack(pady=5)
        return entry

    def load_user_details(self):
        user_id = get_current_user_id()
        user_details = get_user_details_by_id(user_id)
        if user_details:
            self.name_entry.insert(0, user_details['name'])
            self.dob_entry.insert(0, user_details['dob'])
            self.email_entry.insert(0, user_details['email'])
            self.password_entry.insert(0, user_details['password_hash'])
            self.vat_number_entry.insert(0, user_details.get('vat_number', ''))
            self.address_1_entry.insert(0, user_details.get('address_1', ''))
            self.address_2_entry.insert(0, user_details.get('address_2', ''))

    def save_changes(self):
        user_id = get_current_user_id()
        updated_details = {
            'name': self.name_entry.get(),
            'dob': self.dob_entry.get(),
            'email': self.email_entry.get(),
            'password_hash': self.password_entry.get(),
            'vat_number': self.vat_number_entry.get(),
            'address_1': self.address_1_entry.get(),
            'address_2': self.address_2_entry.get(),
        }
        update_user_details(user_id, updated_details)
        self.app.header.update_header()
        self.app.router.show_index_page()