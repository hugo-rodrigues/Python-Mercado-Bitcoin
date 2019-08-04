
from flask import Flask, render_template, request
import requests
import sqlite3 as sql
app = Flask(__name__)
conn = sql.connect('mercadoBitcoin.db')
c = conn.cursor()



def create_table():
    c.execute('CREATE TABLE meses (mes INTEGER,amount INTEGER,volume REAL)')
    c.execute('CREATE TABLE total (id INTEGER,amountMedia INTEGER, volumeMedia REAL,amount INTEGER , volume REAL)')
    conn.commit()
    
    
    

   
 
 
def pegar(mesatual,fimMes):
	try:
		mes = mesatual
	
		dia = 1
	
		while dia <= fimMes :
	
			mesTexto = str(mes)
			diaT = str(dia)

    
    
			r = requests.get('https://www.mercadobitcoin.net/api/BTC/day-summary/2016/'+mesTexto+'/'+diaT+'/')
  
			json_object = r.json()
  
			volumeDiario = float(json_object['volume'])
			amountDiario = float(json_object['amount'])
		
			c.execute("INSERT INTO meses VALUES (?,?,?)",(mes,amountDiario,volumeDiario))
			conn.commit()
  
	
			dia = dia + 1
	except:
		conn.rollback()
	

def InserirNovaTabela():
	try:	
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 1" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 2" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()

		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 3" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 4" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()

		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 5" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 6" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 7" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 8" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()

		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 9" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 10" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()

		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 11" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
		c.execute(" SELECT mes , AVG(amount) , AVG(volume), SUM(amount), SUM(volume)  FROM meses where mes= 12" ) 
		Total = c.fetchone()
		idmes = Total[0]
		avgamt = Total[1]
		avgvol = Total[2]
		somamt = Total[3]
		somvol = Total[4]
		c.execute("INSERT INTO total VALUES (?,?,?,?,?)",(idmes,avgamt,avgvol,somamt,somvol))
		conn.commit()
  
	except:
		conn.rollback()

  
  
  
  
		
 
 

def InserirTabela(): 
    mesCom30 = [4,6,9,11]
    mesCom31 = [1,3,5,7,8,10,12]
    
    for x in mesCom30:
        pegar(x,30)
        
    for y in mesCom31:
        pegar(y,31)
    
    pegar(2,29)
    
    
create_table()
InserirTabela()
InserirNovaTabela()







