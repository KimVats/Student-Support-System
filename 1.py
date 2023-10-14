from tkinter import *
import sqlite3
import tkinter.messagebox
from   PIL import Image,ImageTk          #pip install pillow
import webbrowser




window=Tk()
window.geometry("500x500")
window.title(" STUDENT SUPPORT SYSTEM")

imge=Image.open("/images/galaxy.jpg")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo)
lab.pack()




def exit1():
    exit()

def abt():
    tkinter.messagebox.showinfo("Welcome to Author's","This is Demo menu field")

def sign_up():
    window1=Toplevel()
    window1.title("Welcome to Sign-Up Page")
    window1.geometry("500x500")

    imge1 = Image.open("/images/signup.jpg")
    photo1 = ImageTk.PhotoImage(imge1)
    lab2 = Label(window1,image=photo1)
    lab2.pack()

    label1 = Label(window1, text="Sign In", fg="red", relief="solid", width=20, font=("arial", 19, "bold"))
    label1.place(x=90, y=53)

    label2 = Label(window1, text="Name", width=20, font=("arial", 10, "bold"))
    label2.place(x=80, y=130)
    entry_1 = Entry(window1, textvar=name1, width=20)
    entry_1.place(x=300, y=130)

    label3 = Label(window1, text="USN", width=20, font=("arial", 10, "bold"))
    label3.place(x=80, y=180)
    entry_2 = Entry(window1, textvar=usn1, width=20)
    entry_2.place(x=300, y=180)

    label4 = Label(window1, text="Branch :", width=20, font=("bold", 10))
    label4.place(x=80, y=230)

    r1 = Radiobutton(window1, text="Computer Science", variable=dno1, value="1").place(x=300, y=230)
    r1 = Radiobutton(window1, text="Information Science", variable=dno1, value="2").place(x=300, y=260)
    r1 = Radiobutton(window1, text="Electronics Communication", variable=dno1, value="3").place(x=300, y=290)

    label4 = Label(window1, text="Date of Birth:", width=20, font=("bold", 10))
    label4.place(x=80, y=330)

    entry_3 = Entry(window1, textvar=dob1, width=20)
    entry_3.place(x=300, y=330)

    label5 = Label(window1, text="Password:", width=20, font=("bold", 10))
    label5.place(x=80, y=380)

    entry_4 = Entry(window1, textvar=password1, width=20)
    entry_4.place(x=300, y=380)

    b1 = Button(window1, text="Submit", width=12, bg="brown", fg="white",command=database1)
    b1.place(x=230, y=430)

    window.bind("<Return>", course)

    window1.mainloop()


def login():
    window2=Toplevel()
    window2.title("Welcome to Login Page")
    window2.geometry("500x500")

    imge2 = Image.open("/images/signup.jpg")
    photo2 = ImageTk.PhotoImage(imge2)
    lab3 = Label(window2,image=photo2)
    lab3.pack()

    label1 = Label(window2, text="Login", fg="red", relief="solid", width=20, font=("arial", 19, "bold"))
    label1.place(x=90, y=53)

    label2 = Label(window2, text="Username", width=20, font=("arial", 10, "bold"))
    label2.place(x=80, y=130)
    entry_1 = Entry(window2, textvar=name2, width=20)
    entry_1.place(x=300, y=130)

    label3 = Label(window2, text="Password", width=20, font=("arial", 10, "bold"))
    label3.place(x=80, y=180)
    entry_2 = Entry(window2, textvar=password2, width=20)
    entry_2.place(x=300, y=180)



    b1 = Button(window2, text="Login", width=12, bg="brown", fg="white",command=database2)
    b1.place(x=230, y=430)

    window2.bind("<Return>", database2)

    window2.mainloop()

def database1():
    name=name1.get()
    usn=usn1.get()
    branch=branch1.get()
    dob=dob1.get()
    password=password1.get()
    dno=dno1.get()
    conn=sqlite3.connect("test.db")
    with conn:
        cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS sign_in (Name TEXT,USN TEXT,DOB TEXT,Password TEXT,Dno INTEGER,PRIMARY KEY(Password),FOREIGN KEY(Dno) REFERENCES Department(Dno))')

    cursor.execute('INSERT INTO sign_in(Name,USN,DOB,Password,Dno) VALUES(?,?,?,?,?)',(name,usn,dob,password,dno))
    cursor.execute('CREATE TABLE IF NOT EXISTS Login (Username TEXT,Password TEXT,FOREIGN KEY(Username) REFERENCES sign_in(Name),FOREIGN KEY(Password) REFERENCES sign_in(Password))')
    cursor.execute('INSERT INTO Login(Username,Password) VALUES(?,?)', (name,password))
    #cursor.execute('INSERT INTO Login(Username,Password) VALUES(?,?)',(name,password))
    tkinter.messagebox.showinfo("Welcome", 'User is successfully Logged in')
    course()

    conn.commit()


def database2():
    name=name2.get()
    password=password2.get()


    found=0
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT Username,Password from Login where Username=? and password=?',[name,password])
        if cursor.fetchall():
               tkinter.messagebox.showinfo("Welcome", 'User is successfully Logged in')
               course()

        else:
            tkinter.messagebox.showinfo("Wrong password",'Try Again or go for sign up')

    conn.commit()
def insertinstudent():
    name = name2.get()
    usn = usn2.get()
    courseid1=courseid.get()
    dob = dob2.get()
    dno = dno2.get()
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS  student (Name TEXT,USN TEXT,Dno INTEGER,DOB	TEXT,course_id	INTEGER,FOREIGN KEY(Dno) REFERENCES Department(Dno),FOREIGN KEY(USN) REFERENCES sign_in(USN),FOREIGN KEY(course_id) REFERENCES AI(course_id))')

    cursor.execute('INSERT INTO student(Name,USN,Dno,DOB,course_id) VALUES(?,?,?,?,?)', (name, usn, dno, dob,courseid1))
    cursor.execute('SELECT Username from Login where Username=?', [name])

    if cursor.fetchall():
                    tkinter.messagebox.showinfo("Congratulations",'Successfully Enrolled in the course')
                    course()

    else:
        tkinter.messagebox.showinfo("Wrong password", 'Try Again or go for sign up')
    conn.commit()




def course():
    window3 = Toplevel()
    window3.title("Welcome to Courses Page")
    window3.geometry("500x500")
    print("created")
    window3.configure(bg='black')
    print("copy sign contents to student along with courseid and name")
    lable_0 = Label(window3, text="", bg='black').pack()

    label_e = Label(window3, text="YOUR COURSES", bg='black', fg='white', font=("bold", 20))
    label_e.pack()
    # Code to display whic all courses you are enrolled in and next to the course there will the button which when you click
    # should take you to the  another window where your course content will be displayed
    lable_0 = Label(window3, text="", bg='black').pack()

    lable_0 = Label(window3, text="", bg='black').pack()
    Button(window3, text='My Courses', width=20, bg='black', fg='white',command=display).pack()
    lable_0 = Label(window3, text="", bg='black').pack()
    Button(window3, text='Explore', width=20, bg='black', fg='white',command=branch).pack()
    lable_0 = Label(window3, text="", bg='black').pack()

def mycourses():
    top=Toplevel()
    top.title("Welcome to Courses Page")
    top.geometry("500x500")
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('Select * from student')
    rows=cursor.fetchall()
    e = [i[0] for i in rows.fetchall()]

    label_e = Label(top, textvariable=e, bg='black', fg='white', font=("bold", 20))
    label_e.pack()

def branch():
    top = Toplevel()
    top.geometry('400x400')
    top.title("WELCOME")
    top.configure(bg='black')

    lable_0 = Label(top, text="", bg='black').pack()
    label_e = Label(top, text="Select your branch", bg='black', fg='white', font=("bold", 14))
    label_e.pack()

    lable_0 = Label(top, text="", bg='black').pack()
    Button(top, text=' COMPUTER SCIENCE  ', padx=50, pady=50, bg='black', fg='white', command=cs).pack()
    lable_0 = Label(top, text="", bg='black').pack()
    Button(top, text='INFORMATION SCIENCE', padx=50, pady=50, bg='black', fg='white', command=common).pack()
    lable_0 = Label(top, text="", bg='black').pack()

def cs():
    top = Toplevel()
    top.geometry('400x400')
    top.title("Computer Science")
    top.configure(bg='black')

    lable_0 = Label(top, text="", bg='black').pack()
    label_e = Label(top, text="Select your Domain", bg='black', fg='white', font=("bold", 14))
    label_e.pack()

    lable_0 = Label(top, text="", bg='black').pack()
    Button(top, text='Artificial Intelligence', padx=30, pady=30, bg='black', fg='white',command=ai).pack()
    lable_0 = Label(top, text="", bg='black').pack()


def common():
    top = Toplevel()
    top.geometry('400x400')
    top.title("Information Science")
    top.configure(bg='black')

    lable_0 = Label(top, text="", bg='black').pack()
    label_e = Label(top, text="Select your Domain", bg='black', fg='white', font=("bold", 14))
    label_e.pack()

    lable_0 = Label(top, text="", bg='black').pack()
    Button(top, text='Artificial Intelligence', padx=30, pady=30, bg='black', fg='white',command=ai).pack()
    lable_0 = Label(top, text="", bg='black').pack()


def ai():
    top = Toplevel()
    top.geometry('1400x1400')
    top.title("WELCOME TO AI COURSES")
    top.configure(bg='black')

    lable_0 = Label(top, text="", bg='black').grid(row=0, column=0)
    label_e = Label(top, text="Enroll for the courses", bg='black', fg='white', font=("bold", 14))
    label_e.grid(row=2, column=3)

    lable_0 = Label(top, text="", bg='black').grid(row=3, column=0)
    label_1 = Label(top, text="Courses", bg='black', fg='white', font=("bold", 14))
    label_1.grid(row=4, column=3)
    lable_0 = Label(top, text="", bg='black').grid(row=5, column=0)

    label_2 = Label(top, text="", bg='black', fg='white', font=("bold", 14))
    label_2.grid(row=4, column=4)
    lable_0 = Label(top, text="", bg='black').grid(row=5, column=0)

    button1 = Button(top, state='disabled', text="AI Beginning level course 1", width=40, bg='black', fg='white', font=("bold", 14)).grid(
        row=6, column=3)
    buttone1 = Button(top, text="Enroll", width=20, bg='black', fg='white', font=("bold", 14),command=enroll).grid(
        row=6, column=4)

    button2 = Button(top, state='disabled', text="AI: Reinforcement Learning", width=40, bg='black', fg='white', font=("bold", 14)).grid(
        row=7, column=3)
    buttone2 = Button(top, text="Enroll", width=20, bg='black', fg='white', font=("bold", 14),command=enroll).grid(
        row=7, column=4)

    button3 = Button(top, state='disabled', text="AI:Professional's Choice", width=40, bg='black', fg='white', font=("bold", 14)).grid(
        row=8, column=3)
    buttone3 = Button(top, text="Enroll", width=20, bg='black', fg='white', font=("bold", 14),command=enroll).grid(
        row=8, column=4)

    button4 = Button(top, state='disabled', text="AI:The Future", width=40, bg='black', fg='white', font=("bold", 14)).grid(
        row=9, column=3)
    buttone4 = Button(top, text="Enroll", width=20, bg='black', fg='white', font=("bold", 14),command=enroll).grid(
        row=9, column=4)

    button5 = Button(top, state='disabled', text="Artificial Intelligence", width=40, bg='black', fg='white', font=("bold", 14)).grid(
        row=10, column=3)
    buttone5 = Button(top, text="Enroll", width=20, bg='black', fg='white', font=("bold", 14),command=enroll).grid(
        row=10, column=4)

def enroll():
    top = Toplevel()
    top.geometry('600x600')
    top.title("Enrollment")
    top.configure(bg='black')

    label0 = Label(top, text="Get Enrolled to the Course", fg="red", relief="solid", width=24, font=("arial", 19, "bold"))
    label0.place(x=90, y=53)


    label2 = Label(top, text="Name", width=20, font=("arial", 10, "bold"))
    label2.place(x=80, y=130)
    entry_1 = Entry(top, textvar=name2, width=20)
    entry_1.place(x=300, y=130)

    label3 = Label(top, text="USN", width=20, font=("arial", 10, "bold"))
    label3.place(x=80, y=180)
    entry_2 = Entry(top, textvar=usn2, width=20)
    entry_2.place(x=300, y=180)

    label4 = Label(top, text="Branch :", width=20, font=("bold", 10))
    label4.place(x=80, y=230)

    r1 = Radiobutton(top, text="Computer Science", variable=dno2, value="1").place(x=300, y=230)
    r1 = Radiobutton(top, text="Information Science", variable=dno2, value="2").place(x=300, y=260)
    r1 = Radiobutton(top, text="Electronics Communication", variable=dno2, value="3").place(x=300, y=290)

    label4 = Label(top, text="Date of Birth:", width=20, font=("bold", 10))
    label4.place(x=80, y=330)

    entry_3 = Entry(top, textvar=dob2, width=20)
    entry_3.place(x=300, y=330)

    label5 = Label(top, text="Course Name :", width=20, font=("bold", 10))
    label5.place(x=80, y=380)

    r1 = Radiobutton(top, text="AI Beginning level course 1", variable=courseid, value="1").place(x=300, y=380)
    r1 = Radiobutton(top, text="AI: Reinforcement Learning", variable=courseid, value="2").place(x=300, y=410)
    r1 = Radiobutton(top, text="AI:Professional's Choice", variable=courseid, value="3").place(x=300, y=440)



    b1 = Button(top, text="Submit", width=12, bg="brown", fg="white",command=insertinstudent)
    b1.place(x=230, y=480)

    top.bind("<Return>", database1)
    top.mainloop()

def OpenUrlai1():
        webbrowser.open_new("https://www.edx.org/micromasters/columbiax-artificial-intelligence")


def OpenUrlai2():
    webbrowser.open_new("https://www.udemy.com/course/artificial-intelligence-az/")


def OpenUrlai3():
    webbrowser.open_new("https://www.coursera.org/specializations/ai-foundations-for-everyone")

def OpenNotesai1():
    webbrowser.open_new("https://drive.google.com/open?id=1Q1TliIGkJB3NhoYTUAykN6mtBh2H7XBR")

def OpenNotesai2():
    webbrowser.open_new("https://drive.google.com/open?id=1eJOe13id1yyZ-pUwq878qiqhQEA8tIMr")

def OpenNotesai3():
        webbrowser.open_new("https://drive.google.com/open?id=1s2kbTbK0pUC8IxHVCLec_os801E9rQvl")

def OpenUrl1(url):
    webbrowser.open_new(url)


def callback(url):
    webbrowser.open_new(url)


def display():
    top = Toplevel()
    top.geometry('1400x1400')
    top.title("MY COURSES")
    top.configure(bg='black')
    name=name2.get()
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()
    data = cursor.execute('SELECT a.course_name,a.course_desc,a.course_url,a.course_id from AI a,student s where a.course_id=s.course_id AND s.Name=?',[name])

    # Label1 = Label(top, text="MY COURSES",bg='black', fg='white', font=("bold", 20), width=85)
    # Label1.grid(row=0, column=0)

    Label1 = Label(top, text="", bg='black', fg='white', font=("bold", 14), width=14)
    Label1.grid(row=0, column=0)
    Label1 = Label(top, text="", bg='black', fg='white', font=("bold", 14), width=14)
    Label1.grid(row=1, column=0)
    Label1 = Label(top, text="", bg='black', fg='white', font=("bold", 14), width=14)
    Label1.grid(row=2, column=1)
    Label1 = Label(top, text="", bg='black', fg='white', font=("bold", 14), width=14)
    Label1.grid(row=2, column=2)

    Label1 = Label(top, text="Courses Name", bg="grey", font=("bold", 14), width=30)
    Label1.grid(row=2, column=0)
    Label2 = Label(top, text="Description", bg="grey", font=("bold", 14), width=50)
    Label2.grid(row=2, column=1)
    Label3 = Label(top, text="Notes", bg="grey", font=("bold", 14), width=20)
    Label3.grid(row=2, column=2)
    Label3 = Label(top, text="URL", bg="grey", font=("bold", 14), width=20)
    Label3.grid(row=2, column=3)

    for index, dat in enumerate(data):
        Label(top, text=dat[0], font=("bold", 14), width=30, height=3).grid(row=index + 3, column=0)
        Label(top, text=dat[1], font=("bold", 14), width=50, height=3, wraplength=400).grid(row=index + 3, column=1)
        i = dat[3]
        if (i == 1):
            b3 = Button(top, text="Start", bg="red", font=("bold", 14), width=15, command=OpenUrlai1).grid(
                row=index + 3,
                column=3)
            b3 = Button(top, text="Get It", bg="red", font=("bold", 14), width=15, command=OpenNotesai1).grid(
                row=index + 3,
                column=2)
        elif (i == 2):
            b3 = Button(top, text="Start", bg="red", font=("bold", 14), width=15, command=OpenUrlai2).grid(
                row=index + 3,
                column=3)
            b3 = Button(top, text="Get it", bg="red", font=("bold", 14), width=15, command=OpenNotesai2).grid(
                row=index + 3,
                column=2)
        else:
            b3 = Button(top, text="Start", bg="red", font=("bold", 14), width=15, command=OpenUrlai3).grid(
                row=index + 3,
                column=3)
            b3 = Button(top, text="Get It", bg="red", font=("bold", 14), width=15, command=OpenNotesai3).grid(
                row=index + 3,
                column=2)

        # Label(top, text=dat[2],font=("bold", 14), width=40,height=3,wraplength=600).grid(row=index + 3, column=2)
#  Label(top, text=dat[2],font=("bold", 14), width=40,height=3,wraplength=600).grid(row=index + 3, column=2)
       # b3 = Button(top, text="Start",bg="red",font=("bold", 14), width=20,command=OpenUrl).grid(row=index + 5, column=1)



name1=StringVar()
usn1=StringVar()
branch1=StringVar()
dno1=StringVar()
dob1=StringVar()
password1=StringVar()
var_c1="Java"
var_c2="Python"
Dno1=StringVar()

name2=StringVar()
password2=StringVar()

usn2=StringVar()
dno2=StringVar()
dob2=StringVar()

courseid=StringVar()

def print1():
    first=fn.get()
    sec=ln.get()
    dob1=dob.get()


    tkinter.messagebox.showinfo("Welcome",'User is successfully signed in')

def printt():
    print("Demo Tkinter")

def second_win():
    window1=Tk()
    window1.title("Welcome to Second window")
    window1.geometry('500x500')
    label_01=Label(window1,text='Registration Completed',relief="solid",font=('arial',12,'bold')).place(x=30,y=70)
    but_01=Button(window1,text="Demo",width=12,bg="brown",fg="white",command=abt).place(x=80,y=110)

    label2 = Label(window1, text="First Name", width=20, font=("arial", 10, "bold"))
    label2.place(x=80, y=130)

    entry_1 = Entry(window1, textvar=fn, width=20)
    entry_1.place(x=300, y=130)

    label3 = Label(window1, text="Last Name", width=20, font=("arial", 10, "bold"))
    label3.place(x=80, y=180)

    entry_2 = Entry(window1, textvar=ln, width=20)
    entry_2.place(x=300, y=180)

    label4 = Label(window1, text="DOB", width=20, font=("arial", 10, "bold"))
    label4.place(x=80, y=230)

    entry_2 = Entry(window1, textvar=dob, width=20)
    entry_2.place(x=300, y=230)

    label3 = Label(window1, text="Country :", width=20, font=("bold", 10))
    label3.place(x=80, y=280)

    var = StringVar()

    list1 = ['Nepal', 'India', 'Canada']
    droplist = OptionMenu(window1, var, *list1)
    var.set("select country")
    droplist.config(width=15)
    droplist.place(x=300, y=280)

    label4 = Label(window1, text="Prog Lang :", width=20, font=("bold", 10))
    label4.place(x=80, y=330)

    c1 = Checkbutton(window1, text="Java", variable=var_c1).place(x=300, y=330)
    c1 = Checkbutton(window1, text="Python", variable=var_c2).place(x=360, y=330)

    r1 = Radiobutton(window1, text="Male", variable=radio_var, value="Male").place(x=300, y=370)
    r1 = Radiobutton(window1, text="Female", variable=radio_var, value="Female").place(x=360, y=370)

    label4 = Label(window1, text="Gender :", width=20, font=("bold", 10))
    label4.place(x=80, y=370)

    b1 = Button(window1, text="Sign-up", width=12, bg="brown", fg="white", command=database)
    b1.place(x=150, y=400)
    window.bind("<Return>", database)

    b2 = Button(window1, text="exit", width=12, bg="brown", fg="white", command=exit1)
    b2.place(x=280, y=400)

    b3 = Button(window, text="Login", width=12, bg="brown", fg="white", command=second_win)
    b3.place(x=215, y=440)

label1=Label(window,text="Login Page",fg="red",relief="solid",width=20,font=("arial",19,"bold"))
label1.place(x=90,y=53)

b1=Button(window,text="Login",width=20,height=2,bg="brown",fg="white",command=login)
b1.place(x=60,y=150)
#window.bind("<Return>",database)

b2=Button(window,text="Sign-Up",width=20,height=2,bg="brown",fg="white",command=sign_up)
b2.place(x=280,y=150)

b3=Button(window,text="Exit",width=20,height=2,bg="brown",fg="white",command=exit1)
b3.place(x=170,y=220)

window.mainloop()
