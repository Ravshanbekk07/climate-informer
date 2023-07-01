from flask import Flask, request

app = Flask(__name__)

from climate import routes
