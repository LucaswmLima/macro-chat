import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from main_window import CallHelper


def resource_path(filename):
    """
    Returns the correct path both when running normally
    and when running as a PyInstaller executable.
    """
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, filename)


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("Macro Chat")

    # =====================================================
    # APPLICATION ICON
    # =====================================================

    icon_path = resource_path("icon.ico")
    icon = QIcon(icon_path)

    app.setWindowIcon(icon)

    # =====================================================
    # WINDOW
    # =====================================================

    window = CallHelper()

    window.setWindowIcon(icon)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()