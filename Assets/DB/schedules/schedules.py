from Assets.DB.Teachers.teachers import Teacher

class Schedule:
    def __init__(self, start_time: str, end_time: str, branch: str, batch_id: str, teacher_id):
        self.start_time = start_time
        self.end_time = end_time
        self.branch = branch,
        self.batch_id = batch_id,
        self.teacher_id = teacher_id

schedules = [
    Schedule(
        '10:00 AM',
        '11:40 AM',
        'CSE',
        '2017-2021',
        '1'
    ),
    Schedule(
        '11:40 AM',
        '01:20 PM',
        'IT',
        '2017-2021',
        '1'
    ),
]

def getSchedule(branch, batch_id):
    return list(filter(lambda schedule: schedule.branch == branch and schedule.batch_id == batch_id, schedules))