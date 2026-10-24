import paramiko
import glob
import os
from dotenv import load_dotenv

load_dotenv()

SSH_HOST = os.getenv('SSH_HOST')
SSH_PORT = os.getenv('SSH_PORT')
SSH_USER = os.getenv('SSH_USER')
SSH_KEY = os.getenv('SSH_KEY')

class SSH():
    def connect(self):
        self.pc_client = paramiko.SSHClient()
        self.pc_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.pc_client.connect(
            hostname=SSH_HOST,
            port=SSH_PORT,
            username=SSH_USER,
            key_filename=SSH_KEY,
            timeout=20
        )

        self.sftp = self.pc_client.open_sftp()

    def exec_command(self, command):
        command_stdin, command_stdout, command_stderr = self.pc_client.exec_command(command)
        return command_stdout.read().decode(), command_stderr.read().decode(), command_stdout.channel.recv_exit_status()
        self.pc_client.close()

    def send_file(self,local_dir, remote_dir):
        sended = []
        home_directory = os.path.expanduser('~')
        remote_home_directory_stdin, remote_home_directory_stdout, remote_home_directory_stderr = self.pc_client.exec_command('echo $HOME')
        remote_home_directory = remote_home_directory_stdout.read().decode()
        for file_path in glob.glob(os.path.join(home_directory, local_dir, '*')):
            filename = os.path.basename(file_path)
            self.sftp.put(f'{os.path.join(home_directory, file_path)}', f'{os.path.join(remote_home_directory, remote_dir)}')
            sended.append(filename)
        self.sftp.close()
        self.pc_client.close()
        return sended
    def get_file(self, local_dir, remote_dir):
        uploaded = []
        home_directory = os.path.expanduser('~')
        remote_directory_stdin, remote_directory_stdout, remote_directory_stderr = self.pc_client.exec_command(f'ls -la {remote_dir}')
        remote_directory = remote_directory_stdout.read().decode()
        local_directory = os.path.join(home_directory, local_dir)
        for filepath in remote_directory:
            self.sftp.get(filepath, local_directory)
            uploaded.append(filepath)
            return uploaded

        self.sftp.close()
        self.pc_client.close()
        return uploaded
