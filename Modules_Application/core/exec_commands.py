import subprocess

def run(Command, timeout=10):
    try:
        exec_command = subprocess.run(Command, capture_output=True, text=True, timeout=timeout)
        return exec_command.stdout, exec_command.stderr, exec_command.returncode
    except FileNotFoundError as e:
        return None, f'Команда не найдена! Ошибка: {e}', -1
    except subprocess.TimeoutExpired:
        return None, f'Таймаут: {timeout} секунд', -1
    except Exception as e:
        return None, f'Неизвестная ошибка! Подробнее: {e}', -1
