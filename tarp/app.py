import ast
import serial
from flask import Flask, render_template
import psycopg2
from flask_session import Session
import json
conn = psycopg2.connect(
    dbname="tarp",
    user="postgres",
    password="ganesh99",
    host="localhost",
    port="5432"
)
def changeString(s):
    n = ""
    for i in s:
        if i == "'":
            n = n + '"'
        elif i == '"':
            n = n + "'"
        else:
            n = n + i
    return n
app = Flask(__name__)
globalVal = '{"Name":"Lorem","Allergies":"ipsum", "id": "4CF73749"}'
ser = serial.Serial('/dev/ttyACM0', 9600) 
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/patientData")
def patientData():
    cur = conn.cursor()
    uid = "fkjlksdalsdjla"
    cur.execute("SELECT * FROM patients;")
    userData = cur.fetchall()
    cur.close()
    return render_template("display.html", data = userData)


@app.route('/rfid')
def rfid():
    while True:
        try:
            rfid_code = ser.readline().decode('utf-8').strip()
            d = changeString(rfid_code)
            globalVal = d
            if rfid_code:  
                print(d)
                break   
            else:
                print(rfid_code)
        except:
            print("No Data")
    return render_template('display.html', data = d)
@app.route('/comp-data')
def data():
    cur = conn.cursor()
    l = globalVal.split(":")
    e = l[3]

    e = e.rstrip(e[-1])
    print(e)

   
    cur.execute("SELECT * FROM patients  WHERE cardid = '4CF73749';")
    userData = cur.fetchall()
    cur.close()
    return userData

if __name__ == '__main__':
    app.run()
