from core.ssh import SSH

def test():
    ssh = SSH()
    connect_stdout, connect_stderr, connect_returncode = ssh.connect()
    print(connect_stdout)
    print(connect_stderr)
    print(connect_returncode)
    if connect_returncode != -1:
        ls_stdout, ls_stderr, ls_returncode = ssh.run('ls -la ~')
        print(ls_stdout)
        print(ls_stderr)
        print(ls_returncode)
    else:
        print('cannot exec')
