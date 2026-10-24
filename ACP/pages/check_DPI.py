from core.ssh import SSH

def check():
    connect_stdout, connect_stderr, connect_returncode = SSH.connect()
    if connect_returncode != -1:
        check_youtube_stdout, check_youtube_stderr, check_youtube_returncode = SSH.run('ping -c 3 https://www.youtube.com')
        check_tg_stdout, check_tg_stderr, check_tg_returncode = SSH.run('systemctl status tg-ws-proxy.service')
        if check_youtube_returncode == -1:
            check_service_stdout, check_service_stderr, check_service_returncode = SSH.run('systemctl status zapret_discord_youtube.service')
        else:
            return 'Доступ к ютубу',
