import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    application = QApplication(sys.argv)
    application_window = MainWindow()
    sys.exit(application.exec())
