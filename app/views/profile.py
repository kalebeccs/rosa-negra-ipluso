from tkinter import messagebox
import customtkinter as ctk

from app.global_state import get_current_user_id, logout_user
from src.models.users import delete_user, get_user_details_by_id, update_user_details
from src.utils import is_of_age, validate_dob, validate_email, validate_required_fields, validate_vat_number

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

        # Botão para remover o usuário
        delete_button = ctk.CTkButton(
            self, 
            text="Remover Usuário", 
            command=self.delete_account,
            font=("Arial", 12, "bold"),
            fg_color="#FF6347",
            hover_color="#FF4500",
            text_color="#FFFFFF"
        )
        delete_button.pack(pady=10)
        
        # Label para exibir o status das modificações
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)
        
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
        name = self.name_entry.get()
        email = self.email_entry.get()
        dob = self.dob_entry.get()
        password = self.password_entry.get()
        vat_number = self.vat_number_entry.get()

        # Verificar se todos os campos foram preenchidos usando a função validate_required_fields
        if not validate_required_fields(name, email, dob, password):
            self.status_label.configure(text="Todos os campos devem ser preenchidos!", text_color="gray")
            return

        # Validar o formato do email usando a função validate_email
        if not validate_email(email):
            self.status_label.configure(text="Email inválido!", text_color="gray")
            return

        # Validar o formato da data de nascimento usando a função validate_dob
        if not validate_dob(dob):
            self.status_label.configure(text="Data de nascimento inválida! Use AAAA-MM-DD.", text_color="gray")
            return

        # Verificar se a idade é menor que 18 anos usando a função is_of_age
        if not is_of_age(dob, 18):
            self.status_label.configure(text="Você deve ter pelo menos 18 anos para se registrar.", text_color="gray")
            return
        
        # Validar o NIF usando a função validate_vat_number
        if vat_number and not validate_vat_number(vat_number):
            self.status_label.configure(text="Número de IVA inválido!", text_color="gray")
            return

        user_id = get_current_user_id()
        updated_details = {
            'name': name,
            'dob': dob,
            'email': email,
            'password_hash': password,
            'vat_number': vat_number,
            'address_1': self.address_1_entry.get(),
            'address_2': self.address_2_entry.get(),
        }
        update_user_details(user_id, updated_details)
        self.app.header.update_header()
        self.status_label.configure(text="Alterações salvas com sucesso!", text_color="gray")

    def delete_account(self):
        confirm = messagebox.askyesno("Confirmação", "Tem certeza de que deseja excluir sua conta?")
        if confirm:
            user_id = get_current_user_id()
            delete_user(user_id)
            logout_user()
            self.app.header.update_header()
            self.app.router.show_login_page()
            self.status_label.configure(text="Conta excluída com sucesso!", text_color="gray")
