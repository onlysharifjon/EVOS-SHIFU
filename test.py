import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()



cursor.execute("DELETE FROM korzinka WHERE status=0")
connect.commit()
connect.close()

