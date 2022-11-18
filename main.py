import random
from tkinter import *
from tkinter import messagebox
 
#width=400,height=500
root=Tk()
root.title("math based capcha")
root.geometry("520x400")
root.config(bg="white")

#expression generation
def verify():
    bm.configure(width=20)
    bm.place(x=250,y=83)
    l1.place(x=50,y=250)
    x=random.randint(1,4)
    a=random.randint(1,9)
    b=random.randint(1,9)
    a1.insert(END,str(a))
    b1.insert(END,str(b))
    x1.insert(END,str(x))
    if(x==1):
        txt=''+str(a)+'   +   '+str(b)+" ? "
        l=Label(f,text=txt)
        l.configure(font=("sans-serif",26,"normal"))
        l.place(x=50,y=80)

        b2=Button(f,text="verify",command=check)
        b2.configure(font=("sans-serif",16,"normal"),width=20)
        b2.place(x=250,y=250)
    if(x==2):
        txt=''+str(a)+'   -   '+str(b)+" ? " 
        l=Label(f,text=txt)
        l.configure(font=("sans-serif",26,"normal"))
        l.place(x=50,y=80)

        b2=Button(f,text="verify",command=check)
        b2.configure(font=("sans-serif",16,"normal"),width=20)
        b2.place(x=250,y=250)
    if(x==3):
        txt=''+str(a)+'   *   '+str(b)+" ? "
        l=Label(f,text=txt)
        l.configure(font=("sans-serif",26,"normal"))
        l.place(x=50,y=80)

        b2=Button(f,text="verify",command=check)
        b2.configure(font=("sans-serif",16,"normal"),width=20)
        b2.place(x=250,y=250)
    if(x==4):
        txt=''+str(a)+'   /   '+str(b)+" ? "
        l=Label(f,text=txt)
        l.configure(font=("sans-serif",26,"normal"))
        l.place(x=50,y=80)

        b2=Button(f,text="verify",command=check)
        b2.configure(font=("sans-serif",16,"normal"),width=20)
        b2.place(x=250,y=250)
        
        
#messagebox.showerror("error","wrong answer")
# Expression functioning code          
def check():
    ctr=0
    ctr1=0
    ans=l1.get()
    print(ans)
    anum=a1.get()
    bnum=b1.get()
    xnum=x1.get()
    for i in anum:
        ctr+=1
    for i in anum:
        ctr1+=1
        if(ctr1==ctr):
            anum=i
    print(anum)
    ctr=0
    ctr1=0
    for i in bnum:
        ctr+=1
    for i in bnum:
        ctr1+=1
        if(ctr1==ctr):
            bnum=i
    print(bnum)
    ctr=0
    ctr1=0
    for i in xnum:
        ctr+=1
    for i in xnum:
        ctr1+=1
        if(ctr1==ctr):
            xnum=i
    print(xnum)
            
    if(int(xnum)==1):
        if(float(ans)==int(anum)+int(bnum)):
            messagebox.showinfo("information","Human verified!")
        else:
            messagebox.showerror("error","Wrong answer. Try again.")
    if(int(xnum)==2):
        if(float(ans)==int(anum)-int(bnum)):
            messagebox.showinfo("information","Human verified!")
        else:
            messagebox.showerror("error","Wrong answer. Try again.")
    if(int(xnum)==3):
        if(float(ans)==int(anum)*int(bnum)):
            messagebox.showinfo("information","Human verified!")
        else:
            messagebox.showerror("error","Wrong answer. Try again.")
    if(int(xnum)==4):
        if(float(ans)==int(anum)/int(bnum)):
            messagebox.showinfo("information","Human verified!")
        else:
            messagebox.showerror("error","Wrong answer. Try again.")
            
f=Frame(root)
f.configure(bg="grey",width=550,height=400)
f.place(x=0,y=0)

bm=Button(f,text="refresh",command=verify)
bm.configure(font=("sans-serif",16,"normal"),width=0)
bm.place(x=8000,y=4000)

a1=Entry(f)
a1.place(x=10000,y=20000)
b1=Entry(f)
b1.place(x=10000,y=20000)
x1=Entry(f)
x1.place(x=10000,y=20000)

h=Label(f,text="Human Verification")
h.configure(font=("sans-serif",20,"bold"))
h.place(x=146,y=15)

ec=Label(f,text="Enter the correct value.")
ec.configure(font=("sans-serif",18,"normal"))
ec.place(x=146,y=170)

l1=Entry(f)
l1.configure(font=("sans-serif",26,"normal"),width=7)
l1.place(x=11000,y=12000)
verify()
root.mainloop()
