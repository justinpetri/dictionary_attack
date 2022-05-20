import concurrent.futures
from protocols.https_dictionary import https
from protocols.ssh_dictionary import ssh
from protocols.ftp_dictionary import ftp
from itertools import repeat
import time

# Parameters
url = '192.168.1.1'
user = 'admin'
file = open('C:/ENTER_WORDLIST_HERE')
data = file.read()
file.close()
word_list = data.split('\n')

print('Scan started at', time.strftime("%H:%M:%S"))

# Uncomment one pair of lines when using specific protocol.

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(https, repeat(url), repeat(user), word_list)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(ssh, repeat(url), repeat(user), word_list)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(ftp, repeat(url), repeat(user), word_list)

print(time.strftime("%H:%M:%S"), 'Attempt completed.')