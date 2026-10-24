from PyQt6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget
from pages.main_page import MainPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.stack = QStackedWidget()
        self.stack.addWidget(MainPage(self.stack))
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.show()
