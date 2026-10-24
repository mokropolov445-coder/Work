from PyQt6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.stack = QStackedWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        self.show()
