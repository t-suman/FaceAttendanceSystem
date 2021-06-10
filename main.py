import cv2
import numpy as np
import face_recognition
import os
from utils.recordAttendance import give_attendance
from utils.constants import IMAGE_PATH

images = []
personNames = []
myList = os.listdir(IMAGE_PATH)

print(myList)

for cu_img in myList:
    current_img = cv2.imread(f'{IMAGE_PATH}/{cu_img}')
    current_img = cv2.cvtColor(current_img, cv2.COLOR_BGR2RGB)
    images.append(current_img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)


def faceEncodings(images):
    encodeList = []
    for img in images:
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

 

encodedList = faceEncodings(images)
print('All Encodings Complete!!!')

cap = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()
    cameraFace = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    cameraFace = cv2.cvtColor(cameraFace, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(cameraFace)
    encodesCurrentFrame = face_recognition.face_encodings(cameraFace, facesCurrentFrame)
    
    if(len(encodesCurrentFrame) > 1 and i == 0):
        print(encodesCurrentFrame)
        i+=1

    for encodeFace, faceLoc in zip(encodesCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodedList, encodeFace)
        faceDis = face_recognition.face_distance(encodedList, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            give_attendance(name)
    
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(10) == 13:
        break




cap.release()
cv2.destroyAllWindows()