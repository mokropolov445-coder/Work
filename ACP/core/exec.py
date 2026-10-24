import subprocess
def exec(command, timeout=10):
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
        return result.stdout, result.stderr, result.returncode
    except FileNotFoundError as e:
        return '', f'Команда {e} не найдена!', -1
    except subprocess.TimeoutExpired:
        return '', f'Превышено время ожидания: {timeout}с!', -1
    except Exception as e:
        return '', f'Неизвестная ошибка: {e}!', -1
