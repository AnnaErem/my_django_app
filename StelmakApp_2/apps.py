from django.apps import AppConfig
from flask import Flask, render_template
import sqlite3 

StelmakApp_2 = Flask(__name__)

@StelmakApp_2.route('/')
def index():
    return render_template("index.html")


class Stelmakapp2Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "StelmakApp_2"
