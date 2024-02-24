# import sqlite3

# connect = sqlite3.connect('C:/Users/Sharifjon/PycharmProjects/EVOS-SHIFU/evos_.database.db')
# cursor = connect.cursor()
# # cursor.execute("DROP TABLE korzinka")

# # Connect to the SQLite database (creates a new database if not exist)


# # SQL query to create the table
# create_table_query = '''
# CREATE TABLE korzinka (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   mahsulot VARCHAR(20),
#   user_id BIGINT NOT NULL,
#   soni INTEGER,
#   status INTEGER CHECK (status IN (0, 1)) -- Ensure status is either 0 or 1
# );
# '''

# # Execute the SQL query
# cursor.execute(create_table_query)

# # Commit the changes
# connect.commit()

# # Close the connection
# connect.close()

# a = "51882851050058"
# print(len(a))