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

with open("myaccount.txt", "r") as fptr:
    z = fptr.readlines()
# print z
    x = z[0]
    y = z[1]


import medicalhistory_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Medical_History(root)
    medicalhistory_support.init(root, top)
    root.mainloop()


w = None


def create_Medical_History(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Medical_History(w)
    medicalhistory_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Medical_History():
    global w
    w.destroy()
    w = None


class Medical_History:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b'  # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8'  # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4'  # Closest X11 color: '{medium turquoise}'
        font11 = "-family {Product Sans} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x700+650+114")
        top.title("Medical History")
        top.configure(background="#455a64")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=-0.017, rely=0.0, height=108, width=674)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Medical History''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.217, rely=0.029, height=66, width=66)
        self.Button1.configure(activebackground="#263238")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#263238")
        self.Button1.configure(borderwidth="0")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./history (1).png"))
        self.Button1.configure(image=self._img1)
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.033, rely=0.186, height=27, width=103)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#455a64")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''My Account :''')

        self.Label2_1 = Label(top)
        self.Label2_1.place(relx=0.233, rely=0.186, height=27, width=183)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor=W)
        self.Label2_1.configure(background="#455a64")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font12)
        self.Label2_1.configure(foreground="#fff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text=y)

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.233, rely=0.229, height=27, width=163)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor=W)
        self.Label2_2.configure(background="#455a64")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text=x)

        self.Label2_3 = Label(top)
        self.Label2_3.place(relx=0.033, rely=0.943, height=27, width=103)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#455a64")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font12)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Logged in at :''')

        self.Label2_4 = Label(top)
        self.Label2_4.place(relx=0.217, rely=0.943, height=27, width=103)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(anchor=W)
        self.Label2_4.configure(background="#455a64")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#fff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text=time.strftime("%X"))

        self.Label2_5 = Label(top)
        self.Label2_5.place(relx=0.35, rely=0.943, height=27, width=33)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(anchor=W)
        self.Label2_5.configure(background="#455a64")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font12)
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''on''')

        self.Label2_6 = Label(top)
        self.Label2_6.place(relx=0.417, rely=0.943, height=27, width=103)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(anchor=W)
        self.Label2_6.configure(background="#455a64")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font12)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text=time.strftime("%d-%m-%Y"))

        def back():
            root.destroy()
            subprocess.call("python2 studdashscreen1.py")

        self.Button2 = Button(top)
        self.Button2.place(relx=0.833, rely=0.186, height=35, width=73)
        self.Button2.configure(activebackground="#263238")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#263238")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font13)
        self.Button2.configure(foreground="#fff")
        self.Button2.configure(highlightbackground="#5b9ed8")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Back''')
        self.Button2.configure(command=back)

        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.05, rely=0.3,
                           relheight=0.619, relwidth=0.888)
        self.Canvas1.configure(background="#263238")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=533)

        self.Label3 = Label(self.Canvas1)
        self.Label3.place(relx=0.056, rely=0.069, height=377, width=475)
        self.Label3.configure(anchor=NW)
        self.Label3.configure(background="#263238")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#FFF")
        self.Label3.configure(text='''Label''')
        self.Label3.configure(width=475)
        with open("template.txt", "r") as fpt:
            lines = fpt.readlines()
            if len(lines) < 2:
                self.Label3.configure(text="NO PREVIOUS PRESCRIPTIONS")
            else:
                output = ""
                for i in range(0, len(lines)):
                    output = output + lines[i] + "\n"
                self.Label3.configure(text=output)


if __name__ == '__main__':
    vp_start_gui()
