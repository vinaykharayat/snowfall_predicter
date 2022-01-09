from flask import Flask, render_template, jsonify
import pandas as pd
import pickle
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    #  json_ = request.json
    #  query_df = pd.DataFrame(json_)
    #  query = pd.get_dummies(query_df)
    return jsonify({'prediction': 'success', 'rootPath': str(os.getcwd())})
    
    # loaded_model = pickle.load(open(picklePath, 'rb'))

if __name__ == "__main__":
    app.run(port=8080)

