import json



if __name__ == '__main__' :

    with open("../model/model_function.json","r") as my_file :

        model_function = json.load(my_file)

else :

    with open("./model/model_function.json","r") as my_file :

        model_function = json.load(my_file)
        

def predict(preprocessed_property_data) :

    predict_price = model_function["interception"]

    for key in model_function["coefficient"].keys() :

        predict_price = predict_price + model_function["coefficient"][key]*preprocessed_property_data[key]

    return int(round(predict_price,-3))