from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget, QScrollArea
from PyQt6.QtCore import Qt
from modules.list_directory import list_directory

class LsPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.init_ui()
    def init_ui(self):
        self.ls_output = QLabel('Тут будет вывод')
        self.ls_output.setWordWrap(True)
        self.ls_output.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidget(self.ls_output)
        scroll.setWidgetResizable(True)

        self.ls_input = QLineEdit()
        self.ls_input.setPlaceholderText('Введите директорию для просмотра(оставьте пустым для выбора домашней директории)...')

        ls_button = QPushButton('Сканировать')
        ls_button.clicked.connect(self.ls_clicked)
        ls_button.setAutoDefault(True)
        back_button = QPushButton('Назад')
        back_button.clicked.connect(self.back_clicked)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        layout.addWidget(self.ls_input)
        layout.addWidget(ls_button)
        layout.addWidget(back_button)
        self.setLayout(layout)
    def back_clicked(self):
        self.stack.setCurrentIndex(0)
        self.ls_output.setText('Тут будет вывод')
    def ls_clicked(self):
        directory = self.ls_input.text().strip() or None
        stdout, stderr, returncode = list_directory(directory)
        if returncode == 0:
            self.ls_output.setText(stdout)
        else:
            self.ls_output.setText(stderr)
