from flask import Flask, render_template, request, redirect

import requests

import pandas as pd

import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file


app = Flask(__name__)


@app.route('/')
def home():




    return render_template('home.html')



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
