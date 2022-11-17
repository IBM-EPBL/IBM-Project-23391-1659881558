# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:05:54 2022

@author: Rithiha
"""

from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import bcrypt
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;Security=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wpy86763;PWD=ib01vP5v5WYQDNRY",'','')



app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/",methods=['GET'])
def home():
    if 'email' not in session:
      return redirect(url_for('pda_homepage'))
    return render_template('pda_homepage.html',name='Home')
@app.route("/pda_homepage")
def pda_homepage():
  return render_template('pda_homepage.html')

@app.route("/pda_helpdesk")
def pda_helpdesk():
  return render_template('pda_helpdesk.html')

@app.route("/pda_contactpage")
def pda_contactpage():
  return render_template('pda_contactpage.html')

@app.route("/pda_feedbackform")
def pda_feedbackform():
  return render_template('pda_feedbackform.html')

@app.route("/pda_welcomepage")
def pda_welcomepage():
  return render_template('pda_welcomepage.html')

@app.route("/pda_dashboard")
def pda_dashboard():
  return render_template('pda_dashboard.html')

@app.route("/pda_donorpage")
def pda_donorpage():
  return render_template('pda_donorpage.html')

@app.route("/pda_patientpage")
def pda_patientpage():
  return render_template('pda_patientpage.html')



@app.route("/pda_register",methods=['GET','POST'])
def register():
  if request.method == 'POST':
    name = request.form['name']
    phn = request.form['phn']
    email = request.form['email']
    psw = request.form['psw']

    if not name or not email or not phn or not psw:
      return render_template('pda_register.html',error='Please fill all fields')
    hash=bcrypt.hashpw(psw.encode('utf-8'),bcrypt.gensalt())
    query = "SELECT * FROM user_detail WHERE email=? OR phn=?"
    stmt = ibm_db.prepare(conn, query)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,phn)
    ibm_db.execute(stmt)
    isUser = ibm_db.fetch_assoc(stmt)
    if not isUser:
      insert_sql = "INSERT INTO user_detail(name, email, phn, psw) VALUES (?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, phn)
      ibm_db.bind_param(prep_stmt, 4, hash)
      ibm_db.execute(prep_stmt)
      return render_template('pda_register.html',success="You can login")
    else:
      return render_template('pda_register.html',error='Invalid Credentials')

  return render_template('pda_register.html',name='Home')

@app.route("/pda_loginpage",methods=['GET','POST'])
def login():
    if request.method == 'POST':
      email = request.form['email']
      psw = request.form['psw']

      if not email or not psw:
        return render_template('pda_loginpage.html',error='Please fill all fields')
      query = "SELECT * FROM user_detail WHERE email=?"
      stmt = ibm_db.prepare(conn, query)
      ibm_db.bind_param(stmt,1,email)
      ibm_db.execute(stmt)
      isUser = ibm_db.fetch_assoc(stmt)
      print(isUser,psw)

      if not isUser:
        return render_template('pda_loginpage.html',error='Invalid Credentials')
      
      isPasswordMatch = bcrypt.checkpw(psw.encode('utf-8'),isUser['PSW'].encode('utf-8'))

      if not isPasswordMatch:
        return render_template('pda_loginpage.html',error='Invalid Credentials')

      session['email'] = isUser['EMAIL']
      return redirect(url_for('pda_welcomepage'))

    return render_template('pda_loginpage.html',name='Home')



@app.route("/pda_donorpage",methods=['GET','POST'])
def donar():
  if request.method == 'POST':
    bldgrp=request.form['bldgrp']
    fname = request.form['fname']
    phn = request.form['phn']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    area = request.form['area']
    state = request.form['state']
    
    insert_sql = "INSERT INTO donar(bldgrp,fname, phn, email,date,time,area,state) VALUES (?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, bldgrp)
    ibm_db.bind_param(prep_stmt, 2, fname)
    ibm_db.bind_param(prep_stmt, 3, phn)
    ibm_db.bind_param(prep_stmt, 4, email)
    ibm_db.bind_param(prep_stmt, 5, date)
    ibm_db.bind_param(prep_stmt, 6, time)
    ibm_db.bind_param(prep_stmt, 7, area)
    ibm_db.bind_param(prep_stmt, 8, state)
    ibm_db.execute(prep_stmt)
    return render_template('pda_dashboard.html',success="Thanks for your support")
  else:
      return render_template('pda_dashboard.html',error='Invalid Credentials')

@app.route("/pda_patientpage",methods=['GET','POST'])
def patientt():
  if request.method == 'POST':
    pname=request.form['pname']
    hname = request.form['hname']
    dname = request.form['dname']
    bldgrp = request.form['bldgrp']
    when = request.form['when']
    num = request.form['num']
    email = request.form['email']
    city = request.form['city']
    insert_sql = "INSERT INTO patient(pname,hname,dname,bldgrp,when,num,email,city) VALUES (?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, pname)
    ibm_db.bind_param(prep_stmt, 2, hname)
    ibm_db.bind_param(prep_stmt, 3, dname)
    ibm_db.bind_param(prep_stmt, 4, bldgrp)
    ibm_db.bind_param(prep_stmt, 5, when)
    ibm_db.bind_param(prep_stmt, 6, num)
    ibm_db.bind_param(prep_stmt, 7, email)
    ibm_db.bind_param(prep_stmt, 8, city)
    ibm_db.execute(prep_stmt)
    return render_template('pda_dashboard.html',success="Connect with complete care")
  else:
      return render_template('pda_dashboard.html',error='Invalid Credentials')


@app.route("/data")
def display():
  donar_list=[]
 # patient_list=[]

  
  

  #selecting_donar
  sql = "SELECT * FROM donar "
  stmt = ibm_db.exec_immediate(conn, sql)
  donar = ibm_db.fetch_both(stmt)
  while donar!= False :
      donar_list.append(donar)
      donar = ibm_db.fetch_both(stmt)
  print(donar_list)
  return render_template('pda_dashboard.html',bldgrp=donar_list)

  #selecting_col1
 # sql = "SELECT * FROM donar"
 # stmt = ibm_db.exec_immediate(conn, sql)
  #donar = ibm_db.fetch_both(stmt)
  #while donar!= False :
    # donar_list.append(donar)
    # donar = ibm_db.fetch_both(stmt)
  #print(donar_list)
  #return render_template('pda_dashboard.html',fname=donar_list)
 
    
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(debug=True)





