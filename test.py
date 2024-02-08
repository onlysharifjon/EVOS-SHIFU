import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
cursor.execute('INSERT INTO mahsulotlar VALUES (?,?,?,?)',
               ("Lavash mol go'sht", 26000, "Lavash_mol_gosht.jpg", 'lavashlar'))
connect.commit()
#