from typing import List, Union
import motor.motor_asyncio
import os
from fastapi.encoders import jsonable_encoder
from models.Schemas import *
from models.Datatypes import *
from tools.useful import *

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client["twatter"]


async def search_twaats(search: str, token: Union[str, None] = "") -> Schema:
    is_login = await check_if_loggin(token)
    if is_login is False:
        return Schema([])
    result = (
        await db["twaats"]
        .find({"message": {"$regex": search, "$options": "gmi"}})
        .to_list(length=100)
    )
    print(result)
    twaats: List[Twaat] = []
    for document in result:
        twaats.append(Twaat(dict=document))
    return Schema(twaats=twaats)


def echo(self, echo: Union[str, None] = "") -> str:
    return echo
