from app import db
from app.models import Student,Tutor, TutorRoom, StudentAvailability, TutorAvailability, StudentPreference, TutorPreference, Course,TutorCount, Day,CourseTutorMatch, CourseCount, TutorStudentMatch
from app.models import MondayRoomAvailability, TuesdayRoomAvailability, WednesdayRoomAvailability, ThursdayRoomAvailability, FridayRoomAvailability, SaturdayRoomAvailability

courses = db.session.query(Course)
days = db.session.query(Day)
counts =db.session.query(TutorCount)
matches =db.session.query(CourseTutorMatch.tutor_id_1, CourseTutorMatch.tutor_id_2)
tutors_ava = db.session.query(TutorAvailability)
students_ava = db.session.query(StudentAvailability)
tutors = db.session.query(Tutor)

def Schedule():
   
    for m in matches:
        start_times = db.session.query(TutorAvailability.start_time).filter_by(tutor_id = m)
        
        result_times = available_times(m)
        results_query = result_times[0]
        results_day = result_times[1]
        
        slot_times (results_query, results_day,m)
        
        
        
        def available_times(tutor_m):
            tut_day = db.session.query(TutorAvailability.day_id).filter_by(tutor_id = tutor_m)
            
            if tut_day == 'Mon':
                query = db.session.query(MondayRoomAvailability).filter_by(status = "")
            elif tut_day == 'Tues':
                query = db.session.query(TuesdayRoomAvailability).filter_by(status = "")
            elif tut_day == 'Wed':
                query = db.session.query(WednesdayRoomAvailability).filter_by(status = "")
            elif tut_day == 'Thur':
                query = db.session.query(ThursdayRoomAvailability).filter_by(status = "")
            elif tut_day == 'Fri':
                query = db.session.query(FridayRoomAvailability).filter_by(status = "")
            else:
                query = db.session.query(SaturdayRoomAvailability).filter_by(status = "")
                    
            return (query,tut_day)
        
        def slot_times(query, day, tut_id):
            for q in query:
                for s in start_times:
                    start = int(s[:2])
                    if start == q.time:
                        match = TutorRoom(tutor_id = tut_id, room_id = q.room_id)
                        db.session.add(match)
                        db.session.commit()
                            
                        if day == 'Mon':
                            update_status = db.session.query(MondayRoomAvailability).filter_by(room_id = q.room_id)
                        elif day == 'Tues':
                            update_status = db.session.query(TuesdayRoomAvailability).filter_by(room_id = q.room_id)
                        elif day == 'Wed':
                            update_status = db.session.query(WednesdayRoomAvailability).filter_by(room_id = q.room_id)
                        elif day == 'Thur':
                            update_status = db.session.query(ThursdayRoomAvailability).filter_by(room_id = q.room_id)
                        elif day == 'Fri':
                            update_status = db.session.query(FridayRoomAvailability).filter_by(room_id = q.room_id)
                        else:
                            update_status = db.session.query(SaturdayRoomAvailability).filter_by(room_id = q.room_id)
                                    
                            
                        update_status.status = "Blocked"
                        db.session.commit()
                        return
                    
                    else: return("No rooms available.")
                    

def MatchStudentTutor():
    students = db.session.query(Student.student_id)
    for s in students:
        tutStu(s)
        
def tutStu(stu_id):
    stu_pref1 = db.session.query(StudentPreference.stucourse_id_1)
    stu_pref2 = db.session.query(StudentPreference.stucourse_id_2)
    preferences = [stu_pref1,stu_pref2]
    stu_available = db.session.query(StudentAvailability).filter_by(student_id = stu_id)
    
    def tuts():
            tutors_list = []
            for tut in tutors:
                exists = db.session.query(TutorStudentMatch).filter_by(tutor_id = tut, student_id = stu_id).scalar()
                if exists is not None:
                    break
                else:
                    tutors_list.append(tut)
                return tutors_list
    
    def match(listing):
        for r in listing:
            tut_available = db.session.query(TutorAvailability).filter_by(tutor_id = r)
            count = db.session.query(TutorCount.count_students).filter_by(tutor_id = r)
            if (count == 20):
                continue
            else:
                for a in tut_available:
                    for s in stu_available:
                        stu_start = int(s.start_timee[:2])
                        tut_start = int(a.start_time[:2])
                        tut_end = int(a.end_time[:2])
                        stu_end = int(s.end_time[:2])
                            
                        if (a.day_id == s.day_id) and ((tut_start == stu_start) or (stu_start > tut_start and stu_end < tut_end) or (stu_start >tut_start and stu_end == tut_end)):
                            update_count = db.session.query(TutorCount).filter_by(tutor_id = r)
                            update_count.count_students += 1
                            db.session.commit()
                        
                            match = TutorStudentMatch(tutor_id = r, student_id = stu_id)
                            db.session.add(match)
                            db.session.commit()
                                
                            return("Match for "+ stu_id + " is " + r + "." )
                        else:
                            return("No tutors found.")
                
    for p in preferences:
        cid = db.session.query(Course.course_id).filter_by(course_id = p)
        tutors = db.session.query(CourseTutorMatch.tutor_id_1,CourseTutorMatch.tutor_id_2).filter_by(course_id = cid)
        
        tuts_result = tuts() 
        if tuts_result == []:
            break
        else:
            tut_stu_match = match(tuts_result)
            return tut_stu_match
            
                    
                

                        
        

