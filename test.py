import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
# cursor.execute("DELETE FROM mahsulotlar WHERE name='Gamburger'")
# connect.commit()
# connect.commit()
# Gamburger,22000,Gamburger.jpg,burgerlar
# cursor.execute('INSERT INTO mahsulotlar VALUES (?,?,?,?)', ('Gamburger', 22000, 'Gamburger.jpg', 'burgerlar'))
# connect.commit()
# cursor.execute(f"UPDATE mahsulotlar SET image = 'Cheese_burger.jpg' WHERE image=';Cheese_burger.jpg'");
# connect.commit()