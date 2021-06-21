
from typing import List
import uuid

class Teacher:
    def __init__(self, id: str, name: str, image_url: str):
        self.id = id
        self.name = name
        self.image_url = image_url

teachers = [
    Teacher(
        '1',
        'Soumik Ghosh Sir',
        '/home/suman/CollegeProject/FaceAttendanceSystem/Assets/images/SoumikGhosh.jpeg'
    ),
    Teacher(
        '2',
        '/home/suman/CollegeProject/FaceAttendanceSystem/Assets/images/SKGsir.png'
    )
]