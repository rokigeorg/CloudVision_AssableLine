from flask import render_template
from app import app
from database import students
print("***** Create the routes ******")

@app.route('/all')
def show_all():
   return render_template('show_all.html', students = students.query.all() )


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)





