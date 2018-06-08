from app import db

class students(db.Model):
    __tablename__ = "students"
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


def init_db():
    db.create_all()

    # Create a test user
    student1 = students('nata','Leipzig','a@a.com', '123')
    db.session.add(student1)
    db.session.commit()


if __name__ == '__main__':
    init_db()