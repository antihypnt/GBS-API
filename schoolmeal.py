import requests as rq

meal = "https://open.neis.go.kr/hub/mealServiceDietInfo?KEY=67c2bd83a7e14117a89cd682f1bb8673&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530851&MLSV_YMD="

def getMeal(ymd):

    global meal
    response = rq.get(meal + ymd)
    mealContents = response.text

    morning = mealContents.split("<DDISH_NM>")[1]
    morning = morning.split("</DDISH_NM>")[0].replace("<![CDATA[", "").replace("]]>", "").split("<br/>")
    morning = "\n".join(morning)

    lunch = mealContents.split("<DDISH_NM>")[2]
    lunch = lunch.split("</DDISH_NM>")[0].replace("<![CDATA[", "").replace("]]>", "").split("<br/>")
    lunch = "\n".join(lunch)

    dinner = mealContents.split("<DDISH_NM>")[3]
    dinner = dinner.split("</DDISH_NM>")[0].replace("<![CDATA[", "").replace("]]>", "").split("<br/>")
    dinner = "\n".join(dinner)

    return [morning, lunch, dinner]
