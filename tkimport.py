import tkinter as tk
import tkinter.font as font
import PIL.Image
import PIL.ImageTk
from functools import partial
from tkinter import ttk
import sqlite3
from module import *
from dbfunctions import *
from datetime import date




c1="white"
c2="maroon"
c3="deep sky blue"
c4="cyan"
c5="spring green"
c6="yellow"
c7="medium violet red"
c8="aquamarine"
c9="slate blue"
q1="rosy brown"
q2="saddle brown"
q3="sandy brown"
q4="salmon"
q5="dark salmon"
q6="light salmon"
q7="Moccasin"
q8="PeachPuff"
q9="PapayaWhip"
w1="LemonChiffan"
w2="LightYellow"
w3="khaki"
w4="pink"
w5="LightPink"
w6="PowderBlue"
w7="Aqua"
w8="SkyBlue"
w9="DodgerBlue"
z1="Light Coral"
z2="Crimson"
z3="Tomato"
z4="DeepPink"
z5="HotPink"
z6="MediumVioletRed"
z7="coral"
z8="light coral"
g1="#449c3e"
g2="#baff00"
g3="#46edab"
g4="#83da2f"
g5="#3cd159"
g6="#73ded7"
bg1="gold"
bg2="light goldenrod"
bg3='deepskyblue3' 
bg4='light blue'
bg5='deepskyblue4'

bgn1='#ee91bc' # velvet + pink + brown
bgn2='#ffcbcb'
bgn3='#562349'

bgs1='#ca5116'
bgs2='#f9b384'
bgs3='#581c0c'


f1="courier 18 bold"
f2='Helvetica 15'
f3='mincho 15 bold'
f4='msserif 15'
f5='Verdana 15'
f6="Times 18 bold underline"
f7="Times 15 bold"
f8="Times 25 bold"
f9="Times 12 bold"
f10="courier 15 bold"
f11='Times 18 bold'

geo="1500x1700"

class app(tk.Tk):

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect('medical.db')

        self.user=tk.Frame(self,bg=bg1)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        self.topbar=tk.Frame(self,bg=bg1)
        self.topbar.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

        self.valid=False
        self.users()


    def logout(self):
        self.topbar.destroy()
        self.topbar=tk.Frame(self.user,bg='#ffffff')
        self.topbar.pack(fill=tk.BOTH,side=tk.BOTTOM)

        d=tk.Button(self.topbar,width=10,text='LOG OUT',fg='#442727',bg='#eae7d9',font=f2,command=partial(self.users))
        d.pack(side=tk.RIGHT)


    def users(self):
        self.geometry(geo)
        self.title('Login Page --- HOSPITAL MANAGEMENT SYSTEM')

        self.user.destroy()
        self.topbar.destroy()

        self.user=tk.Frame(self,width=30,bg=bg2)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

#-----------------added portion for inserting imgage in the user page-----------------------------------------------------
        image = PIL.Image.open("hospital.png")
        photo = PIL.ImageTk.PhotoImage(image)
        hosp_img = Label(image=photo)
        
        hosp_img.image = photo # keep a reference!
        hosp_img.place(x=0,y=0)
#------------------------------------------------------------------------------------------------------------------------------        


        l1=tk.Label(self.user,text='STATE YOUR DESIGNATION!',bg='dark orange',fg='white',font=('Times 18 bold'))
        l1.place(x=1000,y=20)


        d=tk.Button(self.user,width=25,text='DOCTOR',fg=c1,font=f1,bg="coral",command=partial(self.doctor))
        d.place(x=1000,y=150)

        p=tk.Button(self.user,width=25,text='PATIENT',fg=c1,font=f1,bg="Darkcyan",command=partial(self.patient))
        p.place(x=1000,y=250)

        n=tk.Button(self.user,width=25,text='NURSE',fg=c1,font=f1,bg="goldenrod",command=partial(self.nurse))
        n.place(x=1000,y=350)

        s=tk.Button(self.user,width=25,text='MEDICAL STAFF',fg=c1,font=f1,bg="maroon",command=partial(self.staff))
        s.place(x=1000,y=450)

        a=tk.Button(self.user,width=25,text='ADMIN',fg=c1,font=f1,bg="crimson",command=partial(self.admin))
        a.place(x=1000,y=550)




    def admin(self):
        self.geometry(geo)
        self.title('Admin Page --- HOSPITAL MANAGEMENT SYSTEM')
        def forgot_pass():
            self.error=''
            def back():
                self.confirm.destroy()
                self.des.destroy()
                self.admin()
            def check2(pid):
                p1=self.ename.get()
                p2=self.ename1.get()
                print(self.ename.get())
                print(self.ename1.get())
                print(self.ename.get()==self.ename1.get())
                if p1==p2:
                    try:
                        self.conn = sqlite3.connect('medical.db')
                        sql = 'UPDATE admin SET password = ? WHERE admin_id = ?'
                        cur = self.conn.cursor()
                        cur.execute(sql,(p1,pid))
                        self.conn.commit()
                        self.conn.close()
                        self.user.destroy()
                        self.des.destroy()
                        self.confirm.destroy()
                        self.admin()
                    except:
                        self.error='Error'
                        reset(pid)
                else:
                    self.error='Try again'
                    reset(pid)

            def reset(pid):
                 self.confirm.destroy()
                 self.user.destroy()

                 ldes['text']="RESET PASSWORD"
                 ldes1['text']=self.error

                 self.user=tk.Frame(self,width=30,bg=w4)
                 self.user.pack(fill=tk.BOTH,expand=tk.YES)

                 lname=tk.Label(self.user,width=20,bg=z5,text='NEW PASSWORD',font=f7)
                 lname.grid(row=0,column=0,padx=10,pady=20)

                 self.ename=tk.Entry(self.user,width=20,font=f7)
                 self.ename.grid(row=0,column=1,padx=10,pady=20)

                 lname1=tk.Label(self.user,width=20,bg=z5,text='RE-ENTER PASSWORD',font=f7)
                 lname1.grid(row=1,column=0,padx=10,pady=20)

                 self.ename1=tk.Entry(self.user,width=20,font=f7)
                 self.ename1.grid(row=1,column=1,padx=10,pady=20)

                 self.confirm=tk.Frame(self,width=30,bg=w4)
                 self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                 eback=tk.Button(self.confirm,text='BACK',font=f9,fg='red',width=16,command=partial(back))
                 eback.grid(row=0,column=0,padx=50,pady=15)

                 log=tk.Button(self.confirm,text='CONFIRM!',font=f9,fg='green',width=16,command=partial(check2,pid))
                 log.grid(row=0,column=1,padx=60,pady=15)

            def check1():
                def back():
                     self.confirm.destroy()
                     self.des.destroy()
                     self.admin()

                def verify(otp,pid):
                    if otp==self.ename.get():
                        reset(pid)
                    else:
                        ldes1['text']='INVALID OTP'

                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   pid=self.ename.get()
                   cur.execute("SELECT Email FROM admin WHERE admin_id=?", (pid,))
                   rows = cur.fetchall()
                   otp=str(generateOTP())
                   res=send(rows[0][0],otp)
                   if res==1:
                     self.confirm.destroy()
                     ldes['text']='ONE TIME PASSWORD | SINGLE USE CODE'
                     lname['text']='ENTER THE OTP'
                     self.ename.delete(0,'end')
                     self.confirm=tk.Frame(self,width=30,bg=w4)
                     self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                     eback=tk.Button(self.confirm,text='BACK',font=f9,fg='red',width=10,command=partial(back))
                     eback.grid(row=0,column=0,padx=30,pady=15)

                     log=tk.Button(self.confirm,text='CHECK',font=f9,fg='green',width=10,command=partial(verify,otp,pid))
                     log.grid(row=0,column=1,padx=30,pady=15)

                     resend=tk.Button(self.confirm,text='RESEND',font=f9,fg='blue',width=10,command=partial(forgot_pass))
                     resend.grid(row=0,column=3,padx=30,pady=15)
                   else:
                     ldes1['text']='INVALID e-MAIL ID'
                except:
                    forgot_pass()




            self.confirm.destroy()
            self.user.destroy()
            self.des.destroy()

            self.des=tk.Frame(self,bg=z4)
            self.des.pack(fill=tk.BOTH,expand=tk.YES)

            ldes=tk.Label(self.des,bg=z4,text='ENTER ID TO Get-OTP!',font=f6,fg=c1)
            ldes.pack(fill=tk.BOTH,expand=tk.YES)

            ldes1=tk.Label(self.des,bg=w4,text=self.error,fg='red',font=f3)
            ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            self.user=tk.Frame(self,width=30,bg=w4)
            self.user.pack(fill=tk.BOTH,expand=tk.YES)

            lname=tk.Label(self.user,width=20,bg=z5,text='ADMIN ID',font=f7)
            lname.grid(row=0,column=0,padx=10,pady=20)

            self.ename=tk.Entry(self.user,width=20,font=f7)
            self.ename.grid(row=0,column=1,padx=10,pady=20)

            self.confirm=tk.Frame(self,width=30,bg=w4)
            self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            eback=tk.Button(self.confirm,text='BACK',font=f9,fg='red',width=16,command=partial(back))
            eback.grid(row=0,column=0,padx=50,pady=15)

            log=tk.Button(self.confirm,text='Get-OTP',font=f9,fg='green',width=16,command=partial(check1))
            log.grid(row=0,column=1,padx=60,pady=15)

        def back():
            self.confirm.destroy()
            self.des.destroy()
            self.topbar.destroy()
            self.users()

        def profile1():#    
                                                               # hh
            self.geometry(geo)
            self.user.destroy()
            self.user=tk.Frame(self,bg=q8)
            self.user.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            self.user1=tk.Frame(self.user,bg=q8)
            self.user1.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            l1=tk.Label(self.user1,text='ADD A NEW PERSON | BY CHOOSING A DESIGNATION! | ADMIN Rights Only',bg=q8,fg=c2,font="Times 18 bold")
            l1.grid(row=0,column=0,padx=10,pady=10)

            d=tk.Button(self.user1,width=25,text='DOCTOR',fg=c1,bg=q3,font=f7,command=partial(add_doc))
            d.grid(row=2,column=0,padx=10,pady=10)

            p=tk.Button(self.user1,width=25,text='PATIENT',fg=c1,bg=q3,font=f7,command=partial(add_patient))
            p.grid(row=3,column=0,padx=10,pady=10)

            n=tk.Button(self.user1,width=25,text='NURSE',fg=c1,bg=q3,font=f7,command=partial(add_nurse))
            n.grid(row=4,column=0,padx=10,pady=10)

            s=tk.Button(self.user1,width=25,text='MEDICAL STAFF',fg=c1,bg=q3,font=f7,command=partial(add_staff))
            s.grid(row=5,column=0,padx=10,pady=10)

            a=tk.Button(self.user1,width=25,text='NEW MEDICINE',fg=c1,bg=q3,font=f7,command=partial(add_medicine))
            a.grid(row=6,column=0,padx=10,pady=10)

            b=tk.Button(self.user1,width=25,text='EDIT MEDICINE',fg=c1,bg=q3,font=f7,command=partial(add_med_edit))
            b.grid(row=7,column=0,padx=10,pady=10)

            self.topbar=tk.Frame(self.user,bg=q8)
            self.topbar.pack(fill=tk.BOTH,side=tk.BOTTOM)

            d=tk.Button(self.topbar,width=10,text='LOG OUT',fg='#442727',bg='#eae7d9',font=f2,command=partial(self.users))
            d.pack(side=tk.RIGHT)



        today = date.today()
        d1 = today.strftime("%d-%m-%Y")


        def add_doc():


                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    try:

                        data=('D'+str(id1),ename.get(),edob.get(),int(eblood.get()),ephone.get(),email.get(),epass.get())

                        if valid_admission(data[2]):
                             insertDoctor(data)
                             s=espe.get()
                             addSpeciality(data[0],s)
                             print("Success!")
                             profile1()
                        else:
                            print("Failed1")
                            self.error='error message'
                            add_doc()

                    except:

                        print("Failed")
                        self.error='error message'
                        add_doc()

                self.user.destroy()
                rows=0
                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   cur.execute("SELECT max(doctor_id) FROM doctor")
                   rows = cur.fetchall()
                   print(rows)
                   l=len(rows[0][0])
                   if l>1:
                       rows=rows[0][0]
                       rows=int(rows[1:l])
                       print(rows)
                except:
                    rows=0

                #self.geometry("1500x1700")
                self.geometry(geo)

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER DETAILS OF THE DOCTOR',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='DOCTOR ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=q7,font=f7,text='D'+str(rows+1))
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=z8,text='DOCTOR NAME',font=f7,fg=c1)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)

                lpass=tk.Label(self.user,width=20,bg=z8,text='PASSWORD',font=f7,fg=c1)
                lpass.grid(row=2,column=0,padx=10,pady=20)

                epass=tk.Entry(self.user,width=20,font=f7)
                epass.grid(row=2,column=1,padx=10,pady=20)

                ldob=tk.Label(self.user,width=20,bg=z8,text='DATE OF BIRTH',font=f7,fg=c1)
                ldob.grid(row=3,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=3,column=1,padx=10,pady=20)
                edob.insert(0,d1)

                lblood=tk.Label(self.user,width=20,bg=z8,text='SALARY',font=f7,fg=c1)
                lblood.grid(row=4,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=4,column=1,padx=10,pady=20)

                lphone=tk.Label(self.user,width=20,bg=z8,text='CONTACT NUMBER',font=f7,fg=c1)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)

                lmail=tk.Label(self.user,width=20,bg=z8,text='e-MAIL ID',font=f7,fg=c1)
                lmail.grid(row=6,column=0,padx=10,pady=20)

                email=tk.Entry(self.user,width=20,font=f7)
                email.grid(row=6,column=1,padx=10,pady=20)

                lspe=tk.Label(self.user,width=20,bg=z8,text='SPECIALIZATION',font=f7,fg=c1)
                lspe.grid(row=7,column=0,padx=10,pady=20)

                espe=tk.Entry(self.user,width=20,font=f7)
                espe.grid(row=7,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',font=f9,fg='red',width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',font=f9,fg='green',width=16,command=partial(summit,rows+1))
                log.grid(row=0,column=1,padx=60,pady=15)


        def add_patient():

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    try:
                        data=('P'+str(id1),ename.get(),edob.get(),eblood.get(),ephone.get(),email.get(),epass.get())

                        if valid_admission(data[2]):
                             insertpatient(data)
                             print("success")
                             profile1()
                        else:
                            print("failed1")
                            self.error='error message'
                            add_patient()

                    except:
                        print("failed")
                        self.error='error message'
                        add_patient()


                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)
                rows=0
                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   cur.execute("SELECT max(patient_id) FROM patient")
                   rows = cur.fetchall()
                   print(rows)
                   l=len(rows[0][0])
                   if l>1:
                       rows=rows[0][0]
                       rows=int(rows[1:l])
                       print(rows)
                except:
                    rows=0

                self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER DETAILS OF THE PATIENT',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='PATIENT ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=q7,font=f7,text='P'+str(rows+1))
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=z8,text='PATIENT NAME',font=f7,fg=c1)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)

                lpass=tk.Label(self.user,width=20,bg=z8,text='PASSWORD',font=f7,fg=c1)
                lpass.grid(row=6,column=0,padx=10,pady=20)

                epass=tk.Entry(self.user,width=20,font=f7)
                epass.grid(row=6,column=1,padx=10,pady=20)

                ldob=tk.Label(self.user,width=20,bg=z8,text='DATE OF BIRTH',font=f7,fg=c1)
                ldob.grid(row=2,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=2,column=1,padx=10,pady=20)
                edob.insert(0,d1)

                lblood=tk.Label(self.user,width=20,bg=z8,text='BLOOD GROUP',font=f7,fg=c1)
                lblood.grid(row=3,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=3,column=1,padx=10,pady=20)

                lphone=tk.Label(self.user,width=20,bg=z8,text='CONTACT NUMBER',font=f7,fg=c1)
                lphone.grid(row=4,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=4,column=1,padx=10,pady=20)

                lmail=tk.Label(self.user,width=20,bg=z8,text='e-MAIL ID',font=f7,fg=c1)
                lmail.grid(row=5,column=0,padx=10,pady=20)

                email=tk.Entry(self.user,width=20,font=f7)
                email.grid(row=5,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',font=f9,width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',font=f9,width=16,command=partial(summit,rows+1))
                log.grid(row=0,column=1,padx=60,pady=15)

        def add_nurse():

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    try:

                        data=('N'+str(id1),ename.get(),edob.get(),int(eblood.get()),ephone.get(),email.get(),epass.get())
                        if valid_admission(data[2]):
                             insertNurse(data)
                             print("Success")
                             profile1()
                        else:
                            print("Failed1")
                            self.error='error message'
                            add_nurse()

                    except:

                        print("Failed")
                        self.error='error message'
                        add_nurse()

                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)
                rows=0
                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   cur.execute("SELECT max(nurse_id) FROM nurse")
                   rows = cur.fetchall()
                   print(rows)
                   l=len(rows[0][0])
                   if l>1:
                       rows=rows[0][0]
                       rows=int(rows[1:l])
                       print(rows)
                except:
                    rows=0

                self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER DETAILS OF THE NURSE',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='NURSE ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=q7,font=f7,text='N'+str(rows+1))
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=z8,text='NURSE NAME',font=f7,fg=c1)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)

                lpass=tk.Label(self.user,width=20,bg=z8,text='PASSWORD',font=f7,fg=c1)
                lpass.grid(row=2,column=0,padx=10,pady=20)

                epass=tk.Entry(self.user,width=20,font=f7)
                epass.grid(row=2,column=1,padx=10,pady=20)

                ldob=tk.Label(self.user,width=20,bg=z8,text='DATE OF BIRTH',font=f7,fg=c1)
                ldob.grid(row=3,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=3,column=1,padx=10,pady=20)
                edob.insert(0,d1)

                lblood=tk.Label(self.user,width=20,bg=z8,text='SALARY',font=f7,fg=c1)
                lblood.grid(row=4,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=4,column=1,padx=10,pady=20)

                lphone=tk.Label(self.user,width=20,bg=z8,text='CONTACT NUMBER',font=f7,fg=c1)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)

                lmail=tk.Label(self.user,width=20,bg=z8,text='e-MAIL ID',font=f7,fg=c1)
                lmail.grid(row=6,column=0,padx=10,pady=20)

                email=tk.Entry(self.user,width=20,font=f7)
                email.grid(row=6,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',font=f9,width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',font=f9,width=16,command=partial(summit,rows+1))
                log.grid(row=0,column=1,padx=60,pady=15)


        def add_staff():

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    try:

                        data=('S'+str(id1),ename.get(),edob.get(),int(eblood.get()),ephone.get(),email.get(),epass.get())
                        if valid_admission(data[2]):
                             insertMedicalStaff(data)
                             print("success")
                             profile1()
                        else:
                            print("failed1")
                            self.error='error message'
                            add_staff()

                    except:

                        print("failed")
                        self.error='error message'
                        add_staff()
                    #edit_profile(no)

                self.user.destroy()
                #self.geometry("1500x1700")
                self.geometry(geo)
                rows=0
                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   cur.execute("SELECT max(med_stf_id) FROM medical_staff")
                   rows = cur.fetchall()
                   print(rows)
                   l=len(rows[0][0])
                   if l>1:
                       rows=rows[0][0]
                       rows=int(rows[1:l])
                       print(rows)
                except:
                    rows=0

                self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER DETAILS OF THE MEDICAL STAFF',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='MEDICAL_STAFF ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,font=f7,bg=q7,text='S'+str(rows+1))
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=z8,text='MEDICAL_STAFF NAME',font=f7,fg=c1)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)

                lpass=tk.Label(self.user,width=20,bg=z8,text='PASSWORD',font=f7,fg=c1)
                lpass.grid(row=2,column=0,padx=10,pady=20)

                epass=tk.Entry(self.user,width=20,font=f7)
                epass.grid(row=2,column=1,padx=10,pady=20)

                ldob=tk.Label(self.user,width=20,bg=z8,text='DATE OF BIRTH',font=f7,fg=c1)
                ldob.grid(row=3,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=3,column=1,padx=10,pady=20)
                edob.insert(0,d1)

                lblood=tk.Label(self.user,width=20,bg=z8,text='SALARY',font=f7,fg=c1)
                lblood.grid(row=4,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=4,column=1,padx=10,pady=20)

                lphone=tk.Label(self.user,width=20,bg=z8,text='CONTACT NUMBER',font=f7,fg=c1)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)

                lmail=tk.Label(self.user,width=20,bg=z8,text='e-MAIL ID',font=f7,fg=c1)
                lmail.grid(row=6,column=0,padx=10,pady=20)

                email=tk.Entry(self.user,width=20,font=f7)
                email.grid(row=6,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',font=f9,fg='red',width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',font=f9,fg='green',width=16,command=partial(summit,rows+1))
                log.grid(row=0,column=1,padx=60,pady=15)


        def add_medicine():

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    try:

                        data=('M'+str(id1),ename.get(),eprice.get(),eque.get())
                        insertMedicine(data)
                        print("Success")
                        profile1()

                    except:

                        print("Failed")
                        self.error='error message'
                        add_medicine()
                    #edit_profile(no)

                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)
                rows=0
                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   cur.execute("SELECT max(med_id) FROM medicine")
                   rows = cur.fetchall()
                   print(rows)
                   l=len(rows[0][0])
                   if l>1:
                       rows=rows[0][0]
                       rows=int(rows[1:l])
                       print(rows)
                except:
                    rows=0

                # self.geometry("1500x1700")
                self.geometry(geo)

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER DETAILS OF THE MEDICINE',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='MEDICINE ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,font=f7,bg=q7,text='M'+str(rows+1))
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=z8,text='MEDICINE NAME',font=f7,fg=c1)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)

                lque=tk.Label(self.user,width=20,bg=z8,text='QUANTITY',font=f7,fg=c1)
                lque.grid(row=2,column=0,padx=10,pady=20)

                eque=tk.Entry(self.user,width=20,font=f7)
                eque.grid(row=2,column=1,padx=10,pady=20)

                lprice=tk.Label(self.user,width=20,bg=z8,text='PRICE',font=f7,fg=c1)
                lprice.grid(row=3,column=0,padx=10,pady=20)

                eprice=tk.Entry(self.user,width=20,font=f7)
                eprice.grid(row=3,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',font=f9,width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='ADD',fg='green',font=f9,width=16,command=partial(summit,rows+1))
                log.grid(row=0,column=1,padx=60,pady=15)


        def add_med_edit():

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile1()

                def summit(id1):
                    self.confirm.destroy()
                    self.des.destroy()
                    #try:
                    if True:

                        data=(self.ename.get(),self.eque.get(),self.eprice.get(),id1)
                        update_medicine(data)
                        print("Success")
                        profile1()

                    #except:
                    else:

                        print("Failed")
                        self.error='error message'
                        add_med_edit()
                    #edit_profile(no)

                def Next():
                   def back():
                       self.user.destroy()
                       self.confirm.destroy()
                       add_med_edit()
                   id1=self.eid.get()
                   self.user.destroy()
                   self.confirm.destroy()
                   self.geometry(geo)
                   # self.geometry("1500x1700")
                   try:
                       print(id1)
                       self.conn = sqlite3.connect('medical.db')
                       cur = self.conn.cursor()
                       cur.execute("SELECT * FROM medicine where Med_id=?",(id1,))
                       rows = cur.fetchall()
                       print(rows)
                   except:
                       add_med_edit()


                   self.des.destroy()
                   self.user.destroy()
                   self.confirm.destroy()
                   self.des=tk.Frame(self,bg=q7)
                   self.des.pack(fill=tk.BOTH,expand=tk.YES)

                   ldes=tk.Label(self.des,bg=z2,text='EDIT DETAILS OF MEDICINE',font=f6,fg=c1)
                   ldes.pack(fill=tk.BOTH,expand=tk.YES)

                   ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                   ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                   self.user=tk.Frame(self,width=30,bg=q7)
                   self.user.pack(fill=tk.BOTH,expand=tk.YES)

                   lid=tk.Label(self.user,width=20,bg=z8,text='MEDICINE ID',font=f7,fg=c1)
                   lid.grid(row=0,column=0,padx=10,pady=20)

                   eid=tk.Label(self.user,width=20,bg=q7,text=id1,font=f7)
                   eid.grid(row=0,column=1,padx=10,pady=20)

                   lname=tk.Label(self.user,width=20,bg=z8,text='MEDICINE NAME',font=f7,fg=c1)
                   lname.grid(row=1,column=0,padx=10,pady=20)

                   self.ename=tk.Entry(self.user,width=20,font=f7)
                   self.ename.grid(row=1,column=1,padx=10,pady=20)
                   self.ename.insert(0,rows[0][1])

                   lque=tk.Label(self.user,width=20,bg=z8,text='MEDICINE COST',font=f7,fg=c1)
                   lque.grid(row=2,column=0,padx=10,pady=20)

                   self.eque=tk.Entry(self.user,width=20,font=f7)
                   self.eque.grid(row=2,column=1,padx=10,pady=20)
                   self.eque.insert(0,rows[0][2])

                   lprice=tk.Label(self.user,width=20,bg=z8,text='MEDICINE QUANTITY',font=f7,fg=c1)
                   lprice.grid(row=3,column=0,padx=10,pady=20)

                   self.eprice=tk.Entry(self.user,width=20,font=f7)
                   self.eprice.grid(row=3,column=1,padx=10,pady=20)
                   self.eprice.insert(0,rows[0][3])

                   self.confirm=tk.Frame(self,width=30,bg=q7)
                   self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                   back=tk.Button(self.confirm,text='CANCEL',font=f9,fg='red',width=16,command=partial(back))
                   back.grid(row=0,column=0,padx=50,pady=15)

                   log=tk.Button(self.confirm,text='SUBMIT',font=f9,fg='green',width=16,command=partial(summit,id1))
                   log.grid(row=0,column=1,padx=60,pady=15)




                self.user.destroy()
                self.geometry(geo)
                # self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=q7)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='ENTER THE MEDICINE ID',font=f6,fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=q7,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=q7)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=z8,text='MEDICINE ID',font=f7,fg=c1)
                lid.grid(row=0,column=0,padx=10,pady=20)

                self.eid=tk.Entry(self.user,width=20,font=f7)
                self.eid.grid(row=0,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=q7)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',font=f9,fg='red',width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',font=f9,fg='green',width=16,command=partial(Next))
                log.grid(row=0,column=1,padx=60,pady=15)


        def verify():
            id1=ename.get()
            pass1=epass.get()
            self.conn = sqlite3.connect('medical.db')
            cur=self.conn.cursor()
            self.confirm.destroy()
            self.des.destroy()
            self.user.destroy()
            try:
                cur.execute("SELECT password FROM admin where admin_id=?",(id1,))
                rows = cur.fetchall()
                if pass1==rows[0][0]:
                    profile1()
                    self.error=''
                    self.id=id1
                else:
                   print('Invalid id')
                   self.admin()
            except:
                print('Invalid id')
                self.admin()




        self.user.destroy()

        self.des=tk.Frame(self,bg="coral")
        self.des.pack(fill=tk.BOTH,expand=tk.YES)

        ldes=tk.Label(self.des,bg="coral",text='ENTER VALID ID & PASSWORD',font=f6,fg=c1)
        ldes.pack(fill=tk.BOTH,expand=tk.YES)

        self.user=tk.Frame(self,width=30,bg="coral")
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        lname=tk.Label(self.user,width=20,bg="bisque",text='ADMIN ID',font=f7)
        lname.grid(row=0,column=0,padx=10,pady=20)

        ename=tk.Entry(self.user,width=20,font=f7)
        ename.grid(row=0,column=1,padx=10,pady=20)

        lpass=tk.Label(self.user,width=20,bg="bisque",text='PASSWORD',font=f7)
        lpass.grid(row=2,column=0,padx=10,pady=20)

        epass=tk.Entry(self.user,width=20,font=f7)
        epass.grid(row=2,column=1,padx=10,pady=20)

        self.confirm=tk.Frame(self,width=30,bg="coral")
        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

        back=tk.Button(self.confirm,text='BACK',fg='red',font=f9,width=16,command=partial(back))
        back.grid(row=0,column=0,padx=50,pady=15)

        log=tk.Button(self.confirm,text='LOGIN',fg='green',font=f9,width=16,command=partial(verify))
        log.grid(row=0,column=1,padx=60,pady=15)

        forg=tk.Button(self.confirm,text='FORGOT PASSWORD',font=f9,fg='red',width=20,command=partial(forgot_pass))
        forg.grid(row=1,column=0,padx=50,pady=15)

#staff ------------------------------------------------------------------------------------------------------------
    def staff(self):
        self.geometry(geo)
        # self.geometry("1500x1700")
        self.title('MEDICAL STAFF  ---HOSPITAL MANAGEMENT SYSTEM')
        def forgot_pass():
            self.error=''
            def back():
                self.confirm.destroy()
                self.des.destroy()
                self.staff()
            def check2(pid):
                p1=self.ename.get()
                p2=self.ename1.get()
                print(self.ename.get())
                print(self.ename1.get())
                print(self.ename.get()==self.ename1.get())
                if p1==p2:
                    try:
                        self.conn = sqlite3.connect('medical.db')
                        sql = 'UPDATE medical_staff SET passwd = ? WHERE med_stf_id = ?'
                        cur = self.conn.cursor()
                        cur.execute(sql,(p1,pid))
                        self.conn.commit()
                        self.conn.close()
                        self.user.destroy()
                        self.des.destroy()
                        self.confirm.destroy()
                        self.staff()
                    except:
                        self.error='error'
                        reset(pid)
                else:
                    self.error='try again'
                    reset(pid)

            def reset(pid):
                 self.confirm.destroy()
                 self.user.destroy()

                 ldes['text']="RESET PASSWORD"
                 ldes1['text']=self.error

                 self.user=tk.Frame(self,width=30,bg=bgs1)
                 self.user.pack(fill=tk.BOTH,expand=tk.YES)

                 lname=tk.Label(self.user,width=20,bg=bgs2,text='NEW PASSWORD',font=f7)
                 lname.grid(row=0,column=0,padx=10,pady=20)

                 self.ename=tk.Entry(self.user,width=20,font=f7)
                 self.ename.grid(row=0,column=1,padx=10,pady=20)

                 lname1=tk.Label(self.user,width=20,bg=bgs2,text='CONFIRM !',font=f7)
                 lname1.grid(row=1,column=0,padx=10,pady=20)

                 self.ename1=tk.Entry(self.user,width=20,font=f7)
                 self.ename1.grid(row=1,column=1,padx=10,pady=20)

                 self.confirm=tk.Frame(self,width=30,bg=bgs1)
                 self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                 eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
                 eback.grid(row=0,column=0,padx=50,pady=15)

                 log=tk.Button(self.confirm,text='CONFIRM',fg='green',width=20,command=partial(check2,pid),font=f9)
                 log.grid(row=0,column=1,padx=60,pady=15)

            def check1():
                def back():
                     self.confirm.destroy()
                     self.des.destroy()
                     self.staff()

                def verify(otp,pid):
                    if otp==self.ename.get():
                        reset(pid)
                    else:
                        ldes1['text']='invalid OTP'

                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   pid=self.ename.get()
                   cur.execute("SELECT Email FROM medical_staff WHERE med_stf_id=?", (pid,))
                   rows = cur.fetchall()
                   otp=str(generateOTP())
                   res=send(rows[0][0],otp)
                   if res==1:
                     self.confirm.destroy()
                     ldes['text']='Enter the OTP'
                     lname['text']='OTP'
                     self.ename.delete(0,'end')
                     self.confirm=tk.Frame(self,width=30,bg=bgs1)
                     self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                     eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
                     eback.grid(row=0,column=0,padx=30,pady=15)

                     log=tk.Button(self.confirm,text='CHECK',fg='green',width=20,command=partial(verify,otp,pid),font=f9)
                     log.grid(row=0,column=1,padx=30,pady=15)

                     resend=tk.Button(self.confirm,text='RESEND',fg='blue',width=20,command=partial(forgot_pass),font=f9)
                     resend.grid(row=0,column=3,padx=30,pady=15)
                   else:
                     ldes1['text']='INVALID e-MAIL ID'
                except:
                    forgot_pass()




            self.confirm.destroy()
            self.user.destroy()
            self.des.destroy()

            self.title('RESET PASSWORD')

            self.des=tk.Frame(self,bg=bgs1)
            self.des.pack(fill=tk.BOTH,expand=tk.YES)

            ldes=tk.Label(self.des,bg=bgs3,fg='white',text='ENTER THE ID TO Get-OTP',font=f6)# enter the id to get otp
            ldes.pack(fill=tk.BOTH,expand=tk.YES)

            ldes1=tk.Label(self.des,bg=bgs1,text=self.error,fg='red',font=f3)
            ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            self.user=tk.Frame(self,width=30,bg=bgs1)
            self.user.pack(fill=tk.BOTH,expand=tk.YES)

            lname=tk.Label(self.user,width=20,bg=bgs2,text='STAFF ID',font=f7)
            lname.grid(row=0,column=0,padx=10,pady=20)

            self.ename=tk.Entry(self.user,width=20,font=f7)
            self.ename.grid(row=0,column=1,padx=10,pady=20)

            self.confirm=tk.Frame(self,width=30,bg=bgs1)
            self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
            eback.grid(row=0,column=0,padx=50,pady=15)

            log=tk.Button(self.confirm,text='Get-OTP',fg='green',width=20,command=partial(check1),font=f9)
            log.grid(row=0,column=1,padx=60,pady=15)


        def back():
            self.confirm.destroy()
            self.des.destroy()
            self.users()

        def verify():
            id1=ename.get()
            pass1=epass.get()
            self.conn = sqlite3.connect('medical.db')
            cur=self.conn.cursor()
            self.confirm.destroy()
            self.des.destroy()
            self.user.destroy()
            try:
                cur.execute("SELECT passwd FROM medical_staff where med_stf_id=?",(id1,))
                rows = cur.fetchall()
                if pass1==rows[0][0]:
                    print(rows)
                    profile(id1)
                    self.error=''
                else:
                   self.error='invalid pass'
                   self.staff()
            except:
                self.error='invalid id'
                self.staff()


        def profile(id1):
            self.error=''
            def admission(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def med():
                    aid=self.eproblem.get()
                    self.confirm.destroy()
                    self.des.destroy()
                    self.user.destroy()

                    self.conn = sqlite3.connect('medical.db')
                    cur=self.conn.cursor()
                    sql="SELECT i.med_id,m.Med_name from medicine m,issue i where i.med_id=m.Med_id and i.ad_id=?"
                    cur.execute(sql,(aid,))
                    row = cur.fetchall()
                    #row+=[('','')]
                    print(row)
                    self.i=0
                    self.rate=0
                    def done():
                      self.confirm.destroy()
                      self.des.destroy()
                      self.user.destroy()
                      try:
                        data=[no,self.rate,'completed',aid]
                        cur=self.conn.cursor()
                        sql="UPDATE admission set s_id=?,Med_fees=?,status=? where ad_id=?"
                        cur.execute(sql,data)
                        self.conn.commit()
                        admission(no)
                      except:
                          print('failed')
                          admission(no)


                    def summit():                       #                    price 

                        self.confirm.destroy()
                        self.des.destroy()
                        self.user.destroy()

                        self.des=tk.Frame(self,bg=bgs1)
                        self.des.pack(fill=tk.BOTH,expand=tk.YES)

                        ldes=tk.Label(self.des,bg=bgs3,text='TOTAL FEE',fg='white',font=f6)
                        ldes.pack(fill=tk.BOTH,expand=tk.YES)

                        ldes1=tk.Label(self.des,bg=bgs1,text=self.error,fg='red',font=f3)
                        ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                        self.user=tk.Frame(self,width=30,bg=bgs1)
                        self.user.pack(fill=tk.BOTH,expand=tk.YES)

                        lmid=tk.Label(self.user,width=20,bg=bgs2,text='TOTAL PRICE',font=f7)
                        lmid.grid(row=0,column=0,padx=10,pady=20)

                        emid=tk.Label(self.user,width=20,text=self.rate,font=f7)
                        emid.grid(row=0,column=1,padx=10,pady=20)

                        self.confirm=tk.Frame(self,width=30,bg=bgs1)
                        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back1),font=f9)
                        back.grid(row=0,column=0,padx=50,pady=15)

                        log=tk.Button(self.confirm,text='DONE',fg='green',width=20,command=partial(done),font=f9)
                        log.grid(row=0,column=1,padx=60,pady=15)



                    def next2():
                        qua=self.eq.get()

                        self.user.destroy()
                        self.confirm.destroy()
                        self.des.destroy()

                        cur=self.conn.cursor()
                        sql='SELECT Rate,Qty  from medicine where Med_id=?'
                        cur.execute(sql,(row[self.i][0],))
                        row1 = cur.fetchall()
                        nqua=int(row1[0][1])-int(qua)
                        print(nqua)
                        if nqua>=0:
                           p=int(row1[0][0])*int(qua)
                           data=[qua,p,aid,row[self.i][0]]
                           sql="UPDATE issue set qua=?,price=? where ad_id=? and med_id=?"
                           cur.execute(sql,data)
                           sql='UPDATE medicine set Qty=? where Med_id=?'
                           cur.execute(sql,(nqua,row[self.i][0]))
                           self.rate+=p
                           self.i+=1
                           self.error=''
                        elif int(row1[0][1]==0):
                           self.i+=1
                           self.error=''
                        else:
                            self.error='only '+str(row1[0][1])+' quantity available'
                        if self.i==len(row):
                            summit()
                        else:
                           next1()


                    def next1():

                        self.des=tk.Frame(self,bg=bgs1)
                        self.des.pack(fill=tk.BOTH,expand=tk.YES)

                        ldes=tk.Label(self.des,bg=bgs3,text='ISSUE MEDICINE',fg='white',font=f6)
                        ldes.pack(fill=tk.BOTH,expand=tk.YES)

                        ldes1=tk.Label(self.des,bg=bgs1,text=self.error,fg='red',font=f3)
                        ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                        self.user=tk.Frame(self,width=30,bg=bgs1)
                        self.user.pack(fill=tk.BOTH,expand=tk.YES)

                        lmid=tk.Label(self.user,width=20,bg=bgs2,text='MEDICINE ID',font=f7)
                        lmid.grid(row=0,column=0,padx=10,pady=20)

                        emid=tk.Label(self.user,width=20,text=row[self.i][0],font=f7)
                        emid.grid(row=0,column=1,padx=10,pady=20)

                        lmname=tk.Label(self.user,width=20,bg=bgs2,text='MEDICINE NAME',font=f7)
                        lmname.grid(row=1,column=0,padx=10,pady=20)

                        emname=tk.Label(self.user,width=20,text=row[self.i][1],font=f7)
                        emname.grid(row=1,column=1,padx=10,pady=20)

                        lq=tk.Label(self.user,width=20,bg=bgs2,text='QUANTITY',font=f7)
                        lq.grid(row=2,column=0,padx=10,pady=20)

                        self.eq=tk.Entry(self.user,width=20,font=f7)
                        self.eq.grid(row=2,column=1,padx=10,pady=20)

                        self.confirm=tk.Frame(self,width=30,bg=bgs1)
                        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back1),font=f9)
                        back.grid(row=0,column=0,padx=50,pady=15)

                        log=tk.Button(self.confirm,text='NEXT',fg='green',width=20,command=partial(next2),font=f9)
                        log.grid(row=0,column=1,padx=60,pady=15)


                    if self.i<len(row):
                        next1()
                    else:
                        summit()

                self.user.destroy()
                self.geometry(geo)
                # self.geometry("1500x1700")

                self.conn = sqlite3.connect('medical.db')
                cur=self.conn.cursor()
                sql="SELECT a.ad_id, p.patient_name from patient p,admission a where a.p_id=p.patient_id and a.status='stage2'"
                cur.execute(sql)
                row = cur.fetchall()
                print(row)

                self.des=tk.Frame(self,bg=bgs1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=bgs3,fg='white',text='CHOOSE THE PATIENT',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bgs1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bgs1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lproblem=tk.Label(self.user,width=20,bg=bgs2,text='ADMISSION ID',font=f7)
                lproblem.grid(row=0,column=0,padx=10,pady=20)

                self.eproblem=tk.Entry(self.user,width=20,font=f7)
                self.eproblem.grid(row=0,column=1,padx=10,pady=20)

                def get():
                     value=lt2.curselection()
                     value=int(value[0])
                     print (row[value][0])
                     if self.eproblem.get()!=None:
                        self.eproblem.delete(0,'end')
                     self.eproblem.insert(0,row[value][0])

                lt2=tk.Listbox(self.user,width=25,font=f10)
                lt2.grid(row=2,column=1,padx=0,pady=20)
                for i in range(len(row)):
                    lt2.insert(i,row[i][0]+'-'+row[i][1])

                log1=tk.Button(self.user,text='_SELECT_',fg='green',width=20,command=partial(get),font=f9)
                log1.grid(row=1,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=bgs1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='BACK',fg='red',width=16,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='NEXT',fg='green',width=16,command=partial(med),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)

            def edit_profile(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def summit():
                    self.confirm.destroy()
                    self.des.destroy()
                    try: # ---******----**** removed eblood.get() to eblood  variable 

                        data=[ename.get(),edob.get(),eblood,eph.get(),ephone.get(),no]
                        update_medical_staff(data)
                        back1()

                    except:
                        print("Failed")
                        self.error='error message'
                        edit_profile(no)

                self.user.destroy()
                self.geometry(geo)
                # self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=bgs1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                self.conn = sqlite3.connect('medical.db')
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM medical_staff WHERE med_stf_id=?", (no,))
                rows = cur.fetchall()
                rows=list(rows[0])

                for i in range(len(rows)):
                    if rows[i]==None:
                        rows[i]=''

                ldes=tk.Label(self.des,bg=bgs3,text='EDIT DETAILS',fg='white',font=f6) # edit details
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bgs1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bgs1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=bgs2,text='STAFF ID',font=f7)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=bgs2,text=no,font=f7)
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=bgs2,text='NAME',font=f7)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)
                ename.insert(0,rows[1])

                ldob=tk.Label(self.user,width=20,bg=bgs2,text='DATE OF BIRTH',font=f7)
                ldob.grid(row=2,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=2,column=1,padx=10,pady=20)
                edob.insert(0,rows[2])

                # lblood=tk.Label(self.user,width=20,bg=bgs2,text='SALARY',font=f7)
                # lblood.grid(row=3,column=0,padx=10,pady=20)

                # eblood=tk.Entry(self.user,width=20,font=f7)
                # eblood.grid(row=3,column=1,padx=10,pady=20)
                #eblood.insert(0,rows[3])
                eblood=rows[3] #*********** not an entry box 

                lph=tk.Label(self.user,width=20,bg=bgs2,text='PHONE NO:',font=f7)
                lph.grid(row=4,column=0,padx=10,pady=20)

                eph=tk.Entry(self.user,width=20,font=f7)
                eph.grid(row=4,column=1,padx=10,pady=20)
                eph.insert(0,rows[4])

                lphone=tk.Label(self.user,width=20,bg=bgs2,text='e-MAIL ID',font=f7)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)
                ephone.insert(0,rows[5])

                self.confirm=tk.Frame(self,width=30,bg=bgs1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',width=20,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',width=20,command=partial(summit),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)


            # self.geometry("1500x1700")
            self.geometry(geo)
            self.user.destroy()
            self.user=tk.Frame(self,bg=bgs1)
            self.user.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            self.data=tk.Frame(self.user,bg=bgs1)
            self.data.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            adm=tk.Frame(self.user,bg=bgs1)
            adm.pack(fill=tk.BOTH,side=tk.LEFT,expand=tk.YES)

            pre=tk.Label(adm,text='Hello  ',width=15,fg='white',bg=bgs1,font=f11)
            pre.grid(row=0,column=0,padx=10,pady=10)

            newadmi=tk.Button(adm,text='START ISSUE',width=20,fg='green',command=partial(admission,id1),font=f9)
            newadmi.grid(row=0,column=1,padx=10,pady=10)

            edit=tk.Button(adm,text='EDIT PROFILE',width=20,fg='green',command=partial(edit_profile,id1),font=f9)
            edit.grid(row=0,column=2,padx=10,pady=10)

            lname=tk.Label(self.data,text='STAFF ID   :',bg=bgs2,font=f7)
            lname.grid(row=0,column=0,padx=20,pady=10)

            cname=tk.Label(self.data,text=str(id1),bg=bgs2,font=f7)
            cname.grid(row=0,column=1,padx=20,pady=10)

            self.logout()

        self.user.destroy()

        self.des=tk.Frame(self,bg=bgs1)
        self.des.pack(fill=tk.BOTH,expand=tk.YES)

        ldes=tk.Label(self.des,bg=bgs1,text='ENTER VALID ID & PASSWORD',fg='white',font=f6)
        ldes.pack(fill=tk.BOTH,expand=tk.YES)

        self.user=tk.Frame(self,width=30,bg=bgs1)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        lname=tk.Label(self.user,width=20,bg=bgs2,text='STAFF ID',font=f7)
        lname.grid(row=0,column=0,padx=10,pady=20)

        ename=tk.Entry(self.user,width=20,font=f7)
        ename.grid(row=0,column=1,padx=10,pady=20)

        lpass=tk.Label(self.user,width=20,bg=bgs2,text='PASSWORD',font=f7)
        lpass.grid(row=2,column=0,padx=10,pady=20)

        epass=tk.Entry(self.user,width=20,font=f7)
        epass.grid(row=2,column=1,padx=10,pady=20)

        self.confirm=tk.Frame(self,width=30,bg=bgs1)
        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,font=f9,command=partial(back))
        back.grid(row=0,column=0,padx=50,pady=15)

        log=tk.Button(self.confirm,text='LOGIN',fg='green',width=20,font=f9,command=partial(verify))
        log.grid(row=0,column=1,padx=60,pady=15)

        forg=tk.Button(self.confirm,text='FORGOT PASSWORD',fg='red',width=20,font=f9,command=partial(forgot_pass))
        forg.grid(row=1,column=0,padx=50,pady=15)








#nurse --------------------------------------------------------------------------------------------------------------

    def nurse(self):
        # self.geometry("1500x1700")
        self.geometry(geo)
        self.title('NURSE PAGE  -----HOSPITAL MANAGEMENT SYSTEM')
        def forgot_pass():
            self.error=''
            def back():
                self.confirm.destroy()
                self.des.destroy()
                self.nurse()
            def check2(pid):
                p1=self.ename.get()
                p2=self.ename1.get()
                print(self.ename.get())
                print(self.ename1.get())
                print(self.ename.get()==self.ename1.get())
                if p1==p2:
                    try:
                        self.conn = sqlite3.connect('medical.db')
                        sql = 'UPDATE nurse SET passwd = ? WHERE nurse_id = ?'
                        cur = self.conn.cursor()
                        cur.execute(sql,(p1,pid))
                        self.conn.commit()
                        self.conn.close()
                        self.user.destroy()
                        self.des.destroy()
                        self.confirm.destroy()
                        self.nurse()
                    except:
                        self.error='ERROR'
                        reset(pid)
                else:
                    self.error='TRY AGAIN'
                    reset(pid)

            def reset(pid):
                 self.confirm.destroy()
                 self.user.destroy()

                 ldes['text']="RESET PASSWORD"
                 ldes1['text']=self.error

                 self.user=tk.Frame(self,width=30,bg=bgn1)
                 self.user.pack(fill=tk.BOTH,expand=tk.YES)

                 lname=tk.Label(self.user,width=20,bg=bgn2,text='NEW PASSWORD',font=f7)
                 lname.grid(row=0,column=0,padx=10,pady=20)

                 self.ename=tk.Entry(self.user,width=20,font=f7)
                 self.ename.grid(row=0,column=1,padx=10,pady=20)

                 lname1=tk.Label(self.user,width=20,bg=bgn2,text='CONFIRM !',font=f7)
                 lname1.grid(row=1,column=0,padx=10,pady=20)

                 self.ename1=tk.Entry(self.user,width=20,font=f7)
                 self.ename1.grid(row=1,column=1,padx=10,pady=20)

                 self.confirm=tk.Frame(self,width=30,bg=bgn1)
                 self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                 eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
                 eback.grid(row=0,column=0,padx=50,pady=15)

                 log=tk.Button(self.confirm,text='CONFIRM !',fg='green',width=20,command=partial(check2,pid),font=f9)
                 log.grid(row=0,column=1,padx=60,pady=15)

            def check1():
                def back():
                     self.confirm.destroy()
                     self.des.destroy()
                     self.nurse()

                def verify(otp,pid):
                    if otp==self.ename.get():
                        reset(pid)
                    else:
                        ldes1['text']='INVALID OTP'

                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   pid=self.ename.get()
                   cur.execute("SELECT Email FROM nurse WHERE nurse_id=?", (pid,))
                   rows = cur.fetchall()
                   otp=str(generateOTP())
                   res=send(rows[0][0],otp)
                   if res==1:
                     self.confirm.destroy()
                     ldes['text']='Enter the OTP'
                     lname['text']='OTP'
                     self.ename.delete(0,'end')
                     self.confirm=tk.Frame(self,width=30,bg=bgn1)
                     self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                     eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
                     eback.grid(row=0,column=0,padx=30,pady=15)

                     log=tk.Button(self.confirm,text='CHECK',fg='green',width=20,command=partial(verify,otp,pid),font=f9)
                     log.grid(row=0,column=1,padx=30,pady=15)

                     resend=tk.Button(self.confirm,text='RESEND',fg='blue',width=20,command=partial(forgot_pass),font=f9)
                     resend.grid(row=0,column=3,padx=30,pady=15)
                   else:
                     ldes1['text']='INVALID e-MAIL ID'
                except:
                    forgot_pass()




            self.confirm.destroy()
            self.user.destroy()
            self.des.destroy()

            self.title('RESET PASSWORD')

            self.des=tk.Frame(self,bg=bgn1)
            self.des.pack(fill=tk.BOTH,expand=tk.YES)

            ldes=tk.Label(self.des,bg=bgn3,fg='white',text='ENTER THE ID TO Get-OTP',font=f6)
            ldes.pack(fill=tk.BOTH,expand=tk.YES)

            ldes1=tk.Label(self.des,bg=bgn1,text=self.error,fg='red',font=f3)
            ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            self.user=tk.Frame(self,width=30,bg=bgn1)
            self.user.pack(fill=tk.BOTH,expand=tk.YES)

            lname=tk.Label(self.user,width=20,bg=bgn2,text='NURSE ID  :',font=f7)
            lname.grid(row=0,column=0,padx=10,pady=20)

            self.ename=tk.Entry(self.user,width=20,font=f7)
            self.ename.grid(row=0,column=1,padx=10,pady=20)

            self.confirm=tk.Frame(self,width=30,bg=bgn1)
            self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            eback=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
            eback.grid(row=0,column=0,padx=50,pady=15)

            log=tk.Button(self.confirm,text='Get-OTP',fg='green',width=20,command=partial(check1),font=f9)
            log.grid(row=0,column=1,padx=60,pady=15)

        def back():
            self.confirm.destroy()
            self.des.destroy()
            self.users()

        def verify():
            id1=ename.get()
            pass1=epass.get()
            self.conn = sqlite3.connect('medical.db')
            cur=self.conn.cursor()
            self.confirm.destroy()
            self.des.destroy()
            self.user.destroy()
            try:
                cur.execute("SELECT passwd FROM nurse where nurse_id=?",(id1,))
                rows = cur.fetchall()
                if pass1==rows[0][0]:
                    print(rows)
                    profile(id1)
                    self.error=''
                else:
                   self.error='INVALID PASSWORD'
                   self.nurse()
            except:
                self.error='Invalid id'
                self.nurse()

        def profile(id1):
            self.error=''

            def admission(no):

                def back1():
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)




                def next2():
                    print("yy2"+self.aid)
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()
                    try:
                        data=[no,'stage1',self.aid]
                        sql='update admission set n_id=?,status=? where ad_id=?'
                        print(self.aid)
                        cur=self.conn.cursor()
                        print(self.aid)
                        cur.execute(sql,data)
                        print(self.aid)
                        print('sucess')
                        self.conn.commit()
                        admission(no)
                    except:
                        print("failed")
                        admission(no)



                def med():
                    self.aid=self.eproblem.get()
                    next1()

                def next1():
                    print('yy11'+self.aid)
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()

                    self.des=tk.Frame(self,bg=bgn1)
                    self.des.pack(fill=tk.BOTH,expand=tk.YES)

                    ldes=tk.Label(self.des,bg=bgn3,fg='white',text='CONFIRM ADMISSION ID',font=f6)
                    ldes.pack(fill=tk.BOTH,expand=tk.YES)

                    self.user=tk.Frame(self,width=30,bg=bgn1)
                    self.user.pack(fill=tk.BOTH,expand=tk.YES)

                    lmed=tk.Label(self.user,width=20,bg=bgn2,text='ADMISSION ID',font=f7)
                    lmed.grid(row=0,column=0,padx=10,pady=20)

                    lmed1=tk.Label(self.user,width=20,bg=bgn2,text=self.aid,font=f7)
                    lmed1.grid(row=0,column=1,padx=10,pady=20)


                    self.confirm=tk.Frame(self,width=30,bg=bgn1)
                    self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                    back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back1),font=f9)
                    back.grid(row=0,column=0,padx=50,pady=15)

                    log=tk.Button(self.confirm,text='CONFIRM',fg='green',width=20,command=partial(next2),font=f9)
                    log.grid(row=0,column=1,padx=60,pady=15)




                self.user.destroy()
                self.geometry(geo)
                # self.geometry("1500x1700")

                today = date.today()
                d1 = today.strftime("%d-%m-%Y")

                self.conn = sqlite3.connect('medical.db')
                cur=self.conn.cursor()
                sql="SELECT a.ad_id, p.patient_name from patient p,admission a where a.p_id=p.patient_id and a.ad_date=? and a.status='stage0'"
                cur.execute(sql,(d1,))
                row = cur.fetchall()
                print(row)

                self.des=tk.Frame(self,bg=bgn1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=bgn3,text='CHOOSE PATIENT',fg='white',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bgn1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bgn1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lproblem=tk.Label(self.user,width=20,bg=bgn2,text='PATIENT ID',font=f7)
                lproblem.grid(row=0,column=0,padx=10,pady=20)

                self.eproblem=tk.Entry(self.user,width=20,font=f7)
                self.eproblem.grid(row=0,column=1,padx=10,pady=20)

                def get():
                     value=lt2.curselection()
                     value=int(value[0])
                     print (row[value][0])
                     if self.eproblem.get()!=None:
                        self.eproblem.delete(0,'end')
                     self.eproblem.insert(0,row[value][0])

                lt2=tk.Listbox(self.user,width=25,font=f10)
                lt2.grid(row=2,column=1,padx=0,pady=20)
                for i in range(len(row)):
                    lt2.insert(i,row[i][0]+'-'+row[i][1])

                log1=tk.Button(self.user,text='_SELECT_',fg='green',width=20,command=partial(get),font=f9)
                log1.grid(row=1,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=bgn1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='NEXT',fg='green',width=20,command=partial(med),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)



            def edit_profile(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def summit():
                    self.confirm.destroy()
                    self.des.destroy()
                    try:
                        data=[ename.get(),edob.get(),eblood.get(),eph.get(),ephone.get(),no]
                        update_nurse(data)
                        back1()

                    except:
                        print("Failed")
                        self.error='error message'
                        edit_profile(no)

                self.user.destroy()
                self.geometry(geo)
                # self.geometry("1500x1700")

                self.des=tk.Frame(self,bg=bgn1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                self.conn = sqlite3.connect('medical.db')
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM nurse WHERE nurse_id=?", (no,))
                rows = cur.fetchall()
                rows=list(rows[0])

                for i in range(len(rows)):
                    if rows[i]==None:
                        rows[i]=''

                ldes=tk.Label(self.des,bg=bgn3,fg='white',text='EDIT DETAILS',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bgn1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bgn1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=bgn2,text='NURSE ID',font=f7)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=bgn1,text=no,font=f7)
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=bgn2,text='NURSE NAME',font=f7)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)
                ename.insert(0,rows[1])

                ldob=tk.Label(self.user,width=20,bg=bgn2,text='DATE OF BIRTH',font=f7)
                ldob.grid(row=2,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=2,column=1,padx=10,pady=20)
                edob.insert(0,rows[2])

                lblood=tk.Label(self.user,width=20,bg=bgn2,text='SALARY',font=f7)
                lblood.grid(row=3,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=3,column=1,padx=10,pady=20)
                eblood.insert(0,rows[3])

                lph=tk.Label(self.user,width=20,bg=bgn2,text='CONTACT NUMBER',font=f7)
                lph.grid(row=4,column=0,padx=10,pady=20)

                eph=tk.Entry(self.user,width=20,font=f7)
                eph.grid(row=4,column=1,padx=10,pady=20)
                eph.insert(0,rows[4])

                lphone=tk.Label(self.user,width=20,bg=bgn2,text='e-MAIL ID',font=f7)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)
                ephone.insert(0,rows[5])

                self.confirm=tk.Frame(self,width=30,bg=bgn1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',width=20,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',width=20,command=partial(summit),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)




            # self.geometry("1500x1700")
            self.geometry(geo)
            self.user.destroy()
            self.user=tk.Frame(self,bg=bgn1)
            self.user.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            self.data=tk.Frame(self.user,bg=bgn1)
            self.data.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            adm=tk.Frame(self.user,bg=bgn1)
            adm.pack(fill=tk.BOTH,side=tk.LEFT,expand=tk.YES)

            pre=tk.Label(adm,text='Hello ',width=15,fg='white',bg=bgn1,font=f11)  # Hello
            pre.grid(row=0,column=0,padx=10,pady=10)

            newadmi=tk.Button(adm,text='NEW ADMISSION',width=20,fg='green',command=partial(admission,id1),font=f9)
            newadmi.grid(row=0,column=1,padx=10,pady=10)

            edit=tk.Button(adm,text='EDIT PROFILE',width=20,fg='green',command=partial(edit_profile,id1),font=f9)
            edit.grid(row=0,column=2,padx=10,pady=10)

            lname=tk.Label(self.data,text='NURSE ID  :',bg=bgn2,font=f7)
            lname.grid(row=0,column=0,padx=20,pady=10)

            cname=tk.Label(self.data,text=str(id1),bg=bgn2,font=f7)
            cname.grid(row=0,column=1,padx=20,pady=10)

            self.logout()

        self.user.destroy()

        self.des=tk.Frame(self,bg=bgn1)
        self.des.pack(fill=tk.BOTH,expand=tk.YES)

        ldes=tk.Label(self.des,bg=bgn1,fg='white',text='ENTER VALID ID & PASSWORD',font=f6)
        ldes.pack(fill=tk.BOTH,expand=tk.YES)

        self.user=tk.Frame(self,width=30,bg=bgn1)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        lname=tk.Label(self.user,width=20,bg=bgn2,text='NURSE ID',font=f7)
        lname.grid(row=0,column=0,padx=10,pady=20)

        ename=tk.Entry(self.user,width=20,font=f7)
        ename.grid(row=0,column=1,padx=10,pady=20)

        lpass=tk.Label(self.user,width=20,bg=bgn2,text='PASSWORD',font=f7)
        lpass.grid(row=2,column=0,padx=10,pady=20)

        epass=tk.Entry(self.user,width=20,font=f7)
        epass.grid(row=2,column=1,padx=10,pady=20)

        self.confirm=tk.Frame(self,width=30,bg=bgn1)
        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
        back.grid(row=0,column=0,padx=50,pady=15)

        log=tk.Button(self.confirm,text='LOGIN',fg='green',width=20,command=partial(verify),font=f9)
        log.grid(row=0,column=1,padx=60,pady=15)

        forg=tk.Button(self.confirm,text='FORGOT PASSWORD',fg='red',width=20,command=partial(forgot_pass),font=f9)
        forg.grid(row=1,column=0,padx=50,pady=15)




#patient ---------------------------------------------------------------------------------------------------------------

    def patient(self):
        # self.geometry("1500x1700")
        self.geometry(geo)
        self.title('PATIENT PAGE --- HOSPITAL MANAGEMENT SYSTEM')
        def forgot_pass():
            self.error=''
            def back():
                self.confirm.destroy()
                self.des.destroy()
                self.patient()
            def check2(pid):
                p1=self.ename.get()
                p2=self.ename1.get()
                print(self.ename.get())
                print(self.ename1.get())
                print(self.ename.get()==self.ename1.get())
                if p1==p2:
                    try:
                        self.conn = sqlite3.connect('medical.db')
                        sql = 'UPDATE patient SET passwd = ? WHERE patient_id = ?'
                        cur = self.conn.cursor()
                        cur.execute(sql,(p1,pid))
                        self.conn.commit()
                        self.conn.close()
                        self.user.destroy()
                        self.des.destroy()
                        self.confirm.destroy()
                        self.patient()
                    except:
                        self.error='error'
                        reset(pid)
                else:
                    self.error='try again'
                    reset(pid)

            def reset(pid):
                 self.confirm.destroy()
                 self.user.destroy()

                 ldes['text']="RESET PASSWORD"
                 ldes1['text']=self.error

                 self.user=tk.Frame(self,width=30,bg=bg3)
                 self.user.pack(fill=tk.BOTH,expand=tk.YES)

                 lname=tk.Label(self.user,width=20,bg=bg4,text='NEW PASSWORD',font=f7)
                 lname.grid(row=0,column=0,padx=10,pady=20)

                 self.ename=tk.Entry(self.user,width=20)
                 self.ename.grid(row=0,column=1,padx=10,pady=20)

                 lname1=tk.Label(self.user,width=20,bg=bg4,text='CONFIRM !',font=f7)
                 lname1.grid(row=1,column=0,padx=10,pady=20)

                 self.ename1=tk.Entry(self.user,width=20,font=f7)
                 self.ename1.grid(row=1,column=1,padx=10,pady=20)

                 self.confirm=tk.Frame(self,width=30,bg=bg3)
                 self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                 eback=tk.Button(self.confirm,text='BACK-',fg='red',width=20,command=partial(back),font=f9)
                 eback.grid(row=0,column=0,padx=50,pady=15)

                 log=tk.Button(self.confirm,text='CONFIRM',fg='green',width=20,command=partial(check2,pid),font=f9)
                 log.grid(row=0,column=1,padx=60,pady=15)

            def check1():
                def back():
                     self.confirm.destroy()
                     self.des.destroy()
                     self.patient()

                def verify(otp,pid):
                    if otp==self.ename.get():
                        reset(pid)
                    else:
                        ldes1['text']='INVALID OTP'

                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   pid=self.ename.get()
                   cur.execute("SELECT Email FROM patient WHERE patient_id=?", (pid,))
                   rows = cur.fetchall()
                   otp=str(generateOTP())
                   res=send(rows[0][0],otp)
                   if res==1:
                     self.confirm.destroy()
                     ldes['text']='ONE TIME PASSWORD | SINGLE USE CODE'
                     lname['text']='ENTER THE OTP'
                     self.ename.delete(0,'end')
                     self.confirm=tk.Frame(self,width=30,bg=bg3)
                     self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                     eback=tk.Button(self.confirm,text='BACK',fg='red',width=10,command=partial(back),font=f9)
                     eback.grid(row=0,column=0,padx=30,pady=15)

                     log=tk.Button(self.confirm,text='CHECK',fg='green',width=10,command=partial(verify,otp,pid),font=f7)
                     log.grid(row=0,column=1,padx=30,pady=15)

                     resend=tk.Button(self.confirm,text='RESEND',fg='blue',width=10,command=partial(forgot_pass),font=f7)
                     resend.grid(row=0,column=3,padx=30,pady=15)
                   else:
                     ldes1['text']='INVALID e-MAIL ID'
                except:
                    forgot_pass()




            self.confirm.destroy()
            self.user.destroy()
            self.des.destroy()

            self.title('PASSWORD RESET')

            self.des=tk.Frame(self,bg=bg3)
            self.des.pack(fill=tk.BOTH,expand=tk.YES)

            ldes=tk.Label(self.des,bg=bg3,text='ENTER THE ID TO Get-OTP',fg='white',font=f6)
            ldes.pack(fill=tk.BOTH,expand=tk.YES)

            ldes1=tk.Label(self.des,bg=bg3,text=self.error,fg='red',font=f3)
            ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            self.user=tk.Frame(self,width=30,bg=bg3)
            self.user.pack(fill=tk.BOTH,expand=tk.YES)

            lname=tk.Label(self.user,width=20,bg=bg4,text='PATIENT ID',font=f7)
            lname.grid(row=0,column=0,padx=10,pady=20)

            self.ename=tk.Entry(self.user,width=20,font=f7)
            self.ename.grid(row=0,column=1,padx=10,pady=20)

            self.confirm=tk.Frame(self,width=30,bg=bg3)
            self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            eback=tk.Button(self.confirm,text='BACK',fg='red',width=16,command=partial(back),font=f9)
            eback.grid(row=0,column=0,padx=50,pady=15)

            log=tk.Button(self.confirm,text='Get-OTP',fg='green',width=16,command=partial(check1),font=f9)
            log.grid(row=0,column=1,padx=60,pady=15)

        def back():
            self.confirm.destroy()
            self.des.destroy()
            self.users()

        def verify():
            id1=ename.get()
            pass1=epass.get()
            self.conn = sqlite3.connect('medical.db')
            cur=self.conn.cursor()
            self.confirm.destroy()
            self.des.destroy()
            self.user.destroy()
            try:
                cur.execute("SELECT passwd FROM patient where patient_id=?",(id1,))
                rows = cur.fetchall()
                if pass1==rows[0][0]:
                    print(rows)
                    profile(id1)
                    self.error=''
                else:
                   self.error='invalid pass'
                   self.patient()
            except:
                self.error='invalid id'
                self.patient()

        def profile(id1):
            self.error=''
            def admission(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def summit():
                    self.confirm.destroy()
                    self.des.destroy()
                    #try:
                    if True:
                         rows=0
                         try:
                             self.conn = sqlite3.connect('medical.db')
                             cur = self.conn.cursor()
                             cur.execute("SELECT count(*) FROM admission")
                             rows = cur.fetchall()
                             rows=int(rows[0][0])
                             print(rows)
                             # #l=len(rows[0][0])
                             # if int(rows)>=1:
                             #     rows=rows[0][0]
                             #     rows=int(rows[1:l])
                             # print(rows)
                         except:
                             rows=0
                         rows='A'+str(rows+1)
                         print('hi')
                         data=[rows,no,edoctor.get(),eproblem.get(),edate.get(),'stage0']
                         print(data)

                         if valid_admission1(data[4]):
                              print('good')
                              new_admission(data)
                              profile(no)
                         else:
                             self.error='error message1'
                             admission(no)
                    #except:
                    else:
                       self.error='error message'
                       admission(no)

                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)

                self.conn = sqlite3.connect('medical.db')
                cur=self.conn.cursor()
                sql='SELECT d.doctor_id, d.doctor_name,s.speciality from doctor d,doc_speciality s where d.doctor_id=s.doctor_id'
                cur.execute(sql)
                row = cur.fetchall()
                self.conn.close()
                print(row)

                self.des=tk.Frame(self,bg=bg3)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=bg5,fg='white',text='ENTER THE DETAILS OF AILEMENT',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bg3,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bg3)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lproblem=tk.Label(self.user,width=20,bg=bg4,text='AILMENT/DISEASE',font=f7)
                lproblem.grid(row=0,column=0,padx=10,pady=20)

                eproblem=tk.Entry(self.user,width=20,font=f7)
                eproblem.grid(row=0,column=1,padx=10,pady=20)

                ldoctor=tk.Label(self.user,width=20,bg=bg4,text='DOCTOR ID',font=f7)
                ldoctor.grid(row=1,column=0,padx=10,pady=20)

                edoctor=tk.Entry(self.user,width=20,font=f7)
                edoctor.grid(row=1,column=1,padx=10,pady=20)

                def get():
                     value=lt2.curselection()
                     value=int(value[0])
                     print (row[value][0])
                     if edoctor.get()!=None:
                        edoctor.delete(0,'end')
                     edoctor.insert(0,row[value][0])


                lt2=tk.Listbox(self.user,width=25,font=f10)
                lt2.grid(row=2,column=1,padx=0,pady=20)
                for i in range(len(row)):
                    lt2.insert(i,row[i][0]+'-'+row[i][1]+'-'+row[i][2])

                log1=tk.Button(self.user,text='_SELECT_',fg='green',width=20,command=partial(get),font=f9)
                log1.grid(row=3,column=1,padx=10,pady=20)

                today = date.today()
                d1 = today.strftime("%d-%m-%Y")

                ldate=tk.Label(self.user,width=20,bg=bg4,text='DATE',font=f7)
                ldate.grid(row=4,column=0,padx=10,pady=20)

                edate=tk.Entry(self.user,width=20,font=f7)
                edate.grid(row=4,column=1,padx=10,pady=20)
                edate.insert(0,d1)


                self.confirm=tk.Frame(self,width=30,bg=bg3)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',width=20,command=partial(summit),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)

            def edit_profile(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def summit():
                    self.confirm.destroy()
                    self.des.destroy()
                    try:
                        data=[ename.get(),edob.get(),eblood.get(),eph.get(),ephone.get(),no]
                        update_patient(data)
                        back1()

                    except:
                        print("Failed")
                        self.error='error message'
                        edit_profile(no)

                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)

                self.des=tk.Frame(self,bg=bg3)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                self.conn = sqlite3.connect('medical.db')
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM patient WHERE patient_id=?", (no,))
                rows = cur.fetchall()
                rows=list(rows[0])

                for i in range(len(rows)):
                    if rows[i]==None:
                        rows[i]=''

                ldes=tk.Label(self.des,bg=bg5,fg='white',text='EDIT DETAILS',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=bg3,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=bg3)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=bg4,text='PATIENT ID',font=f7)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=bg3,text=no,font=f7)
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=bg4,text='PATIENT NAME',font=f7)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)
                ename.insert(0,rows[1])

                ldob=tk.Label(self.user,width=20,bg=bg4,text='DATE OF BIRTH',font=f7)
                ldob.grid(row=2,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=2,column=1,padx=10,pady=20)
                edob.insert(0,rows[2])

                lblood=tk.Label(self.user,width=20,bg=bg4,text='BLOOD GROUP',font=f7)
                lblood.grid(row=3,column=0,padx=10,pady=20)

                eblood=tk.Entry(self.user,width=20,font=f7)
                eblood.grid(row=3,column=1,padx=10,pady=20)
                eblood.insert(0,rows[3])

                lph=tk.Label(self.user,width=20,bg=bg4,text='PHONE NUMBER',font=f7)
                lph.grid(row=4,column=0,padx=10,pady=20)

                eph=tk.Entry(self.user,width=20,font=f7)
                eph.grid(row=4,column=1,padx=10,pady=20)
                eph.insert(0,rows[4])

                lphone=tk.Label(self.user,width=20,bg=bg4,text='e-MAIL ID',font=f7)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)
                ephone.insert(0,rows[5])

                self.confirm=tk.Frame(self,width=30,bg=bg3)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',width=20,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',width=20,command=partial(summit),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)


            def details(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)


                def table(root,data):
                    def fun_cancel(i):
                         conn = sqlite3.connect('medical.db')
                         mycursor = conn.cursor()
                         data=['failed',i]
                         query= 'UPDATE admission set status=? where ad_id=?'
                         mycursor.execute(query,data)
                         conn.commit()
                         conn.close()
                         self.confirm.destroy()
                         self.des.destroy()
                         details(no)
                    row=len(data)
                    column=len(data[0])
                    cancel=[tk.Label(root,text='CANCEL',fg='red',bg=bg4,width=20,font=f7)]
                    cancel[0].grid(row=0,column=column,padx=50,pady=15) 
                    for i in range(row):
                        cancel+=[tk.Button(root,text='CANCEL',fg='red',font=f9,width=20,command=partial(fun_cancel,data[i][0]))]
                        cancel[i+1].grid(row=i+1,column=column,padx=50,pady=15) 
                        for j in range(column):
                            e=tk.Message(root, width=200,bg=root['bg'], font=f7) 
                            e.grid(row=i+1, column=j,padx=10,pady=10) 
                            if j==0:
                                e['text']=i+1           
                            else:
                                e['text']=data[i][j]



                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)

                self.conn = sqlite3.connect('medical.db')
                cur=self.conn.cursor()
                sql='SELECT a.ad_id,a.ad_date,d.doctor_name from doctor d,admission a where a.p_id=? and d.doctor_id=a.d_id and a.status not in (?,?) order by a.ad_date'
                cur.execute(sql,(no,'completed','failed'))
                details_list = cur.fetchall()
                self.conn.close()
                print(details_list)

                self.des=tk.Frame(self,bg=bg3,height=20)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=bg5,fg='white',text='YOUR HEALTH IS GOOD ',font=f6)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)


                self.user=tk.Frame(self,width=30,bg=bg3)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)


                if len(details_list)!=0:
                          ldes['text']="YOUR UPCOMMING ADMISSIONS"

                          sno=tk.Label(self.user,width=20,bg=bg4,text='S.NO',font=f7)
                          sno.grid(row=0,column=0,padx=10,pady=10)

                          ldate=tk.Label(self.user,width=20,bg=bg4,text='DATE',font=f7)
                          ldate.grid(row=0,column=1,padx=10,pady=10)

                          ldoctor=tk.Label(self.user,width=20,bg=bg4,text='DOCTOR',font=f7)
                          ldoctor.grid(row=0,column=2,padx=10,pady=10)

                          table(self.user,details_list)

                self.confirm=tk.Frame(self,width=30,bg=bg3)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='BACK',fg='red',width=16,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)




            # self.geometry("1500x1700")
            self.geometry(geo)
            self.user.destroy()
            self.user=tk.Frame(self,bg=bg3)
            self.user.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            self.data=tk.Frame(self.user,bg=bg3)
            self.data.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            adm=tk.Frame(self.user,bg=bg3)
            adm.pack(fill=tk.BOTH,side=tk.LEFT,expand=tk.YES)

            pre=tk.Button(adm,text='UPCOMING EVENTS',width=20,fg='green',command=partial(details,id1),font=f7)
            pre.grid(row=0,column=0,padx=10,pady=10)

            newadmi=tk.Button(adm,text='NEW ADMISSION',width=20,fg='green',command=partial(admission,id1),font=f7)
            newadmi.grid(row=0,column=1,padx=10,pady=10)

            edit=tk.Button(adm,text='EDIT PROFILE',width=20,fg='green',command=partial(edit_profile,id1),font=f7)
            edit.grid(row=0,column=2,padx=10,pady=10)

            lname=tk.Label(self.data,text='PATIENT ID  :',bg=bg4,font=f7)
            lname.grid(row=0,column=0,padx=20,pady=10)

            cname=tk.Label(self.data,text=str(id1),bg=bg4,font=f7)
            cname.grid(row=0,column=1,padx=20,pady=10)

            self.conn = sqlite3.connect('medical.db')
            sql = 'SELECT patient_name from patient WHERE patient_id = ?'
            cur = self.conn.cursor()
            cur.execute(sql,(str(id1),))
            rows = cur.fetchall()
            self.conn.close()

            lname1=tk.Label(self.data,text='PATIENT NAME  :',bg=bg4,font=f7)
            lname1.grid(row=1,column=0,padx=20,pady=10)

            cname1=tk.Label(self.data,text=rows[0][0],bg=bg4,font=f7)
            cname1.grid(row=1,column=1,padx=20,pady=10)

            self.logout()

        self.user.destroy()

        self.des=tk.Frame(self,bg=bg3)
        self.des.pack(fill=tk.BOTH,expand=tk.YES)

        ldes=tk.Label(self.des,bg=bg3,text='ENTER THE VALID ID & PASSWORD',fg='white',font=f6)
        ldes.pack(fill=tk.BOTH,expand=tk.YES)

        ldes1=tk.Label(self.des,bg=bg3,text='',fg='red')
        ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)
        try:
            ldes1['text']=self.error
        except:
            ldes1['text']=''
        self.user=tk.Frame(self,width=30,bg=bg3)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        lname=tk.Label(self.user,width=20,bg=bg4,text='PATIENT ID',font=f7)
        lname.grid(row=0,column=0,padx=10,pady=20)

        ename=tk.Entry(self.user,width=20,font=f7)
        ename.grid(row=0,column=1,padx=10,pady=20)

        lpass=tk.Label(self.user,width=20,bg=bg4,text='PASSWORD',font=f7)
        lpass.grid(row=2,column=0,padx=10,pady=20)

        epass=tk.Entry(self.user,width=20,font=f7)
        epass.grid(row=2,column=1,padx=10,pady=20)

        self.confirm=tk.Frame(self,width=30,bg=bg3)
        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
        back.grid(row=0,column=0,padx=50,pady=15)

        log=tk.Button(self.confirm,text='LOGIN',fg='green',width=20,command=partial(verify),font=f9)
        log.grid(row=0,column=1,padx=60,pady=15)

        forg=tk.Button(self.confirm,text='FORGOT PASSWORD',fg='red',width=20,command=partial(forgot_pass),font=f9)
        forg.grid(row=1,column=0,padx=50,pady=15)


#doctor-----------------------------------------------------------------------------------------------------------
    def doctor(self):
        # self.geometry("1500x1700")
        self.geometry(geo)
        self.title('Doctor Page --- HOSPITAL MANAGEMENT SYSTEM')
        def forgot_pass():
            self.error=''
            def back():
                self.confirm.destroy()
                self.des.destroy()
                self.doctor()
            def check2(pid):
                p1=self.ename.get()
                p2=self.ename1.get()
                print(self.ename.get())
                print(self.ename1.get())
                print(self.ename.get()==self.ename1.get())
                if p1==p2:
                    try:
                        self.conn = sqlite3.connect('medical.db')
                        sql = 'UPDATE doctor SET passwd = ? WHERE doctor_id = ?'
                        cur = self.conn.cursor()
                        cur.execute(sql,(p1,pid))
                        self.conn.commit()
                        self.conn.close()
                        self.user.destroy()
                        self.des.destroy()
                        self.confirm.destroy()
                        self.doctor()
                    except:
                        self.error='error'
                        reset(pid)
                else:
                    self.error='try again'
                    reset(pid)

            def reset(pid):
                 self.confirm.destroy()
                 self.user.destroy()

                 ldes['text']="RESET PASSWORD"
                 ldes1['text']=self.error

                 self.user=tk.Frame(self,width=30,bg=z1)
                 self.user.pack(fill=tk.BOTH,expand=tk.YES)

                 lname=tk.Label(self.user,width=20,bg=w5,text='NEW PASSWORD',font=f7)
                 lname.grid(row=0,column=0,padx=10,pady=20)

                 self.ename=tk.Entry(self.user,width=20,font=f7)
                 self.ename.grid(row=0,column=1,padx=10,pady=20)

                 lname1=tk.Label(self.user,width=20,bg=w5,text='RE-ENTER PASSWORD',font=f7)
                 lname1.grid(row=1,column=0,padx=10,pady=20)

                 self.ename1=tk.Entry(self.user,width=20,font=f7)
                 self.ename1.grid(row=1,column=1,padx=10,pady=20)

                 self.confirm=tk.Frame(self,width=30,bg=z1)
                 self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                 eback=tk.Button(self.confirm,text='BACK',fg='red',width=16,font=f9,command=partial(back))
                 eback.grid(row=0,column=0,padx=50,pady=15)

                 log=tk.Button(self.confirm,text='CONFIRM!',fg='green',font=f9,width=16,command=partial(check2,pid))
                 log.grid(row=0,column=1,padx=60,pady=15)

            def check1():
                def back():
                     self.confirm.destroy()
                     self.des.destroy()
                     self.doctor()

                def verify(otp,pid):
                    if otp==self.ename.get():
                        reset(pid)
                    else:
                        ldes1['text']='INVALID OTP'

                try:
                   self.conn = sqlite3.connect('medical.db')
                   cur = self.conn.cursor()
                   pid=self.ename.get()
                   cur.execute("SELECT Email FROM doctor WHERE doctor_id=?", (pid,))
                   rows = cur.fetchall()
                   otp=str(generateOTP())
                   res=send(rows[0][0],otp)
                   if res==1:
                     self.confirm.destroy()
                     ldes['text']='ONE TIME PASSWORD | SINGLE USE CODE'
                     lname['text']='ENTER THE OTP'
                     self.ename.delete(0,'end')
                     self.confirm=tk.Frame(self,width=30,bg=z1)
                     self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                     eback=tk.Button(self.confirm,text='BACK',fg='red',width=10,font=f9,command=partial(back))
                     eback.grid(row=0,column=0,padx=30,pady=15)

                     log=tk.Button(self.confirm,text='CHECK',fg='green',width=10,font=f9,command=partial(verify,otp,pid))
                     log.grid(row=0,column=1,padx=30,pady=15)

                     resend=tk.Button(self.confirm,text='RESEND',fg='blue',width=10,font=f9,command=partial(forgot_pass))
                     resend.grid(row=0,column=3,padx=30,pady=15)
                   else:
                     print("Good")
                     ldes1['text']='INVALID e-MAIL ID'
                except:
                    print("Error")
                    forgot_pass()




            self.confirm.destroy()
            self.user.destroy()
            self.des.destroy()

            self.des=tk.Frame(self,bg=z1)
            self.des.pack(fill=tk.BOTH,expand=tk.YES)

            ldes=tk.Label(self.des,bg=z2,text='ENTER ID TO Get-OTP!',font=f6,fg=c1)
            ldes.pack(fill=tk.BOTH,expand=tk.YES)

            ldes1=tk.Label(self.des,bg=z1,text=self.error,fg='red',font=f3)
            ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            self.user=tk.Frame(self,width=30,bg=z1)
            self.user.pack(fill=tk.BOTH,expand=tk.YES)

            lname=tk.Label(self.user,width=20,bg=w5,text='DOCTOR ID',font=f7)
            lname.grid(row=0,column=0,padx=10,pady=20)

            self.ename=tk.Entry(self.user,width=20,font=f7)
            self.ename.grid(row=0,column=1,padx=10,pady=20)

            self.confirm=tk.Frame(self,width=30,bg=z1)
            self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

            eback=tk.Button(self.confirm,text='BACK',fg='red',font=f9,width=16,command=partial(back))
            eback.grid(row=0,column=0,padx=50,pady=15)

            log=tk.Button(self.confirm,text='Get-OTP',fg='green',font=f9,width=16,command=partial(check1))
            log.grid(row=0,column=1,padx=60,pady=15)

        def back():
            self.confirm.destroy()
            self.des.destroy()
            self.users()

        def verify():
            id1=ename.get()
            pass1=epass.get()
            self.conn = sqlite3.connect('medical.db')
            cur=self.conn.cursor()
            self.confirm.destroy()
            self.des.destroy()
            self.user.destroy()
            try:
                cur.execute("SELECT passwd FROM doctor where doctor_id=?",(id1,))
                rows = cur.fetchall()
                print(rows)
                if pass1==rows[0][0]:
                    profile(id1)
                    self.error=''
                else:
                   self.error='invalid pass'
                   self.doctor()
            except:
                self.error='invalid id'
                self.doctor()


        def profile(id1):
            self.error=''
            def admission(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def done():
                    try:
                         print("yy"+self.aid)
                         data=[self.emed.get(),'stage2',self.aid]
                         print(data)
                         sql='UPDATE admission set doc_fees=?,status=? where  ad_id=?'
                         cur=self.conn.cursor()
                         cur.execute(sql,data)
                         self.conn.commit()
                         self.user.destroy()
                         self.confirm.destroy()
                         self.des.destroy()
                         admission(no)
                    except:
                    #else:
                       self.user.destroy()
                       self.confirm.destroy()
                       self.des.destroy()
                       self.error='error message'
                       admission(no)

                def summit():
                    print("yy1"+self.aid)
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()

                    self.des=tk.Frame(self,bg=z1)
                    self.des.pack(fill=tk.BOTH,expand=tk.YES)

                    ldes=tk.Label(self.des,bg=z2,text='DOCTOR FEE OF THE PATIENT',font=f6,fg=c1)
                    ldes.pack(fill=tk.BOTH,expand=tk.YES)

                    self.user=tk.Frame(self,width=30,bg=z1)
                    self.user.pack(fill=tk.BOTH,expand=tk.YES)

                    lmed=tk.Label(self.user,width=20,bg=w5,text='DOCTOR FEE (IN Rupees)',font=f7)
                    lmed.grid(row=0,column=0,padx=10,pady=20)

                    self.emed=tk.Entry(self.user,width=20,font=f7)
                    self.emed.grid(row=0,column=1,padx=10,pady=20)

                    self.confirm=tk.Frame(self,width=30,bg=z1)
                    self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                    log=tk.Button(self.confirm,text='FINISH|COMPLETE',fg='green',font=f9,width=20,command=partial(done))
                    log.grid(row=0,column=1,padx=50,pady=15)

                    def again():
                       self.user.destroy()
                       self.confirm.destroy()
                       self.des.destroy()
                       self.error='error message'
                       admission(no)

                    back=tk.Button(self.confirm,text='CANCEL',fg='red',font=f9,width=16,command=partial(again))
                    back.grid(row=0,column=0,padx=50,pady=15)


                def next2():
                    print("yy2"+self.aid)
                    mid=self.emed.get()
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()
                    try:
                        data=[self.aid,mid]
                        sql='insert into issue(ad_id,med_id) values(?,?)'
                        print(self.aid,mid)
                        cur=self.conn.cursor()
                        print(self.aid,mid)
                        cur.execute(sql,data)
                        print(self.aid,mid)
                        print('success')
                        next1()
                    except:
                        next1()



                def med():
                    self.aid=self.eproblem.get()
                    next1()

                def next1():
                    print('yy11'+self.aid)
                    self.user.destroy()
                    self.confirm.destroy()
                    self.des.destroy()

                    self.des=tk.Frame(self,bg=z1)
                    self.des.pack(fill=tk.BOTH,expand=tk.YES)

                    ldes=tk.Label(self.des,bg=z2,text='PRESCRIPTION|TREATMENT',font=f6,fg=c1)
                    ldes.pack(fill=tk.BOTH,expand=tk.YES)

                    self.user=tk.Frame(self,width=30,bg=z1)
                    self.user.pack(fill=tk.BOTH,expand=tk.YES)

                    lmed=tk.Label(self.user,width=20,bg=w5,text='MEDICINE ID',font=f7)
                    lmed.grid(row=0,column=0,padx=10,pady=20)

                    self.emed=tk.Entry(self.user,width=20,font=f7)
                    self.emed.grid(row=0,column=1,padx=10,pady=20)

                    cur=self.conn.cursor()
                    sql='SELECT Med_id,Med_name from medicine'
                    cur.execute(sql)
                    row = cur.fetchall()
                    print(row)

                    def get():
                         value=lt2.curselection()
                         value=int(value[0])
                         print (row[value][0])
                         if self.emed.get()!=None:
                              self.emed.delete(0,'end')
                         self.emed.insert(0,row[value][0])


                    lt2=tk.Listbox(self.user,width=25,font=f10)
                    lt2.grid(row=2,column=1,padx=0,pady=20)
                    for i in range(len(row)):
                         lt2.insert(i,row[i][0]+'-'+row[i][1])

                    log1=tk.Button(self.user,text='_SELECT_',fg='green',font=f9,width=20,command=partial(get))
                    log1.grid(row=1,column=1,padx=10,pady=20)

                    self.confirm=tk.Frame(self,width=30,bg=z1)
                    self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                    back=tk.Button(self.confirm,text='BACK',fg='red',font=f9,width=16,command=partial(back1))
                    back.grid(row=0,column=0,padx=50,pady=15)

                    log=tk.Button(self.confirm,text='NEXT MEDICINE',fg='green',font=f9,width=16,command=partial(next2))
                    log.grid(row=0,column=1,padx=60,pady=15)

                    log2=tk.Button(self.confirm,text='COMPLETE!',fg='green',width=16,font=f9,command=partial(summit))
                    log2.grid(row=1,column=1,padx=60,pady=15)




                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)

                self.conn = sqlite3.connect('medical.db')
                cur=self.conn.cursor()
                sql="select a.ad_id, p.patient_name,a.condition from patient p,admission a where a.p_id=p.patient_id and a.d_id=? and a.status='stage1'"
                cur.execute(sql,(no,))
                row = cur.fetchall()
                print(row)

                self.des=tk.Frame(self,bg=z1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                ldes=tk.Label(self.des,bg=z2,text='CHOOSE PATIENT',font="Times 18 bold underline",fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=z1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=z1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lproblem=tk.Label(self.user,width=20,bg=w5,text='PATIENT ID',font=f7)
                lproblem.grid(row=0,column=0,padx=10,pady=20)

                self.eproblem=tk.Entry(self.user,width=20,font=f7)
                self.eproblem.grid(row=0,column=1,padx=10,pady=20)

                def get():
                     value=lt2.curselection()
                     value=int(value[0])
                     print (row[value][0])
                     if self.eproblem.get()!=None:
                        self.eproblem.delete(0,'end')
                     self.eproblem.insert(0,row[value][0])

                lt2=tk.Listbox(self.user,width=25,font=f10)
                lt2.grid(row=2,column=1,padx=0,pady=20)
                for i in range(len(row)):
                    lt2.insert(i,row[i][0]+'-'+row[i][1]+'-'+row[i][2])

                log1=tk.Button(self.user,text='_SELECT_',fg='green',font=f9,width=20,command=partial(get))
                log1.grid(row=1,column=1,padx=10,pady=20)

                self.confirm=tk.Frame(self,width=30,bg=z1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='BACK',fg='red',font=f9,width=16,command=partial(back1))
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='NEXT',fg='green',font=f9,width=16,command=partial(med))
                log.grid(row=0,column=1,padx=60,pady=15)

            def edit_profile(no):

                def back1():
                    self.confirm.destroy()
                    self.des.destroy()
                    profile(no)

                def summit():
                    self.confirm.destroy()
                    self.des.destroy()
                    #try:
                    if True:
                        data=[ename.get(),edob.get(),eph.get(),ephone.get(),str(no)]
                        update_doctor(data)
                        back1()

                    #except:
                    else:
                        print("failed")
                        self.error='error message'
                        edit_profile(no)

                self.user.destroy()
                # self.geometry("1500x1700")
                self.geometry(geo)

                self.des=tk.Frame(self,bg=z1)
                self.des.pack(fill=tk.BOTH,expand=tk.YES)

                self.conn = sqlite3.connect('medical.db')
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM doctor WHERE doctor_id=?", (no,))
                rows = cur.fetchall()
                rows=list(rows[0])

                for i in range(len(rows)):
                    if rows[i]==None:
                        rows[i]=''

                ldes=tk.Label(self.des,bg=z2,text='EDIT DETAILS',font='Times 18 bold underline',fg=c1)
                ldes.pack(fill=tk.BOTH,expand=tk.YES)

                ldes1=tk.Label(self.des,bg=z1,text=self.error,fg='red',font=f3)
                ldes1.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                self.user=tk.Frame(self,width=30,bg=z1)
                self.user.pack(fill=tk.BOTH,expand=tk.YES)

                lid=tk.Label(self.user,width=20,bg=w5,text='DOCTOR ID',font=f7)
                lid.grid(row=0,column=0,padx=10,pady=20)

                eid=tk.Label(self.user,width=20,bg=z1,text=no,font=f7)
                eid.grid(row=0,column=1,padx=10,pady=20)

                lname=tk.Label(self.user,width=20,bg=w5,text='DOCTOR NAME',font=f7)
                lname.grid(row=1,column=0,padx=10,pady=20)

                ename=tk.Entry(self.user,width=20,font=f7)
                ename.grid(row=1,column=1,padx=10,pady=20)
                ename.insert(0,rows[1])

                ldob=tk.Label(self.user,width=20,bg=w5,text='DATE OF BIRTH',font=f7)
                ldob.grid(row=2,column=0,padx=10,pady=20)

                edob=tk.Entry(self.user,width=20,font=f7)
                edob.grid(row=2,column=1,padx=10,pady=20)
                edob.insert(0,rows[2])

                lph=tk.Label(self.user,width=20,bg=w5,text='CONTACT NUMBER',font=f7)
                lph.grid(row=4,column=0,padx=10,pady=20)

                eph=tk.Entry(self.user,width=20,font=f7)
                eph.grid(row=4,column=1,padx=10,pady=20)
                eph.insert(0,rows[4])

                lphone=tk.Label(self.user,width=20,bg=w5,text='e-MAIL ID',font=f7)
                lphone.grid(row=5,column=0,padx=10,pady=20)

                ephone=tk.Entry(self.user,width=20,font=f7)
                ephone.grid(row=5,column=1,padx=10,pady=20)
                ephone.insert(0,rows[5])

                self.confirm=tk.Frame(self,width=30,bg=z1)
                self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

                back=tk.Button(self.confirm,text='CANCEL',fg='red',width=16,command=partial(back1),font=f9)
                back.grid(row=0,column=0,padx=50,pady=15)

                log=tk.Button(self.confirm,text='SUBMIT',fg='green',width=16,command=partial(summit),font=f9)
                log.grid(row=0,column=1,padx=60,pady=15)




            # self.geometry("1500x1700")
            self.geometry(geo)
            self.user.destroy()
            self.user=tk.Frame(self,bg=q4)
            self.user.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            self.data=tk.Frame(self.user,bg=q4)
            self.data.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=tk.YES)

            adm=tk.Frame(self.user,bg=q4)
            adm.pack(fill=tk.BOTH,side=tk.LEFT,expand=tk.YES)

            pre=tk.Label(adm,text='WELCOME! DOCTOR, HAVE A GREAT DAY!!',width=40,fg=c1,font=f7,bg=q4)
            pre.grid(row=0,column=0,padx=10,pady=10)

            newadmi=tk.Button(adm,text='CASES-TODAY',width=20,font=f7,fg=c1,bg="coral",command=partial(admission,id1))
            newadmi.grid(row=0,column=1,padx=10,pady=10)

            edit=tk.Button(adm,text='EDIT MY PROFILE',width=15,font=f7,fg=c1,bg="coral",command=partial(edit_profile,id1))
            edit.grid(row=0,column=2,padx=10,pady=10)

            self.conn = sqlite3.connect('medical.db')
            cur = self.conn.cursor()
            cur.execute("SELECT doctor_name FROM doctor WHERE doctor_id=?", (str(id1),))
            rows = cur.fetchall()
            rows=list(rows[0])


            lname=tk.Label(self.data,text='DOCTOR ID',bg=w5,font=f7)
            lname.grid(row=0,column=0,padx=20,pady=10)

            cname=tk.Label(self.data,text=str(id1),bg=w5,font=f7)
            cname.grid(row=0,column=1,padx=20,pady=10)

            lname1=tk.Label(self.data,text='DOCTOR NAME',bg=w5,font=f7)
            lname1.grid(row=1,column=0,padx=20,pady=10)

            cname1=tk.Label(self.data,text=str(rows[0]),bg=w5,font=f7)
            cname1.grid(row=1,column=1,padx=20,pady=10)

            self.logout()

        self.user.destroy()

        self.des=tk.Frame(self,bg=q7)
        self.des.pack(fill=tk.BOTH,expand=tk.YES)

        ldes=tk.Label(self.des,bg=q4,text='LOGIN - ENTER VALID ID & PASSWORD!',fg=c1,font='Times 18 bold underline')
        ldes.pack(fill=tk.BOTH,expand=tk.YES)

        self.user=tk.Frame(self,width=30,bg=q4)
        self.user.pack(fill=tk.BOTH,expand=tk.YES)

        lname=tk.Label(self.user,width=20,bg=w5,text='DOCTOR ID',font=f7)
        lname.grid(row=0,column=0,padx=10,pady=20)

        ename=tk.Entry(self.user,width=20,font=f7)
        ename.grid(row=0,column=1,padx=10,pady=20)

        lpass=tk.Label(self.user,width=20,bg=w5,text='PASSWORD',font=f7)
        lpass.grid(row=2,column=0,padx=10,pady=20)

        epass=tk.Entry(self.user,width=20,font=f7)
        epass.grid(row=2,column=1,padx=10,pady=20)

        self.confirm=tk.Frame(self,width=30,bg=q4)
        self.confirm.pack(fill=tk.BOTH,expand=tk.YES,side=tk.BOTTOM)

        back=tk.Button(self.confirm,text='BACK',fg='red',width=20,command=partial(back),font=f9)
        back.grid(row=0,column=0,padx=50,pady=15)

        log=tk.Button(self.confirm,text='LOGIN',fg='green',width=20,command=partial(verify),font=f9)
        log.grid(row=0,column=1,padx=60,pady=15)

        forg=tk.Button(self.confirm,text='FORGOT PASSWORD',fg='red',width=20,command=partial(forgot_pass),font=f9)
        forg.grid(row=1,column=0,padx=50,pady=15)

def referesh():
     today = date.today()
     d1 = today.strftime("%d-%m-%Y")
     print("d1 =", d1)
     conn = sqlite3.connect('medical.db')
     cur=conn.cursor()
     data=['failed',d1]
     sql="UPDATE admission set status=? where ad_date < ? and status not in ('failed','completed')"
     if '17-05-2020'<d1:
         print("hh")
     cur.execute(sql,data)
     conn.commit()
     conn.close()

if __name__ == "__main__":
    referesh()
    app1=app()
    app1.mainloop()
