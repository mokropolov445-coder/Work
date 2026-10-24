import sys
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6.QtCore import Qt
from main_window import MainWindow

if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyleSheet("""
        QWidget {
            background-color: #111111;
        }
        QLineEdit {
            color: #E1E1E1;
            border: 1px solid #E1E1E1;
            border-radius: 5px;
        }
        QLabel {
            color: #E1E1E1;
            border: 1px solid #E1E1E1;
            border-radius: 5px;
        }
        QPushButton {
        padding: 8px 16px;
        border: 1px solid #E1E1E1;
        background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                          stop: 0 #666B85,
                                          stop: 0.2 #5D5E8E,
                                          stop: 0.4 #5E5893,
                                          stop: 0.6 #61528F,
                                          stop: 0.8 #5F419F,
                                          stop: 1 #542F97);
            color: #E1E1E1;
            border-radius: 5px;
        }
    """)
    application_window = MainWindow()
    application_window.resize(400, 300)
    application_window.show()
    application_window.raise_()
    application_window.activateWindow()
    sys.exit(application.exec())
