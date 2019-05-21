from . import db

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.String,primary_key=True)
    course_name = db.Column(db.String, nullable = False)
    
    '''student_pref = db.relationship('StudentPreference',  backref="student_pref", cascade="all, delete-orphan")
    student_pref1 = db.relationship('StudentPreference',  backref="student_pref1", cascade="all, delete-orphan")
    student_ava = db.relationship('StudentAvailability', backref="student_ava", cascade="all, delete-orphan")
    tut_pref = db.relationship('TutorPreference', backref="tut_pref", cascade="all, delete-orphan")
    tut_pref1 = db.relationship('TutorPreference', backref="tut_pref1", cascade="all, delete-orphan")
    tut_ava = db.relationship('TutorAvailability', backref="tut_ava", cascade="all, delete-orphan")
    tutor_match = db.relationship('CourseTutorMatch', backref="tutor_match", cascade="all, delete-orphan")'''

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
    
    '''tut_room = db.relationship('TutorRoom', backref="tut_room", cascade="all, delete-orphan")
    mon = db.relationship('MondayRoomAvailability', backref="mon", cascade="all, delete-orphan")
    tues = db.relationship('TuesdayRoomAvailability', backref="tues", cascade="all, delete-orphan")
    wed = db.relationship('WednesdayRoomAvailability', backref="wed", cascade="all, delete-orphan")
    thur = db.relationship('ThursdayRoomAvailability', backref="thur", cascade="all, delete-orphan")
    fri = db.relationship('FridayRoomAvailability', backref="fri", cascade="all, delete-orphan")
    sat = db.relationship('SaturdayRoomAvailability', backref="sat", cascade="all, delete-orphan")'''
    
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

class Day(db.Model):
    __tablename__ = 'day'
    day_id = db.Column(db.String, primary_key = True)
    day_name = db.Column(db.String, nullable = False)
    
    '''student_day = db.relationship('StudentAvailability', backref="student_day", cascade="all, delete-orphan")
    tutor_day = db.relationship('StudentAvailability', backref="tutor_day", cascade="all, delete-orphan")'''

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
    
    stu_pref = db.relationship('StudentPreference', backref="stu_pref", cascade="all, delete-orphan")
    stu_ava = db.relationship('StudentAvailability', backref="stu_ava", cascade="all, delete-orphan")
    tut_stu = db.relationship('TutorStudentMatch', backref="tut_stu", cascade="all, delete-orphan")
    
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

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutor_id = db.Column(db.String, primary_key=True)
    tutor_firstname = db.Column(db.String, nullable = False)
    tutor_lastname = db.Column(db.String, nullable = False)
    tutor_email = db.Column(db.String, nullable = False)
    area_study = db.Column(db.String, nullable = False)
    
    '''pref_tut = db.relationship('TutorPreference', backref="pref_tut", cascade="all, delete-orphan")
    ava_tut = db.relationship('TutorAvailability', backref="tut_ava", cascade="all, delete-orphan")
    match_tutor = db.relationship('CourseTutorMatch', backref="match_tutor", cascade="all, delete-orphan")
    stu_tut = db.relationship('TutorStudentMatch', backref="stu_tut", cascade="all, delete-orphan")
    count_tut = db.relationship('TutorCount', backref="count_tut", cascade="all, delete-orphan")
    room_tut = db.relationship('TutorRoom', backref="room_tut", cascade="all, delete-orphan")'''
    
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
        return '<Tutor is %r %r>' % (self.tutor_firstname,self.tutor_lastname)

class TutorRoom(db.Model):
    __tablename__ = 'tutorroom'
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    tutor = db.relationship("Tutor", backref = "tutor_room")
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"))
    room = db.relationship("Room", backref = "room1")
    
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
        return '<%r is assigned room %r>' % (self.tutor_id,self.room_id)
        

class StudentPreference(db.Model):
    __tablename__ = 'studentpreference'
    student_id = db.Column(db.String, db.ForeignKey('student.student_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    student = db.relationship("Student", backref = "student_pref")
    
    stucourse_id_1  = db.Column(db.String, db. ForeignKey('course.course_id', ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    course = db.relationship("Course", foreign_keys=[stucourse_id_1], backref = "stu_course1")
    
    stucourse_id_2  = db.Column(db.String, db. ForeignKey('course.course_id', ondelete="CASCADE", onupdate="CASCADE"))
    course1 = db.relationship("Course", foreign_keys=[stucourse_id_2], backref = "stu_course2")
    
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
    student_id = db.Column(db.String, db.ForeignKey('student.student_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    student = db.relationship("Student", backref = "student_ava")
    
    day_id = db.Column(db.String, db.ForeignKey('day.day_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable=False)
    day = db.relationship("Day", backref = "stu_day")
    
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
            return unicode(self.student_id,self.day_id,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.student_id,self.day_id,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Student %r is available on %r between the hours of %r and %r. >' % (self.student_id,self.day_id, self.start_time, self.end_time)

class TutorPreference(db.Model):
    __tablename__ = 'tutorpreference'
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"),primary_key=True, nullable = False)
    tutor = db.relationship("Tutor", backref = "tutor_pref")
    
    preference_1 = db.Column(db.String, db.ForeignKey('course.course_id',ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    course = db.relationship("Course", foreign_keys=[preference_1], backref = "tut_course1")
    
    preference_2 = db.Column(db.String, db.ForeignKey('course.course_id', ondelete="CASCADE", onupdate="CASCADE"))
    course1 = db.relationship("Course", foreign_keys=[preference_2], backref = "tut_course2")
    
    
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
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    tutor = db.relationship("Tutor", backref = "tutor_ava")
    
    day_id = db.Column(db.String, db.ForeignKey('day.day_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True, nullable = False)
    day = db.relationship("Day", backref = "day_tut")
    
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
            return unicode(self.tutor_id,self.day_id,self.start_time, self.end_time)  # python 2 support
        except NameError:
            return str(self.tutor_id,self.day_id,self.start_time, self.end_time)  # python 3 support

    def __repr__(self):
        return '<Tutor %r is available on %r between the hours of %r and %r. >' % (self.tutor_id,self.day_id, self.start_time, self.end_time)


class CourseCount (db.Model):
    __tablename__= 'coursecount'
    course_id = db.Column(db.String, db.ForeignKey('course.course_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    course = db.relationship("Course", backref = "course_count")
    
    count_tutors = db.Column(db.Integer, nullable = False)

    
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
        return '<Number of tutors in course are %r respectively. >' % (self.count_tutors)

class TutorCount (db.Model):
    __tablename__= 'tutorcount'
    
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    tutor = db.relationship("Tutor", backref = "tutor_count")
    
    count_students = db.Column(db.Integer)
    
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
        return '<Number of students for tutor %r is %r. >' % (self.tutor_id, self.count_students)

class CourseTutorMatch(db.Model):
    __tablename__ = 'coursematch'
    course_id = db.Column(db.String, db.ForeignKey('course.course_id', ondelete="CASCADE", onupdate="CASCADE"),primary_key = True)
    course = db.relationship("Course", backref = "course")
    
    tutor_id_1 = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"), nullable = False)
    tutor = db.relationship("Tutor", foreign_keys = [tutor_id_1], backref = "tutor1")
    
    tutor_id_2 = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"))
    tutor1 = db.relationship("Tutor", foreign_keys=[tutor_id_2], backref = "tutor2")
    
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
    tutor_id = db.Column(db.String, db.ForeignKey('tutor.tutor_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    tutor = db.relationship("Tutor", backref = "tutor_stu")
    
    student_id = db.Column(db.String, db.ForeignKey('student.student_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    student = db.relationship("Student", backref = "student")
    
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

class MondayRoomAvailability(db.Model):
    __tablename__='mondayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "mon_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)

class TuesdayRoomAvailability(db.Model):
    __tablename__='tuesdayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "tues_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)

class WednesdayRoomAvailability(db.Model):
    __tablename__='wednesdayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "wed_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)

class ThursdayRoomAvailability(db.Model):
    __tablename__='thursdayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "thur_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)

class FridayRoomAvailability(db.Model):
    __tablename__='fridayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "fri_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)

class SaturdayRoomAvailability(db.Model):
    __tablename__='saturdayroom'
    
    room_id = db.Column(db.String, db.ForeignKey('room.room_id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    room = db.relationship("Room", backref = "sat_room")
    time = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    
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
        return '<Room %r has the status %r >' % (self.room_id,self.status)


    
    
