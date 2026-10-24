from core.exec_commands import run
import os


def find_service(service):
    if not service.endswith('.service'):
        service += '.service'
    result_stdout, result_stderr, result_returncode = run(['systemctl', 'show', '-p', 'LoadState', service])
    return result_stdout
def start_service(service):
    result_stdout, result_stderr, result_returncode = run(['systemctl', 'start', service])
    if result_returncode != 0:
        return True, '', 0
    else:
        return False, result_stderr, 1
def stop_service(service):
    result_stdout, result_stderr, result_returncode = run(['systemctl', 'stop', service])
    if result_returncode != 0:
        return True, '', 0
    else:
        return False, result_stderr, 1
def restart_service(service):
    result_stdout, result_stderr, result_returncode = run(['systemctl', 'restart', service])
    if result_returncode != 0:
        return True, '', 0
    else:
        return False, result_stderr, 1
