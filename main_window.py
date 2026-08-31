from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

import i18n
import storage
import theme
from button_manager import ButtonManager


class CallHelper(QMainWindow):

    def __init__(self):
        super().__init__()

        self.buttons = storage.load_buttons()

        self.setWindowTitle("Macro chat")
        self.setWindowIcon(QIcon("icon.ico"))

        self.resize(400, 500)
        self.setMinimumSize(420, 380)

        self.setWindowFlag(
            Qt.WindowType.WindowStaysOnTopHint,
            True,
        )

        self.setStyleSheet(
            theme.STYLESHEET
        )

        self.create_interface()
        self.refresh_main_buttons()
        self.update_language()

    # =========================================================
    # INTERFACE
    # =========================================================

    def create_interface(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        main_layout.setContentsMargins(
            10,
            8,
            10,
            8,
        )

        main_layout.setSpacing(7)

        # =====================================================
        # HEADER
        # =====================================================

        header = QHBoxLayout()
        header.setSpacing(5)

        self.title = QLabel(
            ""
        )

        self.title.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT};
                font-size: 13px;
                font-weight: 700;
                background: transparent;
            }}
            """
        )

        header.addWidget(
            self.title
        )

        header.addStretch()

        # =====================================================
        # SETTINGS
        # =====================================================

        self.settings_button = QPushButton(
            "⚙ Settings"
        )

        self.settings_button.setFixedHeight(
            30
        )

        self.settings_button.setToolTip(
            "Configure buttons"
        )

        self.settings_button.clicked.connect(
            self.open_manager
        )

        header.addWidget(
            self.settings_button
        )

        # =====================================================
        # LANGUAGE
        # =====================================================

        self.language_button = QPushButton(
            "Language  ▼"
        )

        self.language_button.setFixedHeight(
            30
        )

        self.language_button.setMinimumWidth(
            105
        )

        self.language_button.setCursor(
            Qt.CursorShape.PointingHandCursor
        )

        self.language_button.clicked.connect(
            self.show_language_menu
        )

        header.addWidget(
            self.language_button
        )

        # =====================================================
        # HELP
        # =====================================================

        self.help_button = QPushButton(
            "Help"
        )

        self.help_button.setFixedHeight(
            30
        )

        self.help_button.setMinimumWidth(
            50
        )

        self.help_button.clicked.connect(
            self.show_help
        )

        header.addWidget(
            self.help_button
        )

        main_layout.addLayout(
            header
        )

        # =====================================================
        # BUTTON PANEL
        # =====================================================

        self.buttons_panel = QFrame()

        self.buttons_panel.setObjectName(
            "buttonsPanel"
        )

        self.buttons_panel.setStyleSheet(
            f"""
            QFrame#buttonsPanel {{
                background-color: {theme.PANEL};
                border: 1px solid {theme.BORDER};
                border-radius: 6px;
            }}
            """
        )

        buttons_panel_layout = QVBoxLayout(
            self.buttons_panel
        )

        buttons_panel_layout.setContentsMargins(
            7,
            7,
            7,
            7,
        )

        self.buttons_frame = QWidget()

        # IMPORTANT:
        # This MUST be QGridLayout because we use row/column.
        self.buttons_layout = QGridLayout(
            self.buttons_frame
        )

        self.buttons_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        self.buttons_layout.setHorizontalSpacing(
            7
        )

        self.buttons_layout.setVerticalSpacing(
            7
        )

        buttons_panel_layout.addWidget(
            self.buttons_frame
        )

        main_layout.addWidget(
            self.buttons_panel,
            0,
        )

        # =====================================================
        # CHAT TITLE
        # =====================================================

        self.chat_title = QLabel(
            "CHAT"
        )

        self.chat_title.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 9px;
                font-weight: 700;
                background: transparent;
            }}
            """
        )

        main_layout.addWidget(
            self.chat_title
        )

        # =====================================================
        # CHAT
        # =====================================================

        chat_container = QFrame()

        chat_container.setMinimumHeight(200)


        chat_container.setObjectName(
            "chatContainer"
        )

        chat_container.setStyleSheet(
            f"""
            QFrame#chatContainer {{
                background-color: {theme.PANEL};
                border: 1px solid {theme.BORDER};
                border-radius: 6px;
            }}
            """
        )

        chat_layout = QVBoxLayout(
            chat_container
        )

        chat_layout.setContentsMargins(
            5,
            5,
            5,
            5,
        )

        self.chat = QTextEdit()

        self.chat.setReadOnly(
            False
        )

        self.chat.setMinimumHeight(
            135
        )

        chat_layout.addWidget(
            self.chat
        )

        # Chat gets most of the remaining vertical space
        main_layout.addWidget(
            chat_container,
            1,
        )

        # =====================================================
        # CLEAR BUTTON
        # =====================================================

        self.clear_button = QPushButton(
            "Clear chat"
        )

        self.clear_button.setFixedHeight(
            30
        )

        self.clear_button.clicked.connect(
            self.clear_chat
        )

        main_layout.addWidget(
            self.clear_button,
            0,
            Qt.AlignmentFlag.AlignHCenter,
        )

    # =========================================================
    # LANGUAGE MENU
    # =========================================================

    def show_language_menu(self):

        menu = QMenu(
            self
        )

        menu.setStyleSheet(
            f"""
            QMenu {{
                background-color: {theme.PANEL};
                color: {theme.TEXT};
                border: 1px solid {theme.BORDER};
                padding: 4px;
            }}

            QMenu::item {{
                padding: 7px 16px;
                border-radius: 4px;
            }}

            QMenu::item:selected {{
                background-color: {theme.BUTTON_HOVER};
            }}
            """
        )

        english_action = QAction(
            "English",
            self,
        )

        portuguese_action = QAction(
            "Português (Brasil)",
            self,
        )

        english_action.triggered.connect(
            lambda: self.change_language("en")
        )

        portuguese_action.triggered.connect(
            lambda: self.change_language("pt-BR")
        )

        menu.addAction(
            english_action
        )

        menu.addAction(
            portuguese_action
        )

        menu.exec(
            self.language_button.mapToGlobal(
                self.language_button.rect().bottomLeft()
            )
        )

    def change_language(self, language):

        if language not in (
            "en",
            "pt-BR",
        ):
            return

        i18n.language.set(
            language
        )

        self.update_language()

    def update_language(self):

        current = i18n.language.current

        if current == "en":

            self.settings_button.setText(
                "⚙ Settings"
            )

            self.settings_button.setToolTip(
                "Configure buttons"
            )

            self.language_button.setText(
                "Language  ▼"
            )

            self.language_button.setToolTip(
                "Change language"
            )

            self.help_button.setText(
                "Help"
            )

            self.chat.setPlaceholderText(
                "Messages will appear here..."
            )

            self.clear_button.setText(
                "Clear chat"
            )

        else:

            self.settings_button.setText(
                "⚙ Configurar"
            )

            self.settings_button.setToolTip(
                "Configurar botões"
            )

            self.language_button.setText(
                "Idioma  ▼"
            )

            self.language_button.setToolTip(
                "Alterar idioma"
            )

            self.help_button.setText(
                "Help"
            )

            self.chat.setPlaceholderText(
                "As mensagens aparecerão aqui..."
            )

            self.clear_button.setText(
                "Limpar chat"
            )

    # =========================================================
    # HELP
    # =========================================================

    def show_help(self):

        QMessageBox.information(
            self,
            i18n.t("help_title"),
            i18n.t("help_text"),
        )

    # =========================================================
    # MAIN BUTTONS
    # =========================================================

    def refresh_main_buttons(self):

        while self.buttons_layout.count():

            item = self.buttons_layout.takeAt(
                0
            )

            widget = item.widget()

            if widget is not None:
                widget.deleteLater()

        columns = 2

        for index, button_data in enumerate(
            self.buttons
        ):

            row = index // columns
            column = index % columns

            # =================================================
            # USER CONFIGURED BUTTON
            # =================================================
            #
            # These are NEVER translated.
            # Their name and message remain exactly as saved.
            #
            # =================================================

            button = QPushButton(
                button_data["name"]
            )

            button.setMinimumHeight(
                36
            )

            button.setToolTip(
                button_data["text"]
            )

            button.clicked.connect(
                lambda checked=False,
                data=button_data:
                    self.add_text(
                        data["text"]
                    )
            )

            self.buttons_layout.addWidget(
                button,
                row,
                column,
            )

        for column in range(columns):

            self.buttons_layout.setColumnStretch(
                column,
                1,
            )

    # =========================================================
    # CHAT
    # =========================================================

    def add_text(self, text):
        self.chat.append(
            text
        )

    def clear_chat(self):
        self.chat.clear()

    # =========================================================
    # SETTINGS
    # =========================================================

    def open_manager(self):

        dialog = ButtonManager(
            parent=self,
            buttons=self.buttons,
            on_change=self.on_buttons_changed,
        )

        dialog.exec()

    def on_buttons_changed(
        self,
        buttons,
    ):

        self.buttons = buttons

        storage.save_buttons(
            self.buttons
        )

        self.refresh_main_buttons()
