from ftplib import FTP

def ftp(url, user, pswd):
    ftp = FTP(url)
    try:
        ftp.login(user, pswd)
    except:
        pass
    else:
        print('FTP password is ' + pswd)
        
