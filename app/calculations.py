from app import db
from app.models import Student,Tutor, TutorRoom, StudentAvailability, TutorAvailability, StudentPreference, TutorPreference, Course,TutorCount, Day,CourseTutorMatch, CourseCount, TutorStudentMatch
from app.models import MondayRoomAvailability, TuesdayRoomAvailability, WednesdayRoomAvailability, ThursdayRoomAvailability, FridayRoomAvailability, SaturdayRoomAvailability
import operator

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
    
    def tutStu(stu_id):
        stu_pref1 = db.session.query(StudentPreference.stucourse_id_1)
        stu_pref2 = db.session.query(StudentPreference.stucourse_id_2)
        preferences = [stu_pref1,stu_pref2]
        stu_available = db.session.query(StudentAvailability).filter_by(student_id = stu_id)
        return(preferences, stu_available)
        
    
    def tuts(stu_id):
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
                            
    for s in students:
        tutStu(s)
                
    for p in preferences:
        cid = db.session.query(Course.course_id).filter_by(course_id = p)
        tutors = db.session.query(CourseTutorMatch.tutor_id_1,CourseTutorMatch.tutor_id_2).filter_by(course_id = cid)
        
        tuts_result = tuts() 
        if tuts_result == []:
            break
        else:
            tut_stu_match = match(tuts_result)
            return tut_stu_match

def tutcourse():
    tutors = db.session.query(Tutor.tutor_id).all()
    course = db.session.query(Course.course_id).all()
    course_name = db.session.query(Course.course_name).all()
    searches = []
    course_list_id = []
    course_list_name = []
    course_list_count=[]
    course_list_match = []
    course_list = []
    
    def courses():
    
        def courses_id():
            for c in course:
                course_list_id.append(c.course_id)
            return course_list_id
        
        def courses_name():
            for c in course_name:
                course_list_name.append(c.course_name)
            return course_list_name
        
        i = courses_id()
        n = courses_name()
        
        def courses_count(list_ids):
            for l in list_ids:
                count = db.session.query(CourseCount.count_tutors).filter_by(course_id = l).first()
                course_list_count.append(count.count_tutors)
            return course_list_count
        
        c = courses_count(i)
        
        for ln in range(len(i)):
            course_list.append([str(i[ln]),str(n[ln]), c[ln]])
        
        f = course_list
        return f
    
    def get_prefs(tut_id):
        pref_1=[]
        pref_2=[]
        prefs1 = db.session.query(TutorPreference.preference_1).filter_by(tutor_id = tut_id).all()
        prefs2 =db.session.query(TutorPreference.preference_2).filter_by(tutor_id = tut_id).all()
        for pref1 in prefs1:
            pref_1.append(pref1.preference_1)
        for pref2 in prefs2:
            pref_2.append(pref2.preference_2)
        '''
        area = db.session.query(Tutor.area_study).filter_by(tutor_id = tut_id).all()
        for a in area:
            area_name = a.area_study
        area_id = db.session.query(Course.course_id).filter(Course.course_name.ilike("%area_name%")).first()
        areaId = area_id.course_id'''
        search = [str(pref_1[0]),str(pref_2[0])]
        return search
    
    def match_tut(option1,option2,id_number,c):
        for cid in c:
            if (option1 == cid[0] and cid[2] != 2):
                pick = option1
                update_count = db.session.query(CourseCount.count_tutors).filter_by(course_id = pick).first()
                up_count = update_count.count_tutors + 1
                '''up_count = db.session.merge(update_count)
                db.session.commit()
                
                m_id = db.session.query(CourseTutorMatch.course_id).filter_by(course_id = cid[0]).first()
                if m_id != None:
                    match_id = m_id.course_id
                    update_match = db.session.query(CourseTutorMatch).filter_by(course_id = cid[0]).first()
                    update_match.tutor_id_2 = id_number
                    db.session.commit()
                    return
                else:
                    match = CourseTutorMatch(course_id=pick, tutor_id_1 = id_number, tutor_id_2 = "")
                    db.session.add(match)
                    db.session.commit()
                    return'''
                    
            elif ((option1 != cid[0]) and (option2 == cid[0]) and (cid[2] != 2)):
                pick = option2
                update_count = db.session.query(CourseCount.count_tutors).filter_by(course_id = pick).first()
                up_count = update_count.count_tutors + 1
                '''up_count = db.session.merge(update_count)
                db.session.commit()
                
                m_id = db.session.query(CourseTutorMatch.course_id).filter_by(course_id = cid[0]).first()
                if m_id != None:
                    match_id = m_id.course_id
                    update_match = db.session.query(CourseTutorMatch).filter_by(course_id = cid[0]).first()
                    update_match.tutor_id_2 = id_number
                    db.session.commit()
                    return
                else:
                    match = CourseTutorMatch(course_id=pick, tutor_id_1 = id_number, tutor_id_2 = "")
                    db.session.add(match)
                    db.session.commit()
                    return'''
            else:
                print("Nothing")
        return  [pick, up_count]
                
        '''elif ((option1 != cid[0]) and (option2 != cid) and (option3 == cid) and (count != 2)):
                pick = option3
                update_count = db.session.query(CourseCount).filter_by(course_id = pick)
                update_count.count_tutors += 1
                db.session.commit()
                
                if (match1 == ""):
                    match = CourseTutorMatch(course_id=pick, tutor_id_1 = id_number, tutor_id_2 = "")
                    db.session.add(match)
                    db.session.commit()
                    return
                else: 
                        update_match = db.session.query(CourseTutorMatch).filter_by(course_id = pick).first()
                        update_match.tutor_id_2 = id_number
                        db.session.commit()
                        return'''
                
    picks = []
    course_listing = courses()
    for t in tutors:
        searches.append(t.tutor_id)
    for s in searches:
        listing = get_prefs(s)
        pref1 = listing[0]
        pref2 = listing[1]
        #pref3 = listing[2]

        m = match_tut(pref1,pref2,t,course_listing)
        picks.append([s,m])
    return picks
    

    
        
    
    

    
    
            
                
                   
               
               

                        
        

