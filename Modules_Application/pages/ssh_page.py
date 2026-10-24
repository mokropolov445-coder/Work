from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from inspect import stack
from core.ssh import SSH
import paramiko

class SSHPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.SSH = SSH()
        self.init_ui()

    def init_ui(self):
        # Вывод работы
        self.output_ssh = QLabel('Тут будет вывод')
        self.output_ssh.setWordWrap(True)
        self.output_ssh.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.output_ssh_scroll = QScrollArea()
        self.output_ssh_scroll.setWidget(self.output_ssh)
        self.output_ssh_scroll.setWidgetResizable(True)


        # Кнопка подключения
        self.connect_button = QPushButton('Подключиться')
        self.connect_button.clicked.connect(self.clicked_connect_button)
        self.connect_button.setAutoDefault(True)
        # Выбор: Выполнить команду
        self.choose_command_button = QPushButton('Выполнить команду')
        self.choose_command_button.clicked.connect(self.clicked_choose_command_button)
        self.choose_command_button.hide()
        # Выбор: Отправка/Прием/Получение файла
        self.choose_file_button = QPushButton('Отправить/Получить файл')
        self.choose_file_button.clicked.connect(self.clicked_choose_file_button)
        self.choose_file_button.hide()
        # Команда: Ввод команды
        self.input_command = QLineEdit()
        self.input_command.setPlaceholderText('Введите команду для выполнения...')
        self.input_command.hide()
        # Команда: Кнопка выполнения
        self.command_button = QPushButton('Выполнить команду')
        self.command_button.hide()
        self.command_button.clicked.connect(self.clicked_command_button)
        # Отправка/Прием: Ввод папки на устройстве
        self.file_TD_input = QLineEdit()
        self.file_TD_input.setPlaceholderText('Введите папку этого устройсва...')
        self.file_TD_input.hide()
        # Отправка/Прием: Ввод папки на удаленном устройстве
        self.file_SSHD_input = QLineEdit()
        self.file_SSHD_input.setPlaceholderText('Введите папку на удалённом устройстве...')
        self.file_SSHD_input.hide()
        # Отправка/Прием: кнопка отправки
        self.file_send_button = QPushButton('Отправить файл')
        self.file_send_button.hide()
        # Отправка/Прием: кнопка приёма
        self.file_get_button = QPushButton('Получить файл')
        self.file_get_button.hide()
        #  Кнопка назад
        self.back_command = QPushButton('Назад')
        self.back_command.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        # Вывод
        layout = QVBoxLayout()
        layout.addWidget(self.output_ssh_scroll)
        layout.addWidget(self.connect_button)
        layout.addWidget(self.choose_command_button)
        layout.addWidget(self.choose_file_button)
        layout.addWidget(self.input_command)
        layout.addWidget(self.command_button)
        layout.addWidget(self.file_TD_input)
        layout.addWidget(self.file_SSHD_input)
        layout.addWidget(self.file_send_button)
        layout.addWidget(self.file_get_button)
        layout.addWidget(self.back_command)
        self.setLayout(layout)
        self.show()

    def clicked_back_button(self):
        self.stack.setCurrentIndex(0)
        self.connect_button.show()
        self.choose_command_button.hide()
        self.choose_file_button.hide()
        self.command_button.hide()
        self.file_SSHD_input.hide()
        self.file_SSHD_input.setText('')
        self.file_TD_input.hide()
        self.file_TD_input.setText('')
        self.file_get_button.hide()
        self.file_send_button.hide()
        self.input_command.setText('')

    def clicked_file_get_button(self):
        if self.file_SSHD_input.text() or self.file_TD_input.text() == "":
            self.output_ssh.setText('Введите папки для получения файлов!')
        else:
            list_getted = self.SSH.get_file(self.file_TD_input.text(), self.file_SSHD_input.text())
            self.output_ssh.setText(f'{list_getted}')
    # Выбор: Отправка/Получение файлов
    def clicked_choose_file_button(self):
        self.choose_command_button.hide()
        self.choose_file_button.hide()
        self.file_TD_input.show()
        self.file_SSHD_input.show()
        self.file_get_button.show()
        self.file_send_button.show()
    # Отправка файлов
    def clicked_file_send_button(self):
        if self.file_TD_input.text() or self.file_SSHD_input.text() == '':
            self.output_ssh.setText('Введите что то в строки ввода!')
        else:
            sended = self.SSH.send_file(self.file_TD_input.text(), self.file_SSHD_input.text())
            for sended_file in sended:
                if sended_file == []:
                    self.output_ssh.setText('Ни один файл не отправлен! Проверьте путь к файлу')
                else:
                    self.output_ssh.setText(f'Файлы отправлены на удалённое устройство! Список:\n{sended}')
    # Выполнение команды
    def clicked_command_button(self):
        exec_stdout, exec_stderr, exec_returncode = self.SSH.exec_command(self.input_command.text())
        if exec_returncode == 0:
            self.output_ssh.setText(f'Команда {self.input_command} успешно выполнено!\n Вывод:\n{exec_stdout}')
            self.connect_button.show()
            self.input_command.hide()
            self.command_button.hide()
        else:
            self.output_ssh.setText(f'Команда {self.input_command} упала с ошибкой {exec_stderr}!')
    # Выбор: Выполнить команду/отправку на удалённом устройстве
    def clicked_choose_command_button(self):
        self.choose_command_button.hide()
        self.choose_file_button.hide()
        self.input_command.show()
        self.command_button.show()
    # Подключение
    def clicked_connect_button(self):
        self.connect = True
        try:
            self.SSH.connect()
        except paramiko.SSHException as e:
             self.output_ssh.setText(f'Ошибка SSH: {e}!')
             self.connect = False
        except paramiko.AuthenticationException as e:
            self.connect = False
            self.output_ssh.setText(f'Ошибка аунтефикации! {e}')
        except paramiko.BadHostKeyException:
            self.output_ssh.setText('Ключ не совпадает с имеющимися!')
            self.connect = False
        if self.connect != False:
            self.choose_command_button.show()
            self.choose_file_button.show()
            self.connect_button.hide()
            self.connect_button.setAutoDefault(False)
            self.output_ssh.setText('Подключение успешно!')
