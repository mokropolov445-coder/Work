import paramiko
import socket
import os
from dotenv import load_dotenv

SSH_IP = os.getenv('SSH_IP')
SSH_PORT = os.getenv('SSH_PORT')
SSH_CLIENT = os.getenv('SSH_CLIENT')
SSH_KEY = os.getenv('SSH_KEY')
SSH_PASSWORD = os.getenv('SSH_PASSWORD')

class SSH():
    def __init__(self):
        self.host = SSH_IP
        self.port = SSH_PORT
        self.user = SSH_CLIENT
        self.key_path = SSH_KEY
        self.password = SSH_PASSWORD

    def connect(self):
        self.pc_client = paramiko.SSHClient()
        self.pc_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.key_path:
                self.pc_client.connect(hostname=self.host, port=self.port, username=self.user, key_filename=self.key_path, timeout=10)
            else:
                self.pc_client.connect(hostname=self.host, port=self.port, username=self.user, password=SSH_PASSWORD)
        except paramiko.AuthenticationException:
            return '', 'Неверный ключ', -1
        except paramiko.SSHException as e:
            return '', f'Ошибка SSH: {e}', -1
        except socket.timeout:
            return '', 'Превышено время ожидания: 10с!', -1
    def close(self):
        if self.sftp:
            self.sftp.close()
        if self.pc_client:
            self.pc_client.close()
    def run(self, command):
        run_stdin, run_stdout, run_stderr = self.pc_client.exec_command(command)
        run_returncode = run_stdout.channel.recv_exit_status()
        return run_stdout, run_stderr, run_returncode
