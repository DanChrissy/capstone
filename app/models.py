from . import db

class Room(db.Model):
    __tablename__ = 'room'
    room_ID = db.Column(db.String, primary_key = True)
    room_name = db.Column(db.String)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.room_ID)  # python 2 support
        except NameError:
            return str(self.room_ID)  # python 3 support

    def __repr__(self):
        return '<%r ID is %r>' % (self.room_name,self.room_ID)

class CourseRoom(db.Model):
    __tablename__ = 'CourseRoom'
    course_ID = db.Column(db.String, db.ForeignKey('course.course_ID'), primary_key=True)
    room_ID_1 = db.Column(db.String, db.ForeignKey('room.room_ID'))
    room_ID_2 = db.Column(db.String, db.ForeignKey('room.room_ID'))
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_ID)  # python 2 support
        except NameError:
            return str(self.course_ID)  # python 3 support

    def __repr__(self):
        return '<%r is assigned rooms %r and %r>' % (self.course_ID,self.room_ID_1,self.room_ID_2)
        

class Day(db.Model):
    __tablename__ = 'day'
    day_ID = db.Column(db.String, primary_key = True)
    day_name = db.Column(db.String, nullable = False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.day_ID)  # python 2 support
        except NameError:
            return str(self.day_ID)  # python 3 support

    def __repr__(self):
        return '<%r ID is %r>' % (self.day_name,self.day_ID)
        
class Student(db.Model):
    __tablename__ = 'student'
    student_ID = db.Column(db.String, primary_key=True)
    student_firstName = db.Column(db.String, nullable = False)
    student_lastName = db.Column(db.String, nullable = False)
    student_email = db.Column(db.String, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_ID)  # python 2 support
        except NameError:
            return str(self.student_ID)  # python 3 support

    def __repr__(self):
        return '<Student is %r %r>' % (self.student_firstName,self.student_lastName)

class StudentPreferences(db.Model):
    __tablename__ = 'studentPreferences'
    student_ID = db.Column(db.String, db.ForeignKey('student.student_ID'), primary_key=True)
    stuCourse_ID_1  = db.Column(db.String, db. ForeignKey('course.course_ID'), nullable = False)
    stuCourse_ID_2  = db.Column(db.String, db. ForeignKey('course.course_ID'))
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_ID)  # python 2 support
        except NameError:
            return str(self.student_ID)  # python 3 support

    def __repr__(self):
        return '<Student with ID %r selected the courses %r and %r>' % (self.student_ID,self.stuCourse_ID_1,self. stuCourse_ID_2)
    

class StudentAvailability(db.Model):
    __tablename__ = 'studentAvailability'
    student_ID = db.Column(db.String, db.ForeignKey('student.student_ID'), primary_key=True)
    day_ID = db.Column(db.String, db.ForeignKey('day.day_ID'), primary_key=True, nullable = False)
    start_time = db.Column(db.String, primary_key=True, nullable = False)
    end_time = db.Column(db.String, primary_key=True, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_ID,self.day_ID,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.student_ID,self.day_ID,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Student %r is available on %r between the hours of %r and %r. >' % (self.student_ID,self.day_ID, self.start_time, self.end_time)

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutor_ID = db.Column(db.String, primary_key=True)
    tutor_firstName = db.Column(db.String, nullable = False)
    tutor_lastName = db.Column(db.String, nullable = False)
    tutor_email = db.Column(db.String, nullable = False)
    area_study = db.Column(db.String, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_ID)  # python 2 support
        except NameError:
            return str(self.tutor_ID)  # python 3 support

    def __repr__(self):
        return '<Tutor is %r %r>' % (self.tutor_firstName,self.tutor_lastName)

class TutorPreference(db.Model):
    __tablename__ = 'tutorPreference'
    tutor_ID = db.Column(db.String, db.ForeignKey('tutor.tutor_ID'),primary_key=True, nullable = False)
    preference_1 = db.Column(db.String, db.ForeignKey('course.course_ID'), nullable = False)
    preference_2 = db.Column(db.String, db.ForeignKey('course.course_ID'))
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_ID)  # python 2 support
        except NameError:
            return str(self.tutor_ID)  # python 3 support

    def __repr__(self):
        return "<Tutor's preferences are %r and %r>" % (self.preference_1, self.preference_2)

class TutorAvailability(db.Model):
    __tablename__ = 'tutorAvailability'
    tutor_ID = db.Column(db.String, db.ForeignKey('tutor.tutor_ID'), primary_key=True)
    day_ID = db.Column(db.String, db.ForeignKey('day.day_ID'), primary_key=True, nullable = False)
    start_time = db.Column(db.String, primary_key=True, nullable = False)
    end_time = db.Column(db.String, primary_key=True, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_ID,self.day_ID,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.tutor_ID,self.day_ID,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Tutor %r is available on %r between the hours of %r and %r. >' % (self.tutor_ID,self.day_ID, self.start_time, self.end_time)


class Course(db.Model):
    __tablename__ = 'course'
    course_ID = db.Column(db.String,primary_key=True)
    course_name = db.Column(db.String, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_ID)  # python 2 support
        except NameError:
            return str(self.course_ID)  # python 3 support

    def __repr__(self):
        return '<Course is %r>' % (self.course_name)

class CourseCount (db.Model):
    __tablename__= 'courseCount'
    course_ID = db.Column(db.String, db.ForeignKey('course.course_ID'), primary_key=True)
    count_students = db.Column(db.Integer, nullable = False)
    count_tutors = db.Column(db.Integer, nullable = False)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_ID)  # python 2 support
        except NameError:
            return str(self.course_ID)  # python 3 support

    def __repr__(self):
        return '<Number of students and tutors in course are %r and %r respectively. >' % (self.count_students,self.count_tutors)


class CourseTutorMatch(db.Model):
    __tablename__ = 'courseMatch'
    course_ID = db.Column(db.String, db.ForeignKey('course.course_ID'),primary_key = True)
    tutor_ID_1 = db.Column(db.String, db.ForeignKey('tutor.tutor_ID'), nullable = False)
    tutor_ID_2 = db.Column(db.String, db.ForeignKey('tutor.tutor_ID'))
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_ID)  # python 2 support
        except NameError:
            return str(self.tutor_ID)  # python 3 support

    def __repr__(self):
        return '<Course %r will be tutored by %r and %r>' % (self.course_ID,self.tutor_ID_1,self.tutor_ID_2)

class TutorStudentMatch(db.Model):
    __tablename__= 'studentMatch'
    tutor_ID = db.Column(db.String, db.ForeignKey('tutor.tutor_ID'), primary_key=True)
    student_ID = db.Column(db.String, db.ForeignKey('student.student_ID'), primary_key=True)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_ID,self.student_ID)  # python 2 support
        except NameError:
            return str(self.tutor_ID, self.student_ID)  # python 3 support

    def __repr__(self):
        return '<Tutor %r will be tutoring %r >' % (self.tutor_ID,self.student_ID)
