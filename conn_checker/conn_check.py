import socket
import sys
from time import sleep
from url_db import Urls
import argparse

urls_db=Urls()

#urls=['www.facebook.com','www.google.com','www.twitter.com','www.instagram.com','www.github.com']

def check(url):

    ndex=url.find('w.')
    short_url=url[ndex+2:].capitalize()
    while True:
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


def parse():
    parser=argparse.ArgumentParser()
    parser.add_argument("-e","--execute",help="Executes the script",action="store_true" )
    parser.add_argument("-v","--view_url",action="store_true")
    parser.add_argument("-a","--add_url",action="store")
    parser.add_argument("-i","--interval",action="store")

    args=parser.parse_args()

    command=args.execute

    if args.execute:
        get_urls=urls_db.view_urls()
        while True:
            for i in range(5):
                check(get_urls[i][0])
            sleep(int(args.interval))
    elif args.view_url:
        get_urls=urls_db.view_urls()
        print(get_urls)

    elif args.add_url:
        urls_db.insert_url(args.add_url)

parse()
#for url in urls:
    #urls_db.insert_url(url)

#urlview=urls_db.view_table()
#get_urls=urls_db.view_urls()
#print(get_urls)
#for i in range (5):
#    check(get_urls[i][0])
#for url in urlview
