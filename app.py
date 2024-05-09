from flask import Flask, render_template,request,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('food.html')

@app.route('/details',methods=['GET','POST'])
def order():
    if request.method=='POST':
        name = request.form['Name']
        phone_number = request.form['PhoneNumber']
        email_id = request.form['E-mailId']
        door_no = request.form['DoorNo.']
        village = request.form['Village']
        district = request.form['District']
        pin_code = request.form['PinCode']
        payment = request.form['PAYMENTS']

        conn=create_connection()
        cur=conn.cursor()
        cur.execute('''INSERT INTO userData (name, phone_number, email_id, door_no, village, district, pin_code, payment)  VALUES (?,?,?,?,?,?,?,?)''', (name,phone_number,email_id,door_no,village,district,pin_code,payment))
        conn.commit()
        conn.close()
        return 'Succesfully pushed into database'
    return render_template('food1.html')

def create_connection():
    conn = sqlite3.connect('order.db')
    return conn

def create_table():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS userData(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone_number INTEGER NOT NULL,
    email_id TEXT NOT NULL,
    door_no TEXT NOT NULL,
    village TEXT NOT NULL,
    district TEXT NOT NULL,
    pin_code INTEGER NOT NULL,
    payment TEXT NOT NULL)''')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)