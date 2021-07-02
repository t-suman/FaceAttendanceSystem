from datetime import datetime, timedelta
import face_recognition
from Assets.DB.schedules.schedules import getSchedule
from Assets.DB.students.students import students

def faceEncodings(images):
    encodeList = []
    for img in images:
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def getCameraAccess(branch, batch_id):
    schedules = getSchedule(branch, batch_id)
    current_datetime = datetime.now()
    for schedule in schedules:
        if current_datetime.time() > schedule.getStartTime() and (current_datetime-timedelta(minutes=15)).time() < schedule.getStartTime():
            return True, schedule.getTeacherId()
    return False, None

def getStudents(branch, batch_id):
    global students
    students = list(filter(lambda student: student.branch==branch and student.batch_id==batch_id, students))
    return students