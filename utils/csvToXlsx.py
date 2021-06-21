import pandas as pd
import os

def toXlsx(file):
    path = './CollegeAttendance/CSE/Sem8'
    if not os.path.exists(path):
        os.makedirs(path)
    df = pd.read_csv(file)
    df.to_excel(f'{path}/attendance.xlsx', 'attendance', index=False)

