from flask import Flask
from rpn import api

app = Flask(__name__)
api.init_app(app)

app.run(debug=True)