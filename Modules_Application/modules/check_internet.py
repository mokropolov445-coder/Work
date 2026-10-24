import os
from core.exec_commands import run

def CI():
    stdout, stderr, returncode = run(['ping', '-c', '2', 'google.com'])
    if returncode == '0':
        return stdout
    else:
        return stderr
