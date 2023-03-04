from time import time
from tkinter import *
from tkinter import messagebox
from turtle import down

import pyautogui
import time
def exi():
    g=messagebox.showwarning('Exit','nice to met you')
    win.destroy()
def autog():
    messagebox.showinfo('Info','Programmer: Atila Pashazadeh\nYear of construction: 2023-2-26')
def bob():
    win.destroy()


    def vip():
        def start():
            b.config(bg='black')
            s=time.time()
            time.sleep(5)

            for wort in range(int(ja.get())):
                pyautogui.write(ja2.get())
                time.sleep(0.2)
            
                pyautogui.press('enter')
                star.config(text='Finished',fg='red',bg='black')
                time.sleep(3)
                sleep.config(text=('sending message in ',int(time.time())-int(s),'second\U0001F607'),fg='green',bg='black')
        

        if pass1.get()=='987654321':
            root.destroy()
        
            master=Tk()
            master.config(background='black')
            master.title('bomber')
            btm_img=PhotoImage(file='img_btn.png')
            photo = PhotoImage(file = "esticon.png")
            master.iconphoto(False, photo)
            sleep = Label(master, text = "",bg='black')
            star = Label(master, text = "",bg='black')
            sleep.grid(row = 0, column = 2, sticky = W, pady = 2)
            star.grid(row = 2, column = 2, sticky = W, pady = 2)
            tedad = Label(master, text = "How many messages ?\U0001F600",bg='black',fg='white')
            payam = Label(master, text = "Write your message :\U0001F910",bg='black',fg='white')
            tedad.grid(row = 0, column = 1, sticky = W, pady = 2)
            payam.grid(row = 2, column = 1, sticky = W, pady = 2)
            ja = Entry(master)
            ja2 = Entry(master)
            ja.grid(row = 1, column = 2, pady = 2)
            ja2.grid(row = 3, column = 2, pady = 2)
            b=Button(master,text='enter',command=start,image=btm_img,borderwidth=5,fg='white',bg='black')
            b.grid(row=5,column= 1,pady= 0,)
            master.geometry("375x144")

            master.mainloop()
    
            
        else:
            messagebox.showerror('Error','Password is wrong')
    root=Tk()
    root.config(bg='black')
    pass1=Entry(root,show='*')
    pass1.pack()
    enter=Button(root,text='enter',command=vip,borderwidth=5,fg='white',bg='black')
    enter.pack()    
    root.geometry('250x190')
    root.mainloop()


def fr():
        win.destroy()
        def jb():
            if int(a.get())> 10000 :
                z.config(text='  SMALLER')
            elif int(a.get())< -10000:
                z.config(text='    BIGGER')
            else:
                p=1.80*int(a.get())+32
                z.config(text='%f F'%(p))
        master=Tk()
        master.title('Celsius To Fahrenheit')
        Label(master,text=' Celsius :',bg='black',fg='white').place(x=0,y=0)
        a=Entry(master)
        a.place(x=62,y=0)
        Button(master,text='enter',command=jb,width=10).place(x=85,y=50)
        z=Label(master,text='',bg='black',fg='red')
        z.place(x=88,y=100)
        master.geometry('250x190')
        master.config(background='black')
        photo = PhotoImage(file = "icon.png")
        master.iconphoto(False, photo)
        master.mainloop()






def cel():
    win.destroy()
    def jav():
        if int(a.get())> 10000 :
            z.config(text='    SMALLER')
        elif int(a.get())< -10000:
            z.config(text='      BIGGER')
        else:
            k1=int(a.get())+273.15
            z.config(text='%f C'%(k1))
    k=Tk()
    k.title('Celsius To Kelvin')
    Label(k,text=' Celsius :',bg='black',fg='white').place(x=0,y=0)
    a=Entry(k)
    a.place(x=62,y=0)
    Button(k,text='enter',command=jav,width=10).place(x=85,y=50)
    z=Label(k,text='',bg='black',fg='red')
    z.place(x=82,y=100)
    k.geometry('250x190')
    k.config(background='black')
    photo = PhotoImage(file = "icon.png")
    k.iconphoto(False, photo)
    k.mainloop()




def kelvin():
    def javab():
        if int(a.get())> 10000 :
            z.config(text='    SMALLER')
        elif int(a.get())< -10000:
            z.config(text='      BIGGER')
        else:
            kk=int(a.get())-273.15
            z.config(text='%f C'%(kk))
    win.destroy()
    kl=Tk()
    kl.title('Kelvin to Celsius')
    Label(kl,text=' Celsius :',bg='black',fg='white').place(x=0,y=0)
    a=Entry(kl)
    a.place(x=62,y=0)
    Button(kl,text='enter',command=javab,width=10,bg='gray').place(x=85,y=50)
    z=Label(kl,text='',bg='black',fg='red')
    z.place(x=82,y=100)
    kl.geometry('250x190')
    kl.config(background='black')
    photo = PhotoImage(file = "icon.png")
    kl.iconphoto(False, photo)
    kl.mainloop()

    
    
win=Tk()
photo = PhotoImage(file = "icon.png")
win.iconphoto(False, photo)
win.title('Temperature')
Button(win,text='Kelvin to Celsius',command=kelvin,bg='yellow',width=20).pack()

Button(win,text='Celsius To Kelvin',command=cel,bg='green',width=20).pack()
Button(win,text='Celsius To Fahrenheit',command=fr,bg='red',width=20).pack()
Button(win,text='sms bomber(vip)',command=bob,bg='grey',width=20).pack()
win.config(background='black')
menubar = Menu(win)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="info", command=autog)
menubar.add_cascade(label="Help", menu=helpmenu)
exitmenu = Menu(menubar, tearoff=0)
exitmenu.add_command(label='Exit',command=exi)
menubar.add_cascade(label="Exit", menu=exitmenu)
win.config(menu=menubar)
win.geometry('250x190')
win.mainloop()
