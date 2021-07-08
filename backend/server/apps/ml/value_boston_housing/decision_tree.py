import joblib
import pandas as pd
import numpy as np

class DecisionTreeRegressor:
    def __init__(self):
        path_to_artifacts = "../../research/"
        self.values_fill_missing =  joblib.load(path_to_artifacts + "train_mode_b.joblib")
        #self.encoders = joblib.load(path_to_artifacts + "encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "decision_tree.joblib")

    # def preprocessing(self, input_data):
    #     # JSON to pandas DataFrame
    #     input_data = pd.DataFrame(input_data, index=[0])
    #     # fill missing values
    #     input_data.fillna(self.values_fill_missing)
    #     # # convert categoricals
    #     # for column in [
    #     #     "workclass",
    #     #     "education",
    #     #     "marital-status",
    #     #     "occupation",
    #     #     "relationship",
    #     #     "race",
    #     #     "sex",
    #     #     "native-country",
    #     # ]:
    #     #     categorical_convert = self.encoders[column]
    #     #     input_data[column] = categorical_convert.transform(input_data[column])

    #     return input_data

    def predict(self, input_data):
        input_data = pd.DataFrame.from_dict([input_data])
        input_data = np.array(input_data.values.tolist()[0])
        input_data = input_data.reshape(1, -1)
        return self.model.predict(input_data)

    # def postprocessing(self, input_data):
    #     # label = "<=50K"
    #     # if input_data[1] > 0.5:
    #     #     label = ">50K"
    #     # return {"probability": input_data[1], "label": label, "status": "OK"}
    #     return {"medv": input_data[1],"status": "OK"}

    def compute_prediction(self, input_data):
        try:
            #input_data = self.preprocessing(input_data)
            #print("input data 1: ", input_data)
            prediction = self.predict(input_data)[0]  # only one sample

            #print("prediction predict: ", prediction)
            #prediction = self.postprocessing(prediction)
            #print("prediction post process: ", prediction)
        except Exception as e:
            return {"status": "cueck"+str(e), "message": str(e)}

        return {"medv": prediction,"status": "OK"}