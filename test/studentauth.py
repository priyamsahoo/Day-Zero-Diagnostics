
import sys
from PIL import ImageTk
import PIL.Image
import subprocess
import csv

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

filename = "student_database.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        rows.append(row)














import studentauth_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Student_Authentication___Health_App (root)
    studentauth_support.init(root, top)
    root.mainloop()

w = None
def create_Student_Authentication___Health_App(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Student_Authentication___Health_App (w)
    studentauth_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_Authentication___Health_App():
    global w
    w.destroy()
    w = None


class Student_Authentication___Health_App:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b' # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8' # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4' # Closest X11 color: '{medium turquoise}'
        font12 = "-family Roboto -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family Roboto -size 13 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family Roboto -size 9 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        w = (ws/2) - (700/2)
        h = ((hs-50)/2) - (750/2)
        top.geometry("700x750+%d+%d" %(w,h))
        top.title("Student Authentication : Health App")
        top.configure(background="#5b9ed8")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=-0.014, rely=-0.013, relheight=1.02
                , relwidth=1.021)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#263238")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=715)

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.14, rely=0.209, relheight=0.712, relwidth=0.734)

        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#37474f")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=525)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.324, rely=0.936, height=26, width=173)
        self.Label2.configure(activebackground="#37474f")
        self.Label2.configure(activeforeground="white")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#37474f")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''* Authentication required''')

        self.Label3 = Label(self.Frame2)
        self.Label3.place(relx=0.267, rely=0.349, height=29, width=241)
        self.Label3.configure(activebackground="#37474f")
        self.Label3.configure(activeforeground="white")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#37474f")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#fff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Student Login''')

        self.Label3_1 = Label(self.Frame2)
        self.Label3_1.place(relx=0.095, rely=0.495, height=29, width=121)
        self.Label3_1.configure(activebackground="#37474f")
        self.Label3_1.configure(activeforeground="white")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(background="#37474f")
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(font=font12)
        self.Label3_1.configure(foreground="#fff")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        self.Label3_1.configure(text='''Username*''')

        self.Label3_2 = Label(self.Frame2)
        self.Label3_2.place(relx=0.095, rely=0.624, height=29, width=121)
        self.Label3_2.configure(activebackground="#37474f")
        self.Label3_2.configure(activeforeground="white")
        self.Label3_2.configure(activeforeground="black")
        self.Label3_2.configure(background="#37474f")
        self.Label3_2.configure(disabledforeground="#a3a3a3")
        self.Label3_2.configure(font=font12)
        self.Label3_2.configure(foreground="#fff")
        self.Label3_2.configure(highlightbackground="#d9d9d9")
        self.Label3_2.configure(highlightcolor="black")
        self.Label3_2.configure(text='''Password*''')

        self.Text1 = Text(self.Frame2)
        self.Text1.place(relx=0.457, rely=0.495, relheight=0.062, relwidth=0.408)

        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#5b9ed8")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=214)
        self.Text1.configure(wrap=WORD)

        self.Text1_3 = Entry(self.Frame2,show="*")
        self.Text1_3.place(relx=0.457, rely=0.606, relheight=0.062
                , relwidth=0.408)
        self.Text1_3.configure(background="white")
        self.Text1_3.configure(font=font9)
        self.Text1_3.configure(foreground="black")
        self.Text1_3.configure(highlightbackground="#5b9ed8")
        self.Text1_3.configure(highlightcolor="black")
        self.Text1_3.configure(insertbackground="black")
        self.Text1_3.configure(selectbackground="#c4c4c4")
        self.Text1_3.configure(selectforeground="black")
        self.Text1_3.configure(width=214)

        def login():
            self.input1 = str(self.Text1.get("1.0",'end-1c')).strip().upper()
            self.input2 = str(self.Text1_3.get()).strip()
            reg_no=[]
            name=[]
            for i in enumerate(rows):
                l = i[1]
                reg_no.append(l[0])
                name.append(l[1])
            for iter in range(len(reg_no)):
                if self.input1 == reg_no[iter] and (self.input2 == "test" ) :
                    final_reg = str(reg_no[iter])
                    final_name = str(name[iter])
                    with open("myaccount.txt","w") as fptr:
                        fptr.write(final_reg)
                        fptr.write("\n")
                        fptr.write(final_name)

                    root.destroy()
                    subprocess.call("python2 studdashscreen1.py")

        self.Button1 = Button(self.Frame2)
        self.Button1.place(relx=0.4, rely=0.789, height=43, width=97)
        self.Button1.configure(activebackground="#5bd8d4")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#212121")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font14)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(command = login)

        self.Button2 = Button(self.Frame2)
        self.Button2.place(relx=0.362, rely=0.092, height=83, width=136)
        self.Button2.configure(activebackground="#37474f")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#37474f")
        self.Button2.configure(borderwidth="0")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#5b9ed8")
        self.Button2.configure(highlightcolor="black")
        self._img1 =  ImageTk.PhotoImage(PIL.Image.open("./studentlogin.png"))
        self.Button2.configure(image=self._img1)
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')
        self.Button2.configure(width=136)

        self.Button2_1 = Button(self.Frame1)
        self.Button2_1.place(relx=0.434, rely=0.052, height=93, width=96)
        self.Button2_1.configure(activebackground="#263238")
        self.Button2_1.configure(activeforeground="white")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#263238")
        self.Button2_1.configure(borderwidth="0")
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightbackground="#5b9ed8")
        self.Button2_1.configure(highlightcolor="black")
        self._img2 =  ImageTk.PhotoImage(PIL.Image.open("./logo.png"))
        self.Button2_1.configure(image=self._img2)
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text='''Button''')
        self.Button2_1.configure(width=96)






if __name__ == '__main__':
    vp_start_gui()
