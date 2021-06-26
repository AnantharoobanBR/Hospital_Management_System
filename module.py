import smtplib 
from tkinter import *
import math, random 
def send(target,otp):
    try:
        gmailaddress = 'aajtriratnas@gmail.com'
        gmailpassword = '*aaj1221'
        msg = "Hi there!\nYour Single Use Code for Resetting the password is " + str(otp)+"\nRegards,\nHOSPITAL MANAGEMENT SYSTEM "
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress,gmailpassword)
        mailServer.sendmail(gmailaddress,target,msg)
        mailServer.quit()
        print('success')
        return 1
    except:
        print('try again')
        return 0
def generateOTP() : 

    digits = "0123456789"
    OTP = ""
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
    return OTP 
 


