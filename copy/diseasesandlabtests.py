
import sys
import sys
import time
import ast
import subprocess
from disease import *
from lab_test import *

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






import diseasesandlabtests_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Student_Services___Diseases (root)
    diseasesandlabtests_support.init(root, top)
    root.mainloop()

w = None
def create_Student_Services___Diseases(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Student_Services___Diseases (w)
    diseasesandlabtests_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Student_Services___Diseases():
    global w
    w.destroy()
    w = None


class Student_Services___Diseases:
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
        font14 = "-family {Product Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font17 = "-family {Product Sans} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1600x900+110+62")
        root.state("zoomed")
        top.title("Student Services : Diseases")
        top.configure(background="#455a64")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=156, width=1604)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Diseases & Lab Tests''')


        def back():
            root.destroy()
            subprocess.call("python studdashscreen1.py")




        self.Button1 = Button(top)
        self.Button1.place(relx=0.938, rely=0.2, height=35, width=73)
        self.Button1.configure(activebackground="#263238")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#263238")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Back''')
        self.Button1.configure(command = back)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.019, rely=0.2, height=27, width=103)
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
        self.Label2_1.place(relx=0.094, rely=0.2, height=27, width=103)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#455a64")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font12)
        self.Label2_1.configure(foreground="#fff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text=y)

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.231, rely=0.2, height=27, width=103)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#455a64")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text=x)

        self.Label2_3 = Label(top)
        self.Label2_3.place(relx=0.019, rely=0.956, height=27, width=103)
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
        self.Label2_4.place(relx=0.094, rely=0.956, height=27, width=103)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#455a64")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#fff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text=time.strftime("%X"))

        self.Label2_5 = Label(top)
        self.Label2_5.place(relx=0.156, rely=0.956, height=27, width=33)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#455a64")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font12)
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''on''')

        self.Label2_6 = Label(top)
        self.Label2_6.place(relx=0.188, rely=0.956, height=27, width=103)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#455a64")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font12)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text=time.strftime("%d-%m-%Y"))

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.019, rely=0.344, relheight=0.094
                , relwidth=0.434)
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(background="#263238")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=695)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.029, rely=0.353, height=31, width=70)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#263238")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font14)
        self.Label4.configure(foreground="#fff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Search''')

        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.158, rely=0.353, relheight=0.4, relwidth=0.725)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#5b9ed8")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=504)
        self.Text1.configure(wrap=WORD)

        def onClickDisease():
             DiseaseName = self.Text1.get("1.0", "end-1c")
             if not DiseaseName.strip():
                self.Label5.configure(text="No disease found")
                self.Label5_131.configure(text="No disease found")
                self.Label5_145.configure(text="No disease found")
             else:
                diseaseFunc(DiseaseName)
                with open("diseaseData.txt", "r") as fptr:
                    disData = fptr.read()
                if len(disData) < 2:
                    self.Label5.configure(text="None")
                    self.Label5_131.configure(text="None")
                    self.Label5_145.configure(text="None")
                else:
                    disData = str(disData)
                    data = ast.literal_eval(disData)
                    self.Label5.configure(text=data[0]['disease_name'])
                    self.Label5_131.configure(text=data[0]['disease_cat'])
                    self.Label5_145.configure(text=data[0]['disease_info'])

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.906, rely=0.353, height=35, width=39)
        self.Button1.configure(activebackground="#263238")
        self.Button1.configure(activeforeground="white")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#263238")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font15)
        self.Button1.configure(foreground="#fff")
        self.Button1.configure(highlightbackground="#5b9ed8")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Go''')
        self.Button1.configure(command=onClickDisease)

        self.Label3 = Label(top)
        self.Label3.place(relx=0.194, rely=0.278, height=48, width=141)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#455a64")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font17)
        self.Label3.configure(foreground="#fff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Diseases''')

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.019, rely=0.456, relheight=0.072
                , relwidth=0.434)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#263238")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=695)

        self.Label4_8 = Label(self.Frame2)
        self.Label4_8.place(relx=0.029, rely=0.308, height=31, width=70)
        self.Label4_8.configure(activebackground="#f9f9f9")
        self.Label4_8.configure(activeforeground="black")
        self.Label4_8.configure(background="#263238")
        self.Label4_8.configure(disabledforeground="#a3a3a3")
        self.Label4_8.configure(font=font14)
        self.Label4_8.configure(foreground="#fff")
        self.Label4_8.configure(highlightbackground="#d9d9d9")
        self.Label4_8.configure(highlightcolor="black")
        self.Label4_8.configure(text='''Name :''')

        self.Label5 = Label(self.Frame2)
        self.Label5.place(relx=0.144, rely=0.308, height=27, width=395)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor=W)
        self.Label5.configure(background="#263238")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font12)
        self.Label5.configure(foreground="#fff")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Label''')

        self.Frame2_7 = Frame(top)
        self.Frame2_7.place(relx=0.019, rely=0.544, relheight=0.072
                , relwidth=0.434)
        self.Frame2_7.configure(relief=GROOVE)
        self.Frame2_7.configure(borderwidth="2")
        self.Frame2_7.configure(relief=GROOVE)
        self.Frame2_7.configure(background="#263238")
        self.Frame2_7.configure(highlightbackground="#d9d9d9")
        self.Frame2_7.configure(highlightcolor="black")
        self.Frame2_7.configure(width=695)

        self.Label4_9 = Label(self.Frame2_7)
        self.Label4_9.place(relx=0.029, rely=0.308, height=31, width=100)
        self.Label4_9.configure(activebackground="#f9f9f9")
        self.Label4_9.configure(activeforeground="black")
        self.Label4_9.configure(background="#263238")
        self.Label4_9.configure(disabledforeground="#a3a3a3")
        self.Label4_9.configure(font=font14)
        self.Label4_9.configure(foreground="#fff")
        self.Label4_9.configure(highlightbackground="#d9d9d9")
        self.Label4_9.configure(highlightcolor="black")
        self.Label4_9.configure(text='''Category :''')

        self.Label5_131 = Label(self.Frame2_7)
        self.Label5_131.place(relx=0.216, rely=0.308, height=27, width=515)
        self.Label5_131.configure(activebackground="#f9f9f9")
        self.Label5_131.configure(activeforeground="black")
        self.Label5_131.configure(anchor=W)
        self.Label5_131.configure(background="#263238")
        self.Label5_131.configure(disabledforeground="#a3a3a3")
        self.Label5_131.configure(font=font12)
        self.Label5_131.configure(foreground="#fff")
        self.Label5_131.configure(highlightbackground="#d9d9d9")
        self.Label5_131.configure(highlightcolor="black")
        self.Label5_131.configure(text='''Label''')
        self.Label5_131.configure(width=515)

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.019, rely=0.633, relheight=0.306
                , relwidth=0.434)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#263238")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")
        self.Frame3.configure(width=695)

        self.Label4_10 = Label(self.Frame3)
        self.Label4_10.place(relx=0.029, rely=0.073, height=31, width=160)
        self.Label4_10.configure(activebackground="#f9f9f9")
        self.Label4_10.configure(activeforeground="black")
        self.Label4_10.configure(background="#263238")
        self.Label4_10.configure(disabledforeground="#a3a3a3")
        self.Label4_10.configure(font=font14)
        self.Label4_10.configure(foreground="#fff")
        self.Label4_10.configure(highlightbackground="#d9d9d9")
        self.Label4_10.configure(highlightcolor="black")
        self.Label4_10.configure(text='''More Information''')

        self.Label5_145 = Label(self.Frame3)
        self.Label5_145.place(relx=0.029, rely=0.255, height=177, width=645)
        self.Label5_145.configure(activebackground="#f9f9f9")
        self.Label5_145.configure(activeforeground="black")
        self.Label5_145.configure(anchor=NW)
        self.Label5_145.configure(background="#263238")
        self.Label5_145.configure(disabledforeground="#a3a3a3")
        self.Label5_145.configure(font=font12)
        self.Label5_145.configure(foreground="#fff")
        self.Label5_145.configure(highlightbackground="#d9d9d9")
        self.Label5_145.configure(highlightcolor="black")
        self.Label5_145.configure(justify=LEFT)
        self.Label5_145.configure(text='''Label''')
        self.Label5_145.configure(width=645)
        self.Label5_145.configure(wraplength=635)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.463, rely=0.3, relheight=0.644)
        self.TSeparator1.configure(orient="vertical")

        self.Label3_11 = Label(top)
        self.Label3_11.place(relx=0.675, rely=0.278, height=40, width=165)
        self.Label3_11.configure(activebackground="#f9f9f9")
        self.Label3_11.configure(activeforeground="black")
        self.Label3_11.configure(background="#455a64")
        self.Label3_11.configure(disabledforeground="#a3a3a3")
        self.Label3_11.configure(font=font17)
        self.Label3_11.configure(foreground="#fff")
        self.Label3_11.configure(highlightbackground="#d9d9d9")
        self.Label3_11.configure(highlightcolor="black")
        self.Label3_11.configure(text='''Lab Tests''')
        self.Label3_11.configure(width=165)

        self.Frame4 = Frame(top)
        self.Frame4.place(relx=0.475, rely=0.344, relheight=0.094
                , relwidth=0.509)
        self.Frame4.configure(relief=RAISED)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=RAISED)
        self.Frame4.configure(background="#263238")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")
        self.Frame4.configure(width=815)

        self.Label4_12 = Label(self.Frame4)
        self.Label4_12.place(relx=0.037, rely=0.353, height=31, width=70)
        self.Label4_12.configure(activebackground="#f9f9f9")
        self.Label4_12.configure(activeforeground="black")
        self.Label4_12.configure(background="#263238")
        self.Label4_12.configure(disabledforeground="#a3a3a3")
        self.Label4_12.configure(font=font14)
        self.Label4_12.configure(foreground="#fff")
        self.Label4_12.configure(highlightbackground="#d9d9d9")
        self.Label4_12.configure(highlightcolor="black")
        self.Label4_12.configure(text='''Search''')

        self.Text1_13 = Text(self.Frame4)
        self.Text1_13.place(relx=0.135, rely=0.353, relheight=0.4
                , relwidth=0.766)
        self.Text1_13.configure(background="white")
        self.Text1_13.configure(font=font9)
        self.Text1_13.configure(foreground="black")
        self.Text1_13.configure(highlightbackground="#5b9ed8")
        self.Text1_13.configure(highlightcolor="black")
        self.Text1_13.configure(insertbackground="black")
        self.Text1_13.configure(selectbackground="#c4c4c4")
        self.Text1_13.configure(selectforeground="black")
        self.Text1_13.configure(width=624)
        self.Text1_13.configure(wrap=WORD)

        def onClickLab():
            LabName = self.Text1_13.get("1.0", "end-1c")
            if not LabName.strip():
                self.Label5_15.configure(text="No such test found")
                self.Label5_16.configure(text="No such test found")
                self.Label5_17.configure(text="No such test found")
                self.Label5_18.configure(text="No such test found")
                self.Label5_19.configure(text="No such test found")
                self.Label5_20.configure(text="No such test found")
                self.Label5_14.configure(text="No such test found")
            else:
                labFunc(LabName)
                with open("labData.txt", "r") as fptr:
                    disData = fptr.read()
                if len(disData) < 2:
                    self.Label5_15.configure(text="None")
                    self.Label5_16.configure(text="None")
                    self.Label5_17.configure(text="None")
                    self.Label5_18.configure(text="None")
                    self.Label5_19.configure(text="None")
                    self.Label5_20.configure(text="None")
                    self.Label5_14.configure(text="None")
                else:
                    disData = str(disData)
                    data = ast.literal_eval(disData)
                    self.Label5_15.configure(text=data[0]['lab_test_name'])
                    self.Label5_16.configure(
                        text=data[0]['lab_test_data']['Test Code'])
                    self.Label5_17.configure(text=data[0]['alternate_name'])
                    self.Label5_18.configure(
                        text=data[0]['lab_test_data']['Frequency'])
                    self.Label5_19.configure(
                        text=data[0]['lab_test_data']['Laboratory'])
                    self.Label5_20.configure(
                        text=data[0]['lab_test_data']['Specimen types'])
                    self.Label5_14.configure(
                        text=str(data[0]['lab_test_name'][1]))

        self.Button1_14 = Button(self.Frame4)
        self.Button1_14.place(relx=0.92, rely=0.353, height=35, width=39)
        self.Button1_14.configure(activebackground="#263238")
        self.Button1_14.configure(activeforeground="white")
        self.Button1_14.configure(activeforeground="#000000")
        self.Button1_14.configure(background="#263238")
        self.Button1_14.configure(disabledforeground="#a3a3a3")
        self.Button1_14.configure(font=font15)
        self.Button1_14.configure(foreground="#fff")
        self.Button1_14.configure(highlightbackground="#5b9ed8")
        self.Button1_14.configure(highlightcolor="black")
        self.Button1_14.configure(pady="0")
        self.Button1_14.configure(text='''Go''')
        self.Button1_14.configure(command=onClickLab)

        self.Frame2_15 = Frame(top)
        self.Frame2_15.place(relx=0.475, rely=0.456, relheight=0.072
                , relwidth=0.297)
        self.Frame2_15.configure(relief=GROOVE)
        self.Frame2_15.configure(borderwidth="2")
        self.Frame2_15.configure(relief=GROOVE)
        self.Frame2_15.configure(background="#263238")
        self.Frame2_15.configure(highlightbackground="#d9d9d9")
        self.Frame2_15.configure(highlightcolor="black")
        self.Frame2_15.configure(width=475)

        self.Label4_10 = Label(self.Frame2_15)
        self.Label4_10.place(relx=0.042, rely=0.308, height=31, width=70)
        self.Label4_10.configure(activebackground="#f9f9f9")
        self.Label4_10.configure(activeforeground="black")
        self.Label4_10.configure(background="#263238")
        self.Label4_10.configure(disabledforeground="#a3a3a3")
        self.Label4_10.configure(font=font14)
        self.Label4_10.configure(foreground="#fff")
        self.Label4_10.configure(highlightbackground="#d9d9d9")
        self.Label4_10.configure(highlightcolor="black")
        self.Label4_10.configure(text='''Name :''')

        self.Label5_15 = Label(self.Frame2_15)
        self.Label5_15.place(relx=0.211, rely=0.308, height=27, width=335)
        self.Label5_15.configure(activebackground="#f9f9f9")
        self.Label5_15.configure(activeforeground="black")
        self.Label5_15.configure(anchor=W)
        self.Label5_15.configure(background="#263238")
        self.Label5_15.configure(disabledforeground="#a3a3a3")
        self.Label5_15.configure(font=font12)
        self.Label5_15.configure(foreground="#fff")
        self.Label5_15.configure(highlightbackground="#d9d9d9")
        self.Label5_15.configure(highlightcolor="black")
        self.Label5_15.configure(text='''Label''')
        self.Label5_15.configure(width=335)

        self.Frame2_10 = Frame(top)
        self.Frame2_10.place(relx=0.781, rely=0.456, relheight=0.072
                , relwidth=0.203)
        self.Frame2_10.configure(relief=GROOVE)
        self.Frame2_10.configure(borderwidth="2")
        self.Frame2_10.configure(relief=GROOVE)
        self.Frame2_10.configure(background="#263238")
        self.Frame2_10.configure(highlightbackground="#d9d9d9")
        self.Frame2_10.configure(highlightcolor="black")
        self.Frame2_10.configure(width=325)

        self.Label4_11 = Label(self.Frame2_10)
        self.Label4_11.place(relx=0.062, rely=0.308, height=31, width=110)
        self.Label4_11.configure(activebackground="#f9f9f9")
        self.Label4_11.configure(activeforeground="black")
        self.Label4_11.configure(background="#263238")
        self.Label4_11.configure(disabledforeground="#a3a3a3")
        self.Label4_11.configure(font=font14)
        self.Label4_11.configure(foreground="#fff")
        self.Label4_11.configure(highlightbackground="#d9d9d9")
        self.Label4_11.configure(highlightcolor="black")
        self.Label4_11.configure(text='''Test Code :''')

        self.Label5_16 = Label(self.Frame2_10)
        self.Label5_16.place(relx=0.462, rely=0.308, height=27, width=125)
        self.Label5_16.configure(activebackground="#f9f9f9")
        self.Label5_16.configure(activeforeground="black")
        self.Label5_16.configure(anchor=W)
        self.Label5_16.configure(background="#263238")
        self.Label5_16.configure(disabledforeground="#a3a3a3")
        self.Label5_16.configure(font=font12)
        self.Label5_16.configure(foreground="#fff")
        self.Label5_16.configure(highlightbackground="#d9d9d9")
        self.Label5_16.configure(highlightcolor="black")
        self.Label5_16.configure(text='''Label''')
        self.Label5_16.configure(width=125)

        self.Frame2_11 = Frame(top)
        self.Frame2_11.place(relx=0.475, rely=0.544, relheight=0.072
                , relwidth=0.297)
        self.Frame2_11.configure(relief=GROOVE)
        self.Frame2_11.configure(borderwidth="2")
        self.Frame2_11.configure(relief=GROOVE)
        self.Frame2_11.configure(background="#263238")
        self.Frame2_11.configure(highlightbackground="#d9d9d9")
        self.Frame2_11.configure(highlightcolor="black")
        self.Frame2_11.configure(width=475)

        self.Label4_11 = Label(self.Frame2_11)
        self.Label4_11.place(relx=0.042, rely=0.308, height=31, width=160)
        self.Label4_11.configure(activebackground="#f9f9f9")
        self.Label4_11.configure(activeforeground="black")
        self.Label4_11.configure(background="#263238")
        self.Label4_11.configure(disabledforeground="#a3a3a3")
        self.Label4_11.configure(font=font14)
        self.Label4_11.configure(foreground="#fff")
        self.Label4_11.configure(highlightbackground="#d9d9d9")
        self.Label4_11.configure(highlightcolor="black")
        self.Label4_11.configure(text='''Alternate Name :''')

        self.Label5_17 = Label(self.Frame2_11)
        self.Label5_17.place(relx=0.421, rely=0.308, height=27, width=255)
        self.Label5_17.configure(activebackground="#f9f9f9")
        self.Label5_17.configure(activeforeground="black")
        self.Label5_17.configure(anchor=W)
        self.Label5_17.configure(background="#263238")
        self.Label5_17.configure(disabledforeground="#a3a3a3")
        self.Label5_17.configure(font=font12)
        self.Label5_17.configure(foreground="#fff")
        self.Label5_17.configure(highlightbackground="#d9d9d9")
        self.Label5_17.configure(highlightcolor="black")
        self.Label5_17.configure(text='''Label''')
        self.Label5_17.configure(width=255)

        self.Frame2_12 = Frame(top)
        self.Frame2_12.place(relx=0.781, rely=0.544, relheight=0.072
                , relwidth=0.203)
        self.Frame2_12.configure(relief=GROOVE)
        self.Frame2_12.configure(borderwidth="2")
        self.Frame2_12.configure(relief=GROOVE)
        self.Frame2_12.configure(background="#263238")
        self.Frame2_12.configure(highlightbackground="#d9d9d9")
        self.Frame2_12.configure(highlightcolor="black")
        self.Frame2_12.configure(width=325)

        self.Label4_12 = Label(self.Frame2_12)
        self.Label4_12.place(relx=0.062, rely=0.308, height=31, width=110)
        self.Label4_12.configure(activebackground="#f9f9f9")
        self.Label4_12.configure(activeforeground="black")
        self.Label4_12.configure(background="#263238")
        self.Label4_12.configure(disabledforeground="#a3a3a3")
        self.Label4_12.configure(font=font14)
        self.Label4_12.configure(foreground="#fff")
        self.Label4_12.configure(highlightbackground="#d9d9d9")
        self.Label4_12.configure(highlightcolor="black")
        self.Label4_12.configure(text='''Frequency :''')

        self.Label5_18 = Label(self.Frame2_12)
        self.Label5_18.place(relx=0.431, rely=0.308, height=27, width=165)
        self.Label5_18.configure(activebackground="#f9f9f9")
        self.Label5_18.configure(activeforeground="black")
        self.Label5_18.configure(anchor=W)
        self.Label5_18.configure(background="#263238")
        self.Label5_18.configure(disabledforeground="#a3a3a3")
        self.Label5_18.configure(font=font12)
        self.Label5_18.configure(foreground="#fff")
        self.Label5_18.configure(highlightbackground="#d9d9d9")
        self.Label5_18.configure(highlightcolor="black")
        self.Label5_18.configure(text='''Label''')
        self.Label5_18.configure(width=165)

        self.Frame2_13 = Frame(top)
        self.Frame2_13.place(relx=0.475, rely=0.633, relheight=0.072
                , relwidth=0.509)
        self.Frame2_13.configure(relief=GROOVE)
        self.Frame2_13.configure(borderwidth="2")
        self.Frame2_13.configure(relief=GROOVE)
        self.Frame2_13.configure(background="#263238")
        self.Frame2_13.configure(highlightbackground="#d9d9d9")
        self.Frame2_13.configure(highlightcolor="black")
        self.Frame2_13.configure(width=815)

        self.Label4_12 = Label(self.Frame2_13)
        self.Label4_12.place(relx=0.025, rely=0.308, height=31, width=120)
        self.Label4_12.configure(activebackground="#f9f9f9")
        self.Label4_12.configure(activeforeground="black")
        self.Label4_12.configure(background="#263238")
        self.Label4_12.configure(disabledforeground="#a3a3a3")
        self.Label4_12.configure(font=font14)
        self.Label4_12.configure(foreground="#fff")
        self.Label4_12.configure(highlightbackground="#d9d9d9")
        self.Label4_12.configure(highlightcolor="black")
        self.Label4_12.configure(text='''Laboratory :''')

        self.Label5_19 = Label(self.Frame2_13)
        self.Label5_19.place(relx=0.196, rely=0.308, height=27, width=615)
        self.Label5_19.configure(activebackground="#f9f9f9")
        self.Label5_19.configure(activeforeground="black")
        self.Label5_19.configure(anchor=W)
        self.Label5_19.configure(background="#263238")
        self.Label5_19.configure(disabledforeground="#a3a3a3")
        self.Label5_19.configure(font=font12)
        self.Label5_19.configure(foreground="#fff")
        self.Label5_19.configure(highlightbackground="#d9d9d9")
        self.Label5_19.configure(highlightcolor="black")
        self.Label5_19.configure(text='''Label''')
        self.Label5_19.configure(width=615)

        self.Frame2_13 = Frame(top)
        self.Frame2_13.place(relx=0.475, rely=0.722, relheight=0.217
                , relwidth=0.297)
        self.Frame2_13.configure(relief=GROOVE)
        self.Frame2_13.configure(borderwidth="2")
        self.Frame2_13.configure(relief=GROOVE)
        self.Frame2_13.configure(background="#263238")
        self.Frame2_13.configure(highlightbackground="#d9d9d9")
        self.Frame2_13.configure(highlightcolor="black")
        self.Frame2_13.configure(width=475)

        self.Label4_12 = Label(self.Frame2_13)
        self.Label4_12.place(relx=0.042, rely=0.103, height=31, width=160)
        self.Label4_12.configure(activebackground="#f9f9f9")
        self.Label4_12.configure(activeforeground="black")
        self.Label4_12.configure(background="#263238")
        self.Label4_12.configure(disabledforeground="#a3a3a3")
        self.Label4_12.configure(font=font14)
        self.Label4_12.configure(foreground="#fff")
        self.Label4_12.configure(highlightbackground="#d9d9d9")
        self.Label4_12.configure(highlightcolor="black")
        self.Label4_12.configure(text='''Specimen Types :''')

        self.Label5_20 = Label(self.Frame2_13)
        self.Label5_20.place(relx=0.042, rely=0.359, height=97, width=415)
        self.Label5_20.configure(activebackground="#f9f9f9")
        self.Label5_20.configure(activeforeground="black")
        self.Label5_20.configure(anchor=NW)
        self.Label5_20.configure(background="#263238")
        self.Label5_20.configure(disabledforeground="#a3a3a3")
        self.Label5_20.configure(font=font12)
        self.Label5_20.configure(foreground="#fff")
        self.Label5_20.configure(highlightbackground="#d9d9d9")
        self.Label5_20.configure(highlightcolor="black")
        self.Label5_20.configure(justify=LEFT)
        self.Label5_20.configure(text='''Label''')

        self.Frame2_14 = Frame(top)
        self.Frame2_14.place(relx=0.781, rely=0.722, relheight=0.217
                , relwidth=0.203)
        self.Frame2_14.configure(relief=GROOVE)
        self.Frame2_14.configure(borderwidth="2")
        self.Frame2_14.configure(relief=GROOVE)
        self.Frame2_14.configure(background="#263238")
        self.Frame2_14.configure(highlightbackground="#d9d9d9")
        self.Frame2_14.configure(highlightcolor="black")
        self.Frame2_14.configure(width=325)

        self.Label4_13 = Label(self.Frame2_14)
        self.Label4_13.place(relx=0.062, rely=0.103, height=31, width=230)
        self.Label4_13.configure(activebackground="#f9f9f9")
        self.Label4_13.configure(activeforeground="black")
        self.Label4_13.configure(background="#263238")
        self.Label4_13.configure(disabledforeground="#a3a3a3")
        self.Label4_13.configure(font=font14)
        self.Label4_13.configure(foreground="#fff")
        self.Label4_13.configure(highlightbackground="#d9d9d9")
        self.Label4_13.configure(highlightcolor="black")
        self.Label4_13.configure(text='''Minimum Adult Volume :''')

        self.Label5_14 = Label(self.Frame2_14)
        self.Label5_14.place(relx=0.092, rely=0.359, height=77, width=255)
        self.Label5_14.configure(activebackground="#f9f9f9")
        self.Label5_14.configure(activeforeground="black")
        self.Label5_14.configure(anchor=NW)
        self.Label5_14.configure(background="#263238")
        self.Label5_14.configure(disabledforeground="#a3a3a3")
        self.Label5_14.configure(font=font12)
        self.Label5_14.configure(foreground="#fff")
        self.Label5_14.configure(highlightbackground="#d9d9d9")
        self.Label5_14.configure(highlightcolor="black")
        self.Label5_14.configure(justify=LEFT)
        self.Label5_14.configure(text='''Label''')
        self.Label5_14.configure(width=255)
"""

        self.Button2 = Button(top)
        self.Button2.place(relx=0.938, rely=0.2, height=35, width=73)
        self.Button2.configure(activebackground="#263238")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#263238")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font15)
        self.Button2.configure(foreground="#fff")
        self.Button2.configure(highlightbackground="#5b9ed8")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Back''')
        self.Button2.configure(width=73)
        self.Button2.configure(command=onClickLab)


"""



if __name__ == '__main__':
    vp_start_gui()
