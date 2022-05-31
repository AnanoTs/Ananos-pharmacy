import sqlite3

from colorama import Cursor
database = 'pharmacy.db'
con = sqlite3.connect('pharmacy.db', check_same_thread=False)
cur = con.cursor()

cur.execute('''create table drugs (name text , term text,  price text)''')

def add_drugs(name, term , price):
    cur.execute("INSERT INTO drugs (name , term , price))VALUES (?, ?, ?")
    con.commit();

cur.execute('''INSERT INTO DRUGS VALUES ('ნიმესილი','22.05.2023', 22.90)''')
cur.execute('''INSERT INTO DRUGS VALUES ('ნალგეზინი', '13.08.2025', '9')''')
cur.execute('''INSERT INTO DRUGS VALUES ('პარაცეტამოლი', '08.06.2023', '7.90')''')
cur.execute('''INSERT INTO DRUGS VALUES ('კეტონალი', '20.08.2024', '23')''')

cur.execute()
con.commit()

