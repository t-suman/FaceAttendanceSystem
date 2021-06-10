import pandas as pd

def toXlsx(file):
    df = pd.read_csv(file)
    df.to_excel('~/attendance.xlsx', 'attendance', index=False)

