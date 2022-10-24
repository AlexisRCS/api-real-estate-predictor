import json
from fastapi import HTTPException



if __name__ == '__main__' :

    with open("../model/belgium_localisation_score.json","r") as my_file :

        belgium_localisation_score = json.load(my_file)

    with open("../model/features_mean_std_cache.json","r") as my_file :

        features_mean_std_cache = json.load(my_file)

else :

    with open("./model/belgium_localisation_score.json","r") as my_file :

        belgium_localisation_score = json.load(my_file)

    with open("./model/features_mean_std_cache.json","r") as my_file :

        features_mean_std_cache = json.load(my_file)


def preprocess(property_data) :

    property_data_preprocessed = {}


    if property_data["area"] > 24 and property_data["area"] < 1001 :
        property_data_preprocessed["area"] = property_data["area"]
    else : 
        raise HTTPException(status_code = 422 , detail = "the area criteria must be between 25 m² and 1000 m²")


    if property_data["property_type"] == "APARTMENT" :
            property_data_preprocessed["property_type"] = 1
    else :
            property_data_preprocessed["property_type"] = 0


    if property_data["rooms_number"] > 0 and property_data["rooms_number"] < 11 :
        property_data_preprocessed["rooms_number"] = property_data["rooms_number"]
    else : 
        raise HTTPException(status_code = 422 , detail = "the rooms number criteria must be between 1 and 10 ")
    

    if property_data["zip_code"] > 999 & property_data["zip_code"] < 10000 :
        for key in belgium_localisation_score[str(property_data["zip_code"])].keys() :
            if belgium_localisation_score[str(property_data["zip_code"])][key] != 0.0 :
                localisation_score = belgium_localisation_score[str(property_data["zip_code"])][key]
                break
        property_data_preprocessed["localisation_score"] = localisation_score
    else :
        raise HTTPException(status_code = 422 , detail = "the zip code criteria must be a real Belgium zip code")
    

    property_data_preprocessed["land_area"] = property_data["land_area"]


    property_data_preprocessed["garden"] = int(property_data["garden"])
    if property_data["garden"] == True :
            property_data_preprocessed["garden_area"] = property_data["garden_area"]
    else :
            property_data_preprocessed["garden_area"] = 0


    property_data_preprocessed["equipped_kitchen"] = int(property_data["equipped_kitchen"])


    property_data_preprocessed["swimming_pool"] = int(property_data["swimming_pool"])


    property_data_preprocessed["furnished"] = int(property_data["furnished"])


    property_data_preprocessed["open_fire"] = int(property_data["open_fire"])


    property_data_preprocessed["terrace"] = int(property_data["terrace"])
    if property_data["terrace_area"] == True :
        property_data_preprocessed["terrace_area"] = property_data["terrace_area"]
    else :
        property_data_preprocessed["terrace_area"] = 0


    property_data_preprocessed["facades_number"] = property_data["facades_number"]


    if property_data["building_state"] in ["NEW","GOOD","JUST RENOVATED"] :
        property_data_preprocessed["building_state"] = 1
    else :
        property_data_preprocessed["building_state"] = 0

    
    for key in features_mean_std_cache.keys() :

        property_data_preprocessed[key] = (property_data_preprocessed[key]-features_mean_std_cache[key]["mean"])/features_mean_std_cache[key]["std"]


    return property_data_preprocessed