from inspect import stack

from PyQt6.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout
from modules.services import start_service, restart_service, stop_service, find_service

class ServicePage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.init_ui()

    def init_ui(self):
        self.output_service = QLabel('Вывод запуска сервиса')

        self.input_service = QLineEdit()
        self.input_service.setPlaceholderText('Введите нужный сервис')

        self.button_service_check = QPushButton('Проверка сервиса')
        self.button_service_check.clicked.connect(self.clicked_button_check)
        self.button_service_check.setAutoDefault(True)
        self.button_service_start = QPushButton('Запуск сервиса')
        self.button_service_start.clicked.connect(self.clicked_button_start)
        self.button_service_start.hide()

        self.button_service_stop = QPushButton('Остановка сервиса')
        self.button_service_stop.clicked.connect(self.clicked_button_stop)
        self.button_service_stop.hide()

        self.button_service_restart = QPushButton('Перезапуск сервиса')
        self.button_service_restart.clicked.connect(self.clicked_button_restart)
        self.button_service_restart.hide()

        button_back = QPushButton('Назад')
        button_back.clicked.connect(self.clicked_back_button)

        layout = QVBoxLayout()
        layout.addWidget(self.output_service)
        layout.addWidget(self.input_service)
        layout.addWidget(self.button_service_check)
        layout.addWidget(self.button_service_start)
        layout.addWidget(self.button_service_stop)
        layout.addWidget(self.button_service_restart)
        layout.addWidget(button_back)
        self.setLayout(layout)
        self.show()
    def clicked_back_button(self):
        self.stack.setCurrentIndex(0)
        self.output_service.setText('Вывод запуска сервиса')
        self.input_service.setText('')
        self.button_service_check.show()
        self.button_service_restart.hide()
        self.button_service_start.hide()
        self.button_service_stop.hide()
    def clicked_button_check(self):
        self.service = self.input_service.text()
        self.check_output = find_service(self.service)
        self.button_service_check.setText('Выполняется...')
        if self.check_output != '':
            self.output_service.setText(f'Сервис {self.service} найден!')
            self.button_service_check.setText('Проверка сервиса')
        else:
            self.output_service.setText(f'Сервис {self.service} не найден! Попробуйте еще раз')
            self.button_service_check.setText('Проверка сервиса')
        self.button_service_restart.show()
        self.button_service_start.show()
        self.button_service_stop.show()
        self.button_service_check.setAutoDefault(False)

    def clicked_button_start(self):
        start_stdout, start_stderr, start_returncode = start_service(self.service)
        self.button_service_start.setText('Выполняется...')
        if start_stdout == True:
            self.output_service.setText(f'Сервис {self.service} запущен!')
            self.button_service_start.setText('Запуск сервиса')
        else:
            self.output_service.setText(f'Запуск сервиса {self.service} упал с ошибкой {start_stderr}')
            self.button_service_start.setText('Запуск сервиса')

    def clicked_button_stop(self):
        stop_stdout, stop_stderr, stop_returncode = stop_service(self.service)
        self.button_service_stop.setText('Выполняется...')
        if stop_stdout == True:
            self.output_service.setText(f'Сервис {self.service} остановлен!')
            self.button_service_stop.setText('Остановка сервиса')
        else:
            self.output_service.setText(f'Остановка сервиса {self.service} упал с ошибкой {stop_stderr}')
            self.button_service_stop.setText('Остановка сервиса')

    def clicked_button_restart(self):
        restart_stdout, restart_stderr, restart_returncode = restart_service(self.service)
        self.button_service_restart.setText('Выполняется...')
        if restart_stdout == True:
            self.output_service.setText(f'Сервис {self.service} перезапущен!')
            self.button_service_restart.setText('Перезапустить сервис')
        else:
            self.output_service.setText(f'Перезапуск сервиса {self.service} упало с ошибкой {restart_stderr}')
            self.button_service_restart.setText('Перезапустить сервис')
