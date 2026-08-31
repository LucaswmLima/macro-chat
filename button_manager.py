from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (
    QIcon,
    QPainter,
    QPen,
    QColor,
    QPixmap,
)
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

import i18n
import theme


# =============================================================
# ICONS
# =============================================================

def create_icon(icon_type, color):

    pixmap = QPixmap(
        20,
        20,
    )

    pixmap.fill(
        Qt.GlobalColor.transparent
    )

    painter = QPainter(
        pixmap
    )

    painter.setRenderHint(
        QPainter.RenderHint.Antialiasing
    )

    qcolor = QColor(
        color
    )

    pen = QPen(
        qcolor
    )

    pen.setWidthF(
        2.0
    )

    pen.setCapStyle(
        Qt.PenCapStyle.RoundCap
    )

    pen.setJoinStyle(
        Qt.PenJoinStyle.RoundJoin
    )

    painter.setPen(
        pen
    )

    painter.setBrush(
        Qt.BrushStyle.NoBrush
    )

    if icon_type == "up":

        painter.drawLine(
            10, 15,
            10, 5,
        )

        painter.drawLine(
            10, 5,
            5, 10,
        )

        painter.drawLine(
            10, 5,
            15, 10,
        )

    elif icon_type == "down":

        painter.drawLine(
            10, 5,
            10, 15,
        )

        painter.drawLine(
            10, 15,
            5, 10,
        )

        painter.drawLine(
            10, 15,
            15, 10,
        )

    elif icon_type == "edit":

        painter.drawLine(
            5, 15,
            5, 11,
        )

        painter.drawLine(
            5, 11,
            13, 3,
        )

        painter.drawLine(
            13, 3,
            17, 7,
        )

        painter.drawLine(
            17, 7,
            9, 15,
        )

        painter.drawLine(
            9, 15,
            5, 15,
        )

    elif icon_type == "delete":

        painter.drawLine(
            6, 7,
            7, 17,
        )

        painter.drawLine(
            7, 17,
            13, 17,
        )

        painter.drawLine(
            13, 17,
            14, 7,
        )

        painter.drawLine(
            4, 7,
            16, 7,
        )

        painter.drawLine(
            8, 4,
            12, 4,
        )

        painter.drawLine(
            9, 4,
            9, 3,
        )

        painter.drawLine(
            11, 4,
            11, 3,
        )

    painter.end()

    return QIcon(
        pixmap
    )


# =============================================================
# BUTTON MANAGER
# =============================================================

class ButtonManager(QDialog):

    def __init__(
        self,
        parent,
        buttons,
        on_change,
    ):

        super().__init__(
            parent
        )

        self.parent_window = parent

        self.buttons = [
            button.copy()
            for button in buttons
        ]

        self.on_change = on_change

        self.setWindowTitle(
            i18n.t(
                "configure_buttons"
            )
        )

        self.resize(
            560,
            520,
        )

        self.setMinimumSize(
            480,
            420,
        )

        self.setWindowFlag(
            Qt.WindowType.WindowContextHelpButtonHint,
            False,
        )

        self.setStyleSheet(
            theme.STYLESHEET
        )

        self.create_interface()
        self.refresh_cards()

        self.center_window()

    # =========================================================
    # WINDOW
    # =========================================================

    def center_window(self):

        parent_geometry = (
            self.parent_window.frameGeometry()
        )

        own_geometry = (
            self.frameGeometry()
        )

        own_geometry.moveCenter(
            parent_geometry.center()
        )

        self.move(
            own_geometry.topLeft()
        )

    # =========================================================
    # INTERFACE
    # =========================================================

    def create_interface(self):

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            14,
            12,
            14,
            12,
        )

        layout.setSpacing(
            7
        )

        self.title = QLabel(
            i18n.t(
                "configure_buttons"
            )
        )

        self.title.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT};
                font-size: 14px;
                font-weight: 700;
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            self.title
        )

        self.subtitle = QLabel(
            i18n.t(
                "reorder_hint"
            )
        )

        self.subtitle.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 9px;
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            self.subtitle
        )

        self.list_widget = QListWidget()

        self.list_widget.setSpacing(
            5
        )

        self.list_widget.setFrameShape(
            QFrame.Shape.NoFrame
        )

        self.list_widget.setStyleSheet(
            f"""
            QListWidget {{
                background-color: {theme.PANEL};
                border: 1px solid {theme.BORDER};
                border-radius: 6px;
                padding: 5px;
                outline: none;
            }}

            QListWidget::item {{
                background: transparent;
                border: none;
            }}

            QListWidget::item:selected {{
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            self.list_widget,
            1,
        )

        # =====================================================
        # FOOTER
        # =====================================================

        footer = QHBoxLayout()

        self.add_button_widget = QPushButton(
            i18n.t(
                "add_button"
            )
        )

        self.add_button_widget.setFixedHeight(
            32
        )

        self.add_button_widget.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {theme.ACCENT};
                color: white;
                font-weight: 700;
                border: none;
                border-radius: 6px;
                padding: 6px 14px;
            }}

            QPushButton:hover {{
                background-color: {theme.ACCENT_HOVER};
            }}
            """
        )

        self.add_button_widget.clicked.connect(
            self.add_button
        )

        footer.addWidget(
            self.add_button_widget
        )

        footer.addStretch()

        self.close_button = QPushButton(
            i18n.t(
                "close"
            )
        )

        self.close_button.setFixedHeight(
            32
        )

        self.close_button.clicked.connect(
            self.accept
        )

        footer.addWidget(
            self.close_button
        )

        layout.addLayout(
            footer
        )

    # =========================================================
    # CARDS
    # =========================================================

    def refresh_cards(self):

        self.list_widget.setUpdatesEnabled(
            False
        )

        self.list_widget.clear()

        for index, button_data in enumerate(
            self.buttons
        ):

            self.create_card(
                index,
                button_data,
            )

        self.list_widget.setUpdatesEnabled(
            True
        )

        self.list_widget.viewport().update()

    def create_card(
        self,
        index,
        button_data,
    ):

        item = QListWidgetItem()

        item.setSizeHint(
            QSize(
                0,
                62,
            )
        )

        card = QFrame()

        card.setObjectName(
            "buttonCard"
        )

        card.setStyleSheet(
            f"""
            QFrame#buttonCard {{
                background-color: {theme.PANEL_LIGHT};
                border: 1px solid {theme.BORDER};
                border-radius: 6px;
            }}
            """
        )

        layout = QHBoxLayout(
            card
        )

        layout.setContentsMargins(
            8,
            6,
            8,
            6,
        )

        layout.setSpacing(
            6
        )

        # =====================================================
        # DRAG INDICATOR
        # =====================================================

        drag_icon = QLabel(
            "⋮⋮"
        )

        drag_icon.setFixedWidth(
            20
        )

        drag_icon.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        drag_icon.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 13px;
                font-weight: 700;
                background: transparent;
                border: none;
            }}
            """
        )

        layout.addWidget(
            drag_icon
        )

        # =====================================================
        # TEXT
        # =====================================================

        text_container = QWidget()

        text_layout = QVBoxLayout(
            text_container
        )

        text_layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        text_layout.setSpacing(
            1
        )

        name_label = QLabel(
            button_data["name"]
        )

        name_label.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT};
                font-size: 10px;
                font-weight: 700;
                background: transparent;
                border: none;
            }}
            """
        )

        preview = button_data[
            "text"
        ].replace(
            "\n",
            " ",
        )

        if len(preview) > 50:
            preview = (
                preview[:50]
                + "..."
            )

        preview_label = QLabel(
            preview
        )

        preview_label.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 8px;
                background: transparent;
                border: none;
            }}
            """
        )

        text_layout.addWidget(
            name_label
        )

        text_layout.addWidget(
            preview_label
        )

        layout.addWidget(
            text_container,
            1,
        )

        # =====================================================
        # ACTIONS
        # =====================================================

        actions = QHBoxLayout()

        actions.setSpacing(
            3
        )

        up_button = self.create_action_button(
            "up",
            i18n.t(
                "move_up"
            ),
            lambda checked=False,
            i=index:
                self.move_up(i),
        )

        down_button = self.create_action_button(
            "down",
            i18n.t(
                "move_down"
            ),
            lambda checked=False,
            i=index:
                self.move_down(i),
        )

        edit_button = self.create_action_button(
            "edit",
            i18n.t(
                "edit_button"
            ),
            lambda checked=False,
            i=index:
                self.edit_button(i),
        )

        delete_button = self.create_action_button(
            "delete",
            i18n.t(
                "delete_button"
            ),
            lambda checked=False,
            i=index:
                self.delete_button(i),
        )

        actions.addWidget(
            up_button
        )

        actions.addWidget(
            down_button
        )

        actions.addWidget(
            edit_button
        )

        actions.addWidget(
            delete_button
        )

        layout.addLayout(
            actions
        )

        self.list_widget.addItem(
            item
        )

        self.list_widget.setItemWidget(
            item,
            card,
        )

        up_button.setEnabled(
            index > 0
        )

        down_button.setEnabled(
            index < len(self.buttons) - 1
        )

    # =========================================================
    # ACTION BUTTON
    # =========================================================

    def create_action_button(
        self,
        icon_type,
        tooltip,
        command,
    ):

        button = QPushButton()

        button.setFixedSize(
            30,
            30,
        )

        button.setIcon(
            create_icon(
                icon_type,
                theme.TEXT,
            )
        )

        button.setIconSize(
            QSize(
                16,
                16,
            )
        )

        button.setToolTip(
            tooltip
        )

        button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {theme.BUTTON};
                color: {theme.TEXT};
                border: none;
                border-radius: 5px;
                padding: 0;
            }}

            QPushButton:hover {{
                background-color: {theme.BUTTON_HOVER};
            }}

            QPushButton:pressed {{
                background-color: {theme.ACCENT};
            }}

            QPushButton:disabled {{
                background-color: {theme.BUTTON};
                color: #555a66;
            }}
            """
        )

        button.clicked.connect(
            command
        )

        return button

    # =========================================================
    # ORDER
    # =========================================================

    def move_up(
        self,
        index,
    ):

        if index <= 0:
            return

        self.buttons[
            index - 1
        ], self.buttons[
            index
        ] = (
            self.buttons[index],
            self.buttons[index - 1],
        )

        self.on_change(
            self.buttons.copy()
        )

        self.refresh_cards()

    def move_down(
        self,
        index,
    ):

        if index >= len(self.buttons) - 1:
            return

        self.buttons[
            index + 1
        ], self.buttons[
            index
        ] = (
            self.buttons[index],
            self.buttons[index + 1],
        )

        self.on_change(
            self.buttons.copy()
        )

        self.refresh_cards()

    # =========================================================
    # ADD
    # =========================================================

    def add_button(self):
        self.open_editor()

    # =========================================================
    # EDIT
    # =========================================================

    def edit_button(
        self,
        index,
    ):

        if index < 0 or index >= len(self.buttons):
            return

        self.open_editor(
            index=index,
            button_data=self.buttons[index],
        )

    # =========================================================
    # EDITOR
    # =========================================================

    def open_editor(
        self,
        index=None,
        button_data=None,
    ):

        editing = (
            button_data is not None
        )

        editor = ButtonEditor(
            parent=self,
            editing=editing,
            button_data=button_data,
        )

        if (
            editor.exec()
            != QDialog.DialogCode.Accepted
        ):
            return

        new_button = (
            editor.get_button()
        )

        if editing:

            self.buttons[
                index
            ] = new_button

        else:

            self.buttons.append(
                new_button
            )

        self.on_change(
            self.buttons.copy()
        )

        self.refresh_cards()

    # =========================================================
    # DELETE
    # =========================================================

    def delete_button(
        self,
        index,
    ):

        if index < 0 or index >= len(self.buttons):
            return

        button_data = (
            self.buttons[index]
        )

        result = QMessageBox.question(
            self,
            i18n.t(
                "delete_title"
            ),
            i18n.t(
                "delete_message",
                button_name=button_data["name"],
            ),
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if (
            result
            != QMessageBox.StandardButton.Yes
        ):
            return

        del self.buttons[
            index
        ]

        self.on_change(
            self.buttons.copy()
        )

        self.refresh_cards()


# =============================================================
# BUTTON EDITOR
# =============================================================

class ButtonEditor(QDialog):

    def __init__(
        self,
        parent,
        editing,
        button_data=None,
    ):

        super().__init__(
            parent
        )

        self.editing = editing

        self.setWindowTitle(
            i18n.t(
                "edit_button"
            )
            if editing
            else i18n.t(
                "new_button"
            )
        )

        self.resize(
            440,
            330,
        )

        self.setMinimumSize(
            400,
            300,
        )

        self.setWindowFlag(
            Qt.WindowType.WindowContextHelpButtonHint,
            False,
        )

        self.setStyleSheet(
            theme.STYLESHEET
        )

        self.create_interface()

        if editing and button_data:

            self.name_entry.setText(
                button_data["name"]
            )

            self.text_entry.setPlainText(
                button_data["text"]
            )

        self.center_window()

        self.name_entry.setFocus()

    # =========================================================
    # WINDOW
    # =========================================================

    def center_window(self):

        parent_geometry = (
            self.parent().frameGeometry()
        )

        own_geometry = (
            self.frameGeometry()
        )

        own_geometry.moveCenter(
            parent_geometry.center()
        )

        self.move(
            own_geometry.topLeft()
        )

    # =========================================================
    # INTERFACE
    # =========================================================

    def create_interface(self):

        layout = QVBoxLayout(
            self
        )

        layout.setContentsMargins(
            16,
            14,
            16,
            14,
        )

        layout.setSpacing(
            6
        )

        title = QLabel(
            i18n.t(
                "edit_button"
            )
            if self.editing
            else i18n.t(
                "new_button"
            )
        )

        title.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT};
                font-size: 13px;
                font-weight: 700;
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            title
        )

        name_label = QLabel(
            i18n.t(
                "button_name"
            )
        )

        name_label.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 9px;
                font-weight: 700;
                margin-top: 5px;
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            name_label
        )

        self.name_entry = QLineEdit()

        self.name_entry.setFixedHeight(
            34
        )

        layout.addWidget(
            self.name_entry
        )

        text_label = QLabel(
            i18n.t(
                "button_text"
            )
        )

        text_label.setStyleSheet(
            f"""
            QLabel {{
                color: {theme.TEXT_MUTED};
                font-size: 9px;
                font-weight: 700;
                margin-top: 3px;
                background: transparent;
            }}
            """
        )

        layout.addWidget(
            text_label
        )

        self.text_entry = QPlainTextEdit()

        layout.addWidget(
            self.text_entry,
            1,
        )

        footer = QHBoxLayout()

        footer.addStretch()

        cancel_button = QPushButton(
            i18n.t(
                "cancel"
            )
        )

        cancel_button.setFixedHeight(
            32
        )

        cancel_button.clicked.connect(
            self.reject
        )

        footer.addWidget(
            cancel_button
        )

        save_button = QPushButton(
            i18n.t(
                "save"
            )
        )

        save_button.setFixedHeight(
            32
        )

        save_button.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {theme.ACCENT};
                color: white;
                font-weight: 700;
                border: none;
                border-radius: 6px;
                padding: 6px 18px;
            }}

            QPushButton:hover {{
                background-color: {theme.ACCENT_HOVER};
            }}
            """
        )

        save_button.clicked.connect(
            self.save
        )

        footer.addWidget(
            save_button
        )

        layout.addLayout(
            footer
        )

    # =========================================================
    # SAVE
    # =========================================================

    def save(self):

        name = (
            self.name_entry
            .text()
            .strip()
        )

        text = (
            self.text_entry
            .toPlainText()
            .strip()
        )

        if not name:

            QMessageBox.warning(
                self,
                i18n.t(
                    "empty_name_title"
                ),
                i18n.t(
                    "empty_name_message"
                ),
            )

            self.name_entry.setFocus()

            return

        if not text:

            QMessageBox.warning(
                self,
                i18n.t(
                    "empty_text_title"
                ),
                i18n.t(
                    "empty_text_message"
                ),
            )

            self.text_entry.setFocus()

            return

        self.accept()

    # =========================================================
    # RESULT
    # =========================================================

    def get_button(self):

        return {
            "name": (
                self.name_entry
                .text()
                .strip()
            ),
            "text": (
                self.text_entry
                .toPlainText()
                .strip()
            ),
        }
