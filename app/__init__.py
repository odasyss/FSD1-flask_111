#!/usr/bin/env python3
#  -*- coding: utf8 -*-
# SIMPLE FLASK APP 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def about_me():
    me= {
        "first_name": "Odasys",
        "last_name" : "Soberanes",
        "hobbies" : "Basketball",
        "test": True
    }
    return me

    