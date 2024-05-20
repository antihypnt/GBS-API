from pycomcigan import TimeTable, get_school_code
from fastapi import FastAPI
import schoolmeal

app = FastAPI()
get_school_code("경기")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/timetable/{week_num}/{grade_num}/{class_num}/{day_num}")
async def showTimeTable(week_num: int, grade_num: int, class_num: int, day_num: int):
    timetable = TimeTable("경기북과학고", week_num)

    if day_num == 1: day = timetable.MONDAY
    elif day_num == 2: day = timetable.TUESDAY
    elif day_num == 3: day = timetable.WEDNESDAY
    elif day_num == 4: day = timetable.THURSDAY
    elif day_num == 5: day = timetable.FRIDAY
    else: return {"timetable" : None}

    return {"timetable" : timetable.timetable[grade_num][class_num][day]}


@app.get("/schoolmeal")
async def meal():
    return {"message": "Hello World"}