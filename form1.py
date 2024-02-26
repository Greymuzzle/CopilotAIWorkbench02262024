# Using flask for a web framework, create an HTML form that accepts two inputs, subtotal and tax as percentage. Add a button to the form that when submitted, returns subtotal, tax percentage and total on a new page. For the python function, calculate the total by adding the subtotal and tax rate together. Calculate the total using a python function, called when the user clicks on the submit button. Using the re module in python, validate that the first and last name inputs do not contain numbers or special characters.

from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form1.html')

@app.route('/submit', methods=['POST'])

def submit():
    subtotal = float(request.form['subtotal'])
    tax_rate = float(request.form['tax_rate'])
    total = calculate_total(subtotal, tax_rate)
    return render_template('form1.html', subtotal=subtotal, tax_rate=tax_rate, total=total)

def calculate_total(subtotal, tax_rate):