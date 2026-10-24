import os
from core.exec_commands import run


def list_directory(linked_directory=None):
    home_directory = os.path.expanduser('~')
    if linked_directory != None:
        linked_path = os.path.join(home_directory, linked_directory)
    else:
        linked_path = home_directory
    LS_stdout, LS_stderr, LS_returncode = run(['ls', '-la', linked_path])
    if LS_returncode == -1:
        return None, LS_stderr, -1
    else:
        return LS_stdout, None, 0

