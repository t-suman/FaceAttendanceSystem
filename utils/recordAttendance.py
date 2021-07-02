from datetime import datetime

def test():
    with open('Assets/Attendance.csv', 'r+') as f:
        f.readline()
        f.truncate(f.tell())

def give_attendance(persons):
    students = []
    teacher = None
    for person in persons:
        if person.role == 'student':
            students.append(person)
        elif person.role == 'teacher':
            teacher = person

    with open('Assets/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        idList = []
        for line in myDataList:
            entry = line.split(',')
            idList.append(entry[0])
        if teacher and teacher.id not in idList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{teacher.id},{teacher.name},{teacher.role},{tStr},{dStr}')
        for student in students:
            if student and student.id not in idList:
                time_now = datetime.now()
                tStr = time_now.strftime('%H:%M:%S')
                dStr = time_now.strftime('%d/%m/%Y')
                f.writelines(f'\n{student.id},{student.name},{student.role},{tStr},{dStr}')
