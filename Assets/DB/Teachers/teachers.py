
from typing import List
import uuid

class Teacher:
    def __init__(self, id: str, name: str, image_url: str):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.role = 'teacher'

teachers = [
    Teacher(
        'sg123',
        'Soumik Ghosh Sir',
        'sg_sir.jpeg'
    ),
    Teacher(
        'skg123',
        'SKG sir',
        'skg_sir.png'
    )
]

def getTeacherById(teacher_id):
    for teacher in teachers:
        if teacher.id == teacher_id:
            return teacher
    return None