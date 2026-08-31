BG = "#111318"

PANEL = "#191c23"

PANEL_LIGHT = "#20242d"

BORDER = "#2c313c"

TEXT = "#f2f4f8"

TEXT_MUTED = "#9299a8"

ACCENT = "#5865f2"

ACCENT_HOVER = "#6975f5"

DANGER = "#ed4245"

DANGER_HOVER = "#f15b5e"

BUTTON = "#252a34"

BUTTON_HOVER = "#303642"

INPUT_BG = "#0d0f13"

FONT = "Segoe UI"


STYLESHEET = f"""

QWidget {{
    background-color: {BG};
    color: {TEXT};
    font-family: "{FONT}";
}}

QMainWindow {{
    background-color: {BG};
}}

QDialog {{
    background-color: {BG};
}}

QLabel {{
    background-color: transparent;
}}

QPushButton {{
    background-color: {BUTTON};
    color: {TEXT};
    border: none;
    border-radius: 6px;
    padding: 6px 10px;
}}

QPushButton:hover {{
    background-color: {BUTTON_HOVER};
}}

QPushButton:pressed {{
    background-color: {BORDER};
}}

QPushButton:disabled {{
    color: #555a66;
    background-color: {BUTTON};
}}

QLineEdit,
QPlainTextEdit {{
    background-color: {INPUT_BG};
    color: {TEXT};
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 7px;
    selection-background-color: {ACCENT};
}}

QLineEdit:focus,
QPlainTextEdit:focus {{
    border: 1px solid {ACCENT};
}}

QScrollArea {{
    background-color: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 6px;
}}

QScrollBar:vertical {{
    background: {PANEL};
    width: 9px;
    margin: 2px;
}}

QScrollBar::handle:vertical {{
    background: {BORDER};
    border-radius: 5px;
    min-height: 25px;
}}

QScrollBar::handle:vertical:hover {{
    background: #3b414e;
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {{
    height: 0px;
}}

QTextEdit {{
    background-color: {INPUT_BG};
    color: {TEXT};
    border: none;
    border-radius: 4px;
    padding: 7px;
}}

QMenu {{
    background-color: {PANEL};
    color: {TEXT};
    border: 1px solid {BORDER};
}}

QMenu::item {{
    padding: 7px 16px;
}}

QMenu::item:selected {{
    background-color: {BUTTON_HOVER};
}}

QMessageBox {{
    background-color: {BG};
}}

"""
