from tkinter import *
import time
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3
import re

try:
    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute('create table acn(acn_no integer primary key autoincrement,acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,acn_opendate text,acn_gender text)')
    conobj.close()
    print('table created')

except:
    print('Something went wrong, might be already exist')

    
win=Tk()
win.state('zoomed')
win.configure(bg='orange')
win.resizable(width=False,height=False)
title=Label(win,text='Banking Automation',font=('arial',50,'bold','underline'),bg='orange')
title.pack()

dt=time.strftime('%d %b %Y,%A')
date=Label(win,text=f'{dt}',font=('arial',20,'bold','underline'),bg='orange')
date.place(relx=0.75,rely=0.12)

name=Label(win,text='By Anusheel Mishra',font=('arial',20,'underline','bold'),bg='orange')
name.place(relx=0,rely=0.12)
def main_screen():
    frm=Frame(win)
    frm.configure(bg='light blue')
    frm.place(relx=0,rely=0.18,relwidth=1,relheight=0.82)

    def forgotpass():
        frm.destroy()
        forgotpass_screen()

    def newuser():
        frm.destroy()
        newuser_screen()

    def login():
        global gacn
        gacn=e_acn.get()
        pwd=e_pass.get()
        if len(gacn)==0 or len(pwd)==0:
            messagebox.showwarning('Validation','Empty fields are not allowed')
            return

        else:
            acn=e_acn.get()
            pwd=e_pass.get()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select * from acn where acn_no=? and acn_pass=?',(acn,pwd))
            tup=curobj.fetchone()
            conobj.close()

            if tup==None:
                messagebox.showerror('Login','Invalid ACN/PASS')

            else:
                frm.destroy()
                welcome_screen()

    def clear():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')

    
    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='light blue')
    lbl_acn.place(relx=0.3,rely=0.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=0.4,rely=0.1)
    e_acn.focus()

    lbl_pass=Label(frm,text='PASS',font=('arial',20,'bold'),bg='light blue')
    lbl_pass.place(relx=0.3,rely=0.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_pass.place(relx=0.4,rely=0.2)


    btn_login=Button(frm,command=login,text='Login',font=('arial',20,'bold'),bd=5)
    btn_login.place(relx=0.43,rely=0.3)

    btn_clear=Button(frm,command=clear,text='Clear',font=('arial',20,'bold'),bd=5)
    btn_clear.place(relx=0.53,rely=0.3)

    btn_fp=Button(frm,command=forgotpass,text='Forgot Password',font=('arial',20,'bold'),bd=5)
    btn_fp.place(relx=0.424,rely=0.42)

    btn_new=Button(frm,command=newuser,text='Open New Account',font=('arial',20,'bold'),bd=5)
    btn_new.place(relx=0.418,rely=0.54)


def forgotpass_screen():
    frm=Frame(win)
    frm.configure(bg='light blue')
    frm.place(relx=0,rely=0.18,relwidth=1,relheight=0.82)

    def back():
        frm.destroy()
        main_screen()

    def clear():
        e_acn.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')

    def forgotpass_db():
        acn=e_acn.get()
        email=e_email.get()
        mob=e_mob.get()

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select acn_pass from acn where acn_no=? and acn_email=? and acn_mob=?',(acn,email,mob))
        tup=curobj.fetchone()
        if tup==None:
            messagebox.showerror('Forgot Pass','Record not found')
        else:
            messagebox.showinfo('Forgot Pass',f'Your pass={tup[0]}')

        conobj.close()

        
    btn_back=Button(frm,command=back,text='Back',font=('arial',20,'bold'),bd=5)
    btn_back.place(relx=0,rely=0.0)

    lbl_acn=Label(frm,text='ACN',font=('arial',20,'bold'),bg='light blue')
    lbl_acn.place(relx=0.3,rely=0.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=0.4,rely=0.1)
    e_acn.focus()

    lbl_email=Label(frm,text='EMAIL',font=('arial',20,'bold'),bg='light blue')
    lbl_email.place(relx=0.3,rely=0.2)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=0.4,rely=0.2)

    lbl_mob=Label(frm,text='MOB',font=('arial',20,'bold'),bg='light blue')
    lbl_mob.place(relx=0.3,rely=0.3)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=0.4,rely=0.3)

    btn_sub=Button(frm,command=forgotpass_db,text='SUBMIT',font=('arial',20,'bold'),bd=5)
    btn_sub.place(relx=0.4,rely=0.4)

    btn_clear=Button(frm,command=clear,text='CLEAR',font=('arial',20,'bold'),bd=5)
    btn_clear.place(relx=0.53,rely=00.4)


def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='light blue')
    frm.place(relx=0,rely=0.18,relwidth=1,relheight=0.82)

    def back():
        frm.destroy()
        main_screen()

    def clear():
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        cb_gender.delete(0,'end')

    def newuser_db():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        gender=cb_gender.get()
        bal=0
        opendate=time.strftime('%d %b %Y,%A')

       
        match=re.fullmatch('[6-9][0-9]{9}',mob)
        if match==None:
           messagebox.showerror('Validation','Invalid format of mob')
           return

        match=re.fullmatch('[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+',email)
        if match==None:
           messagebox.showerror('Validation','Invalid format of email')
           return
        
        


        import sqlite3

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('insert into acn(acn_name,acn_pass,acn_email,acn_mob,acn_gender,acn_opendate,acn_bal)values(?,?,?,?,?,?,?)',(name,pwd,email,mob,gender,opendate,bal))
        conobj.commit()
        conobj.close()


        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select max(acn_no) from acn')
        tup=curobj.fetchone()
        #print(tup)
        conobj.commit()
        conobj.close()
        
        messagebox.showinfo('New User',f'Account Created Successfully with ACN NO.={tup[0]}')
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        
        

        
    btn_back=Button(frm,command=back,text='Back',font=('arial',20,'bold'),bd=5)
    btn_back.place(relx=0,rely=0.0)

    lbl_name=Label(frm,text='NAME',font=('arial',20,'bold'),bg='light blue')
    lbl_name.place(relx=0.3,rely=0.1)

    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=0.4,rely=0.1)
    e_name.focus()

    lbl_pass=Label(frm,text='PASS',font=('arial',20,'bold'),bg='light blue')
    lbl_pass.place(relx=0.3,rely=0.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_pass.place(relx=0.4,rely=0.2)

    lbl_email=Label(frm,text='EMAIL',font=('arial',20,'bold'),bg='light blue')
    lbl_email.place(relx=0.3,rely=0.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=0.4,rely=0.3)

    lbl_mob=Label(frm,text='MOB',font=('arial',20,'bold'),bg='light blue')
    lbl_mob.place(relx=0.3,rely=0.4)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=0.4,rely=0.4)

    lbl_gender=Label(frm,text='GENDER',font=('arial',20,'bold'),bg='light blue')
    lbl_gender.place(relx=0.3,rely=0.5)

    cb_gender=Combobox(frm,values=['--------select-------','Male','Female'],font=('arial',20,'bold'))
    cb_gender.place(relx=0.4,rely=0.5)
    
    btn_sub=Button(frm,command=newuser_db,text='SUBMIT',font=('arial',20,'bold'),bd=5)
    btn_sub.place(relx=0.4,rely=0.6)

    btn_clear=Button(frm,command=clear,text='CLEAR',font=('arial',20,'bold'),bd=5)
    btn_clear.place(relx=0.53,rely=0.6)

def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='light blue')
    frm.place(relx=0,rely=0.18,relwidth=1,relheight=0.82)

    def logout():
        frm.destroy()
        main_screen()

    def details():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=0.3,rely=0.17,relwidth=0.5,relheight=0.55)

        lbl_details=Label(ifrm,text='This is Details Screen',font=('arial',20,'bold'),bg='white',fg='Blue')
        lbl_details.pack()

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select acn_opendate,acn_bal,acn_gender,acn_email,acn_mob from acn where acn_no=?',(gacn,))
        tup=curobj.fetchone()
        conobj.close()

        lbl_opendate=Label(ifrm,text=f'Open Date: {tup[0]}',font=('arial',15,'bold'),bg='white')
        lbl_opendate.place(relx=0.1,rely=0.15)

        lbl_bal=Label(ifrm,text=f'Bal: {tup[1]}',font=('arial',15,'bold'),bg='white')
        lbl_bal.place(relx=0.1,rely=0.25)

        lbl_gender=Label(ifrm,text=f'Gender: {tup[2]}',font=('arial',15,'bold'),bg='white')
        lbl_gender.place(relx=0.1,rely=0.35)

        lbl_email=Label(ifrm,text=f'Email: {tup[3]}',font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=0.1,rely=0.45)

        lbl_mob=Label(ifrm,text=f'Mobile: {tup[4]}',font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=0.1,rely=0.55)
        

    def update():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=0.3,rely=0.17,relwidth=0.5,relheight=0.55)

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select acn_name,acn_pass,acn_email,acn_mob from acn where acn_no=?',(gacn,))
        tup=curobj.fetchone()
        conobj.close()

        lbl_update=Label(ifrm,text='This is Update Screen',font=('arial',20,'bold'),bg='white',fg='Blue')
        lbl_update.pack()

        lbl_name=Label(ifrm,text='NAME',font=('arial',15,'bold'),bg='white')
        lbl_name.place(relx=0.1,rely=0.1)

        e_name=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_name.place(relx=0.1,rely=0.2)
        e_name.insert(0,tup[0])
        e_name.focus()

        lbl_pass=Label(ifrm,text='PASS',font=('arial',15,'bold'),bg='white')
        lbl_pass.place(relx=0.1,rely=0.5)

        e_pass=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_pass.place(relx=0.1,rely=0.6)
        e_pass.insert(0,tup[1])

        lbl_email=Label(ifrm,text='EMAIL',font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=0.5,rely=0.1)

        e_email=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_email.place(relx=0.5,rely=0.2)
        e_email.insert(0,tup[2])

        lbl_mob=Label(ifrm,text='MOB',font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=0.5,rely=0.5)

        e_mob=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_mob.place(relx=0.5,rely=0.6)
        e_mob.insert(0,tup[3])

        def update_db():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()


            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('update acn set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?',(name,pwd,email,mob,gacn))
            conobj.commit()
            conobj.close()

            messagebox.showinfo('Update','Record Updated')
            welcome_screen()

            
        btn_sub=Button(ifrm,command=update_db,text='SUBMIT',font=('arial',15,'bold'),bd=5)
        btn_sub.place(relx=0.5,rely=0.72)


        
        

    def deposit():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=0.3,rely=0.17,relwidth=0.5,relheight=0.55)

        lbl_update=Label(ifrm,text='This is Deposit Screen',font=('arial',20,'bold'),bg='white',fg='Blue')
        lbl_update.pack()

        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=0.1,rely=0.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=0.3,rely=0.2)
        e_amt.focus()

        def deposit_db():
            amt=float(e_amt.get())

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('update acn set acn_bal=acn_bal+? where acn_no=?',(amt,gacn))
            conobj.commit()
            conobj.close()

            messagebox.showinfo('Update',f'{amt} Amount Deposited')
            

            

        btn_sub=Button(ifrm,command=deposit_db,text='SUBMIT',font=('arial',20,'bold'),bd=5)
        btn_sub.place(relx=0.3,rely=0.35)

        
        
                    

        
    def withdraw():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=0.3,rely=0.17,relwidth=0.5,relheight=0.55)

        lbl_update=Label(ifrm,text='This is Withdraw Screen',font=('arial',20,'bold'),bg='white',fg='Blue')
        lbl_update.pack()

        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=0.1,rely=0.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=0.3,rely=0.2)
        e_amt.focus()

        def withdraw_db():
            amt=float(e_amt.get())

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select acn_bal from acn where acn_no=?',(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()


            if avail_bal>=amt:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute('update acn set acn_bal=acn_bal-? where acn_no=?',(amt,gacn))
                conobj.commit()
                conobj.close()

                messagebox.showinfo('Withdraw',f'{amt} Amount Withdrawn')
            else:
                messagebox.showwarning('Withdraw','Insufficient Bal')

        btn_sub=Button(ifrm,command=withdraw_db,text='SUBMIT',font=('arial',20,'bold'),bd=5)
        btn_sub.place(relx=0.3,rely=0.35)

    def transfer():
        ifrm=Frame(frm)
        ifrm.configure(bg='white')
        ifrm.place(relx=0.3,rely=0.17,relwidth=0.5,relheight=0.55)

        lbl_update=Label(ifrm,text='This is Transfer Screen',font=('arial',20,'bold'),bg='white',fg='Blue')
        lbl_update.pack()

        lbl_amt=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=0.1,rely=0.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=0.3,rely=0.2)
        e_amt.focus()

        lbl_to=Label(ifrm,text='To ACN',font=('arial',20,'bold'),bg='white')
        lbl_to.place(relx=0.1,rely=0.4)

        e_to=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_to.place(relx=0.3,rely=0.4)

        def transfer_db():
            to_acn=e_to.get()
            amt=float(e_amt.get())

            if to_acn==gacn:
                messagebox.showwarning('Transfer',"To and From can't be same")
                return
            
            
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select acn_bal from acn where acn_no=?',(gacn,))
            tup=curobj.fetchone()
            avail_bal=tup[0]
            conobj.close()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select acn_no from acn where acn_no=?',(to_acn,))
            tup=curobj.fetchone()
            #avail_bal=tup[0]
            conobj.close()

            if tup==None:
                messagebox.showwarning('Transfer','Invalid To ACN')
                return
                
            if avail_bal>=amt:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute('Update acn set acn_bal=acn_bal+? where acn_no=?',(amt,to_acn))
                curobj.execute('Update acn set  acn_bal=acn_bal-? where acn_no=?',(amt,gacn))
                conobj.commit()
                conobj.close()

                messagebox.showinfo('Transfer',f'{amt} transfered to ACN {to_acn}')
                 

    
        
        btn_sub=Button(ifrm,command=transfer_db,text='SUBMIT',font=('arial',20,'bold'),bd=5)
        btn_sub.place(relx=0.3,rely=0.55)


        




    conobj=sqlite3.connect(database='bank.sqlite')
    curobj=conobj.cursor()
    curobj.execute('select acn_name from acn where acn_no=?',(gacn,))
    tup=curobj.fetchone()
    conobj.close()
    
    
    lbl_wel=Label(frm,text=f'Welcome,{tup[0]}',font=('arial',20,'bold'),bg='light blue')
    lbl_wel.place(relx=0,rely=0)

    btn_logout=Button(frm,command=logout,text='LOGOUT',font=('arial',20,'bold'),bd=5)
    btn_logout.place(relx=0.89,rely=0.0)

    btn_details=Button(frm,command=details,width=10,text='DETAILS',font=('arial',20,'bold'),bd=5)
    btn_details.place(relx=0,rely=0.15)

    btn_update=Button(frm,command=update,width=10,text='UPDATE',font=('arial',20,'bold'),bd=5)
    btn_update.place(relx=0,rely=0.27)

    btn_deposit=Button(frm,command=deposit,width=10,text='DEPOSIT',font=('arial',20,'bold'),bd=5)
    btn_deposit.place(relx=0,rely=0.39)

    btn_withdraw=Button(frm,command=withdraw,text='WITHDRAW',font=('arial',20,'bold'),bd=5)
    btn_withdraw.place(relx=0,rely=0.51)

    btn_transfer=Button(frm,command=transfer,text='TRANSFER',font=('arial',20,'bold'),bd=5)
    btn_transfer.place(relx=0,rely=0.63)

    


    
    
    
   


    











    
    










    

main_screen()







win.mainloop()
