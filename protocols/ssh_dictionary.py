from pssh.clients import SSHClient
# need to pip install parallel-ssh for script to work

def ssh(url, user, pswd):
    try:
        SSHClient(url, user=user, password=pswd)
    except:
        pass
    else:
        print('SSH password is ' + pswd)
