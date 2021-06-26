import sqlite3
from datetime import date
def createlink():
    conn = sqlite3.connect('medical.db')
    return conn


def update_medicine(data):
 conn=createlink()
 mycursor = conn.cursor()
 query= 'update medicine set Med_name=?,rate=?,Qty=? where med_id=?'
 mycursor.execute(query,data)
 conn.commit()
 conn.close()

def update_patient(data):
 conn=createlink()
 mycursor = conn.cursor()
 query='UPDATE patient set patient_name=?,dob=?,blood_gp=?,Phone_no=?,Email=? where patient_id=?'
 mycursor.execute(query,data)
 conn.commit()
 conn.close()

def update_doctor(data):
 conn=createlink()
 mycursor = conn.cursor()

 query='UPDATE doctor set doctor_name=?,dob=?,Phone_no=?,Email=? where doctor_id=?'
 mycursor.execute(query,data)
 conn.commit()
 conn.close()

def update_nurse(data):
 conn=createlink()
 mycursor = conn.cursor()
 query = 'UPDATE nurse set nurse_name=?,dob=?,salary=?,Phone_no=?,Email=? where nurse_id=?'
 insertDOB(data[3])
 mycursor.execute(query,data)
 conn.commit()
 conn.close()

def update_medical_staff(data):
 conn=createlink()
 mycursor = conn.cursor()
 query='update medical_staff set Med_stf_name=?,dob=?,Salary=?,Phone_no=?,Email=? where med_stf_id=?'
 dob=data[3]
 insertDOB(dob)
 mycursor.execute(query,data)
 conn.commit()
 conn.close()

def update_salary(pid,salary):
    conn=createlink()
    mycursor = conn.cursor()
    if pid[0]=='D':
        query='update doctor set salary=? where doctor_id=?'
    elif pid[0]=='N':
        query='update nurse set salary=? where nurse_id=?'
    elif pid[0]=='S':
        query='update medical_staff set salary=? where med_stf_id=?'
    row=(salary,pid)
    mycursor.execute(query,row)
    conn.commit()
    conn.close()


#RETURNING TABLE VALUES

def insertDOB(dob):
    conn=createlink()
    mycursor = conn.cursor()
    try:
      query = 'INSERT into person_age(dob) values(?)'
      mycursor.execute(query,(dob,))
    except:
        print('present')
    conn.commit()
    conn.close()


	
def getDoctorData(doctor_id):# this function returns the tuple of that particular doctor_id

    conn=createlink()
    mycursor = conn.cursor()
    query = 'SELECT d.doctor_id,doctor_name, d.dob,salary, email,phone_no,speciality from doctor d,doc_speciality ds, where d.doctor_id =? and d.doctor_id=ds.doctor_id'
    mycursor.execute(query,(doctor_id,))
    result = mycursor.fetchall() 
    return result
    conn.close()

def getNurseData(nur_id):# this function returns the tuple of that particular Nurse_id
    conn=createlink()
    mycursor = conn.cursor()
    query = 'SELECT * from nurse where nur_id = ?'
    mycursor.execute(query,(nur_id,))
    result = mycursor.fetchall() 
    return result
    conn.close()

def getMedStaffData(med_stf_id):# this function returns the tuple of that particular Nurse_id
    conn=createlink()
    mycursor = conn.cursor()
    query = 'SELECT * from medical_staff where med_stf_id = ?'
    mycursor.execute(query,(med_stf_id,))
    result = mycursor.fetchall() 
    return result
    conn.close()

#INSERTING TABLE VALUES
def insertDoctor(data):
    conn=createlink()
    mycursor=conn.cursor()
    #insertDOB(data[3])
    insert_query = 'INSERT  into doctor(doctor_id,doctor_name,dob,salary,phone_no,email,passwd) values(?,?,?,?,?,?,?)'
    mycursor.execute(insert_query,data)
    conn.commit()
    conn.close()
    
def insertpatient(data):
    conn=createlink()
    mycursor=conn.cursor()
    #insertDOB(data[3])
    insert_query = 'INSERT  into patient values(?,?,?,?,?,?,?)'
    mycursor.execute(insert_query,data)
    conn.commit()
    conn.close()

def addSpeciality(doctor_id,speciality):
    conn=createlink()
    mycursor=conn.cursor()
    row = (doctor_id,speciality)
    query = 'INSERT into doc_speciality(doctor_id,speciality) values(?,?)'
    mycursor.execute(query,row)
    conn.commit()
    conn.close()

def insertMedicine(data):
    conn=createlink()
    mycursor=conn.cursor()
    query = 'INSERT into medicine(med_id, med_name, rate, qty) values(?,?,?,?)'
    mycursor.execute(query,data)
    conn.commit()
    conn.close()

def insertNurse(data):
	#function to insert into nurse table
    conn=createlink()
    mycursor=conn.cursor()
    insert_query = 'INSERT  into Nurse values(?,?,?,?,?,?,?)'
    mycursor.execute(insert_query,data)
    conn.commit()
    conn.close()

def insertMedicalStaff(data):

    conn=createlink()
    mycursor=conn.cursor()
    insert_query = 'INSERT  into medical_staff values(?,?,?,?,?,?,?)'
    mycursor.execute(insert_query,data)
    conn.commit()
    conn.close()

def new_admission(data):
    conn=createlink()
    mycursor=conn.cursor()
    insert_query = 'INSERT  into admission(ad_id,p_id,d_id,condition,ad_date,status) values(?,?,?,?,?,?)'
    mycursor.execute(insert_query,data)
    conn.commit()
    conn.close()
def valid_admission(data):
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    if data<d1:
        return True
    
    return False

def valid_admission1(data):
    today = date.today()
    d1 = today.strftime("%d-%m-%Y")
    if data>=d1:
        return True
    return False









