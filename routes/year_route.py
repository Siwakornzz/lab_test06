from fastapi import APIRouter
import datetime
year_api_router = APIRouter()
today = datetime.datetime.now()

@year_api_router.get("/service/getage")
async def getage(year: int):
    if year < 0:
        return {"msg": "Year can't be less than zero"}
    elif year > (today.year+543) :
        return {"msg": "Year can't be over than " + str(today.year + 543)}
    else:
        age = (today.year+543) - year
        return {"age": age}