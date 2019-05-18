"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app
from wtforms.form import Form
from flask import render_template, request, redirect, url_for, flash, session, abort
from form import Search, TutorForm, StudentForm, Login, AdminView

@app.route('/')
def home():
    """Render website's home page with vuejs."""
    return render_template('home.html')

@app.route('/tutForm', methods=["GET","POST"])
def tutForm():
    tutorForm=TutorForm()
    
    return render_template('tutForm.html', tutorForm = tutorForm)
    
@app.route('/adminView', methods=["GET","POST"])
def adminView():
    adminView=AdminView()
    
    return render_template('adminView.html',adminView = adminView)
    
@app.route('/login', methods=["GET","POST"])
def login():
    login=Login()
    
    return render_template('login.html',login = login)

@app.route('/stuForm', methods=["GET","POST"])
def stuForm():
    studentForm=StudentForm()
    return render_template('stuForm.html',studentForm = studentForm)
    

@app.route('/search')
def search():
    searchForm = Search()
    return render_template('search.html', form = searchForm)

@app.route('/studentrecord')
def studentRecord():
    return render_template('studentRecord.html')

@app.route('/tutorrecord')
def tutorRecord():
    return render_template('tutorRecord.html')
    
@app.route('/studentEdit') #/<studentId>', methods = ['POST','GET'])
def studentEdit():
    #studentForm = StudentForm()
    #if request.method == 'POST' and studentForm.validate_on_submit():
        #Add student info and keep id
    #studentId = StudentTable.query.get(studentId)
    return render_template('studentEdit.html') #, studentId = studentId)

@app.route('/tutorEdit')
def tutorEdit():
    return render_template('tutorEdit.html')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

