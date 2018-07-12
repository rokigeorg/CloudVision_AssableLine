from flask import Flask, request, flash, url_for, redirect, render_template
import sqlite3

app = Flask(__name__)


class ImgEntrys:
    '''
    __tablename__ = "Bilder"
    id = db.Column('id', db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    sufix = db.Column(db.String(10))
    pathtopic = db.Column(db.String(300))
    #rawbits = db.Column(db.Binary)
    isCircle = db.Column(db.Integer)
    csvlabels = db.Column(db.String(10))
    '''

    def __init__(self, filename="", sufix="", pathtopic="", rawbits=None, isCircle="", csvlabels=""):
        self.filename = filename
        self.sufix = sufix
        self.pathtopic = pathtopic
        self.rawbits = rawbits
        self.isCircle = isCircle
        self.csvlabels = csvlabels

    def queryAll(self):
        # create or connect to database
        conn = sqlite3.connect('/home/pi/EmbeddedSystemsProject/06_Assably/storage/testDB.db')
        # get the curser to do stuff in the db
        cur = conn.cursor()

        cur.execute("""SELECT filename,pathtopic, isCircle, csvlabels FROM Bilder""")
        data = cur.fetchone()
        # send all commands from the cursor to the db
        conn.commit()
        # close the db conncetion savely
        conn.close()
        print(data)
        return ImgEntrys("1", "2", "/path/to/see", None, "1", "a,b,c,d")


class DataBaseAdapter():
    def __init__(self, filename="", sufix="", pathtopic="", rawbits=None, isCircle="", csvlabels=""):
        self.filename = filename
        self.sufix = sufix
        self.pathtopic = pathtopic
        self.rawbits = rawbits
        self.isCircle = isCircle
        self.csvlabels = csvlabels

    def conncetToDB(self):
        # create or connect to database
        self.conn = sqlite3.connect('/home/pi/EmbeddedSystemsProject/06_Assambly/storage/testDB.db')
        # get the curser to do stuff in the db
        self.cur = self.conn.cursor()

    def getAllEntries(self):
        print("Start zu query DB.")
        self.conncetToDB()
        self.cur.execute("""SELECT filename,pathtopic, isCircle, csvlabels FROM Bilder""")
        # data = self.cur.fetchone()
        for row in self.cur.fetchall():
            print(row)
        self.conn.commit()
        self.conn.close()
        # print(data)

    def getLastEntry(self):
        print("Start zu query DB.")
        self.conncetToDB()
        self.cur.execute(
            """SELECT filename,pathtopic,rawbits, isCircle, csvlabels FROM Bilder ORDER BY id desc limit 1""")
        data = self.cur.fetchone()
        self.conn.commit()
        # close the db conncetion savely
        self.conn.close()
        print(data)
        return data

    def getImgDbAndSaveItToStatics(self):
        print("Start zu query DB.")
        self.conncetToDB()
        self.cur.execute("""SELECT filename , rawbits FROM Bilder ORDER BY id desc limit 1""")
        data = self.cur.fetchone()
        self.conn.commit()
        # close the db conncetion savely
        self.conn.close()
        print(data)
        return data



@app.route('/')
def show_all():
    dbA = DataBaseAdapter()
    row = dbA.getLastEntry()
    lastEntry = ImgEntrys(filename=row[0], pathtopic=row[1], rawbits=row[2], isCircle=row[3], csvlabels=row[4])
    return render_template('test.html', imgEntry=lastEntry)


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            # student = students(request.form['name'], request.form['city'],
            #                  request.form['addr'], request.form['pin'])

            # db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
