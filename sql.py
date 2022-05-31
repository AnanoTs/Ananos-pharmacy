import sqlite3
database = 'pharmacy.db'
con = sqlite3.connect('pharmacy.db', check_same_thread=False)
cur = con.cursor()

cur.execute('''create table users (name text , surname text, gmail text, password text)''')

def add_users(name , surname , gmail , password):
    cur.execute("INSERT INTO users (name , surname , gmail , password) VALUES (? , ? , ? , ? ") 
    
con.commit();
