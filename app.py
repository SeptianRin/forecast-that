
import datetime
import time
import os
import bottle
import dataset
import simplejson as json
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app

app = bottle.Bottle()
bottle.TEMPLATE_PATH.insert(0, "./")
app.config["db"] = dataset.connect("sqlite:///data.db?check_same_thread=False")
#app.config["db"] = dataset.connect("mysql+pymysql://septianrin:@septianrin.mysql.pythonanywhere-services.com/septianrin$hidroponia")
#app.config["db"] = dataset.connect("mysql+mysqldb://septianrin:hidroponia@septianrin.mysql.pythonanywhere-services.com/septianrin$hidroponia")
app.config["api_key"] = "JtF2aUE5SGHfVJBCG5SH"


@app.route('/', method=["GET"])
def index():
    logo = "bitmap.png"
    ph = "ph.png"
    thermo = "thermo.png"
    pupuk = "pupuk.png"
    return bottle.template("frontend.html")


# uncomment if deploy on
if os.environ.get('APP_LOCATION') == 'heroku':
    bottle.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    bottle.run(app, host='localhost', port=3000, debug=True)
# uncomment if deploy on pythonanywhere
#application = default_app()
