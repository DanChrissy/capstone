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
from calculations import tutcourse

from app import db
from app.models import Student,Tutor, StudentAvailability, TutorAvailability, StudentPreference, TutorPreference, Course, Day,CourseTutorMatch, CourseCount, TutorStudentMatch
@app.route('/')
def home():
    """Render website's home page with vuejs."""
    return render_template('home.html')
 
@app.route('/tutForm', methods=["GET","POST"])
def tutForm():
    tutorForm=TutorForm()
    courses = db.session.query(Course)
    days = db.session.query(Day)
    
    if request.method == 'POST':
        id_number = request.form.get('ID')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        areaStudy=request.form.get('areaOfStudy')
        tutor_profile = Tutor(tutor_id = id_number,tutor_firstname = firstname,tutor_lastname = lastname,tutor_email = email, area_study = areaStudy)
        db.session.add(tutor_profile)
        db.session.commit()
        
        start1 = request.form.get('start1')
        start2 = request.form.get('start2')
        start3 = request.form.get('start3')
        start4 = request.form.get('start4')
        end1 = request.form.get('end1')
        end2 = request.form.get('end2')
        end3 = request.form.get('end3')
        end4 = request.form.get('end4')
        
        day1 = request.form.get('day1')
        tutor_availability1 = TutorAvailability(tutor_id=id_number, day_id=day1, start_time=start1, end_time=end1)
        db.session.add(tutor_availability1)
        db.session.commit()
        

        day2 = request.form.get('day2')
        day3 = request.form.get('day3')
        day4 = request.form.get('day4')
        if day2 != "":
            tutor_availability2 = TutorAvailability(tutor_id=id_number, day_id=day2, start_time=start2, end_time=end2)
            db.session.add(tutor_availability2)
            db.session.commit()
        elif day3 != "":
            tutor_availability3 = TutorAvailability(tutor_id=id_number, day_id=day3, start_time=start3, end_time=end3)
            db.session.add(tutor_availability3)
            db.session.commit()
        elif day4 != "":
            tutor_availability4 = TutorAvailability(tutor_id=id_number, day_id=day4, start_time=start4, end_time=end4)
            db.session.add(tutor_availability4)
            db.session.commit()
        else:
            return(redirect(url_for('home')))
        
        
        option1 = request.form.get('options1')
        option2 = request.form.get('options2')
        
        course = TutorPreference(tutor_id=id_number,preference_1=option1, preference_2=option2)
        db.session.add(course)
        db.session.commit()
        
        return(redirect(url_for('tutView')))
        
        
    return render_template('tutForm.html', form = tutorForm, courses=courses, days=days)
    
@app.route('/adminView', methods=["GET","POST"])
def adminView():
    adminView=AdminView()
    
    return render_template('adminView.html',adminView = adminView)

@app.route('/tutView')
def tutView():
    return render_template('tutView.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/stuView')
def stuView():
    return render_template('stuView.html')

@app.route('/tutView1')
def tutView1():
    return render_template('tutView1.html')
    
@app.route('/login', methods=["GET","POST"])
def login():
    login=Login()
    
    if request.method == 'POST':
        user = request.form.get("user")
        password = request.form.get("pass")
    
        if (user == "admin" and password == "admin"):
            return(redirect(url_for('adminView')))
        
    return render_template('login.html',login = login)

@app.route('/stuForm', methods=["GET","POST"])
def stuForm():
    studentForm=StudentForm()
    courses = db.session.query(Course)
    days = db.session.query(Day)
    tutors_ava = db.session.query(TutorAvailability)
    tutors = db.session.query(Tutor)
    
    if request.method == 'POST':
        id_number = request.form.get('ID')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        student_profile = Student(student_id = id_number,student_firstname = firstname,student_lastname = lastname,student_email = email)
        db.session.add(student_profile)
        db.session.commit()
        
        start1 = request.form.get('start1')
        start2 = request.form.get('start2')
        start3 = request.form.get('start3')
        start4 = request.form.get('start4')
        end1 = request.form.get('end1')
        end2 = request.form.get('end2')
        end3 = request.form.get('end3')
        end4 = request.form.get('end4')
        
        option1 = request.form.get('options1')
        option2 = request.form.get('options2')
        course = StudentPreference(student_id=id_number,stucourse_id_1=option1, stucourse_id_2=option2)
        db.session.add(course)
        db.session.commit()
        
        day1 = request.form.get('day1')
        student_availability1 = StudentAvailability(student_id=id_number, day_id=day1, start_time=start1, end_time=end1)
        db.session.add(student_availability1)
        db.session.commit()

        day2 = request.form.get('day2')
        day3 = request.form.get('day3')
        day4 = request.form.get('day4')
        
        if day2 != "":
            student_availability2 = StudentAvailability(student_id=id_number, day_id=day2, start_time=start2, end_time=end2 )
            db.session.add(student_availability2)
            db.session.commit()
        elif day3 != "":
            student_availability3 = StudentAvailability(student_id=id_number, day_id=day3, start_time=start3, end_time=end3 )
            db.session.add(student_availability3)
            db.session.commit()
            
        elif day4 !="":
            student_availability4 = StudentAvailability(student_id=id_number, day_id=day4, start_time=start4, end_time=end4 )
            db.session.add(student_availability4)
            db.session.commit()
        else:
            return(redirect(url_for('home')))
            
        return(redirect(url_for('stuView')))
        
        '''if (option1 == option2):
            flash("Please input two different course options")
            return render_template('stuForm.html',studentForm = studentForm, courses=courses, days=days)
        elif (start1 == end1 or start2 == end2 or start3 == end3 or start4 == end4):
            flash("Start and end times cannot be the same.")
            return render_template('stuForm.html',studentForm = studentForm, courses=courses, days=days)
        else:'''
        
                
        
    return render_template('stuForm.html',form = studentForm, courses=courses, days=days)
    

@app.route('/course_tutor', methods=['POST','GET'])
def course_tutor():
    if request.method =='POST':
        tutcourse()
        return redirect(url_for('course_list'))
    return render_template('course_tutor.html')

@app.route('/courseList', methods = ['POST','GET'])
def course_list():
    #matches = db.session.query(CourseTutorMatch).all()
    if request.method == 'POST':
        results = tutcourse()
    return render_template('courseList.html', results=results)
        
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
    
@app.route('/studentEdit') #/<studentid>', methods = ['POST','GET'])
def studentEdit():
    #studentForm = StudentForm()
    #if request.method == 'POST' and studentForm.validate_on_submit():
        #Add student info and keep id
    #studentid = StudentTable.query.get(studentid)
    return render_template('studentEdit.html') #, studentid = studentid)

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

