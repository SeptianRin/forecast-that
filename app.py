import datetime
import time
import os
import bottle
import dataset
import simplejson as json
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app
import joblib
import keras
import numpy as np
import random


app = bottle.Bottle()
bottle.TEMPLATE_PATH.insert(0, "./")
app.config["db"] = dataset.connect("sqlite:///data.db?check_same_thread=False")
#app.config["db"] = dataset.connect("mysql+pymysql://septianrin:@septianrin.mysql.pythonanywhere-services.com/septianrin$hidroponia")
#app.config["db"] = dataset.connect("mysql+mysqldb://septianrin:hidroponia@septianrin.mysql.pythonanywhere-services.com/septianrin$hidroponia")
app.config["api_key"] = "JtF2aUE5SGHfVJBCG5SH"


@app.route('/', method=["GET", "POST"])
def index():
    if bottle.request.method == 'POST':
        user = str(bottle.request.body.read().decode("utf-8"))
        user = user.split("=")
        return bottle.redirect('/predict/'+user[1])
    else:
        return bottle.template("frontend.html")


@app.route('/predict/<count>', method=["GET"])
def predict_count(count):
    predict_this = []
    stop = int(count)
    for i in range(stop):
        predict_this.append([])
        if i == 0:
            for j in range(0, 20):
                predict_this[i].append(random.random())
        else:
            temp = predict_this[i-1][1:]
            temp.append(random.random())
            predict_this[i].extend(temp)

    predict_this = np.array(predict_this).reshape(len(predict_this), 20, 1)
    model = joblib.load("./model/ari_lstm_model.joblib")
    history = model.predict(predict_this)
    bottle.response.content_type = "application/json"
    return json.dumps(history.tolist())


# uncomment if deploy on
if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    bottle.run(app, host='localhost', port=3000, debug=True)
# uncomment if deploy on pythonanywhere
#application = default_app()
