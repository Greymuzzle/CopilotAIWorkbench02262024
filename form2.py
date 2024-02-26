# Using flask for a web framework, create the html code that accepts 4 inputs, first and last name, subtotal and tax as percentage, without using an html file. Add a button to the form that when submitted, returns subtotal, tax percentage and total on a new page. Calculate the total using a python function, called when the user click on the submit button. Using the re module in python, validate that the first and last name inputs do not contain numbers or special characters.

from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')

def index():
    return '''<form method="POST" action="/submit">
    <label for="first_name">First Name:</label><br>
    <input type="text" id="first_name" name="first_name"><br>
    <label for="last_name">Last Name:</label><br>
    <input type="text" id="last_name" name="last_name"><br>
    <label for="subtotal">Subtotal:</label><br>
    <input type="text" id="subtotal" name="subtotal"><br>
    <label for="tax_rate">Tax Percent (ex: 18):</label><br>
    <input type="text" id="tax_rate" name="tax_rate"><br>
    <input type="submit" value="Submit">
    </form>'''

@app.route('/submit', methods=['POST'])

def submit():
    # if the return is asking the user to go back to the form, add a link to the form to go back
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    subtotal = float(request.form['subtotal'])
    # using re module, validate that the subtotal input is a number
    tax_rate = float(request.form['tax_rate'])
    total = calculate_total(subtotal, tax_rate)
    if re.search(r'[0-9]', first_name) or re.search(r'[0-9]', last_name):
      
        return 'First and Last Name cannot contain numbers or special characters. Please go back and try again.'    
    # add a link back to the form
    # ber sure to add a link in the return statement to go back to the form
    return f'First Name: {first_name}<br>Last Name: {last_name}<br>Subtotal: {subtotal}<br>Tax Rate: {tax_rate}<br>Total: {total}'

def calculate_total(subtotal, tax_rate):
    total = subtotal + (subtotal * tax_rate)
    return total

if __name__ == '__main__':
    app.run(debug=True)
