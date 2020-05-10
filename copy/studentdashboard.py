
import sys
from PIL import ImageTk
import PIL.Image
import time
import os
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from medicine_details import *
import ast


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




import studentdashboard_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Dashboard___Student (root)
    studentdashboard_support.init(root, top)
    root.mainloop()

w = None
def create_Dashboard___Student(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Dashboard___Student (w)
    studentdashboard_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Dashboard___Student():
    global w
    w.destroy()
    w = None


class Dashboard___Student:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Product Sans} -size 14 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1600x900+316+34")
        top.title("Medicine")
        top.configure(background="#455a64")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")


        root.state("zoomed")
        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=136, width=1601)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Medicine Search and Information''')

        def back():
            root.destroy()
            subprocess.call("python studdashscreen1.py")




        self.Button1 = Button(top)
        self.Button1.place(relx=0.925, rely=0.178, height=43, width=89)
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
        self.Label2.place(relx=0.65, rely=0.178, height=27, width=115)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#455a64")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Logged in at :''')

        self.LogInTimeLabel = Label(top)
        self.LogInTimeLabel.place(relx=0.725, rely=0.178, height=27, width=95)
        self.LogInTimeLabel.configure(activebackground="#f9f9f9")
        self.LogInTimeLabel.configure(activeforeground="black")
        self.LogInTimeLabel.configure(background="#455a64")
        self.LogInTimeLabel.configure(disabledforeground="#a3a3a3")
        self.LogInTimeLabel.configure(font=font10)
        self.LogInTimeLabel.configure(foreground="#fff")
        self.LogInTimeLabel.configure(highlightbackground="#d9d9d9")
        self.LogInTimeLabel.configure(highlightcolor="black")
        self.LogInTimeLabel.configure(text=time.strftime("%X"))

        self.Label2_2 = Label(top)
        self.Label2_2.place(relx=0.788, rely=0.178, height=27, width=45)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#455a64")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font10)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''on''')

        self.LogInDateLabel = Label(top)
        self.LogInDateLabel.place(relx=0.819, rely=0.181, height=27, width=105)
        self.LogInDateLabel.configure(activebackground="#f9f9f9")
        self.LogInDateLabel.configure(activeforeground="black")
        self.LogInDateLabel.configure(background="#455a64")
        self.LogInDateLabel.configure(disabledforeground="#a3a3a3")
        self.LogInDateLabel.configure(font=font10)
        self.LogInDateLabel.configure(foreground="#fff")
        self.LogInDateLabel.configure(highlightbackground="#d9d9d9")
        self.LogInDateLabel.configure(highlightcolor="black")
        self.LogInDateLabel.configure(text=time.strftime("%d-%m-%Y"))

        self.Label2_4 = Label(top)
        self.Label2_4.place(relx=0.013, rely=0.178, height=27, width=115)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#455a64")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font10)
        self.Label2_4.configure(foreground="#fff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''My Account :''')

        self.StudNameLabel = Label(top)
        self.StudNameLabel.place(relx=0.075, rely=0.178, height=27, width=170)
        self.StudNameLabel.configure(activebackground="#f9f9f9")
        self.StudNameLabel.configure(activeforeground="black")
        self.StudNameLabel.configure(background="#455a64")
        self.StudNameLabel.configure(disabledforeground="#a3a3a3")
        self.StudNameLabel.configure(font=font10)
        self.StudNameLabel.configure(foreground="#fff")
        self.StudNameLabel.configure(highlightbackground="#d9d9d9")
        self.StudNameLabel.configure(highlightcolor="black")
        self.StudNameLabel.configure(text = y)
        self.StudNameLabel.configure(anchor = W)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.688, rely=0.244, relheight=0.15, relwidth=0.297)

        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(background="#263238")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=475)

        self.Button2_6 = Button(self.Frame1)
        self.Button2_6.place(relx=0.042, rely=0.148, height=96, width=76)
        self.Button2_6.configure(activebackground="#263238")
        self.Button2_6.configure(activeforeground="white")
        self.Button2_6.configure(activeforeground="#000000")
        self.Button2_6.configure(background="#263238")
        self.Button2_6.configure(borderwidth="0")
        self.Button2_6.configure(disabledforeground="#a3a3a3")
        self.Button2_6.configure(foreground="#fff")
        self.Button2_6.configure(highlightbackground="#5b9ed8")
        self.Button2_6.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./change.png"))
        self.Button2_6.configure(image=self._img1)
        self.Button2_6.configure(pady="0")
        self.Button2_6.configure(text='''Button''')

        self.Label2_7 = Label(self.Frame1)
        self.Label2_7.place(relx=0.253, rely=0.222, height=27, width=115)
        self.Label2_7.configure(activebackground="#263238")
        self.Label2_7.configure(activeforeground="white")
        self.Label2_7.configure(activeforeground="black")
        self.Label2_7.configure(anchor=W)
        self.Label2_7.configure(background="#263238")
        self.Label2_7.configure(disabledforeground="#a3a3a3")
        self.Label2_7.configure(font=font11)
        self.Label2_7.configure(foreground="#fff")
        self.Label2_7.configure(highlightbackground="#d9d9d9")
        self.Label2_7.configure(highlightcolor="black")
        self.Label2_7.configure(justify=RIGHT)
        self.Label2_7.configure(text='''Price''')

        self.PriceLabel = Label(self.Frame1)
        self.PriceLabel.place(relx=0.253, rely=0.519, height=46, width=272)
        self.PriceLabel.configure(activebackground="#f9f9f9")
        self.PriceLabel.configure(activeforeground="black")
        self.PriceLabel.configure(anchor=W)
        self.PriceLabel.configure(background="#263238")
        self.PriceLabel.configure(disabledforeground="#a3a3a3")
        self.PriceLabel.configure(font=font10)
        self.PriceLabel.configure(foreground="#fff")
        self.PriceLabel.configure(highlightbackground="#d9d9d9")
        self.PriceLabel.configure(highlightcolor="black")
        self.PriceLabel.configure(width=272)

        self.Frame1_1 = Frame(top)
        self.Frame1_1.place(relx=0.019, rely=0.244, relheight=0.15
                , relwidth=0.659)
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(background="#263238")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")
        self.Frame1_1.configure(width=1055)

        self.Frame1_2 = Frame(self.Frame1_1)
        self.Frame1_2.place(relx=0.559, rely=1.963, relheight=4.63
                , relwidth=0.431)
        self.Frame1_2.configure(borderwidth="2")
        self.Frame1_2.configure(background="#263238")
        self.Frame1_2.configure(highlightbackground="#d9d9d9")
        self.Frame1_2.configure(highlightcolor="black")
        self.Frame1_2.configure(width=455)

        self.Label2_6 = Label(self.Frame1_1)
        self.Label2_6.place(relx=0.085, rely=0.444, height=27, width=115)
        self.Label2_6.configure(activebackground="#263238")
        self.Label2_6.configure(activeforeground="white")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(anchor=E)
        self.Label2_6.configure(background="#263238")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font11)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(justify=RIGHT)
        self.Label2_6.configure(text='''Search''')

        self.Text1 = Text(self.Frame1_1)
        self.Text1.place(relx=0.218, rely=0.444, relheight=0.252, relwidth=0.535)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#5b9ed8")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=564)
        self.Text1.configure(wrap=WORD)

        def onClick():
            medicineName = self.Text1.get("1.0","end-1c")
            #print type(medicineName)
            if not medicineName.strip():
                #print "no medicine name provided"
                self.DrugLabel.configure(text="You need to enter a mdecine")
                self.PriceLabel.configure(text="You need to enter a mdecine")
                self.ConstituentLabel.configure(text="You need to enter a mdecine")
                self.PackLabel.configure(text="You need to enter a mdecine")
                self.UsesLabelInfo_7.configure(text="None")
                self.UsesLabelInfo_4.configure(text="None")
                self.UsesLabelInfo_6.configure(text="None")
                return
            else:
                priyamFunc(medicineName)
                with open("manufac.txt", "r+") as fptr:
                    x = fptr.readlines()
                if x[0] == " ":
                    self.DrugLabel.configure(text="No medicine found")
                    self.PriceLabel.configure(text="No medicine found")
                    self.ConstituentLabel.configure(text="No medicine found")
                    self.PackLabel.configure(text="No medicine found")
                else:
                    self.DrugLabel.configure(text=x[0])
                    self.PriceLabel.configure(text=x[1])
                    self.ConstituentLabel.configure(text=x[2])
                    self.PackLabel.configure(text=x[3])

                with open("theraUses.txt","r") as fptr:
                    uses = fptr.readlines()
                    strr = ""
                if uses[0]== " ":
                    self.UsesLabelInfo_7.configure(text="None")
                else:
                    for i in range(0,len(uses)):
                        strr = strr + uses[i] + "\n"
                        self.UsesLabelInfo_7.configure(text=strr)

                with open("sideEffects.txt", "r") as fptr:
                    side = fptr.readlines()
                    SideStrr = ""
                if uses[0] == " ":
                    self.UsesLabelInfo_6.configure(text="None")
                else:
                    for i in range(0, len(side)):
                        SideStrr = SideStrr + side[i] +"\n"
                        self.UsesLabelInfo_6.configure(text=SideStrr)
                with open("similar.txt", "r") as fptr:
                    similarMeds = str(fptr.read())
                    similarMeds = ast.literal_eval(similarMeds)
                    similarStrName = ""
                    similarStrPrice = ""
                if similarMeds[0]['name']==" ":
                    self.UsesLabelInfo_4.configure(text="None")
                else:
                    for i in range(0,len(similarMeds)):
                        similarStrName = similarStrName +"Name : " + similarMeds[i]['name']+"\n"+"Price : "+str(similarMeds[i]['price']) + "\n" + "Manufacturer : "+similarMeds[i]['manufacturer']+"\n" + "--------------------" + "\n"
                        self.UsesLabelInfo_4.configure(text=similarStrName)




        self.Button2 = Button(self.Frame1_1)
        self.Button2.place(relx=0.777, rely=0.444, height=33, width=86)
        self.Button2.configure(activebackground="#263238")
        self.Button2.configure(activeforeground="white")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#263238")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#fff")
        self.Button2.configure(highlightbackground="#5b9ed8")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Go''')
        self.Button2.configure(width=86)
        self.Button2.configure(command=onClick)

        self.Frame1_3 = Frame(top)
        self.Frame1_3.place(relx=0.019, rely=0.411, relheight=0.55
                , relwidth=0.216)
        self.Frame1_3.configure(borderwidth="2")
        self.Frame1_3.configure(background="#263238")
        self.Frame1_3.configure(highlightbackground="#d9d9d9")
        self.Frame1_3.configure(highlightcolor="black")
        self.Frame1_3.configure(width=345)

        self.Label2_1 = Label(self.Frame1_3)
        self.Label2_1.place(relx=0.058, rely=0.04, height=27, width=65)
        self.Label2_1.configure(activebackground="#263238")
        self.Label2_1.configure(activeforeground="white")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor=W)
        self.Label2_1.configure(background="#263238")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=font11)
        self.Label2_1.configure(foreground="#fff")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(justify=RIGHT)
        self.Label2_1.configure(text='''Uses''')
        self.Label2_1.configure(width=65)

        self.UsesLabelInfo_7 = Label(self.Frame1_3)
        self.UsesLabelInfo_7.place(
            relx=0.06, rely=0.130, height=380, width=280)

        self.UsesLabelInfo_7.configure(activebackground="#263238")
        self.UsesLabelInfo_7.configure(activeforeground="white")
        self.UsesLabelInfo_7.configure(activeforeground="black")
        self.UsesLabelInfo_7.configure(anchor=NW)
        self.UsesLabelInfo_7.configure(background="#455A64")
        self.UsesLabelInfo_7.configure(disabledforeground="#a3a3a3")
        self.UsesLabelInfo_7.configure(font=font12)
        self.UsesLabelInfo_7.configure(foreground="#fff")
        self.UsesLabelInfo_7.configure(highlightbackground="#d9d9d9")
        self.UsesLabelInfo_7.configure(highlightcolor="black")
        self.UsesLabelInfo_7.configure(justify=LEFT)

        self.RegNoLabel = Label(top)
        self.RegNoLabel.place(relx=0.169, rely=0.178, height=27, width=115)
        self.RegNoLabel.configure(activebackground="#f9f9f9")
        self.RegNoLabel.configure(activeforeground="black")
        self.RegNoLabel.configure(background="#455a64")
        self.RegNoLabel.configure(disabledforeground="#a3a3a3")
        self.RegNoLabel.configure(font=font10)
        self.RegNoLabel.configure(foreground="#fff")
        self.RegNoLabel.configure(highlightbackground="#d9d9d9")
        self.RegNoLabel.configure(highlightcolor="black")

        self.Frame1_11 = Frame(top)
        self.Frame1_11.place(relx=0.688, rely=0.411, relheight=0.15
                , relwidth=0.297)
        self.Frame1_11.configure(borderwidth="2")
        self.Frame1_11.configure(background="#263238")
        self.Frame1_11.configure(highlightbackground="#d9d9d9")
        self.Frame1_11.configure(highlightcolor="black")
        self.Frame1_11.configure(width=475)

        self.Button2_12 = Button(self.Frame1_11)
        self.Button2_12.place(relx=0.042, rely=0.148, height=96, width=76)
        self.Button2_12.configure(activebackground="#263238")
        self.Button2_12.configure(activeforeground="white")
        self.Button2_12.configure(activeforeground="#000000")
        self.Button2_12.configure(background="#263238")
        self.Button2_12.configure(borderwidth="0")
        self.Button2_12.configure(disabledforeground="#a3a3a3")
        self.Button2_12.configure(foreground="#fff")
        self.Button2_12.configure(highlightbackground="#5b9ed8")
        self.Button2_12.configure(highlightcolor="black")
        self._img2 = ImageTk.PhotoImage(PIL.Image.open("./manufacturing.png"))
        self.Button2_12.configure(image=self._img2)
        self.Button2_12.configure(pady="0")
        self.Button2_12.configure(text='''Button''')

        self.Label2_9 = Label(self.Frame1_11)
        self.Label2_9.place(relx=0.253, rely=0.148, height=27, width=155)
        self.Label2_9.configure(activebackground="#263238")
        self.Label2_9.configure(activeforeground="white")
        self.Label2_9.configure(activeforeground="black")
        self.Label2_9.configure(anchor=W)
        self.Label2_9.configure(background="#263238")
        self.Label2_9.configure(disabledforeground="#a3a3a3")
        self.Label2_9.configure(font=font11)
        self.Label2_9.configure(foreground="#fff")
        self.Label2_9.configure(highlightbackground="#d9d9d9")
        self.Label2_9.configure(highlightcolor="black")
        self.Label2_9.configure(justify=RIGHT)
        self.Label2_9.configure(text='''Manufacturer''')
        self.Label2_9.configure(width=155)

        self.DrugLabel = Label(self.Frame1_11)
        self.DrugLabel.place(relx=0.253, rely=0.444, height=46, width=272)
        self.DrugLabel.configure(activebackground="#f9f9f9")
        self.DrugLabel.configure(activeforeground="black")
        self.DrugLabel.configure(anchor=W)
        self.DrugLabel.configure(background="#263238")
        self.DrugLabel.configure(disabledforeground="#a3a3a3")
        self.DrugLabel.configure(font=font10)
        self.DrugLabel.configure(foreground="#fff")
        self.DrugLabel.configure(highlightbackground="#d9d9d9")
        self.DrugLabel.configure(highlightcolor="black")
        self.DrugLabel.configure(width=272)

        self.Frame1_12 = Frame(top)
        self.Frame1_12.place(relx=0.688, rely=0.578, relheight=0.183
                , relwidth=0.297)
        self.Frame1_12.configure(borderwidth="2")
        self.Frame1_12.configure(background="#263238")
        self.Frame1_12.configure(highlightbackground="#d9d9d9")
        self.Frame1_12.configure(highlightcolor="black")
        self.Frame1_12.configure(width=475)

        self.Button2_13 = Button(self.Frame1_12)
        self.Button2_13.place(relx=0.042, rely=0.182, height=96, width=76)
        self.Button2_13.configure(activebackground="#263238")
        self.Button2_13.configure(activeforeground="white")
        self.Button2_13.configure(activeforeground="#000000")
        self.Button2_13.configure(background="#263238")
        self.Button2_13.configure(borderwidth="0")
        self.Button2_13.configure(disabledforeground="#a3a3a3")
        self.Button2_13.configure(foreground="#fff")
        self.Button2_13.configure(highlightbackground="#5b9ed8")
        self.Button2_13.configure(highlightcolor="black")
        self._img3 = ImageTk.PhotoImage(PIL.Image.open("./studentpack.png"))
        self.Button2_13.configure(image=self._img3)
        self.Button2_13.configure(pady="0")
        self.Button2_13.configure(text='''Button''')

        self.Label2_3 = Label(self.Frame1_12)
        self.Label2_3.place(relx=0.253, rely=0.182, height=27, width=115)
        self.Label2_3.configure(activebackground="#263238")
        self.Label2_3.configure(activeforeground="white")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(anchor=W)
        self.Label2_3.configure(background="#263238")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font11)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(justify=RIGHT)
        self.Label2_3.configure(text='''Packaging''')

        self.PackLabel = Label(self.Frame1_12)
        self.PackLabel.place(relx=0.253, rely=0.424, height=46, width=272)
        self.PackLabel.configure(activebackground="#f9f9f9")
        self.PackLabel.configure(activeforeground="black")
        self.PackLabel.configure(anchor=W)
        self.PackLabel.configure(background="#263238")
        self.PackLabel.configure(disabledforeground="#a3a3a3")
        self.PackLabel.configure(font=font10)
        self.PackLabel.configure(foreground="#fff")
        self.PackLabel.configure(highlightbackground="#d9d9d9")
        self.PackLabel.configure(highlightcolor="black")
        self.PackLabel.configure(width=272)

        self.Frame1_4 = Frame(top)
        self.Frame1_4.place(relx=0.688, rely=0.778, relheight=0.183
                , relwidth=0.297)
        self.Frame1_4.configure(borderwidth="2")
        self.Frame1_4.configure(background="#263238")
        self.Frame1_4.configure(highlightbackground="#d9d9d9")
        self.Frame1_4.configure(highlightcolor="black")
        self.Frame1_4.configure(width=475)

        self.Button2_4 = Button(self.Frame1_4)
        self.Button2_4.place(relx=0.042, rely=0.182, height=96, width=76)
        self.Button2_4.configure(activebackground="#263238")
        self.Button2_4.configure(activeforeground="white")
        self.Button2_4.configure(activeforeground="#000000")
        self.Button2_4.configure(background="#263238")
        self.Button2_4.configure(borderwidth="0")
        self.Button2_4.configure(disabledforeground="#a3a3a3")
        self.Button2_4.configure(foreground="#fff")
        self.Button2_4.configure(highlightbackground="#5b9ed8")
        self.Button2_4.configure(highlightcolor="black")
        self._img4 = ImageTk.PhotoImage(PIL.Image.open("./vitamin-c.png"))
        self.Button2_4.configure(image=self._img4)
        self.Button2_4.configure(pady="0")
        self.Button2_4.configure(text='''Button''')

        self.Label2_5 = Label(self.Frame1_4)
        self.Label2_5.place(relx=0.253, rely=0.182, height=27, width=145)
        self.Label2_5.configure(activebackground="#263238")
        self.Label2_5.configure(activeforeground="white")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(anchor=W)
        self.Label2_5.configure(background="#263238")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font11)
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(justify=RIGHT)
        self.Label2_5.configure(text='''Constituent''')

        self.ConstituentLabel = Label(self.Frame1_4)
        self.ConstituentLabel.place(relx=0.253, rely=0.424, height=46, width=272)

        self.ConstituentLabel.configure(activebackground="#f9f9f9")
        self.ConstituentLabel.configure(activeforeground="black")
        self.ConstituentLabel.configure(anchor=W)
        self.ConstituentLabel.configure(background="#263238")
        self.ConstituentLabel.configure(disabledforeground="#a3a3a3")
        self.ConstituentLabel.configure(font=font10)
        self.ConstituentLabel.configure(foreground="#fff")
        self.ConstituentLabel.configure(highlightbackground="#d9d9d9")
        self.ConstituentLabel.configure(highlightcolor="black")
        self.ConstituentLabel.configure(width=272)

        self.Frame1_1 = Frame(top)
        self.Frame1_1.place(relx=0.244, rely=0.411, relheight=0.55
                , relwidth=0.209)
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(background="#263238")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")
        self.Frame1_1.configure(width=335)

        self.Label2_2 = Label(self.Frame1_1)
        self.Label2_2.place(relx=0.06, rely=0.04, height=27, width=135)
        self.Label2_2.configure(activebackground="#263238")
        self.Label2_2.configure(activeforeground="white")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(anchor=W)
        self.Label2_2.configure(background="#263238")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font11)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(justify=RIGHT)
        self.Label2_2.configure(text='''Side Effects''')

        self.UsesLabelInfo_6 = Label(self.Frame1_1)
        self.UsesLabelInfo_6.place(
            relx=0.06, rely=0.130, height=380, width=280)

        self.UsesLabelInfo_6.configure(activebackground="#263238")
        self.UsesLabelInfo_6.configure(activeforeground="white")
        self.UsesLabelInfo_6.configure(activeforeground="black")
        self.UsesLabelInfo_6.configure(anchor=NW)
        self.UsesLabelInfo_6.configure(background="#455A64")
        self.UsesLabelInfo_6.configure(disabledforeground="#a3a3a3")
        self.UsesLabelInfo_6.configure(font=font10)
        self.UsesLabelInfo_6.configure(foreground="#fff")
        self.UsesLabelInfo_6.configure(highlightbackground="#d9d9d9")
        self.UsesLabelInfo_6.configure(highlightcolor="black")
        self.UsesLabelInfo_6.configure(justify=LEFT)

        self.Frame1_5 = Frame(top)
        self.Frame1_5.place(relx=0.463, rely=0.411, relheight=0.55
                , relwidth=0.216)
        self.Frame1_5.configure(borderwidth="2")
        self.Frame1_5.configure(background="#263238")
        self.Frame1_5.configure(highlightbackground="#d9d9d9")
        self.Frame1_5.configure(highlightcolor="black")
        self.Frame1_5.configure(width=345)

        self.Label2_3 = Label(self.Frame1_5)
        self.Label2_3.place(relx=0.058, rely=0.04, height=27, width=135)
        self.Label2_3.configure(activebackground="#263238")
        self.Label2_3.configure(activeforeground="white")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(anchor=NW)
        self.Label2_3.configure(background="#263238")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font11)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(justify=LEFT)
        self.Label2_3.configure(text='''Substitutes''')

        self.UsesLabelInfo_4 = Label(self.Frame1_5)
        self.UsesLabelInfo_4.place(
            relx=0.05, rely=0.130, height=380, width=310)

        self.UsesLabelInfo_4.configure(activebackground="#263238")
        self.UsesLabelInfo_4.configure(activeforeground="white")
        self.UsesLabelInfo_4.configure(activeforeground="black")
        self.UsesLabelInfo_4.configure(anchor=NW)
        self.UsesLabelInfo_4.configure(background="#455A64")
        self.UsesLabelInfo_4.configure(disabledforeground="#a3a3a3")
        self.UsesLabelInfo_4.configure(font=font10)
        self.UsesLabelInfo_4.configure(foreground="#fff")
        self.UsesLabelInfo_4.configure(highlightbackground="#d9d9d9")
        self.UsesLabelInfo_4.configure(highlightcolor="black")
        self.UsesLabelInfo_4.configure(justify=LEFT)






if __name__ == '__main__':
    vp_start_gui()
