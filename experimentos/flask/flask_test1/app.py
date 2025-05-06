from flask import Flask
from flask import render_template
from routes import api


app = Flask(__name__)

app.register_blueprint(api.bp)

@app.route("/")
def index():
    return render_template('index.html')

app.run(debug=True, port=8033)
