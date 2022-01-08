from flask import Flask
import pandas as pd
import pickle
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    #  json_ = request.json
    #  query_df = pd.DataFrame(json_)
    #  query = pd.get_dummies(query_df)
    
     loaded_model = pickle.load(open('Pickle/xgboost.pkl', 'rb'))
     return jsonify({'prediction': 'success'})

if __name__ == "__main__":
    app.run(port=8080)

