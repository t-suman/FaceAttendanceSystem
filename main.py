from Assets.DB.Teachers.teachers import getTeacherById
import os
from datetime import datetime, timedelta
import logging
from utils.util import getCameraAccess, getStudents, faceEncodings
import numpy as np
import cv2
import face_recognition
from utils.recordAttendance import give_attendance
from utils.constants import IMAGE_PATH



branch = 'CSE'
batch_id = '2017-2021'
camera_access, teacher_id = getCameraAccess(branch, batch_id)
if not (camera_access and teacher_id):
    print('camera access denied')
    exit()
images = []
personNames = []

students = getStudents(branch, batch_id)
teacher = getTeacherById(teacher_id)
if not teacher:
    exit()

for student in students:
    current_img = cv2.imread(f'{IMAGE_PATH}/{student.image_url}')
    current_img = cv2.cvtColor(current_img, cv2.COLOR_BGR2RGB)
    images.append(current_img)
current_img = cv2.imread(f'{IMAGE_PATH}/{teacher.image_url}')
current_img = cv2.cvtColor(current_img, cv2.COLOR_BGR2RGB)
images.append(current_img)
encodedList = faceEncodings(images)
print('All Encodings Complete!!!')

cap = cv2.VideoCapture(0)
teacher_caught = False
while camera_access:
    ret, frame = cap.read()
    cameraClick = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    cameraClick = cv2.cvtColor(cameraClick, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(cameraClick)
    encodesCurrentFrame = face_recognition.face_encodings(cameraClick, facesCurrentFrame)
    persons_in_frame = []

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodedList, encodeFace)
        faceDis = face_recognition.face_distance(encodedList, encodeFace)
        matchIndex = np.argmin(faceDis)
        person = None
        if matches[matchIndex]:
            if matchIndex < len(students):
                person = students[matchIndex]
            else:
                teacher_caught = True
                person = teacher
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, person.name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            persons_in_frame.append(person)

    if teacher_caught:
        give_attendance(persons_in_frame)
    
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(10) == 13:
        break


cap.release()
cv2.destroyAllWindows()