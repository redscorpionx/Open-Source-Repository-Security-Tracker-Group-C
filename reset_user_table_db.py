# use this code to clear the  users table from the database after testing the application. This will ensure that the database is empty when you start the application again.

import sqlite3

# Connect to the database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

# Clear data from the "users" table
cursor.execute("DELETE FROM users")
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()