from . import db

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.String,primary_key=True)
    course_name = db.Column(db.String, nullable = False)
    
    course_room = db.relationship("CourseRoom", foreign_keys = [course_id, course_id],backref = "course", cascade = "all, delete, delete-orphan, save-update" )
    course_count = db.relationship("CourseCount", foreign_keys = [course_id],backref = "course", cascade = "all, delete, delete-orphan, save-update" )
    course_match = db.relationship("CourseTutorMatch", foreign_keys = [course_id],backref = "course", cascade = "all, delete, delete-orphan, save-update" )

    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_id)  # python 2 support
        except NameError:
            return str(self.course_id)  # python 3 support

    def __repr__(self):
        return '<Course is %r>' % (self.course_name)

class Room(db.Model):
    __tablename__ = 'room'
    room_id = db.Column(db.String, primary_key = True)
    room_name = db.Column(db.String)
    
    courseroom = db.relationship("CourseRoom", foreign_keys = [room_id, room_id], backref = "room", cascade = "all, delete, delete-orphan, save-update" )
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.room_id)  # python 2 support
        except NameError:
            return str(self.room_id)  # python 3 support

    def __repr__(self):
        return '<%r id is %r>' % (self.room_name,self.room_id)

class CourseRoom(db.Model):
    __tablename__ = 'courseroom'
    course_id = db.Column(db.String, db.ForeignKey('course.course_id'), primary_key=True)
    room_id_1 = db.Column(db.String, db.ForeignKey('room.room_id'))
    room_id_2 = db.Column(db.String, db.ForeignKey('room.room_id'))
    
    room1 = db.relationship("Room", primaryjoin = "CourseRoom.room_id_1 == Room.room_id")
    room1 = db.relationship("Room", primaryjoin = "CourseRoom.room_id_2 == Room.room_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_id)  # python 2 support
        except NameError:
            return str(self.course_id)  # python 3 support

    def __repr__(self):
        return '<%r is assigned rooms %r and %r>' % (self.course_id,self.room_id_1,self.room_id_2)
        

class Day(db.Model):
    __tablename__ = 'day'
    day_id = db.Column(db.String, primary_key = True)
    day_name = db.Column(db.String, nullable = False)
    
    stu_day = db.relationship("StudentAvailability", foreign_keys = [day_id], backref = "day", cascade = "all, delete, delete-orphan, save-update" )
    tut_day = db.relationship("TutorAvailability", foreign_keys = [day_id], backref = "day", cascade = "all, delete, delete-orphan, save-update" )

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.day_id)  # python 2 support
        except NameError:
            return str(self.day_id)  # python 3 support

    def __repr__(self):
        return '<%r id is %r>' % (self.day_name,self.day_id)
        
class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.String, primary_key=True)
    student_firstname = db.Column(db.String, nullable = False)
    student_lastname = db.Column(db.String, nullable = False)
    student_email = db.Column(db.String, nullable = False)
    
    stu_available = db.relationship("StudentAvailability", foreign_keys = [student_id], backref = "student", cascade = "all, delete, delete-orphan, save-update" )
    stu_pref = db.relationship("StudentPreference", foreign_keys = [student_id, student_id], backref = "student", cascade = "all, delete, delete-orphan, save-update" )
    stu_match = db.relationship("TutorStudentMatch", foreign_keys = [student_id], backref = "student", cascade = "all, delete, delete-orphan, save-update" )

    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_id)  # python 2 support
        except NameError:
            return str(self.student_id)  # python 3 support

    def __repr__(self):
        return '<Student is %r %r>' % (self.student_firstname,self.student_lastname)

class StudentPreference(db.Model):
    __tablename__ = 'studentpreference'
    student_id = db.Column(db.String, db.ForeignKey('student.student_id'), primary_key=True)
    stucourse_id_1  = db.Column(db.String, db. ForeignKey('course.course_id'), nullable = False)
    stucourse_id_2  = db.Column(db.String, db. ForeignKey('course.course_id'))
    
    student1 = db.relationship("Course", primaryjoin = "StudentPreference.stucourse_id_1 == Course.course_id")
    student2 = db.relationship("Course", primaryjoin = "StudentPreference.stucourse_id_2 == Course.course_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_id)  # python 2 support
        except NameError:
            return str(self.student_id)  # python 3 support

    def __repr__(self):
        return '<Student with id %r selected the courses %r and %r>' % (self.student_id,self.stucourse_id_1,self. stucourse_id_2)
    

class StudentAvailability(db.Model):
    __tablename__ = 'studentavailability'
    student_id = db.Column(db.String, db.ForeignKey('student.student_id'), primary_key=True)
    day_id = db.Column(db.String, db.ForeignKey('day.day_id'), primary_key=True, nullable = False)
    start_time = db.Column(db.String, primary_key=True, nullable = False)
    end_time = db.Column(db.String, primary_key=True, nullable = False)
    
    stu_ava = db.relationship("Student", primaryjoin = "StudentAvailability.student_id == Student.student_id")
    stu_day = db.relationship("Day", primaryjoin = "StudentAvailability.day_id == Day.day_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.student_id,self.day_id,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.student_id,self.day_id,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Student %r is available on %r between the hours of %r and %r. >' % (self.student_id,self.day_id, self.start_time, self.end_time)

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutor_id = db.Column(db.String, primary_key=True)
    tutor_firstname = db.Column(db.String, nullable = False)
    tutor_lastname = db.Column(db.String, nullable = False)
    tutor_email = db.Column(db.String, nullable = False)
    area_study = db.Column(db.String, nullable = False)
    
    tut_available = db.relationship("TutorAvailability", foreign_keys = [tutor_id], backref = "tutor", cascade = "all, delete, delete-orphan, save-update" )
    tut_pref = db.relationship("TutorPreference", foreign_keys = [tutor_id, tutor_id],backref = "tutor", cascade = "all, delete, delete-orphan, save-update" )
    tut_match = db.relationship("CourseTutorMatch", foreign_keys = [tutor_id, tutor_id],backref = "tutor", cascade = "all, delete, delete-orphan, save-update" )
    tut_stu_match = db.relationship("TutorStudentMatch", foreign_keys = [tutor_id],backref = "tutor", cascade = "all, delete, delete-orphan, save-update" )

    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_id)  # python 2 support
        except NameError:
            return str(self.tutor_id)  # python 3 support

    def __repr__(self):
        return '<Tutor is %r %r>' % (self.tutor_firstName,self.tutor_lastName)

class TutorPreference(db.Model):
    __tablename__ = 'tutorpreference'
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id'),primary_key=True, nullable = False)
    preference_1 = db.Column(db.String, db.ForeignKey('course.course_id'), nullable = False)
    preference_2 = db.Column(db.String, db.ForeignKey('course.course_id'))
    
    tutor1 = db.relationship("Course", primaryjoin = "TutorPreference.preference_1 == Course.course_id")
    tutor2 = db.relationship("Course", primaryjoin = "TutorPreference.preference_2 == Course.course_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_id)  # python 2 support
        except NameError:
            return str(self.tutor_id)  # python 3 support

    def __repr__(self):
        return "<Tutor's preferences are %r and %r>" % (self.preference_1, self.preference_2)

class TutorAvailability(db.Model):
    __tablename__ = 'tutoravailability'
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id'), primary_key=True)
    day_id = db.Column(db.String, db.ForeignKey('day.day_id'), primary_key=True, nullable = False)
    start_time = db.Column(db.String, primary_key=True, nullable = False)
    end_time = db.Column(db.String, primary_key=True, nullable = False)
    
    tut_ava = db.relationship("Student", primaryjoin = "TutorAvailability.tutor_id == Tutor.tutor_id")
    tut_day = db.relationship("Day", primaryjoin = "TutorAvailability.day_id == Day.day_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_id,self.day_id,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.tutor_id,self.day_id,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Tutor %r is available on %r between the hours of %r and %r. >' % (self.tutor_id,self.day_id, self.start_time, self.end_time)



class CourseCount (db.Model):
    __tablename__= 'coursecount'
    course_id = db.Column(db.String, db.ForeignKey('course.course_id'), primary_key=True)
    count_students = db.Column(db.Integer, nullable = False)
    count_tutors = db.Column(db.Integer, nullable = False)
    
    count_course = db.relationship("Course", primaryjoin = "CourseCount.course_id == Course.course_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.course_id)  # python 2 support
        except NameError:
            return str(self.course_id)  # python 3 support

    def __repr__(self):
        return '<Number of students and tutors in course are %r and %r respectively. >' % (self.count_students,self.count_tutors)


class CourseTutorMatch(db.Model):
    __tablename__ = 'coursematch'
    course_id = db.Column(db.String, db.ForeignKey('course.course_id'),primary_key = True)
    tutor_id_1 = db.Column(db.String, db.ForeignKey('tutor.tutor_id'), nullable = False)
    tutor_id_2 = db.Column(db.String, db.ForeignKey('tutor.tutor_id'))
    
    match1 = db.relationship("Tutor", primaryjoin = "CourseTutorMatch.tutor_id_1 == Tutor.tutor_id")
    match2 = db.relationship("Tutor", primaryjoin = "CourseTutorMatch.tutor_id_2 == Tutor.tutor_id")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_id)  # python 2 support
        except NameError:
            return str(self.tutor_id)  # python 3 support

    def __repr__(self):
        return '<Course %r will be tutored by %r and %r>' % (self.course_id,self.tutor_id_1,self.tutor_id_2)

class TutorStudentMatch(db.Model):
    __tablename__= 'studentmatch'
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id'), primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student.student_id'), primary_key=True)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_id,self.student_id)  # python 2 support
        except NameError:
            return str(self.tutor_id, self.student_id)  # python 3 support

    def __repr__(self):
        return '<Tutor %r will be tutoring %r >' % (self.tutor_id,self.student_id)
