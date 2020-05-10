
import sys
from PIL import ImageTk
import PIL.Image
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

import Gateway_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Gateway (root)
    Gateway_support.init(root, top)
    root.mainloop()

w = None
def create_Gateway(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Gateway (w)
    Gateway_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Gateway():
    global w
    w.destroy()
    w = None


class Gateway:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b' # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8' # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4' # Closest X11 color: '{medium turquoise}'
        font11 = "-family Roboto -size 13 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 28 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Product Sans} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font15 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        root.state('zoomed')
        top.geometry("1600x900")
        top.title("Gateway")
        top.configure(background="#37474f")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Headline = Label(top)
        self.Headline.place(relx=0.0, rely=0.0, height=163, width=1599)
        self.Headline.configure(activebackground="#f9f9f9")
        self.Headline.configure(activeforeground="black")
        self.Headline.configure(background="#263238")
        self.Headline.configure(disabledforeground="#a3a3a3")
        self.Headline.configure(font=font12)
        self.Headline.configure(foreground="#fff")
        self.Headline.configure(highlightbackground="#d9d9d9")
        self.Headline.configure(highlightcolor="black")
        self.Headline.configure(text='''Health App''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.381, rely=0.956, height=27, width=361)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#37474f")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font15)
        self.Label5.configure(foreground="#fff")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Copyright 2018, Health App. All Rights Reserved''')

        self.Label2_6 = Label(top)
        self.Label2_6.place(relx=0.188, rely=0.278, height=37, width=179)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#37474f")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font13)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''Welcome''')






        self.DrButton_6 = Button(top)
        self.DrButton_6.place(relx=0.131, rely=0.411, height=243, width=346)
        self.DrButton_6.configure(activebackground="#37474f")
        self.DrButton_6.configure(activeforeground="white")
        self.DrButton_6.configure(activeforeground="#000000")
        self.DrButton_6.configure(background="#37474f")
        self.DrButton_6.configure(borderwidth="0")
        self.DrButton_6.configure(disabledforeground="#a3a3a3")
        self.DrButton_6.configure(font=font11)
        self.DrButton_6.configure(foreground="#fff")
        self.DrButton_6.configure(highlightbackground="#455a64")
        self.DrButton_6.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./applogogateway.png"))
        self.DrButton_6.configure(image=self._img1)
        self.DrButton_6.configure(pady="0")
        self.DrButton_6.configure(relief=GROOVE)
        self.DrButton_6.configure(text='''Doctor''')





        self.Message1_7 = Message(top)
        self.Message1_7.place(relx=0.069, rely=0.689, relheight=0.222
                , relwidth=0.348)
        self.Message1_7.configure(background="#37474f")
        self.Message1_7.configure(font=font14)
        self.Message1_7.configure(foreground="#fff")
        self.Message1_7.configure(highlightbackground="#d9d9d9")
        self.Message1_7.configure(highlightcolor="black")
        self.Message1_7.configure(justify=CENTER)
        self.Message1_7.configure(text='''Hey There! Thank you for choosing //Health App//.
This application is a health management system integrated with the latest technologies.

Please select one of the modes to access the Application.''')
        self.Message1_7.configure(width=556)

        self.Label3_5 = Label(top)
        self.Label3_5.place(relx=0.681, rely=0.278, height=34, width=242)
        self.Label3_5.configure(activebackground="#f9f9f9")
        self.Label3_5.configure(activeforeground="black")
        self.Label3_5.configure(background="#37474f")
        self.Label3_5.configure(disabledforeground="#a3a3a3")
        self.Label3_5.configure(font=font13)
        self.Label3_5.configure(foreground="#fff")
        self.Label3_5.configure(highlightbackground="#d9d9d9")
        self.Label3_5.configure(highlightcolor="black")
        self.Label3_5.configure(text='''Select a mode''')

        def student_nav():
            root.destroy()
            subprocess.call("python studentauth.py")


        self.StudentButton = Button(top)
        self.StudentButton.place(relx=0.781, rely=0.433, height=263, width=266)
        self.StudentButton.configure(activebackground="#37474f")
        self.StudentButton.configure(activeforeground="white")
        self.StudentButton.configure(activeforeground="#000000")
        self.StudentButton.configure(background="#37474f")
        self.StudentButton.configure(borderwidth="0")
        self.StudentButton.configure(disabledforeground="#a3a3a3")
        self.StudentButton.configure(font=font11)
        self.StudentButton.configure(foreground="#fff")
        self.StudentButton.configure(highlightbackground="#455a64")
        self.StudentButton.configure(highlightcolor="black")
        self._img2 = ImageTk.PhotoImage(PIL.Image.open("./reading (1).png"))
        self.StudentButton.configure(image=self._img2)
        self.StudentButton.configure(pady="0")
        self.StudentButton.configure(relief=GROOVE)
        self.StudentButton.configure(text='''Student''')
        self.StudentButton.configure(command = student_nav)




        def doctor_nav():
            root.destroy()
            subprocess.call("python adminauth.py")

        self.DrButton = Button(top,command=doctor_nav)
        self.DrButton.place(relx=0.563, rely=0.433, height=263, width=266)
        self.DrButton.configure(activebackground="#37474f")
        self.DrButton.configure(activeforeground="white")
        self.DrButton.configure(activeforeground="#000000")
        self.DrButton.configure(background="#37474f")
        self.DrButton.configure(borderwidth="0")
        self.DrButton.configure(disabledforeground="#a3a3a3")
        self.DrButton.configure(font=font11)
        self.DrButton.configure(foreground="#fff")
        self.DrButton.configure(highlightbackground="#455a64")
        self.DrButton.configure(highlightcolor="black")
        self._img3 = ImageTk.PhotoImage(PIL.Image.open("./doctor (1).png"))
        self.DrButton.configure(image=self._img3)
        self.DrButton.configure(pady="0")
        self.DrButton.configure(relief=GROOVE)
        self.DrButton.configure(text='''Doctor''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.5, rely=0.211, relheight=0.733)
        self.TSeparator1.configure(orient="vertical")






if __name__ == '__main__':
    vp_start_gui()
