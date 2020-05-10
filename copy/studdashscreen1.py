
import sys
from PIL import ImageTk
import PIL.Image
import time
import subprocess


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

with open("myaccount.txt","r") as fptr:
    z=fptr.readlines()
    #print z
    x=z[0]
    y=z[1]



import studdashscreen1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Student_Dashboard___Services (root)
    studdashscreen1_support.init(root, top)
    root.mainloop()

w = None
def create_Student_Dashboard___Services(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Student_Dashboard___Services (w)
    studdashscreen1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_Dashboard___Services():
    global w
    w.destroy()
    w = None


class Student_Dashboard___Services:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b' # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8' # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4' # Closest X11 color: '{medium turquoise}'
        font11 = "-family {Product Sans} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Product Sans} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Product Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1600x900+128+48")
        top.title("Student Dashboard : Services")
        top.configure(background="#455a64")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        root.state("zoomed")
        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=166, width=1602)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Dashboard : Student''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.019, rely=0.211, height=27, width=103)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor=W)
        self.Label2.configure(background="#455a64")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''My Account :''')

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.088, rely=0.211, height=27, width=163)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor=W)
        self.Label2_2.configure(background="#455a64")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text=y)

        self.Label2_3 = Label(top)
        self.Label2_3.place(relx=0.2, rely=0.211, height=27, width=103)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(anchor=W)
        self.Label2_3.configure(background="#455a64")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font12)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        #self.Label2_3.configure(text=x)

        self.Label2_4 = Label(top)
        self.Label2_4.place(relx=0.700, rely=0.211, height=27, width=113)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(anchor=W)
        self.Label2_4.configure(background="#455a64")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#fff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''Logged in at :''')

        self.Label2_5 = Label(top)
        self.Label2_5.place(relx=0.757, rely=0.211, height=27, width=70)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(anchor=W)
        self.Label2_5.configure(background="#455a64")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font12)
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text=time.strftime("%X"))

        self.Label2_6 = Label(top)
        self.Label2_6.place(relx=0.794, rely=0.211, height=27, width=33)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(anchor=W)
        self.Label2_6.configure(background="#455a64")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font12)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''on:''')

        self.Label2_1 = Label(top)
        self.Label2_1.place(relx=0.810, rely=0.211, height=27, width=113)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor=W)
        self.Label2_1.configure(background="#455a64")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font12)
        self.Label2_1.configure(foreground="#fff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(anchor = W)
        self.Label2_1.configure(text=time.strftime("%d/%m/%Y"))

        def logging_out():
            root.destroy()
            subprocess.call("python Gateway.py")


        self.Button1 = Button(top)
        self.Button1.place(relx=0.931, rely=0.211, height=35, width=71)
        self.Button1.configure(activebackground="#263238")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#263238")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Logout''')
        self.Button1.configure(command = logging_out)

        self.Label2_7 = Label(top)
        self.Label2_7.place(relx=0.45, rely=0.267, height=27, width=153)
        self.Label2_7.configure(activebackground="#f9f9f9")
        self.Label2_7.configure(activeforeground="black")
        self.Label2_7.configure(background="#455a64")
        self.Label2_7.configure(disabledforeground="#a3a3a3")
        self.Label2_7.configure(font=font14)
        self.Label2_7.configure(foreground="#fff")
        self.Label2_7.configure(highlightbackground="#d9d9d9")
        self.Label2_7.configure(highlightcolor="black")
        self.Label2_7.configure(text='''Services''')

        self.Frame1_10 = Frame(top)
        self.Frame1_10.place(relx=0.263, rely=0.344, relheight=0.617
                , relwidth=0.228)
        self.Frame1_10.configure(relief=GROOVE)
        self.Frame1_10.configure(borderwidth="1")
        self.Frame1_10.configure(relief=GROOVE)
        self.Frame1_10.configure(background="#263238")
        self.Frame1_10.configure(highlightbackground="#d9d9d9")
        self.Frame1_10.configure(highlightcolor="black")
        self.Frame1_10.configure(width=365)

        self.Button3_8 = Button(self.Frame1_10)
        self.Button3_8.place(relx=0.329, rely=0.126, height=130, width=130)
        self.Button3_8.configure(activebackground="#263238")
        self.Button3_8.configure(activeforeground="white")
        self.Button3_8.configure(activeforeground="#000000")
        self.Button3_8.configure(background="#263238")
        self.Button3_8.configure(borderwidth="0")
        self.Button3_8.configure(disabledforeground="#a3a3a3")
        self.Button3_8.configure(foreground="#000000")
        self.Button3_8.configure(highlightbackground="#5b9ed8")
        self.Button3_8.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./yoga.png"))
        self.Button3_8.configure(image=self._img1)
        self.Button3_8.configure(pady="0")
        self.Button3_8.configure(text='''Button''')

        self.Label2_9 = Label(self.Frame1_10)
        self.Label2_9.place(relx=0.247, rely=0.432, height=27, width=183)
        self.Label2_9.configure(activebackground="#f9f9f9")
        self.Label2_9.configure(activeforeground="black")
        self.Label2_9.configure(background="#263238")
        self.Label2_9.configure(disabledforeground="#a3a3a3")
        self.Label2_9.configure(font=font15)
        self.Label2_9.configure(foreground="#fff")
        self.Label2_9.configure(highlightbackground="#d9d9d9")
        self.Label2_9.configure(highlightcolor="black")
        self.Label2_9.configure(text='''Food & Exercise''')

        self.Message1_10 = Message(self.Frame1_10)
        self.Message1_10.place(relx=0.11, rely=0.577, relheight=0.164
                , relwidth=0.781)
        self.Message1_10.configure(anchor=N)
        self.Message1_10.configure(background="#263238")
        self.Message1_10.configure(font=font12)
        self.Message1_10.configure(foreground="#fff")
        self.Message1_10.configure(highlightbackground="#d9d9d9")
        self.Message1_10.configure(highlightcolor="black")
        self.Message1_10.configure(justify=CENTER)
        self.Message1_10.configure(text='''Having trouble with your diet? View this section to get help on food and exercise.''')
        self.Message1_10.configure(width=285)

        def food():
            root.destroy()
            subprocess.call("python foodandexercise.py")

        self.Button4_13 = Button(self.Frame1_10)
        self.Button4_13.place(relx=0.384, rely=0.829, height=35, width=84)
        self.Button4_13.configure(activebackground="#263238")
        self.Button4_13.configure(activeforeground="white")
        self.Button4_13.configure(activeforeground="#000000")
        self.Button4_13.configure(background="#263238")
        self.Button4_13.configure(disabledforeground="#a3a3a3")
        self.Button4_13.configure(font=font13)
        self.Button4_13.configure(foreground="#fff")
        self.Button4_13.configure(highlightbackground="#5b9ed8")
        self.Button4_13.configure(highlightcolor="black")
        self.Button4_13.configure(pady="0")
        self.Button4_13.configure(text='''View''')
        self.Button4_13.configure(command = food)

        self.Frame1_11 = Frame(top)
        self.Frame1_11.place(relx=0.506, rely=0.344, relheight=0.617
                , relwidth=0.228)
        self.Frame1_11.configure(relief=GROOVE)
        self.Frame1_11.configure(borderwidth="1")
        self.Frame1_11.configure(relief=GROOVE)
        self.Frame1_11.configure(background="#263238")
        self.Frame1_11.configure(highlightbackground="#d9d9d9")
        self.Frame1_11.configure(highlightcolor="black")
        self.Frame1_11.configure(width=365)

        self.Button3_9 = Button(self.Frame1_11)
        self.Button3_9.place(relx=0.301, rely=0.126, height=130, width=130)
        self.Button3_9.configure(activebackground="#263238")
        self.Button3_9.configure(activeforeground="white")
        self.Button3_9.configure(activeforeground="#000000")
        self.Button3_9.configure(background="#263238")
        self.Button3_9.configure(borderwidth="0")
        self.Button3_9.configure(disabledforeground="#a3a3a3")
        self.Button3_9.configure(foreground="#000000")
        self.Button3_9.configure(highlightbackground="#5b9ed8")
        self.Button3_9.configure(highlightcolor="black")
        self._img2 = ImageTk.PhotoImage(PIL.Image.open("./folder.png"))
        self.Button3_9.configure(image=self._img2)
        self.Button3_9.configure(pady="0")
        self.Button3_9.configure(text='''Button''')

        self.Label2_2 = Label(self.Frame1_11)
        self.Label2_2.place(relx=0.247, rely=0.432, height=27, width=173)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#263238")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font15)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''My Health Logs''')

        self.Message1_11 = Message(self.Frame1_11)
        self.Message1_11.place(relx=0.082, rely=0.577, relheight=0.164
                , relwidth=0.836)
        self.Message1_11.configure(anchor=N)
        self.Message1_11.configure(background="#263238")
        self.Message1_11.configure(font=font12)
        self.Message1_11.configure(foreground="#fff")
        self.Message1_11.configure(highlightbackground="#d9d9d9")
        self.Message1_11.configure(highlightcolor="black")
        self.Message1_11.configure(justify=CENTER)
        self.Message1_11.configure(text='''View all your health related logs here. Info on your hospital appointments, lab tests, and a lot more!''')
        self.Message1_11.configure(width=305)

        def health():
            root.destroy()
            subprocess.call("python medicalhistory.py")
        self.Button4_14 = Button(self.Frame1_11)
        self.Button4_14.place(relx=0.384, rely=0.829, height=35, width=84)
        self.Button4_14.configure(activebackground="#263238")
        self.Button4_14.configure(activeforeground="white")
        self.Button4_14.configure(activeforeground="#000000")
        self.Button4_14.configure(background="#263238")
        self.Button4_14.configure(disabledforeground="#a3a3a3")
        self.Button4_14.configure(font=font13)
        self.Button4_14.configure(foreground="#fff")
        self.Button4_14.configure(highlightbackground="#5b9ed8")
        self.Button4_14.configure(highlightcolor="black")
        self.Button4_14.configure(pady="0")
        self.Button4_14.configure(text='''View''')
        self.Button4_14.configure(command = health)

        self.Frame1_12 = Frame(top)
        self.Frame1_12.place(relx=0.75, rely=0.344, relheight=0.617
                , relwidth=0.234)
        self.Frame1_12.configure(relief=GROOVE)
        self.Frame1_12.configure(borderwidth="1")
        self.Frame1_12.configure(relief=GROOVE)
        self.Frame1_12.configure(background="#263238")
        self.Frame1_12.configure(highlightbackground="#d9d9d9")
        self.Frame1_12.configure(highlightcolor="black")
        self.Frame1_12.configure(width=375)

        self.Button3_10 = Button(self.Frame1_12)
        self.Button3_10.place(relx=0.32, rely=0.126, height=130, width=130)
        self.Button3_10.configure(activebackground="#263238")
        self.Button3_10.configure(activeforeground="white")
        self.Button3_10.configure(activeforeground="#000000")
        self.Button3_10.configure(background="#263238")
        self.Button3_10.configure(borderwidth="0")
        self.Button3_10.configure(disabledforeground="#a3a3a3")
        self.Button3_10.configure(foreground="#000000")
        self.Button3_10.configure(highlightbackground="#5b9ed8")
        self.Button3_10.configure(highlightcolor="black")
        self._img3 =  ImageTk.PhotoImage(PIL.Image.open("./bacteria.png"))
        self.Button3_10.configure(image=self._img3)
        self.Button3_10.configure(pady="0")
        self.Button3_10.configure(text='''Button''')

        self.Label2_3 = Label(self.Frame1_12)
        self.Label2_3.place(relx=0.293, rely=0.432, height=27, width=153)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#263238")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font15)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Diseases''')

        self.Message1_12 = Message(self.Frame1_12)
        self.Message1_12.place(relx=0.107, rely=0.577, relheight=0.164
                , relwidth=0.787)
        self.Message1_12.configure(anchor=N)
        self.Message1_12.configure(background="#263238")
        self.Message1_12.configure(font=font12)
        self.Message1_12.configure(foreground="#fff")
        self.Message1_12.configure(highlightbackground="#d9d9d9")
        self.Message1_12.configure(highlightcolor="black")
        self.Message1_12.configure(justify=CENTER)
        self.Message1_12.configure(text='''Check out this section for more information on diseases and their symptoms.''')
        self.Message1_12.configure(width=295)

        def disease():
            root.destroy()
            subprocess.call("python diseasesandlabtests.py")

        self.Button4_15 = Button(self.Frame1_12)
        self.Button4_15.place(relx=0.4, rely=0.829, height=35, width=84)
        self.Button4_15.configure(activebackground="#263238")
        self.Button4_15.configure(activeforeground="white")
        self.Button4_15.configure(activeforeground="#000000")
        self.Button4_15.configure(background="#263238")
        self.Button4_15.configure(disabledforeground="#a3a3a3")
        self.Button4_15.configure(font=font13)
        self.Button4_15.configure(foreground="#fff")
        self.Button4_15.configure(highlightbackground="#5b9ed8")
        self.Button4_15.configure(highlightcolor="black")
        self.Button4_15.configure(pady="0")
        self.Button4_15.configure(text='''View''')
        self.Button4_15.configure(command = disease)

        self.Frame1_4 = Frame(top)
        self.Frame1_4.place(relx=0.019, rely=0.344, relheight=0.617
                , relwidth=0.228)
        self.Frame1_4.configure(relief=GROOVE)
        self.Frame1_4.configure(borderwidth="1")
        self.Frame1_4.configure(relief=GROOVE)
        self.Frame1_4.configure(background="#263238")
        self.Frame1_4.configure(highlightbackground="#d9d9d9")
        self.Frame1_4.configure(highlightcolor="black")
        self.Frame1_4.configure(width=365)

        self.Button3_5 = Button(self.Frame1_4)
        self.Button3_5.place(relx=0.329, rely=0.126, height=130, width=130)
        self.Button3_5.configure(activebackground="#263238")
        self.Button3_5.configure(activeforeground="white")
        self.Button3_5.configure(activeforeground="#000000")
        self.Button3_5.configure(background="#263238")
        self.Button3_5.configure(borderwidth="0")
        self.Button3_5.configure(disabledforeground="#a3a3a3")
        self.Button3_5.configure(foreground="#000000")
        self.Button3_5.configure(highlightbackground="#5b9ed8")
        self.Button3_5.configure(highlightcolor="black")
        self._img4 =  ImageTk.PhotoImage(PIL.Image.open("./screen1drug.png"))
        self.Button3_5.configure(image=self._img4)
        self.Button3_5.configure(pady="0")
        self.Button3_5.configure(text='''Button''')

        self.Label2_10 = Label(self.Frame1_4)
        self.Label2_10.place(relx=0.247, rely=0.432, height=27, width=183)
        self.Label2_10.configure(activebackground="#f9f9f9")
        self.Label2_10.configure(activeforeground="black")
        self.Label2_10.configure(background="#263238")
        self.Label2_10.configure(disabledforeground="#a3a3a3")
        self.Label2_10.configure(font=font15)
        self.Label2_10.configure(foreground="#fff")
        self.Label2_10.configure(highlightbackground="#d9d9d9")
        self.Label2_10.configure(highlightcolor="black")
        self.Label2_10.configure(text='''Medicines''')

        self.Message1_6 = Message(self.Frame1_4)
        self.Message1_6.place(relx=0.11, rely=0.577, relheight=0.164
                , relwidth=0.781)
        self.Message1_6.configure(anchor=N)
        self.Message1_6.configure(background="#263238")
        self.Message1_6.configure(font=font12)
        self.Message1_6.configure(foreground="#fff")
        self.Message1_6.configure(highlightbackground="#d9d9d9")
        self.Message1_6.configure(highlightcolor="black")
        self.Message1_6.configure(justify=CENTER)
        self.Message1_6.configure(text='''Check out for more information on medicines, their side effects, substitutes, etc.''')
        self.Message1_6.configure(width=285)

        def medi_redirect():
            root.destroy()
            subprocess.call("python studentdashboard.py")


        self.Button4_12 = Button(self.Frame1_4)
        self.Button4_12.place(relx=0.384, rely=0.829, height=35, width=84)
        self.Button4_12.configure(activebackground="#263238")
        self.Button4_12.configure(activeforeground="white")
        self.Button4_12.configure(activeforeground="#000000")
        self.Button4_12.configure(background="#263238")
        self.Button4_12.configure(disabledforeground="#a3a3a3")
        self.Button4_12.configure(font=font13)
        self.Button4_12.configure(foreground="#fff")
        self.Button4_12.configure(highlightbackground="#5b9ed8")
        self.Button4_12.configure(highlightcolor="black")
        self.Button4_12.configure(pady="0")
        self.Button4_12.configure(text='''View''')
        self.Button4_12.configure(command = medi_redirect)






if __name__ == '__main__':
    vp_start_gui()
