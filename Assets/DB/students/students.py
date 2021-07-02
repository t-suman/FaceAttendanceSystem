class Student:
    def __init__(self, id, name, branch, semester, batch_id, roll, image_url):
        self.id = id
        self.name = name
        self.branch = branch
        self.semester = semester
        self.batch_id = batch_id
        self.roll = roll
        self.image_url = image_url
        self.role = 'student'

students = [
    Student(
        'suman20171033',
        'Suman Thakur',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171033',
        'suman.jpeg'
    ),
    Student(
        'vikash20171033',
        'Vikash Pandey',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171053',
        'vikash.jpeg'
    ),
    Student(
        'kishan20171033',
        'Kishan Thakur',
        'CSE',
        'Sem8',
        '2017-2021',
        '20171026',
        'kishan.jpeg'
    )
]

