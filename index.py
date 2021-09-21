from os import error
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mahmoud1'
app.config['MYSQL_DB'] = 'DocumnetControlSystem'

mysql = MySQL(app)


@app.route("/")
def hello_world():
    return render_template('base.html')


@app.route("/addcustomer", methods=['GET', 'POST'])
def addCustomer():
    if request.method == "POST":
        try:
            details = request.form
            name = details['name']
            id = int(details['c_id'])
            phone = details['phone']
            address = details['address']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Customer(Client_id, Name, Phone, Address) VALUES (%s, %s, %s, %s)",
                        (id, name, phone, address))
            mysql.connection.commit()
            cur.close()
            return render_template('success.html', stat='Added')
        except ValueError as ve:
            error = 'enter appropriate id number'
            return render_template('error.html', error=error)
    return render_template('add.html')


@app.route("/deletecustomer", methods=['GET', 'POST'])
def deleteCustomer():
    if request.method == "POST":
        try:
            details = request.form
            id = int(details['c_id'])
            print(id)
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM %s WHERE Client_id = %s" %
                        ('Customer', id))
            mysql.connection.commit()
            cur.close()
            return render_template('success.html', stat='deleted')
        except ValueError as ve:
            error = 'enter appropriate id number'
            return render_template('error.html', error=error)
    return render_template('delete.html')


@app.route("/updatecustomer", methods=['GET', 'POST'])
def updateCustomer():
    if request.method == "POST":
        try:
            details = request.form
            name = details['name']
            id = int(details['c_id'])
            phone = details['phone']
            address = details['address']

            cur = mysql.connection.cursor()
            cur.execute(
                "UPDATE Customer set Name=%s, Phone=%s, Address=%s where Client_id=%s", (name, phone, address, id))
            mysql.connection.commit()
            cur.close()
            return render_template('success.html', stat='Updated')
        except ValueError as ve:
            error = 'enter appropriate id number'
            return render_template('error.html', error=error)
    return render_template('add.html')


@app.route("/getcustomer", methods=['GET', 'POST'])
def getCustomer():
    if request.method == "POST":
        try:
            details = request.form
            id = int(details['c_id'])
            cur = mysql.connection.cursor()
            cur.execute(
                "SELECT * FROM Customer WHERE Client_id = %s", (id,))
            customer = cur.fetchall()
            cur.close()
            return render_template('customers.html', customer=customer)
        except ValueError as ve:
            error = 'enter appropriate id number'
            return render_template('error.html', error=error)
    return render_template('get.html')


@app.route("/getcustomer/getall", methods=['GET', 'POST'])
def getall():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Customer")
        customer = cur.fetchall()
        cur.close()
        return render_template('customers.html', customer=customer)
    return render_template('get.html')
