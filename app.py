from typing import Optional, Literal
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from fastapi import FastAPI, Body
from pydantic import BaseModel



api = FastAPI()


class Property_data(BaseModel) :
    
    area : int 
    property_type : Literal["APARTMENT","HOUSE"] = "APARTMENT"
    rooms_number : int
    zip_code : int
    land_area : Optional[int] | None  = 0
    garden : Optional[bool] | None = False
    garden_area : Optional[int] | None = 0
    equipped_kitchen : Optional[bool] | None = False
    full_address : Optional[str] | None = None
    swimming_pool : Optional[bool] | None = False
    furnished : Optional[bool] | None = False
    open_fire : Optional[bool] | None = False
    terrace  : Optional[bool] | None = False
    terrace_area : Optional[int] | None = 0
    facades_number : Optional[int] | None = 0
    building_state : Literal["NEW","GOOD","TO RENOVATE","JUST RENOVATED","TO REBUILD",None] = "GOOD"


@api.get("/")
async def server_status() :
    return "Alive : Status Code = 200"


@api.get("/predict")
async def input_data_format() :

    data_expected_format = """{"area": int,"property_type": "APARTMENT" | "HOUSE","rooms_number": int,"zip_code": int,"land_area": int | None,"garden": bool | None, "garden_area": int | None,"equipped_kitchen": bool | None,"full_address": str | None,"swimming_pool": bool | None,"furnished": bool | None,"open_fire": bool | None,"terrace": bool | None,"terrace_area": int | None,"facades_number": int | None,"building_state": "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD" | None}"""
    
    return  str(data_expected_format)


@api.post("/predict", status_code = 200)
async def predict_price(data : Property_data = Body(embed = True)) :

    predict_price_result = {"prediction" : predict(preprocess(data.dict())), "status_code" : 200}

    return predict_price_result