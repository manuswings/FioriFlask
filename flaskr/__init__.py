from flask import Flask
app = Flask(__name__,template_folder='static')
import flaskr.routes
