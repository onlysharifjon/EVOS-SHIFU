import sqlite3

connect = sqlite3.connect('evos_.database.db')
cursor = connect.cursor()



cursor.execute("DELETE FROM buyurtma_tarixi WHERE buyurtmachi_id=5172746353")
connect.commit()


