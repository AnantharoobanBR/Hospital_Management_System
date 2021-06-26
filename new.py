import sqlite3


#----execute this block-----
conn = sqlite3.connect('medical.db')
mycursor = conn.cursor()
query= "ALTER TABLE doctor DROP(ava)"
mycursor.execute(query)
conn.commit()
print("success")
conn.close()
