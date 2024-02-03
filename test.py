import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
cursor.execute('INSERT INTO mahsulotlar VALUES (?,?,?,?)',
               ("Kids COMBO", 24000, "Kids_COMBO.jpg", 'setlar'))
connect.commit()
