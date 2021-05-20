# Matt Rieckenberg
# ClassGradeSoftware_v1.0beta
import sys
import tkinter as tk

class Course:
    StudentList = []

    def __init__(self,courseName,maxStudents,classSize):
        self.courseName = courseName
        self.maxStudents = maxStudents
        self.classSize = classSize

    def getCourseName(self):
        return self.courseName

    def setCourseName(self,courseName):
        self.courseName = courseName
        print("Course name set to "+self.courseName)

    def setMaxStudents(self,maxStudents):
        self.maxStudents = maxStudents
        print("Max students set to "+self.maxStudents)

    def setClassSize(self,classSize):
        self.classSize = classSize
        print("Class size set to "+self.classSize)

    def toString(self):
        courseString = str(self.courseName)+" has a maximum of "+str(self.maxStudents)+" students and currently there are "+str(self.classSize)+" students enrolled"
        return courseString


class Student(Course):
    def __init__(self,firstName,lastName,studentNumber,grade,course):
        super().__init__()
        self.firstName = firstName
        self.lastName = lastName
        self.studentNumber = studentNumber
        self.grade = grade
        self.course = course


class User(Course):
    CourseList = []
    Nightmode = False

class OpeningWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ClassGradeSoftware_v1.0beta")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.configure(bg="blue")

        def AddCourse_onClick():
            print("Adding course")
            #self.destroy()
            # open the CourseEntryWindow(), possibly keep this one open


        def Exit():
            sys.exit()

        def SetToNightmode():
            User.Nightmode = True

        # Labels
        self.WelcomeLabel = tk.Label(self,text="Class Grade Calculator",bg="red",fg="white",height=5,width=100,font=("Georgia",20,'bold'))
        self.WelcomeLabel.pack()

        # Buttons
        self.AddCourseButton = tk.Button(self,text="Add Course",bg="purple",fg="yellow",command=AddCourse_onClick)
        self.AddCourseButton.pack()
        self.ExitButton = tk.Button(self,text="Exit",bg="orange",fg='black',command=Exit)
        self.ExitButton.pack()
        # NightMode button later



class CourseEntryWindow(tk.Tk,Course):
    def __init__(self):
        super().__init__()

        self.title("ClassGradeSoftware_v1.0beta")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.configure(bg="purple")

        def Exit():
            sys.exit()

        def Submit():
            print("Submit clicked")
            newCourse = Course(self.EnterCourseName.get(),str(self.EnterMaxStudents.get()),0)
            print(newCourse.toString())
            self.destroy()
            User.CourseList.append(newCourse)
            return newCourse

        # Entry Boxes
        self.EnterCourseName = tk.Entry(self,bg="blue")
        self.EnterCourseName.pack()
        self.EnterMaxStudents = tk.Entry(self,bg="green")
        self.EnterMaxStudents.pack()

        # Buttons
        self.SubmitButton = tk.Button(self,text="Submit",command=Submit)
        self.SubmitButton.pack()
        self.ExitButton = tk.Button(self, text="Exit", bg="orange", fg='black', command=Exit)
        self.ExitButton.pack()

class StudentEntryWindow(tk.Tk,Student,User):
    def __init__(self):
        super().__init__()
        self.title("ClassGradeSoftware_v1.0beta")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.configure(bg="green")

        def Exit():
            sys.exit()

        # Entry Boxes
        self.EnterFirstName = tk.Entry(self,bg="blue")
        self.EnterFirstName.pack()
        self.EnterLastName = tk.Entry(self,bg="red")
        self.EnterLastName.pack()
        self.EnterStudentNumber = tk.Entry(self,bg="orange")
        self.EnterStudentNumber.pack()


        # Buttons
        self.ExitButton = tk.Button(self, text="Exit", bg="orange", fg='black', command=Exit)
        self.ExitButton.pack()




def RunProgram(): # add parameters and functionality later
    pass



if __name__ == "__main__":
    #OpeningWindow().mainloop()
    CourseEntryWindow().mainloop()
    #print("Second print: "+User.CourseList[0].toString())
    StudentEntryWindow().mainloop()

