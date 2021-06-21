import uuid

class Student:
    def __init__(self, id, name, branch, semester, batch_id, roll, image_url):
        self.id = self.id
        self.name = name
        self.branch = branch
        self.semester = semester
        self.batch_id = batch_id,
        self.roll = roll,
        self.image_url = image_url

studets = [
    Student(
        uuid.uuid1().hex,
        'Suman',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171033',
        '/home/suman/CollegeProject/FaceAttendanceSystem/Assets/images/suman.jpeg'
    ),
    Student(
        uuid.uuid1().hex,
        'Vikash',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171053',
        '/home/suman/CollegeProject/FaceAttendanceSystem/Assets/images/vikash.jpeg'
    ),
    Student(
        uuid.uuid1().hex,
        'Kishan',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171026',
        '/home/suman/CollegeProject/FaceAttendanceSystem/Assets/images/kishan.jpeg'
    )
]