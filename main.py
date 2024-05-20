from pycomcigan import TimeTable, get_school_code
from fastapi import FastAPI
import datetime as dt
from datetime import timedelta
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
    else: return {"timetable" : "유효한 요일을 입력하세요."}

    return {"timetable" : timetable.timetable[grade_num][class_num][day]}


@app.get("/schoolmeal/{mealmode}")
async def meal(mealmode: int):
    now = dt.datetime.now()

    if mealmode <= 4:
        now = now.strftime('%Y%m%d')
        mealList = schoolmeal.getMeal(now)
    else:
        tom = (now + dt.timedelta(days=1)).strftime('%Y%m%d')
        mealList = schoolmeal.getMeal(tom)

    if mealmode == 1 or mealmode == 5: return {"schoolmeal": mealList[0]}
    elif mealmode == 2 or mealmode == 6: return {"schoolmeal": mealList[1]}
    elif mealmode == 3 or mealmode == 7: return {"schoolmeal": mealList[2]}
    elif mealmode == 4 or mealmode == 8: return {"schoolmeal": mealList}
    else: return {"schoolmeal": "유효한 값이 아닙니다."}