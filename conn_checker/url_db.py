import sqlite3
import datetime
import socket


class Urls(object):

    def __init__(self):
        self.con=sqlite3.connect('urls.db')
        self.cur=self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY ,
                                                                url TEXT NOT NULL,
                                                                prevS INT NOT NULL,
                                                                curS INT NOT NULL,
                                                                time_stamp TEXT)
                                                                """)
        self.con.commit()
#prevS stands for previous status , curS stands for current status .
# 1 represents connection , 0 represents disconnection.

    def first_conn_check(self,url):
        try:
            print(f"Evaluating connection to {url}.... ")
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # IPV4 , TCP
            s.settimeout(2)
            s.connect((url,80))
            s.close()
            print(f'{url} is up\n')
            return 1
            sleep(1)
        except Exception:
            print(f'{url} is down\n')
            return 0
            sleep(1)
            sys.exit(0)

    def insert_url(self,url):
        time_stamp=str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        init_conn=self.first_conn_check(url)
        self.cur.execute("INSERT INTO urls VALUES (NULL,?,?,?,?)",(url,init_conn,init_conn,time_stamp))
        self.con.commit()


    def view_table(self):
        self.cur.execute("SELECT id,url,prevS,curS,time_stamp FROM urls")
        table=self.cur.fetchall()
        return table

    def view_urls(self):
        self.cur.execute("SELECT url FROM urls")
        urls=self.cur.fetchall()
        return urls


    def delete(self,id):
        self.cur.execute("DELETE FROM urls WHERE id=?",(id,))
        self.con.commit()
