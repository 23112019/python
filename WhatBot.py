import pywhatkit
from tkinter import*

#functions
def Send():
    message=fmsg.get()
    hours=int(lhrs.get())
    minutes=int(lmins.get())
    mobiles=mobile.get()

    pywhatkit.sendwhatmsg(mobiles, message,hours,minutes)

def clear():
            fmsg.set(" ")
            lhrs.set(" ")
            lmins.set(" ")
            mobile.set(" ")
    
root=Tk()
root.config(background="aqua")
root.title("WHATSAPP BOT")
    
fmsg=StringVar()
lhrs=StringVar()
lmins=StringVar()
mobile=StringVar()

#tital section
Head=Label(root,text="WHATSAPP",font=("Times New Roman",36,"italic","bold"),bg="aqua",fg="Red").grid(row=0,columnspan=4,padx=20,pady=10)

#mobile number label and entry section
lmobile=Label(root,text="Mobile number",font=("Times New Roman",36,"bold"),bg="aqua",fg="Red").grid(row=1,column=0)
entrymobile=Entry(root,textvariable=mobile,width=20,bg="aqua",font=("Times New Roman",36,"bold")).grid(row=1,column=1)

#msg label and entry section
lfmsg=Label(root,text="your message",font=("Times New Roman",36,"bold"),bg="aqua",fg="red").grid(row=2,column=0)
entryfmsg=Entry(root,textvariable=fmsg,width=20,bg="aqua",font=("Times New Roman",36,"bold")).grid(row=2,column=1)

#hour label entry
llhrs=Label(root,text="Time in hours",font=("Times New Roman",36,"bold"),bg="aqua",fg="red").grid(row=3,column=0)
entrylhrs=Entry(root,textvariable=lhrs,width=20,bg="aqua",font=("Times New Roman",36,"bold")).grid(row=3,column=1)

#mins label
llmins=Label(root,text="Time in minutes",font=("Times New Roman",36,"bold"),bg="aqua",fg="red").grid(row=4,column=0)
entrylmins=Entry(root,textvariable=lmins,width=20,bg="aqua",font=("Times New Roman",36,"bold")).grid(row=4,column=1)

#button section
Send_b=Button(root,text="Send",command=Send,bg="red",fg="yellow",font=("Times New Roman",25,"bold")).grid(row=7,column=0,padx=20,pady=10,sticky=E)
clear_b=Button(root,text="Clear",command=clear,bg="red",fg="yellow",font=("Times New Roman",25,"bold")).grid(row=7,column=1,padx=20,pady=10,sticky=E)
