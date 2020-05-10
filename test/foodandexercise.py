import sys
import subprocess
import time
from food import *
from exercise import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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




import foodandexercise_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Student_Services___Food___Exercise(root)
    foodandexercise_support.init(root, top)
    root.mainloop()


w = None


def create_Student_Services___Food___Exercise(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Student_Services___Food___Exercise(w)
    foodandexercise_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Student_Services___Food___Exercise():
    global w
    w.destroy()
    w = None


class Student_Services___Food___Exercise:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#5b9ed8'  # Closest X11 color: 'SteelBlue3'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8955b'  # Closest X11 color: 'LightSalmon3'
        _ana1color = '#5b5fd8'  # Closest X11 color: 'SlateBlue3'
        _ana2color = '#5bd8d4'  # Closest X11 color: '{medium turquoise}'
        font11 = "-family {Product Sans} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Product Sans} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Product Sans} -size 16 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font14 = "-family {Product Sans} -size 12 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font15 = "-family {Product Sans} -size 10 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1600x900+77+31")
        root.state("zoomed")
        top.title("Student Services : Food & Exercise")
        top.configure(background="#455a64")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.0, rely=0.0, height=156, width=1602)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#263238")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Food & Exercise''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.038, rely=0.211, height=27, width=103)
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
        self.Label2_1.place(relx=0.120, rely=0.211, height=27, width=103)
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
        self.Label2_2.place(relx=0.275, rely=0.211, height=27, width=103)
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
        self.Label2_3.place(relx=0.038, rely=0.956, height=27, width=103)
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
        self.Label2_4.place(relx=0.113, rely=0.956, height=27, width=103)
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
        self.Label2_5.place(relx=0.194, rely=0.956, height=27, width=43)
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
        self.Label2_6.place(relx=0.231, rely=0.956, height=27, width=103)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#455a64")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font12)
        self.Label2_6.configure(foreground="#fff")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text=time.strftime("%d-%m-%Y"))

        self.foodframe = Frame(top)
        self.foodframe.place(relx=0.038, rely=0.278,
                             relheight=0.65, relwidth=0.441)
        self.foodframe.configure(relief=RAISED)
        self.foodframe.configure(borderwidth="2")
        self.foodframe.configure(relief=RAISED)
        self.foodframe.configure(background="#455a64")
        self.foodframe.configure(highlightbackground="#d9d9d9")
        self.foodframe.configure(highlightcolor="black")
        self.foodframe.configure(width=705)

        self.Searchframe1 = Frame(self.foodframe)
        self.Searchframe1.place(relx=0.043, rely=0.154,
                                relheight=0.145, relwidth=0.915)
        self.Searchframe1.configure(relief=RAISED)
        self.Searchframe1.configure(borderwidth="2")
        self.Searchframe1.configure(relief=RAISED)
        self.Searchframe1.configure(background="#263238")
        self.Searchframe1.configure(highlightbackground="#d9d9d9")
        self.Searchframe1.configure(highlightcolor="black")
        self.Searchframe1.configure(width=645)

        self.Label9 = Label(self.Searchframe1)
        self.Label9.place(relx=0.047, rely=0.353, height=31, width=70)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#263238")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font=font14)
        self.Label9.configure(foreground="#fff")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Search''')

        self.Text2 = Text(self.Searchframe1)
        self.Text2.place(relx=0.171, rely=0.353, relheight=0.4, relwidth=0.673)
        self.Text2.configure(background="white")
        self.Text2.configure(font=font9)
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#5b9ed8")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(width=434)
        self.Text2.configure(wrap=WORD)

        def onClickFood():
            foodname = self.Text2.get("1.0", "end-1c")
            if not foodname.strip():
                self.Label10.configure(text="No such food found")
                return
            else:
                foodFunc(foodname)
                with open("foodData.txt", "r") as fptr:
                    side = fptr.readlines()
                    SideStrr = ""
                if side[0] == " ":
                    self.Label10.configure(text="None")
                else:
                    for i in range(0, len(side)):
                        SideStrr = SideStrr + side[i] + "\n"
                        self.Label10.configure(text=SideStrr)

        self.Button4 = Button(self.Searchframe1)
        self.Button4.place(relx=0.884, rely=0.353, height=35, width=39)
        self.Button4.configure(activebackground="#263238")
        self.Button4.configure(activeforeground="white")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#263238")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font15)
        self.Button4.configure(foreground="#fff")
        self.Button4.configure(highlightbackground="#5b9ed8")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Go''')
        self.Button4.configure(command=onClickFood)

        self.FoodHeading = Label(self.foodframe)
        self.FoodHeading.place(relx=0.454, rely=0.051, height=40, width=69)
        self.FoodHeading.configure(activebackground="#f9f9f9")
        self.FoodHeading.configure(activeforeground="black")
        self.FoodHeading.configure(background="#455a64")
        self.FoodHeading.configure(disabledforeground="#a3a3a3")
        self.FoodHeading.configure(font=font13)
        self.FoodHeading.configure(foreground="#fff")
        self.FoodHeading.configure(highlightbackground="#d9d9d9")
        self.FoodHeading.configure(highlightcolor="black")
        self.FoodHeading.configure(text='''Food''')

        self.Frame4 = Frame(self.foodframe)
        self.Frame4.place(relx=0.043, rely=0.325,
                          relheight=0.624, relwidth=0.915)
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief=GROOVE)
        self.Frame4.configure(background="#263238")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")
        self.Frame4.configure(width=645)

        self.Label10 = Label(self.Frame4)
        self.Label10.place(relx=0.047, rely=0.082, height=296, width=582)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor=NW)
        self.Label10.configure(background="#263238")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font12)
        self.Label10.configure(foreground="#fff")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(justify=LEFT)
        self.Label10.configure(text='''Label''')
        self.Label10.configure(width=582)

        self.exerciseframe = Frame(top)
        self.exerciseframe.place(
            relx=0.519, rely=0.278, relheight=0.65, relwidth=0.441)
        self.exerciseframe.configure(relief=RAISED)
        self.exerciseframe.configure(borderwidth="2")
        self.exerciseframe.configure(relief=RAISED)
        self.exerciseframe.configure(background="#455a64")
        self.exerciseframe.configure(highlightbackground="#d9d9d9")
        self.exerciseframe.configure(highlightcolor="black")
        self.exerciseframe.configure(width=705)

        self.Label7_6 = Label(self.exerciseframe)
        self.Label7_6.place(relx=0.426, rely=0.051, height=40, width=109)
        self.Label7_6.configure(activebackground="#f9f9f9")
        self.Label7_6.configure(activeforeground="black")
        self.Label7_6.configure(background="#455a64")
        self.Label7_6.configure(disabledforeground="#a3a3a3")
        self.Label7_6.configure(font=font13)
        self.Label7_6.configure(foreground="#fff")
        self.Label7_6.configure(highlightbackground="#d9d9d9")
        self.Label7_6.configure(highlightcolor="black")
        self.Label7_6.configure(text='''Exercise''')

        self.Frame1 = Frame(self.exerciseframe)
        self.Frame1.place(relx=0.043, rely=0.154,
                          relheight=0.145, relwidth=0.915)
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=RAISED)
        self.Frame1.configure(background="#263238")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=645)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.047, rely=0.353, height=31, width=70)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#263238")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font14)
        self.Label3.configure(foreground="#fff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Search''')

        def onclickExer():
            exerciseName = self.Text1.get("1.0", "end-1c")
            print exerciseName
            if not exerciseName.strip():
                self.Label10_2.configure(text="No such exercise found")
                return
            else:
                exerFunc(exerciseName)
                with open("exerciseData.txt", "r") as fptr:
                    side = fptr.readlines()
                    SideStrr = ""
                if side[0] == " ":
                    self.Label10_2.configure(text="None")
                else:
                    for i in range(0, len(side)):
                        SideStrr = SideStrr + side[i] + "\n"
                        self.Label10_2.configure(text=SideStrr)

        self.Button4_1 = Button(self.Frame1)
        self.Button4_1.place(relx=0.884, rely=0.353, height=35, width=39)
        self.Button4_1.configure(activebackground="#263238")
        self.Button4_1.configure(activeforeground="white")
        self.Button4_1.configure(activeforeground="#000000")
        self.Button4_1.configure(background="#263238")
        self.Button4_1.configure(disabledforeground="#a3a3a3")
        self.Button4_1.configure(font=font15)
        self.Button4_1.configure(foreground="#fff")
        self.Button4_1.configure(highlightbackground="#5b9ed8")
        self.Button4_1.configure(highlightcolor="black")
        self.Button4_1.configure(pady="0")
        self.Button4_1.configure(text='''Go''')
        self.Button4_1.configure(command=onclickExer)

        self.Text1 = Text(self.exerciseframe)
        self.Text1.place(relx=0.199, rely=0.205,
                         relheight=0.058, relwidth=0.616)

        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#5b9ed8")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=434)
        self.Text1.configure(wrap=WORD)

        self.Frame2 = Frame(self.exerciseframe)
        self.Frame2.place(relx=0.043, rely=0.325,
                          relheight=0.624, relwidth=0.915)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#263238")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=645)

        self.Label10_2 = Label(self.Frame2)
        self.Label10_2.place(relx=0.047, rely=0.082, height=296, width=582)
        self.Label10_2.configure(activebackground="#f9f9f9")
        self.Label10_2.configure(activeforeground="black")
        self.Label10_2.configure(anchor=NW)
        self.Label10_2.configure(background="#263238")
        self.Label10_2.configure(disabledforeground="#a3a3a3")
        self.Label10_2.configure(font=font12)
        self.Label10_2.configure(foreground="#fff")
        self.Label10_2.configure(highlightbackground="#d9d9d9")
        self.Label10_2.configure(highlightcolor="black")
        self.Label10_2.configure(justify=LEFT)
        self.Label10_2.configure(text='''Label''')
        self.Label10_2.configure(width=582)



        def back():
            root.destroy()
            subprocess.call("python2 studdashscreen1.py")




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



if __name__ == '__main__':
    vp_start_gui()
