import sqlite3

# create or connect to database
conn = sqlite3.connect('testDB.db')

# get the curser to do stuff in the db
cur = conn.cursor()


cur.execute("""SELECT name,bdata FROM pictures WHERE name == 'pic_4.png' """)

data = cur.fetchone()
# send all commands from the cursor to the db
conn.commit()

# close the db conncetion savely
conn.close()

print data

file = open("new.jpg",'wb')
file.write(data[1])
file.close()

