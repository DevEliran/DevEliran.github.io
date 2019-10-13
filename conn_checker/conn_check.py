import socket
import sys
from time import sleep

def check(url,port):
    ndex=url.find('w.')
    short_url=url[ndex+2:].capitalize()
    try:
        print(f"Evaluating connection to {url}.... ")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # IPV4 , TCP
        s.settimeout(2)
        s.connect((url,port))
        s.close()
        print(f'{short_url} is up\n')
        sleep(1)
    except Exception:
        print(f'{short_url} is down\n')
        sleep(1)
        sys.exit(0)

urls=['www.facebook.com','www.google.com','www.twitter.com','www.instagram.com','www.github.com']

for url in urls:
    check(url,80)
