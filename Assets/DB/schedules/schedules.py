from datetime import time, datetime
from Assets.DB.Teachers.teachers import Teacher

class Schedule:
    def __init__(self, start_time: time, end_time: time, branch: str, batch_id: str, teacher_id):
        self.start_time = start_time
        self.end_time = end_time
        self.branch = branch
        self.batch_id = batch_id
        self.teacher_id = teacher_id

    def getStartTime(self):
        return self.start_time

    def getEndTime(self):
        return self.end_time

    def getBranch(self):
        return self.branch

    def getBatchId(self):
        return self.batch_id

    def getTeacherId(self):
        return self.teacher_id

schedules = [
    Schedule(
        datetime.strptime('10:00 AM', "%I:%M %p").time(),
        datetime.strptime('11:40 AM', "%I:%M %p").time(),
        'IT',
        '2017-2021',
        'sg123'
    ),
    Schedule(
        datetime.strptime('08:50 PM', "%I:%M %p").time(),
        datetime.strptime('09:30 PM', "%I:%M %p").time(),
        'CSE',
        '2017-2021',
        'sg123'
    ),
]

def getSchedule(branch, batch_id):
    return list(filter(lambda schedule: schedule.getBranch() == branch and schedule.getBatchId() == batch_id, schedules))
