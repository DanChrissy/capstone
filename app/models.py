class TutorMatch(db.Model):
    tutor_Id = db.Column(db.String,primary_key=True)
    course_Id = db.Column(db.String)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.tutor_Id)  # python 2 support
        except NameError:
            return str(self.tutor_Id)  # python 3 support

    def __repr__(self):
        return '<Tutor/Course Matching %r>' % (self.tutor_Id,self.course_Id)