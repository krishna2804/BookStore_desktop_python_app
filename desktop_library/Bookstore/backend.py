import sqlite3
def connect():
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(ids INTEGER PRIMARY KEY,title TEXT,author VARCHAR ,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows
	
def delete(author):
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE author=?",(author,))
    conn.commit()
    conn.close()
    
def update(key,title,author,year,isbn):
    conn=sqlite3.connect("library.bd")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?,author=?,year=?,isbn=? WHERE ids=?",(title,author,year,isbn,key))
    conn.commit()
    conn.close()


    
connect()
#insert("the indian","APJ",1999,1234567)
#insert("the IIITV","PVKR",2013,5674344)
#print("-----------------------------------------------------------------------------")
#print(view())
#update(3,"the society","RAM",2019,231232)
#print("--------------------------------after delete---------------------------------------------")

#delete("APJ")
#print("-----------------------------------------------------------------------------")

##print(view())
#print("-----------------------------------------------------------------------------")

#print(search(author="RAM"))


