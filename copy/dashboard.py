
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PIL import ImageTk
import PIL.Image
import subprocess
import time
import numpy as np
import pandas as pd 
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from healthoslib.health_os_client import *

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

with open("check.txt","r") as fptr:
    z=fptr.readlines()
    #print z
    x=z[0]
    y=z[1]


import dashboard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Dashboard___Student (root)
    dashboard_support.init(root, top)
    root.mainloop()

w = None
def create_Dashboard___Student(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Dashboard___Student (w)
    dashboard_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Dashboard___Student():
    global w
    w.destroy()
    w = None


class Dashboard___Student:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b' # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8' # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4' # Closest X11 color: '{medium turquoise}'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Product Sans} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Product Sans} -size 9 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font15 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1600x900+4+77")
        top.title("Dashboard : Doctor")
        top.configure(background="#263238")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        host = 'www.healthos.co'
        o_auth_access_token = '6355da35f2498f9e96225b891e7926ac34ffb757aaa5778bbe93a4336df0acc3'
        client = HealthOSClient(host, o_auth_access_token)

        page = 1
        size = 10

        med = ''
        def url_call(med):
            autocomplete_client = client.autocomplete
            medicine_query = med
            try:
                result = autocomplete_client.get_medicines(medicine_query)
                #print result[0]['name']
                return result[0]['name']
            except:
                print ""


        root.state('zoomed')
        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.022, relheight=1.017, relwidth=1.003)

        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#263238")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1605)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.424, rely=0.077, height=48, width=213)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''DASHBOARD''')

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.037, rely=0.186, relheight=0.727
                , relwidth=0.371)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#455a64")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=595)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.353, rely=0.045, height=35, width=169)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#455a64")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Student Details''')

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.403, rely=0.18, height=29, width=123)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#455a64")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#fff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Full Name :''')

        self.Label3_3 = Label(self.Frame2)
        self.Label3_3.place(relx=0.353, rely=0.241, height=29, width=155)
        self.Label3_3.configure(activebackground="#f9f9f9")
        self.Label3_3.configure(activeforeground="black")
        self.Label3_3.configure(background="#455a64")
        self.Label3_3.configure(disabledforeground="#a3a3a3")
        self.Label3_3.configure(font=font13)
        self.Label3_3.configure(foreground="#fff")
        self.Label3_3.configure(highlightbackground="#d9d9d9")
        self.Label3_3.configure(highlightcolor="black")
        self.Label3_3.configure(text='''Reg No :''')

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.202, rely=0.541, height=113, width=116)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#455a64")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./history (1).png"))
        self.Button1.configure(image=self._img1)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Medical History''')

        self.Label4 = Label(self.Frame2)
        self.Label4.place(relx=0.580, rely=0.183, height=26, width=222)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#455a64")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#fff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(anchor = W)
        if len(str(y))<=26:
            self.Label4.configure(font=font15)
            self.Label4.configure(text=y)
        else :
            self.Label4.configure(font=("Product Sans",6))
            self.Label4.configure(width = 280)
            self.Label4.configure(text=y)



        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.550 , rely=0.257, height=26, width=172)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#455a64")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#fff")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(anchor = W)
        self.Label5.configure(text =x)
        self.Label5.configure(font = font14)



        self.Label6 = Label(self.Frame2)
        self.Label6.place(relx=0.521, rely=0.286, height=26, width=162)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#455a64")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.118, rely=0.12, height=163, width=146)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#455a64")
        self.Button3.configure(borderwidth="0")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self._img2 = ImageTk.PhotoImage(PIL.Image.open("./userprofile.png"))
        self.Button3.configure(image=self._img2)
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Button''')

        self.Button1_6 = Button(self.Frame2)
        self.Button1_6.place(relx=0.555, rely=0.526, height=133, width=126)
        self.Button1_6.configure(activebackground="#d9d9d9")
        self.Button1_6.configure(activeforeground="#000000")
        self.Button1_6.configure(background="#455a64")
        self.Button1_6.configure(borderwidth="0")
        self.Button1_6.configure(disabledforeground="#a3a3a3")
        self.Button1_6.configure(font=font14)
        self.Button1_6.configure(foreground="#fff")
        self.Button1_6.configure(highlightbackground="#d9d9d9")
        self.Button1_6.configure(highlightcolor="black")
        self._img3 = ImageTk.PhotoImage(PIL.Image.open("./fitbit.png"))
        self.Button1_6.configure(image=self._img3)
        self.Button1_6.configure(pady="0")
        self.Button1_6.configure(text='''Medical History''')

        self.Label8 = Label(self.Frame2)
        self.Label8.place(relx=0.202, rely=0.707, height=27, width=122)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#455a64")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font=font15)
        self.Label8.configure(foreground="#fff")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Medical History''')

        self.Label8_2 = Label(self.Frame2)
        self.Label8_2.place(relx=0.555, rely=0.707, height=27, width=122)
        self.Label8_2.configure(activebackground="#f9f9f9")
        self.Label8_2.configure(activeforeground="black")
        self.Label8_2.configure(background="#455a64")
        self.Label8_2.configure(disabledforeground="#a3a3a3")
        self.Label8_2.configure(font=font15)
        self.Label8_2.configure(foreground="#fff")
        self.Label8_2.configure(highlightbackground="#d9d9d9")
        self.Label8_2.configure(highlightcolor="black")
        self.Label8_2.configure(text='''Fitbit Analysis''')

        self.Frame2_1 = Frame(self.Frame1)
        self.Frame2_1.place(relx=0.442, rely=0.186, relheight=0.727
                , relwidth=0.514)
        self.Frame2_1.configure(relief=GROOVE)
        self.Frame2_1.configure(borderwidth="2")
        self.Frame2_1.configure(relief=GROOVE)
        self.Frame2_1.configure(background="#455a64")
        self.Frame2_1.configure(highlightbackground="#d9d9d9")
        self.Frame2_1.configure(highlightcolor="black")
        self.Frame2_1.configure(width=825)

        self.Label2_2 = Label(self.Frame2_1)
        self.Label2_2.place(relx=0.388, rely=0.045, height=33, width=178)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#455a64")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Consultation''')

        self.Labelframe1 = LabelFrame(self.Frame2_1)
        self.Labelframe1.place(relx=0.048, rely=0.15, relheight=0.82
                , relwidth=0.909)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font14)
        self.Labelframe1.configure(foreground="#fff")
        self.Labelframe1.configure(text='''Checkup Report''')
        self.Labelframe1.configure(background="#455a64")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=750)

        self.Label3_6 = Label(self.Labelframe1)
        self.Label3_6.place(relx=0.12, rely=0.11, height=29, width=105
                , bordermode='ignore')
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#455a64")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font13)
        self.Label3_6.configure(foreground="#fff")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="black")
        self.Label3_6.configure(text='''Problem''')

        self.Labelframe2 = LabelFrame(self.Labelframe1)
        self.Labelframe2.place(relx=0.04, rely=0.275, relheight=0.67
                , relwidth=0.92, bordermode='ignore')
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(font=font14)
        self.Labelframe2.configure(foreground="#fff")
        self.Labelframe2.configure(text='''Medicines''')
        self.Labelframe2.configure(background="#455a64")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=690)

        self.Label3_1 = Label(self.Labelframe2)
        self.Label3_1.place(relx=0.043, rely=0.137, height=29, width=155
                , bordermode='ignore')
        self.Label3_1.configure(activebackground="#f9f9f9")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#455a64")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font=font13)
        self.Label3_1.configure(foreground="#fff")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Enter Medicine :''')

        def key1(event):
            global med
            x=str(self.Entry1.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1.delete("1.0","end")
            self.Entry1.config(state=NORMAL)
            self.Entry1.mark_set("insert","0.0")
            self.Entry1.insert("1.0","%s"% b)
            self.Entry1.mark_set("insert","0.0")

        self.Entry1 = Text(self.Labelframe2)
        self.Entry1.place(relx=0.275, rely=0.137, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.bind('<Return>', key1)


        def key2(event):
            global med
            x=str(self.Entry1_41.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1_41.delete("1.0","end")
            self.Entry1_41.config(state=NORMAL)
            self.Entry1_41.mark_set("insert","0.0")
            self.Entry1_41.insert("1.0","%s"% b)
            self.Entry1_41.mark_set("insert","0.0")

        self.Entry1_41 = Text(self.Labelframe2)
        self.Entry1_41.place(relx=0.275, rely=0.274, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1_41.configure(background="white")
        self.Entry1_41.configure(font=font10)
        self.Entry1_41.configure(foreground="#000000")
        self.Entry1_41.configure(highlightbackground="#d9d9d9")
        self.Entry1_41.configure(highlightcolor="black")
        self.Entry1_41.configure(insertbackground="black")
        self.Entry1_41.configure(selectbackground="#c4c4c4")
        self.Entry1_41.configure(selectforeground="black")
        self.Entry1_41.bind('<Return>', key2)

        def key3(event):

            global med
            x=str(self.Entry1_5.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1_5.delete("1.0","end")
            self.Entry1_5.config(state=NORMAL)
            self.Entry1_5.mark_set("insert","0.0")
            self.Entry1_5.insert("1.0","%s"% b)
            self.Entry1_5.mark_set("insert","0.0")


        self.Entry1_5 = Text(self.Labelframe2)
        self.Entry1_5.place(relx=0.275, rely=0.548, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(font=font10)
        self.Entry1_5.configure(foreground="#000000")
        self.Entry1_5.configure(highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black")
        self.Entry1_5.configure(insertbackground="black")
        self.Entry1_5.configure(selectbackground="#c4c4c4")
        self.Entry1_5.configure(selectforeground="black")
        self.Entry1_5.bind('<Return>', key3)

        def key4(event):

            global med
            x=str(self.Entry1_6.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1_6.delete("1.0","end")
            self.Entry1_6.config(state=NORMAL)
            self.Entry1_6.mark_set("insert","0.0")
            print b
            self.Entry1_6.insert("1.0","%s"% b)
            self.Entry1_6.mark_set("insert","0.0")


        self.Entry1_6 = Text(self.Labelframe2)
        self.Entry1_6.place(relx=0.275, rely=0.685, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1_6.configure(background="white")
        self.Entry1_6.configure(font=font10)
        self.Entry1_6.configure(foreground="#000000")
        self.Entry1_6.configure(highlightbackground="#d9d9d9")
        self.Entry1_6.configure(highlightcolor="black")
        self.Entry1_6.configure(insertbackground="black")
        self.Entry1_6.configure(selectbackground="#c4c4c4")
        self.Entry1_6.configure(selectforeground="black")
        self.Entry1_6.bind('<Return>', key4)


        def key5(event):
            global med
            x=str(self.Entry1_7.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1_7.delete("1.0","end")
            self.Entry1_7.config(state=NORMAL)
            self.Entry1_7.mark_set("insert","0.0")
            self.Entry1_7.insert("1.0","%s"% b)
            self.Entry1_7.mark_set("insert","0.0")


        self.Entry1_7 = Text(self.Labelframe2)
        self.Entry1_7.place(relx=0.275, rely=0.411, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1_7.configure(background="white")
        self.Entry1_7.configure(font=font10)
        self.Entry1_7.configure(foreground="#000000")
        self.Entry1_7.configure(highlightbackground="#d9d9d9")
        self.Entry1_7.configure(highlightcolor="black")
        self.Entry1_7.configure(insertbackground="black")
        self.Entry1_7.configure(selectbackground="#c4c4c4")
        self.Entry1_7.configure(selectforeground="black")
        self.Entry1_7.bind('<Return>', key5)


        def key6(event):
            global med
            x=str(self.Entry1_31.get("1.0",'end-1c')).strip()
            b =url_call(x)
            self.Entry1_31.delete("1.0","end")
            self.Entry1_31.config(state=NORMAL)
            self.Entry1_31.mark_set("insert","0.0")
            self.Entry1_31.insert("1.0","%s"% b)
            self.Entry1_31.mark_set("insert","0.0")

        self.Entry1_31 = Text(self.Labelframe2)
        self.Entry1_31.place(relx=0.275,rely=0.822, height=24, relwidth=0.296
                , bordermode='ignore')
        self.Entry1_31.configure(background="white")
        self.Entry1_31.configure(font=font10)
        self.Entry1_31.configure(foreground="#000000")
        self.Entry1_31.configure(highlightbackground="#d9d9d9")
        self.Entry1_31.configure(highlightcolor="black")
        self.Entry1_31.configure(insertbackground="black")
        self.Entry1_31.configure(selectbackground="#c4c4c4")
        self.Entry1_31.configure(selectforeground="black")
        self.Entry1_31.bind('<Return>', key6)


        self.Entry1_3 = Entry(self.Labelframe2)
        self.Entry1_3.place(relx=0.58, rely=0.137, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font=font10)
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="#c4c4c4")
        self.Entry1_3.configure(selectforeground="black")


        self.Entry1_19 = Entry(self.Labelframe2)
        self.Entry1_19.place(relx=0.58, rely=0.274, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_19.configure(background="white")
        self.Entry1_19.configure(disabledforeground="#a3a3a3")
        self.Entry1_19.configure(font=font10)
        self.Entry1_19.configure(foreground="#000000")
        self.Entry1_19.configure(highlightbackground="#d9d9d9")
        self.Entry1_19.configure(highlightcolor="black")
        self.Entry1_19.configure(insertbackground="black")
        self.Entry1_19.configure(selectbackground="#c4c4c4")
        self.Entry1_19.configure(selectforeground="black")

        self.Entry1_2 = Entry(self.Labelframe2)
        self.Entry1_2.place(relx=0.58, rely=0.411, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font=font10)
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.Entry1_1 = Entry(self.Labelframe2)
        self.Entry1_1.place(relx=0.58, rely=0.548, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font=font10)
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")

        self.Entry1_25 = Entry(self.Labelframe2)
        self.Entry1_25.place(relx=0.58, rely=0.685, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_25.configure(background="white")
        self.Entry1_25.configure(disabledforeground="#a3a3a3")
        self.Entry1_25.configure(font=font10)
        self.Entry1_25.configure(foreground="#000000")
        self.Entry1_25.configure(highlightbackground="#d9d9d9")
        self.Entry1_25.configure(highlightcolor="black")
        self.Entry1_25.configure(insertbackground="black")
        self.Entry1_25.configure(selectbackground="#c4c4c4")
        self.Entry1_25.configure(selectforeground="black")



        self.Entry1_4 = Entry(self.Labelframe2)
        self.Entry1_4.place(relx=0.58, rely=0.822, height=24, relwidth=0.194
                , bordermode='ignore')
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font=font10)
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")

        self.Text1 = Text(self.Labelframe1)
        self.Text1.place(relx=0.307, rely=0.11, relheight=0.062, relwidth=0.600
                , bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=680)
        self.Text1.configure(wrap=WORD)






        def logout():
            root.destroy()
            subprocess.call("python Gateway.py")

        self.Button2 = Button(self.Frame1,command=logout)
        self.Button2.place(relx=0.872, rely=0.077, height=43, width=129)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#455a64")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#fff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Logout''')

        def proceed():
                problem = self.Text1.get("1.0", "end-1c")          #Problem
                if not problem.strip():
                        self.Entry1.insert("1.0","Problem not specified")
                        self.Entry1_41.insert("1.0","Problem not specified")
                        self.Entry1_7.insert("1.0","Problem not specified")
                        self.Entry1_5.insert("1.0","Problem not specified")
                        self.Entry1_6.insert("1.0","Problem not specified")
                        self.Entry1_31.insert("1.0","Problem not specified")
                        return 
                med1 = self.Entry1.get("1.0", "end-1c")         #1/1 
                med2 = self.Entry1_41.get("1.0", "end-1c")      #2/1
                med3 = self.Entry1_7.get("1.0", "end-1c")       #3/1
                med4 = self.Entry1_5.get("1.0", "end-1c")      #4/1
                med5 = self.Entry1_6.get("1.0", "end-1c")       #5/1
                med6 = self.Entry1_31.get("1.0", "end-1c")      #6/1

                dosage1 = self.Entry1_3.get()                      #1/2
                dosage2 = self.Entry1_19.get()                    #2/2
                dosage3 = self.Entry1_2.get()                    #3/2
                dosage4 = self.Entry1_1.get()                     #4/2
                dosage5 = self.Entry1_25.get()                     #5/2
                dosage6 = self.Entry1_4.get()                      #6/2

                days1= self.Test.get()                         #1/3
                days2 = self.Test_1.get()  # 2/3
                days3 = self.Test_2.get()  # 3/3
                days4 = self.Test_3.get()  # 4/3
                days5 = self.Test_4.get()  # 5/3
                days6 = self.Test_5.get()  # 6/3
                
                dataArray = {
                    'Medicines': [med1, med2, med3, med4, med5, med6],
                    'Days': [days1, days2, days3, days4, days5, days6],
                    'Dosage': [dosage1, dosage2, dosage3, dosage4, dosage5, dosage6]
                }

                medList = [med1, med2, med3, med4, med5, med6]
                DaysList = [days1, days2, days3, days4, days5, days6]
                Dosageist = [dosage1, dosage2, dosage3, dosage4, dosage5, dosage6]
                df = pd.DataFrame(dataArray)

                filteredMedList = filter(None, medList)
                filteredDaysList = filter(None, DaysList)
                filteredDosageList = filter(None, Dosageist)

                df = df[['Medicines', 'Dosage', 'Days']]
                df_list = (df.values.tolist())

                with open("problemName.txt","w") as fptr:
                        fptr.write(str(time.strftime("%d-%m-%Y"))+"\n"+str(problem)+"\n")

                with open("presCurrent.csv", "w") as fptr:
                        for i in df_list:
                                fptr.write(str(i)+"\n")

                with open("presHistory.csv","a+") as fptr:
                        for i in df_list:
                                fptr.write(str(i)+"\n")
                
                MY_ADDRESS = 'dayzerodiag@gmail.com'


                PASSWORD = 'D@y0di@g'

                def main():

                        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
                        s.starttls()
                        s.login(MY_ADDRESS, PASSWORD)
                        with open("check.txt","r") as fptr:
                                name = fptr.readlines()
                        newStr = str(name[1]).lower()
                        newStr = newStr.replace(" ", ".")
                        newStr = newStr+"@vitap.ac.in"
                        with open("template.txt", 'w') as prescription:
                                compiledStr = " "
                                for i in range(0,len(filteredDaysList)):
                                        compiledStr = compiledStr +"---------------"+ "\n" + "Medicine : " + str(filteredMedList[i]) + "\n" + "Days : " + str(filteredDaysList[i]) + "\n" + "Dosage : "+str(filteredDosageList[i]) +"\n" +"---------------"+ "\n"
                                prescriptions = ""
                                prescriptions= prescriptions +"Dear "+str(name[1])+"\n"+",\nKindly find your prescription"+"\n"+"\n"+"Problem : "+str(problem) + "\n" +"\n" + compiledStr +"\nRegards\nDay Zero Diagnostics."
                                        
                                prescription.write(str(prescriptions))

                        msg = MIMEMultipart()
                        message = ''
                        with open("template.txt", 'r') as template_message:
                                message = template_message.read()

                        recipient = str(newStr)
                        recipient_list = ['ritwik1499@gmail.com', 'priyam.sahoo@vitap.ac.in',
                                        'akhil.surendran@vitap.ac.in', 'agnibha.chatterjee@vitap.ac.in']

                        msg['From'] = MY_ADDRESS
                        msg['To'] = ", ".join(recipient_list)
                        msg['Subject'] = 'Test Successful'

                        msg.attach(MIMEText(message, 'plain'))

                        s.sendmail(MY_ADDRESS, recipient, msg.as_string())
                        del msg

                        s.quit()
                main()
                print "email sent"

        self.Button1_1 = Button(self.Frame1)
        self.Button1_1.place(relx=0.854, rely=0.929, height=53, width=166)
        self.Button1_1.configure(activebackground="#d9d9d9")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#455a64")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(font=font14)
        self.Button1_1.configure(foreground="#fff")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Proceed''')
        self.Button1_1.configure(command=proceed)

        self.Message1_1 = Message(self.Frame1)
        self.Message1_1.place(relx=0.031, rely=0.929, relheight=0.055, relwidth=0.141)
        self.Message1_1.configure(anchor=W)
        self.Message1_1.configure(background="#263238")
        self.Message1_1.configure(font=font15)
        self.Message1_1.configure(foreground="#fff")
        self.Message1_1.configure(highlightbackground="#d9d9d9")
        self.Message1_1.configure(highlightcolor="black")
        self.Message1_1.configure(text='''Logged in as Admin''')
        self.Message1_1.configure(width=226)

        self.Message1_2 = Message(self.Frame1)
        self.Message1_2.place(relx=0.822, rely=0.131, relheight=0.055
                , relwidth=0.141)
        self.Message1_2.configure(anchor=E)
        self.Message1_2.configure(background="#263238")
        self.Message1_2.configure(font=font15)
        self.Message1_2.configure(foreground="#fff")
        self.Message1_2.configure(highlightbackground="#d9d9d9")
        self.Message1_2.configure(highlightcolor="black")
        self.Message1_2.configure(text=time.strftime("%X"))
        self.Message1_2.configure(width=226)

        self.Message1_3 = Message(self.Frame1)
        self.Message1_3.place(relx=0.779, rely=0.131, relheight=0.055
                , relwidth=0.141)
        self.Message1_3.configure(anchor=E)
        self.Message1_3.configure(background="#263238")
        self.Message1_3.configure(font=font15)
        self.Message1_3.configure(foreground="#fff")
        self.Message1_3.configure(highlightbackground="#d9d9d9")
        self.Message1_3.configure(highlightcolor="black")
        self.Message1_3.configure(text='''Login Time''')
        self.Message1_3.configure(width=226)

        self.Message1_4 = Message(self.Frame1)
        self.Message1_4.place(relx=0.729, rely=0.131, relheight=0.055
                , relwidth=0.141)
        self.Message1_4.configure(anchor=E)
        self.Message1_4.configure(background="#263238")
        self.Message1_4.configure(font=font15)
        self.Message1_4.configure(foreground="#fff")
        self.Message1_4.configure(highlightbackground="#d9d9d9")
        self.Message1_4.configure(highlightcolor="black")
        self.Message1_4.configure(text=time.strftime("%d/%m/%Y"))
        self.Message1_4.configure(width=226)

        self.Message1_5 = Message(self.Frame1)
        self.Message1_5.place(relx=0.667, rely=0.131, relheight=0.055
                , relwidth=0.141)
        self.Message1_5.configure(anchor=E)
        self.Message1_5.configure(background="#263238")
        self.Message1_5.configure(font=font15)
        self.Message1_5.configure(foreground="#fff")
        self.Message1_5.configure(highlightbackground="#d9d9d9")
        self.Message1_5.configure(highlightcolor="black")
        self.Message1_5.configure(text='''Date :''')
        self.Message1_5.configure(width=226)


#############################################################################
        self.Test = Entry(self.Labelframe2)
        self.Test.place(relx=0.783, rely=0.137, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test.configure(background="white")
        self.Test.configure(disabledforeground="#a3a3a3")
        self.Test.configure(font=font10)
        self.Test.configure(foreground="#000000")
        self.Test.configure(highlightbackground="#d9d9d9")
        self.Test.configure(highlightcolor="black")
        self.Test.configure(insertbackground="black")
        self.Test.configure(selectbackground="#c4c4c4")
        self.Test.configure(selectforeground="black")
        self.Test.configure(takefocus="0")
        self.Test.configure(width =114)


        self.Test_1 = Entry(self.Labelframe2)
        self.Test_1.place(relx=0.783, rely=0.274, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test_1.configure(background="white")
        self.Test_1.configure(disabledforeground="#a3a3a3")
        self.Test_1.configure(font=font10)
        self.Test_1.configure(foreground="#000000")
        self.Test_1.configure(highlightbackground="#d9d9d9")
        self.Test_1.configure(highlightcolor="black")
        self.Test_1.configure(insertbackground="black")
        self.Test_1.configure(selectbackground="#c4c4c4")
        self.Test_1.configure(selectforeground="black")
        self.Test_1.configure(takefocus="0")
        self.Test_1.configure(width =114)

        self.Test_2 = Entry(self.Labelframe2)
        self.Test_2.place(relx=0.783, rely=0.411, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test_2.configure(background="white")
        self.Test_2.configure(disabledforeground="#a3a3a3")
        self.Test_2.configure(font=font10)
        self.Test_2.configure(foreground="#000000")
        self.Test_2.configure(highlightbackground="#d9d9d9")
        self.Test_2.configure(highlightcolor="black")
        self.Test_2.configure(insertbackground="black")
        self.Test_2.configure(selectbackground="#c4c4c4")
        self.Test_2.configure(selectforeground="black")
        self.Test_2.configure(takefocus="0")
        self.Test_2.configure(width =114)



        self.Test_3 = Entry(self.Labelframe2)
        self.Test_3.place(relx=0.783, rely=0.548, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test_3.configure(background="white")
        self.Test_3.configure(disabledforeground="#a3a3a3")
        self.Test_3.configure(font=font10)
        self.Test_3.configure(foreground="#000000")
        self.Test_3.configure(highlightbackground="#d9d9d9")
        self.Test_3.configure(highlightcolor="black")
        self.Test_3.configure(insertbackground="black")
        self.Test_3.configure(selectbackground="#c4c4c4")
        self.Test_3.configure(selectforeground="black")
        self.Test_3.configure(takefocus="0")
        self.Test_3.configure(width =114)



        self.Test_4 = Entry(self.Labelframe2)
        self.Test_4.place(relx=0.783, rely=0.685, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test_4.configure(background="white")
        self.Test_4.configure(disabledforeground="#a3a3a3")
        self.Test_4.configure(font=font10)
        self.Test_4.configure(foreground="#000000")
        self.Test_4.configure(highlightbackground="#d9d9d9")
        self.Test_4.configure(highlightcolor="black")
        self.Test_4.configure(insertbackground="black")
        self.Test_4.configure(selectbackground="#c4c4c4")
        self.Test_4.configure(selectforeground="black")
        self.Test_4.configure(takefocus="0")
        self.Test_4.configure(width =114)



        self.Test_5 = Entry(self.Labelframe2)
        self.Test_5.place(relx=0.783, rely=0.822, height=24, relwidth=0.165
                , bordermode='ignore')
        self.Test_5.configure(background="white")
        self.Test_5.configure(disabledforeground="#a3a3a3")
        self.Test_5.configure(font=font10)
        self.Test_5.configure(foreground="#000000")
        self.Test_5.configure(highlightbackground="#d9d9d9")
        self.Test_5.configure(highlightcolor="black")
        self.Test_5.configure(insertbackground="black")
        self.Test_5.configure(selectbackground="#c4c4c4")
        self.Test_5.configure(selectforeground="black")
        self.Test_5.configure(takefocus="0")
        self.Test_5.configure(width =114)

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()
    #main()
