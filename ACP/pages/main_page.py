from inspect import stack

from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QSizePolicy


class MainPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.init_ui()
    def init_ui(self):
        welcome_text = QLabel('Рад видеть вас снова!')
        welcome_text.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)

        check_DPI = QPushButton('Проверить работу DPI')
        check_DPI.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        check_DPI.clicked.connect(self.clicked_check_DPI)
        connect_PC = QPushButton('Подключиться к ПК')
        connect_PC.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        connect_PC.clicked.connect(self.clicked_connect_PC)
        close_button = QPushButton('X')
        close_button.setFixedSize(35, 35)
        close_button.clicked.connect(self.clicked_close_button)
        close_layout = QVBoxLayout()
        close_layout.setContentsMargins(0, 0, 5, 0)
        close_layout.addStretch()
        close_layout.addWidget(close_button)
        close_layout.addWidget(welcome_text)

        pages_layout = QVBoxLayout()
        pages_layout.addWidget(check_DPI)
        pages_layout.addWidget(connect_PC)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.addLayout(close_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(pages_layout)
        main_layout.addStretch(1)
        self.setLayout(main_layout)
    def clicked_close_button(self):
        QApplication.quit()
    def clicked_check_DPI(self):
        self.stack.setCurrentIndex(1)
    def clicked_connect_PC(self):
        self.stack.setCurrentIndex(2)
