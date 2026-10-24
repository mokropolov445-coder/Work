from PyQt6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QSizePolicy, QApplication
from PyQt6.QtCore import Qt

class MainPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.init_ui()
    def init_ui(self):
        ls_button = QPushButton('Просканировать директорию')
        ls_button.clicked.connect(self.on_ls)
        ls_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        check_internet_button = QPushButton('Проверить интернет')
        check_internet_button.clicked.connect(self.on_check)
        check_internet_button.resize(check_internet_button.sizeHint())
        check_internet_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        services_button = QPushButton('Сервисы')
        services_button.clicked.connect(self.on_service)
        services_button.resize(check_internet_button.sizeHint())
        services_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        ssh_connect_button = QPushButton('Подключение по SSH')
        ssh_connect_button.clicked.connect(self.on_ssh)
        ssh_connect_button.resize(ssh_connect_button.sizeHint())
        ssh_connect_button.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        close_button = QPushButton('X')
        close_button.clicked.connect(self.close_app)
        close_button.setFixedSize(35, 35)

        layout_close = QVBoxLayout()
        layout_close.setContentsMargins(0, 0, 5 ,0)
        layout_close.addStretch()
        layout_close.addWidget(close_button)

        layout_pages = QVBoxLayout()
        layout_pages.addWidget(ls_button)
        layout_pages.addWidget(check_internet_button)
        layout_pages.addWidget(services_button)
        layout_pages.addWidget(ssh_connect_button)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addLayout(layout_close)
        main_layout.addStretch(1)
        main_layout.addLayout(layout_pages)
        main_layout.addStretch(1)
        self.setLayout(main_layout)
    def close_app(self):
        QApplication.quit()
    def on_ls(self):
        self.stack.setCurrentIndex(1)
    def on_check(self):
        self.stack.setCurrentIndex(2)
    def on_service(self):
        self.stack.setCurrentIndex(3)
    def on_ssh(self):
        self.stack.setCurrentIndex(4)
