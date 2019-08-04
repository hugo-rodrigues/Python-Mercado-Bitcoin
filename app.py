from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

import requests
import sqlite3 as sql
conn = sql.connect('mercadoBitcoin.db')
c = conn.cursor()
app = Flask(__name__)





# Index
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/dashboard')
def dashboard():
    try:
    
        conn = sql.connect('mercadoBitcoin.db')
        c = conn.cursor()
    
  
    
        c.execute("SELECT sum(volume) FROM total ") 
   
    
        data1 = c.fetchone()
        dado= data1[0]
   
    
        c.execute("SELECT sum(amount) FROM total ") 
        data2 = c.fetchone()
        dado1= data2[0]
    
        c.execute("SELECT avg(volumeMedia) FROM total ") 
        data3 = c.fetchone()
        dado2= data3[0]
    
        c.execute("SELECT avg(amountMedia) FROM total ") 
        data4 = c.fetchone()
        dado3 = data4[0]
    
        c.execute("select * from total order by volume desc")
        data5 =[dict (id = row[0], volume = row[4]) for row in c.fetchall()]
   
        return render_template('dashboard.html',VolTotal = dado,NegTotal = dado1 , MediaVol = dado2, MediaNeg = dado3 ,row = data5)
   
    except:
      conn.rollback()

    
    finally:
        c.close()





if __name__ == '__main__':
    
    app.run(debug=True)
