from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="arsha" 
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def insert_data():
    # Extract data from the form
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    phoneNumber = request.form['phoneNumber']
    investmentAmount = request.form['investmentAmount']
    tenure = request.form['tenure']
    payRhythm = request.form['payRhythm']

    # Insert data into MySQL database
    sql = "INSERT INTO users (name, age, email, phoneNumber, investmentAmount, tenure, payRhythm) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name, age, email, phoneNumber, investmentAmount, tenure, payRhythm)

    cursor.execute(sql, values)
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
