from PyQt6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget
from pages.main_page import MainPage
from pages.ls_page import LsPage
from pages.check_page import CheckPage
from pages.services_page import ServicePage
from pages.ssh_page import SSHPage

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.stack = QStackedWidget()
        self.stack.addWidget(MainPage(self.stack))
        self.stack.addWidget(LsPage(self.stack))
        self.stack.addWidget(CheckPage(self.stack))
        self.stack.addWidget(ServicePage(self.stack))
        self.stack.addWidget(SSHPage(self.stack))
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.show()
