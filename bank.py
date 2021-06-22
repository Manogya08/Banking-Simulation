#banking application main page
from tkinter import *
from tkinter import ttk
import db
import account
from tkinter import messagebox
from PIL import Image, ImageTk
import re


Dict={}
Names={}
buffer={"key":"NULL"}


accno=0
root=Tk()
root.geometry("512x300")
root.iconbitmap("bank1.ico")
class First(Frame):
    def __init__(self,master):
            Frame.__init__(self,master)
            self.grid()
            self.create_widgets()
    def create_widgets(self):
        cl="gray"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=0,column=1)
        
        self.label=Label(self,font="arial 16 bold",bg=cl,fg="white")
        self.label["text"]="Welcome to Niet Bank"
        self.label.grid(row=2,column=1)
        self.label=Label(self,font="arial 12",bg=cl,fg="white")
        self.label["text"]="Log In to Continue"
        self.label.grid(row=3,column=1,sticky=S)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=4,column=1)
        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Username"
        self.label.grid(row=5,column=0,sticky=S)
        self.user=Entry(self,font="Arial")
        self.user.grid(row=5,column=1,sticky=S)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=6,column=1)
        #password field
        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Password"
        self.label.grid(row=7,column=0,sticky=S)
        self.password=Entry(self,font="Arial",show="*")
        self.password.grid(row=7,column=1,sticky=S)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=8,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=10,column=1)
        self.submit=Button(self,cursor="hand2",bg="gray95",relief=RAISED,font="Arial",fg="black")
        self.bbutton=Button(self,cursor="hand2",bg="gray95",relief=RAISED,font="Arial",fg="black")
        self.bbutton["text"]="Create New Account"
        self.submit["text"]="SUBMIT"
        self.submit["command"]=self.data
        self.bbutton["command"]=win1
        self.submit.grid(row=9,column=1,sticky=S)
        self.bbutton.grid(row=11,column=1,sticky=S)
    def data(self):
        
        user=self.user.get()
        password=self.password.get()
        if not user or not password:
            messagebox.showerror("Error", "Please Fill All entries")
        else:
            q="select username,pass,balance,accno from user"
            db.cursor.execute(q)
            d=db.cursor.fetchall()
            c=0
            for u in d:
                if u[0]==user and u[1]==password:
                    c=1
                    Dict["accno"]=u[3]
                    Dict["balance"]=u[2]
                    main()
            if c==0:
                 messagebox.showinfo("Unauthorized", "Incorrect Username Or Password")
                
class Welcome(Frame):
    def __init__(self,master):
            Frame.__init__(self,master)
            self.grid()
            self.create_widgets()
    def create_widgets(self):
        print(Dict)
        cl="peachpuff"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=0,column=1)
        self.label=Label(self,text="Welcome to Niet Bank    ",font="arial 15 bold",fg="black",bg=cl)
        self.label.grid(row=3,column=1,sticky=S)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=4,column=1)
        self.logout=Button(self,cursor="hand2",text="Logout",command=logout,bg="red",fg="white")
        self.logout.grid(row=3,column=3)
        
        #self.label.grid(row=5,column=2)
        
        #body start
        #button1
        self.button1=Button(self,width=12,padx=20,cursor="hand2",bg="sky blue")
        self.button1["text"]="Balance"
        self.button1["command"]=win2
        self.button1["font"]="Arial 12 italic"
        self.button1.grid(row=5,column=0)
        #button2
        self.button2=Button(self,width=12,padx=20,cursor="hand2",bg="sky blue")
        self.button2["text"]="Deposit"
        self.button2["command"]=win3
        self.button2["font"]="Arial 12 italic"
        self.button2.grid(row=7,column=0)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=12,column=1)
        #button3
        self.button3=Button(self,width=12,padx=20,cursor="hand2",bg="sky blue")
        self.button3["text"]="Withdraw"
        self.button3["command"]=win4
        self.button3["font"]="Arial 12 italic"
        self.button3.grid(row=8,column=0)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=9,column=1)
        #button4
        self.button4=Button(self,width=12,padx=20,cursor="hand2",bg="sky blue")
        self.button4["text"]="Mini Statement"
        self.button4["command"]=win5
        self.button4["font"]="Arial 12 italic"
        self.button4.grid(row=9,column=0)
        #button5
        self.button5=Button(self,width=12,padx=20,cursor="hand2",bg="sky blue")
        self.button5["text"]="Money Transfer"
        self.button5["command"]=win6
        self.button5["font"]="Arial 12 italic"
        self.button5.grid(row=11,column=0)
        #canvas
        '''self.canvas=Canvas(self,width=800,height=800)
        img = Image.open("digibank.gif")
        gif=ImageTk.PhotoImage(img)
        self.canvas.create_image(350,300,image=gif)
        self.canvas.image=gif
        self.canvas.grid(row=9,column=1)'''

        '''img = Image.open("digibank.gif")
       # im2=img.resize((300, 320), Image.NEAREST)
        tkimage =ImageTk.PhotoImage(img)
        label=Label(self,image=tkimage,width=300,bg=cl)
        label.image=tkimage
        label.place(x=0,y=0)'''
    

       
class Create(Frame):
    def __init__(self,master):
            Frame.__init__(self,master)
            self.grid()
            self.create_widgets()
    def create_widgets(self):
        cl="gray"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=5,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=9,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=11,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=13,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=15,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=17,column=1)

        
        self.label=Label(self,font="arial 15 bold",bg=cl,fg="white")
        self.label["text"]="Create New Account"
        self.label.grid(row=2,column=1,sticky=S)
        #body start
        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Full Name"
        self.label.grid(row=4,column=0,sticky=S)
        self.name=Entry(self,font="Arial")
        self.name.grid(row=4,column=1,sticky=S)
        
        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Phone no"
        self.label.grid(row=6,column=0,sticky=S)
        self.phone=Entry(self,font="Arial",validate="key")
        self.phone.grid(row=6,column=1,sticky=S)
        

        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Aadhar No"
        self.label.grid(row=8,column=0,sticky=S)
        self.aadhar=Entry(self,font="Arial")
        self.aadhar.grid(row=8,column=1,sticky=S)

        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Account Type"
        self.label.grid(row=10,column=0,sticky=S)
        self.acctype=ttk.Combobox(self,values=["saving","current"],font="Arial")
        self.acctype.grid(row=10,column=1,sticky=S)
        self.acctype.current(0)
        self.acctype.config(state="readonly")

        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Initial Amount"
        self.label.grid(row=12,column=0,sticky=S)
        self.amount=Entry(self,font="Arial")
        self.amount.insert(0,"5000")
        self.amount.config(state="readonly")
        self.amount.grid(row=12,column=1,sticky=S)


        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Password"
        self.label.grid(row=14,column=0,sticky=S)
        self.pas=Entry(self,font="Arial",show="*")
        self.pas.grid(row=14,column=1,sticky=S)


        self.label=Label(self,font="Arial",bg=cl,fg="white")
        self.label["text"]="Re-Password"
        self.label.grid(row=16,column=0,sticky=S)
        self.rpas=Entry(self,font="Arial",show="*")
        self.rpas.grid(row=16,column=1,sticky=S)
        
        
        self.submit=Button(self,cursor="hand2",bg="gray95",fg="black")
        self.submit["command"]=self.data
        
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="gray95",fg="black")
        self.bbutton["text"]="back"
        
        self.submit["text"]="Create Account"
        self.bbutton["command"]=clear
        self.submit.grid(row=18,column=1,sticky=S)
        self.bbutton.grid(row=18,column=0,sticky=S)
    def data(self):
        username=account.username()
        name=self.name.get()
        phone=self.phone.get()
        aadhar=self.aadhar.get()
        amount=self.amount.get()
        acctype=self.acctype.get()
        accno=account.acc_no()
        password=self.pas.get()
        rpas=self.rpas.get()
        q="select * from user where aadharno='%s'"%(aadhar)
        db.cursor.execute(q)
        d=db.cursor.fetchone()
        x=re.findall("[0-9]",aadhar)
        y=re.findall("[0-9]",phone)
        if not name or not phone or not aadhar or not amount or not password or not rpas:
                messagebox.showerror("Error", "Please fill All entries")
        elif len(name)!=len(re.findall("[a-zA-Z ]",name)):
               messagebox.showerror("Error", "Invalid name")
        elif len(y)!=10 or len(phone)!=10:
                messagebox.showerror("Error", "Invalid Phone No")
        elif len(x)!=12 or len(aadhar)!=12:
                messagebox.showerror("Error", "Invalid Aadhar No")
        
        elif d is None:
            
            if password!=rpas:
                messagebox.showerror("Error", "Password not Matched")
            elif not (account.validate(password)):
                messagebox.showerror("Error", "Password Should contain at least contain \n one lowercase,one uppercase,one digit,one special symbol")
            else:
                q="insert into user values('%s','%s','%s','%s','%s','%s','%s','%s')"%(name,password,accno,phone,aadhar,acctype,amount,username)
                db.cursor.execute(q)
                db.cursor.execute("insert into transaction values('%s',date(now()),(select balance from user where accno='%s'),'self','%s','0',time(now()))"%(accno,accno,amount))
                db.cursor.execute("commit")
                messagebox.showinfo("Important message", "please copy your Account no and password \n Account no: %s \n Username : %s \npassword : %s"%(accno,username,password))
                print("account created\n username : %s \n accno : %s"%(username,accno))
        else:
            messagebox.showerror("Error","Aadhar card Already registered")
            

class Balance(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        cl="salmon"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)
        
        self.label=Label(self,bg=cl,font="arial 15 bold")
        self.label["text"]="Account No : "+Dict["accno"]
        self.label.grid(row=2,column=1,sticky=S)
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="sky blue",font="arial 12")
        self.bbutton["text"]="back"
        self.bbutton["command"]=main
        self.bbutton.grid(row=8,column=1)
        self.msg=Text(self,width=40,height=5,wrap=WORD,font="Arial")
        self.data()
        self.msg.configure(state="disable")
        self.msg.grid(row=4,column=1,sticky=S)
    def data(self):
        q="select balance from user where accno='%s'"%(Dict["accno"])
        db.cursor.execute(q)
        d=db.cursor.fetchone()
        self.msg.insert(0.0,"   Your Account Balance is : "+d[0])
class Deposit(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        cl="salmon"
        self.space=Label(self,text=" ",bg=cl)
        
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=5,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)

        self.label=Label(self,bg=cl,font="arial 15 bold")
        self.label["text"]="Deposit Money"
        self.label.grid(row=2,column=1,sticky=S)


        self.label=Label(self,bg=cl,font="arial",fg="black")
        self.label["text"]="Enter Amount"
        self.label.grid(row=4,column=0)
        
        self.amount=Entry(self,font="arial")
        self.amount.grid(row=4,column=1)
        
        self.button=Button(self,cursor="hand2",bg="cyan2",font="arial 10")
        self.button["text"]="SUBMIT"
        self.button["command"]=self.data
        self.button.grid(row=6,column=1,sticky=S)
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="black",fg="white",font="arial 10")
        self.bbutton["text"]="back"
        self.bbutton["command"]=main
        self.bbutton.grid(row=8,column=1)
    def data(self):
        amount=self.amount.get()
        if not amount:
            messagebox.showinfo("Enter Amount","please enter amount")
        elif float(amount)<=0:
            messagebox.showinfo("Error","Enter Amount Greater than zero")
        else:
            msg=messagebox.askquestion("confirm Transaction","confirm to deposit")
            if msg=="yes":
                q="update user set balance=balance+'%s' where accno='%s'"%(amount,Dict["accno"])
                db.cursor.execute(q)
                db.cursor.execute("insert into transaction values('%s',date(now()),(select balance from user where accno='%s'),'self','%s','0',time(now()))"%(Dict["accno"],Dict["accno"],amount))
                db.cursor.execute("commit")
                messagebox.showinfo("Success","Transaction Success")
            else:
                messagebox.showinfo("Cancelled","Transaction Cancelled")
        
	
class Withdraw(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        cl="salmon"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=5,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)
       
        self.label=Label(self,bg=cl,font="arial 15 bold")
        self.label["text"]="Withdraw Money"
        self.label.grid(row=2,column=1,sticky=S)



        self.label=Label(self,bg=cl,font="arial")
        self.label["text"]="Enter Amount"
        self.label.grid(row=4,column=0,sticky=S)
        
        self.amount=Entry(self,font="arial")
        self.amount.grid(row=4,column=1,sticky=S)
        
        self.button=Button(self,cursor="hand2",bg="cyan2",font="arial 10")
        self.button["text"]="SUBMIT"
        self.button["command"]=self.data
        self.button.grid(row=6,column=1,sticky=S)
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="black",fg="white",font="arial 10")
        self.bbutton["text"]="back"
        self.bbutton["command"]=main
        self.bbutton.grid(row=8,column=1)
    def data(self):
        amount=self.amount.get()
        db.cursor.execute("select balance from user where accno='%s'"%(Dict["accno"]))
        d=db.cursor.fetchone()
        
        if not amount:
            messagebox.showinfo("Enter Amount","please enter amount")
        elif float( amount)>float(d[0]):
            messagebox.showerror("Error","Insufficient balance")
        elif float(amount)<=0:
            messagebox.showerror("Error","Enter amount greater than zero")
        else:
            msg=messagebox.askquestion("confirm Transaction","confirm to Withdrawn")
            if msg=="yes":
                q="update user set balance=balance-'%s' where accno='%s'"%(amount,Dict["accno"])
                db.cursor.execute(q)
                db.cursor.execute("insert into transaction values('%s',date(now()),(select balance from user where accno='%s'),'self','0','%s',time(now()))"%(Dict["accno"],Dict["accno"],amount))
                db.cursor.execute("commit")
                messagebox.showinfo("Success","Transaction Success")
            else:
                messagebox.showinfo("Cancelled","Transaction Cancelled")
	
class Statement(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        cl="salmon"
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)
        
        self.label=Label(self,bg=cl,font="arial 15 bold")
        self.label["text"]="Mini Statement"
        self.label.grid(row=2,column=1,sticky=S)
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="black",fg="white",font="arial 10")
        self.bbutton["text"]="back"
        self.bbutton["command"]=main
        self.bbutton.grid(row=8,column=1,sticky=S)
        self.msg=Text(self,width=80,height=15,bg="black",fg="white",font="arial")
        
        self.msg.grid(row=6,column=1)
        self.data()
    def data(self):
        q="select date,time,credit,debit,Amount,sender from transaction where accno='%s'"%(Dict['accno'])
        db.cursor.execute(q)
        d=list(db.cursor.fetchall())
        
        
        self.msg.insert(0.0,"            DATE         TIME        CREDIT       DEBIT       BALANCE      SENDER\n")
        for item in d:
            self.msg.insert(END,tuple(display(item)))
            self.msg.insert(END,"\n")
            
        self.msg.configure(state="disable")
class Send(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        cl="salmon"
        self.bank_names()
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=1,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=3,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=5,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=7,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=9,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=11,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=13,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=15,column=1)
        self.space=Label(self,text=" ",bg=cl)
        self.space.grid(row=17,column=1)
        
        self.label=Label(self,bg=cl,font="arial 15 bold")
        self.label["text"]="  Money Transfer"
        self.label.grid(row=2,column=0,columnspan=2)
        #combo box for bank names
        self.label=Label(self,text="Select Bank Name",bg=cl,font="arial")
        self.label.grid(row=4,column=0)

        self.combo=ttk.Combobox(self,values=list(Names.keys()),font="arial")
        self.combo.grid(row=4,column=1)
        self.combo.current(0)
        self.combo.config(state="readonly")

        #ifsc code
        label=Label(self,text="Enter IFSC CODE",bg=cl,font="arial")
        label.grid(row=6,column=0)

        self.code=Entry(self,font="arial")
        self.code.grid(row=6,column=1)

        
        
        self.label2=Label(self,bg=cl,font="arial")
        self.label2["text"]="Enter Receiver's Account No"
        self.label2.grid(row=8,column=0)
        self.accno=Entry(self,font="arial")
        self.accno.grid(row=8,column=1)

        #search
        self.search=Button(self,text="Search",command=self.search,width=32,cursor="hand2",bg="cyan2",font="arial 10")
        self.search.grid(row=10,column=0,columnspan=3)
        #text view
        self.view=Text(self,width=40,height=10,bg="black",fg="white",font="arial")
        self.view.grid(row=12,column=0,columnspan=3)
        self.view.config(state="disable")
        
        
        #amount
        self.label3=Label(self,bg=cl,font="arial")
        self.label3["text"]="Enter Amount"
        self.label3.grid(row=14,column=0,sticky=S)
        self.amount=Entry(self,font="arial")
        self.amount.grid(row=14,column=1,sticky=S)
        self.submit=Button(self,cursor="hand2",bg="cyan2",font="arial 10",width=32)
        self.submit["text"]="Transfer"
        self.submit["command"]=self.data
        self.submit.grid(row=16,column=0,columnspan=3)
        self.bbutton=Button(self,cursor="sb_left_arrow",bg="black",fg="white",font="arial 10")
        self.bbutton["text"]="back"
        self.bbutton["command"]=main
        self.bbutton.grid(row=18,column=0,sticky=S)
    def bank_names(self):
        q="select bank_name,code from ifsc"
        db.cursor.execute(q)
        d=db.cursor.fetchall()
        for bank in d:
            Names[bank[0]]=bank[1]
            
        #print(Names)
    def search(self):
        accno=self.accno.get()
        ifsc=self.code.get()
        bank_name=self.combo.get()
        if bank_name=="Niet":
            i=Names["Niet"]
            bank_name="user"
        q="select name,accno from %s where accno='%s'"%(bank_name,accno)
        db.cursor.execute(q)
        d=db.cursor.fetchone()
        #print(d)
        if bank_name=="user":
            bank_name="Niet"
            
        
        if  not accno or not ifsc:
            messagebox.showerror("Error","Please fill all entries")
        elif ifsc!=Names[bank_name]:
            messagebox.showerror("Error","Incorrect IFSC code")
        elif d is not None:
            buffer["key"]=True
            self.view.config(state="normal")
            self.view.delete(1.0,END)
            self.view.insert(0.0,"\t Check Details \n\n  Receiver's Name : "+d[0]+" \n  Receiver Bank : "+bank_name+"\n  Bank IFSC : "+ifsc+" \n   Account No : "+d[1]+"")
            self.view.config(state="disable")
        else:
            buffer["key"]=False
            messagebox.showerror("Error","Account Doesn't Exist")
            self.view.config(state="normal")
            self.view.delete(1.0,END)
    def data(self):
        accno=self.accno.get()
        amount=(self.amount.get())
        ifsc=self.code.get()
        bank_name=self.combo.get()
        if not amount or not accno or not ifsc:
            messagebox.showerror("Error","Please Fill all Entries")
            return
        amount=float(amount)
        q="select balance from user where accno='%s'"%(Dict["accno"])
        db.cursor.execute(q)
        d1=db.cursor.fetchone()
        
        if accno==Dict["accno"]:
                messagebox.showerror("Error","You Cannot send money to self")
                return
        if amount<=0:
                messagebox.showerror("Error","Enter amount greater than zero")
                return
        if amount>float(d1[0]):
                messagebox.showerror("Insufficient Balance","Insufficient Balance")
                return
        if buffer["key"]==True:
            buffer["key"]=False
            
            if bank_name=="Niet":
                bank_name="user"
            
            msg=messagebox.askquestion("confirm Transaction","confirm to Transfer Money")
            if msg=="yes":
                q="update user set balance=balance-'%s' where accno='%s'"%(amount,Dict["accno"])
                q1="update %s set balance=balance+'%s' where accno='%s'"%(bank_name,amount,accno)

                db.cursor.execute(q)
                db.cursor.execute(q1)
                
                db.cursor.execute("insert into transaction values('%s',date(now()),(select balance from user where accno='%s'),'self','0','%s',time(now()))"%(Dict["accno"],Dict["accno"],amount))
                if bank_name=="user":
                    db.cursor.execute("insert into transaction values('%s',date(now()),(select balance from user where accno='%s'),(select name from user where accno='%s'),'%s','0',time(now()))"%(accno,accno,Dict["accno"],amount))
                d= db.cursor.execute("commit")
                messagebox.showinfo("Success","Transaction Success")
                self.accno.delete(0,END)
                self.amount.delete(0,END)
                self.code.delete(0,END)
                self.view.config(state="normal")
                self.view.delete(1.0,END)
                self.view.config(state="disable")
            else:
                messagebox.showinfo("Cancelled","Transaction Cancelled")
        else:
            messagebox.showerror("Information","Incorrect Details")
                
                
        
        



def center(x,y):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (x/2))
    y_cordinate = int((screen_height/2) - (y/2))

    root.geometry("{}x{}+{}+{}".format(x,y, x_cordinate, y_cordinate))
    
def delete():
    for widget in root.winfo_children():
        widget.destroy()
    
def first():
    root.title("Niet Bank")
    First(root)
    root.geometry("300x340")
    root.configure(bg="gray")
    for widget in root.winfo_children():
        widget.configure(bg="gray")
    center(340,300)
    root.resizable(False,False)
    root.mainloop()
def win1():
    
    delete()
    Create(root)
    root.title("Create Account")
    root.geometry("350x430")
    root.configure(bg="gray")
    for widget in root.winfo_children():
        widget.configure(bg="gray")
    center(350,450)
    root.resizable(False,False)
    root.mainloop()
    
def win2():
    delete()
    Balance(root)
    root.title("Balance")
    root.configure(bg="salmon")
    for widget in root.winfo_children():
        widget.configure(bg="salmon")
    center(350,270)
    root.resizable(False,False)
    root.mainloop()
def win3():
    delete()
    app=Deposit(root)
    root.title("Deposit Amount")
    root.configure(bg="salmon")
    for widget in root.winfo_children():
        widget.configure(bg="salmon")
    center(330,280)
    root.resizable(False,False)
    root.mainloop()
def win4():
    delete()
    app=Withdraw(root)
    root.title("Withdraw Amount")
    root.configure(bg="salmon")
    for widget in root.winfo_children():
        widget.configure(bg="salmon")
    center(330,280)
    root.resizable(False,False)
    root.mainloop()
def win5():
    delete()
    
    Statement(root)
    root.configure(bg="salmon")
    for widget in root.winfo_children():
        widget.configure(bg="salmon")
    root.title("Mini Statement")
    center(650,440)
    root.resizable(False,False)
    root.mainloop()
def win6():
    delete()
    app=Send(root)
    root.title("Money Transfer")
    root.configure(bg="salmon")
    for widget in root.winfo_children():
        widget.configure(bg="salmon")
    center(450,600)
    #root.resizable(False,False)
    root.mainloop()

def clear():
    for widget in root.winfo_children():
        widget.destroy()
    first()
def main():
    delete()
    Welcome(root)
    root.title("Services Available")
    root.geometry("512x300")
    root.configure(bg="peachpuff")
    for widget in root.winfo_children():
        widget.configure(bg="peachpuff")
    center(512,300)
    root.resizable(False,False)
    root.mainloop()
def logout():
    delete()
    first()
       
def display(x):
    l1=[]
    i=1
    for item in x:
        t=""
        if i==3:
            t="Credit : "+str(item)
        elif i==4:
            t="Debit : "+str(item)
        elif i==5:
            t="Balance : "+str(item)
        else:
            t=" "+str(item)+" "
        i=i+1   
        l1.append(t)
    return l1
        


first()


    
   
    
