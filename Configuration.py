import sqlite3 as sql
con = sql.connect("Storage.db")
c = con.cursor()
c.execute("""
CREATE TABLE support (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Issue VARCHAR(100),
    Description VARCHAR(100)
)
""")
con.commit()
con.close()