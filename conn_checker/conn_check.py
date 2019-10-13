import socket
import sys
from time import sleep
from url_db import Urls

urls_db=Urls()

#urls=['www.facebook.com','www.google.com','www.twitter.com','www.instagram.com','www.github.com']

def check(url):
    ndex=url.find('w.')
    short_url=url[ndex+2:].capitalize()
    try:
        print(f"Evaluating connection to {url}.... ")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # IPV4 , TCP
        s.settimeout(2)
        s.connect((url,80))
        s.close()
        print(f'{short_url} is up\n')
        return 1
        sleep(1)
    except Exception:
        print(f'{short_url} is down\n')
        return 0
        sleep(1)
        sys.exit(0)



#for url in urls:
    #urls_db.insert_url(url)

urlview=urls_db.view_table()
print(urlview)
