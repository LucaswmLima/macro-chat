import json
import os


LANGUAGE_FILE = "language.json"

TRANSLATIONS = {
    "en": {
        "settings": "Settings",
        "configure_buttons": "Configure buttons",
        "language": "Language",
        "help": "Help",
        "chat": "CHAT",
        "chat_placeholder": "Messages will appear here...",
        "clear_chat": "Clear chat",

        "reorder_hint": "Use ↑ and ↓ to change the button order.",
        "add_button": "+  Add button",
        "close": "Close",

        "edit_button": "Edit button",
        "new_button": "New button",
        "button_name": "Button name",
        "button_text": "Text that will be sent to chat",
        "cancel": "Cancel",
        "save": "Save",

        "delete_button": "Delete button",
        "delete_title": "Delete button",
        "delete_message": 'Delete button "{button_name}"?',
        "yes": "Yes",
        "no": "No",

        "empty_name_title": "Empty name",
        "empty_name_message": "Enter a name for the button.",
        "empty_text_title": "Empty text",
        "empty_text_message": "Enter the text that will be sent to chat.",

        "move_up": "Move up",
        "move_down": "Move down",

        "help_title": "Help",
        "help_text": (
            "<b>How to use</b><br><br>"
            "Click a button to add its message to the chat.<br><br>"
            "Use <b>⚙ Settings</b> to create, edit, delete "
            "or reorder buttons."
        ),

        "english": "English",
        "portuguese": "Português (Brasil)",
    },

    "pt-BR": {
        "settings": "Configurar",
        "configure_buttons": "Configurar botões",
        "language": "Idioma",
        "help": "Help",
        "chat": "CHAT",
        "chat_placeholder": "As mensagens aparecerão aqui...",
        "clear_chat": "Limpar chat",

        "reorder_hint": "Use ↑ e ↓ para alterar a ordem dos botões.",
        "add_button": "+  Adicionar botão",
        "close": "Fechar",

        "edit_button": "Editar botão",
        "new_button": "Novo botão",
        "button_name": "Nome do botão",
        "button_text": "Texto que será enviado ao chat",
        "cancel": "Cancelar",
        "save": "Salvar",

        "delete_button": "Excluir botão",
        "delete_title": "Excluir botão",
        "delete_message": 'Excluir o botão "{button_name}"?',
        "yes": "Sim",
        "no": "Não",

        "empty_name_title": "Nome vazio",
        "empty_name_message": "Digite um nome para o botão.",
        "empty_text_title": "Texto vazio",
        "empty_text_message": "Digite o texto que será enviado ao chat.",

        "move_up": "Mover para cima",
        "move_down": "Mover para baixo",

        "help_title": "Help",
        "help_text": (
            "<b>Como usar</b><br><br>"
            "Clique em um botão para adicionar sua mensagem ao chat.<br><br>"
            "Use <b>⚙ Configurar</b> para criar, editar, excluir "
            "ou reorganizar botões."
        ),

        "english": "English",
        "portuguese": "Português (Brasil)",
    },
}


class Language:
    def __init__(self):
        self.current = self.load()

    def load(self):
        if not os.path.exists(LANGUAGE_FILE):
            return "en"

        try:
            with open(
                LANGUAGE_FILE,
                "r",
                encoding="utf-8",
            ) as file:
                data = json.load(file)

            language = data.get("language")

            if language in TRANSLATIONS:
                return language

        except Exception:
            pass

        return "en"

    def set(self, language):
        if language not in TRANSLATIONS:
            return

        self.current = language

        with open(
            LANGUAGE_FILE,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                {"language": language},
                file,
                ensure_ascii=False,
                indent=4,
            )

    def get(self, key, **kwargs):
        text = TRANSLATIONS[self.current].get(
            key,
            key,
        )

        if kwargs:
            text = text.format(**kwargs)

        return text


language = Language()


def t(key, **kwargs):
    return language.get(key, **kwargs)
