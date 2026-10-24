from modules.check_internet import CI
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
class CheckPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.init_ui()
    def init_ui(self):
        self.check_output = QLabel('Тут будет вывод')

        self.check_button = QPushButton('Проверить интернет')
        self.check_button.clicked.connect(self.check_clicked)
        self.check_button.setAutoDefault(True)
        self.back_button = QPushButton('Назад')
        self.back_button.clicked.connect(self.close_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.check_output)
        layout.addWidget(self.check_button)
        layout.addWidget(self.back_button)
        self.setLayout(layout)
    def close_clicked(self):
        self.stack.setCurrentIndex(0)
        self.check_output.setText('Тут будет вывод')
    def check_clicked(self):
        result = CI()
        if result != None:
            self.check_output.setText('Интернет есть!')
        else:
            self.check_output.setText('Интернет отсутствует!')
