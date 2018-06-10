import sqlite3
from picamera import PiCamera
from time import gmtime, strftime
import sys

PWD = sys.path[0]

camera = PiCamera()
camera.start_preview()
ts = strftime("%d-%b-%Y%H-%M-%S", gmtime())
tmp = PWD + "/img_" + str(ts) + ".jpg"
camera.capture(tmp)
camera.stop_preview()

file = open(tmp, "r")

# create or connect to database
conn = sqlite3.connect('testDB.db')

# get the curser to do stuff in the db
cur = conn.cursor()

'''
cur.execute("""CREATE TABLE pictures(
              name text,
              createAt text,
              bdata blob)
              """)
'''

# cur.execute("""INSERT INTO pictures VALUES ('img_1.png', '06-06-2018-01-05','8000')""")

# cur.execute("INSERT INTO pictures VALUES (:name, :createAt, :pay)", {'name': "pic_2.png", 'createAt':"00-22-33-44-55", 'pay':'700'})
cur.execute("INSERT INTO pictures VALUES (:name, :createAt, :bdata)",
            {'name': "pic_4.png", 'createAt': "00-22-33-44-55", 'bdata': sqlite3.Binary(file.read())})

cur.execute("""SELECT * FROM pictures""")
data = cur.fetchall()
print data
# send all commands from the cursor to the db
conn.commit()

# close the db conncetion savely
conn.close()
