from flask import Flask, render_template, jsonify, request
import pandas as pd
import pickle
import os
import sklearn
from sklearn import preprocessing
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])

def predict():
    json = request.json
    weather_df = pd.DataFrame.from_dict(json, orient='index').T
    # print(json)
    weather_df["maxtempC"] = weather_df["maxtempC"] - 273.15
    weather_df["FeelsLikeC"] = weather_df["FeelsLikeC"] - 273.15
    weather_df["visibility"] = weather_df["visibility"]/1000
    weather_df["windspeedKmph"] = weather_df["windspeedKmph"] * 3.6

    #data sacaling (normalizing)
    def normalize_data(df):
        min_max_scaler = preprocessing.MinMaxScaler()
        df["winddirDegree"] = min_max_scaler.fit_transform(df["winddirDegree"].values.reshape(-1,1))
        return df
    normalize_data(weather_df)
    with open('./Pickle/xgboost.pkl','rb') as f:
        xgb=pickle.load(f)
    y_pred = xgb.predict(weather_df)
    return jsonify({'prediction': y_pred.tolist()[0]})


if __name__ == "__main__":
    app.run(port=8080)

