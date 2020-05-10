
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



import admindashscreen1_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Admin_Dashboard (root)
    admindashscreen1_support.init(root, top)
    root.mainloop()

w = None
def create_Admin_Dashboard(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Admin_Dashboard (w)
    admindashscreen1_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Admin_Dashboard():
    global w
    w.destroy()
    w = None


class Admin_Dashboard:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b' # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8' # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4' # Closest X11 color: '{medium turquoise}'
        font11 = "-family {Product Sans} -size 20 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1600x900+88+47")
        top.title("Admin Dashboard")
        top.configure(background="#37474f")


        root.state('zoomed')
        self.AdminDashTitle = Label(top)
        self.AdminDashTitle.place(relx=0.0, rely=0.0, height=136, width=1602)
        self.AdminDashTitle.configure(background="#263238")
        self.AdminDashTitle.configure(disabledforeground="#a3a3a3")
        self.AdminDashTitle.configure(font=font11)
        self.AdminDashTitle.configure(foreground="#fff")
        self.AdminDashTitle.configure(text='''Dashboard : Administrator''')
        self.AdminDashTitle.configure(width=1602)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.513, rely=0.211, relheight=0.739
                , relwidth=0.459)
        self.Frame2.configure(borderwidth="1")
        self.Frame2.configure(background="#263238")
        self.Frame2.configure(width=735)

        self.Label2 = Label(self.Frame2)
        self.Label2.place(relx=0.422, rely=0.06, height=40, width=125)
        self.Label2.configure(background="#263238")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(text='''Prescribe''')

        self.Label2_3 = Label(self.Frame2)
        self.Label2_3.place(relx=0.299, rely=0.421, height=40, width=295)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#263238")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=font13)
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Enter Student Details''')
        self.Label2_3.configure(width=295)

        self.Label2_4 = Label(self.Frame2)
        self.Label2_4.place(relx=0.109, rely=0.556, height=40, width=175)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(anchor=E)
        self.Label2_4.configure(background="#263238")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font13)
        self.Label2_4.configure(foreground="#fff")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''Registration No :''')
        self.Label2_4.configure(width=175)

        self.RegNoEntry = Text(self.Frame2)
        self.RegNoEntry.place(relx=0.408, rely=0.556, relheight=0.051
                , relwidth=0.454)
        self.RegNoEntry.configure(background="white")
        self.RegNoEntry.configure(font=font9)
        self.RegNoEntry.configure(foreground="black")
        self.RegNoEntry.configure(highlightbackground="#5b9ed8")
        self.RegNoEntry.configure(highlightcolor="black")
        self.RegNoEntry.configure(insertbackground="black")
        self.RegNoEntry.configure(selectbackground="#c4c4c4")
        self.RegNoEntry.configure(selectforeground="black")
        self.RegNoEntry.configure(width=334)
        self.RegNoEntry.configure(wrap=WORD)

        def go_to_dash():
            self.input1 = str(self.RegNoEntry .get("1.0",'end-1c')).rstrip().upper()
            #self.input2 = str(self.Text2.get("1.0",'end-1c')).rstrip()
            reg_no=[]
            name=[]
            for i in enumerate(rows):
                l = i[1]
                reg_no.append(l[0])
                name.append(l[1])
            for iter in range(len(reg_no)):
                if self.input1 == reg_no[iter] :
                    final_reg = str(reg_no[iter])
                    final_name = str(name[iter])
                    with open("check.txt","w") as fptr:
                        fptr.write(final_reg)
                        fptr.write("\n")
                        fptr.write(final_name)
                    root.destroy()
                    subprocess.call("python dashboard.py")

        self.GoButton = Button(self.Frame2)
        self.GoButton.place(relx=0.449, rely=0.737, height=35, width=79)
        self.GoButton.configure(activebackground="#263238")
        self.GoButton.configure(activeforeground="white")
        self.GoButton.configure(activeforeground="#000000")
        self.GoButton.configure(background="#263238")
        self.GoButton.configure(disabledforeground="#a3a3a3")
        self.GoButton.configure(font=font14)
        self.GoButton.configure(foreground="#fff")
        self.GoButton.configure(highlightbackground="#5b9ed8")
        self.GoButton.configure(highlightcolor="black")
        self.GoButton.configure(pady="0")
        self.GoButton.configure(text='''Go''')
        self.GoButton.configure(width=79)
        self.GoButton.configure(command = go_to_dash)

        self.PrescribeImage = Button(self.Frame2)
        self.PrescribeImage.place(relx=0.408, rely=0.15, height=130, width=130)
        self.PrescribeImage.configure(activebackground="#263238")
        self.PrescribeImage.configure(activeforeground="white")
        self.PrescribeImage.configure(activeforeground="#000000")
        self.PrescribeImage.configure(background="#263238")
        self.PrescribeImage.configure(borderwidth="0")
        self.PrescribeImage.configure(disabledforeground="#a3a3a3")
        self.PrescribeImage.configure(foreground="#000000")
        self.PrescribeImage.configure(highlightbackground="#5b9ed8")
        self.PrescribeImage.configure(highlightcolor="black")
        self._img1 = ImageTk.PhotoImage(PIL.Image.open("./prescription.png"))
        self.PrescribeImage.configure(image=self._img1)
        self.PrescribeImage.configure(pady="0")
        self.PrescribeImage.configure(text='''Button''')

        self.Frame1_1 = Frame(top)
        self.Frame1_1.place(relx=0.031, rely=0.211, relheight=0.739
                , relwidth=0.459)
        self.Frame1_1.configure(borderwidth="1")
        self.Frame1_1.configure(background="#263238")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")
        self.Frame1_1.configure(width=735)

        self.Label2_2 = Label(self.Frame1_1)
        self.Label2_2.place(relx=0.367, rely=0.06, height=40, width=195)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#263238")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=font12)
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Admin Profile''')
        self.Label2_2.configure(width=195)

        self.AdminDP = Button(self.Frame1_1)
        self.AdminDP.place(relx=0.15, rely=0.211, height=130, width=130)
        self.AdminDP.configure(activebackground="#263238")
        self.AdminDP.configure(activeforeground="white")
        self.AdminDP.configure(activeforeground="#000000")
        self.AdminDP.configure(background="#263238")
        self.AdminDP.configure(borderwidth="0")
        self.AdminDP.configure(disabledforeground="#a3a3a3")
        self.AdminDP.configure(foreground="#000000")
        self.AdminDP.configure(highlightbackground="#5b9ed8")
        self.AdminDP.configure(highlightcolor="black")
        self._img2 = ImageTk.PhotoImage(PIL.Image.open("./userprofile.png"))
        self.AdminDP.configure(image=self._img2)
        self.AdminDP.configure(pady="0")
        self.AdminDP.configure(text='''Button''')

        self.Label2_5 = Label(self.Frame1_1)
        self.Label2_5.place(relx=0.367, rely=0.271, height=40, width=125)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(anchor=E)
        self.Label2_5.configure(background="#263238")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font13)
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Username :''')
        self.Label2_5.configure(width=125)

        self.Label2_6 = Label(self.Frame1_1)
        self.Label2_6.place(relx=0.571, rely=0.271, height=40, width=125)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(anchor=W)
        self.Label2_6.configure(background="#263238")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font13)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''Admin''')

        def sign_out():
            root.destroy()
            subprocess.call("python Gateway.py")

        self.SignOutButton = Button(self.Frame1_1)
        self.SignOutButton.place(relx=0.408, rely=0.662, height=45, width=119)
        self.SignOutButton.configure(activebackground="#263238")
        self.SignOutButton.configure(activeforeground="white")
        self.SignOutButton.configure(activeforeground="#000000")
        self.SignOutButton.configure(background="#263238")
        self.SignOutButton.configure(disabledforeground="#a3a3a3")
        self.SignOutButton.configure(font=font14)
        self.SignOutButton.configure(foreground="#fff")
        self.SignOutButton.configure(highlightbackground="#5b9ed8")
        self.SignOutButton.configure(highlightcolor="black")
        self.SignOutButton.configure(pady="0")
        self.SignOutButton.configure(text='''Sign Out''')
        self.SignOutButton.configure(width=119)
        self.SignOutButton.configure(command = sign_out)






if __name__ == '__main__':
    vp_start_gui()
