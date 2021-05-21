# Matt Rieckenberg
# ClassGradeSoftware_v1.0beta

# Future additions to v1.0beta:
# Read saved answers from a text file

# v2.0beta:
# Add try: blocks for error handling

import sys
import tkinter as tk

class Course:
    StudentList = []
    numStudents = 0

    def __init__(self,courseName,maxStudents,numStudents):
        self.courseName = courseName
        self.maxStudents = maxStudents
        self.numStudents = numStudents

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
        if self.numStudents == 1:
            string = str(self.courseName) + " has a maximum of " + str(
                self.maxStudents) + " students and currently there is " + str(
                self.numStudents) + " student currently enrolled"+'\n'
            return string
        else:
            string = str(self.courseName)+" has a maximum of "+str(self.maxStudents)+" students and currently there are "+str(self.numStudents)+" students currently enrolled"+'\n'
            return string

    def classListToString(self):
        string = ""
        for i in range(len(self.StudentList)):
            string += self.StudentList[i].toString()
        return string

    def printClassList(self):
        print("Class List------------------------------------------------------------")
        print(self.classListToString())
        print("----------------------------------------------------------------------")





class Student:
    def __init__(self,firstName,lastName,studentNumber,grade,course):
        super().__init__()
        self.firstName = firstName
        self.lastName = lastName
        self.studentNumber = studentNumber
        self.grade = grade
        self.course = course

    def toString(self):
        string = self.firstName+" "+self.lastName+", "+self.studentNumber+" has a grade of "+self.grade+" in "+self.course.getCourseName()+'\n'
        return string

class User:
    SampleCourse = Course("","",0) # default parameters
    Nightmode = False


class OpeningWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ClassGradeSoftware_v1.0beta")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.configure(bg="blue")

        def Start_onClick():
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
        self.AddCourseButton = tk.Button(self,text="Add Course",bg="purple",fg="yellow",command=Start_onClick)
        self.AddCourseButton.pack()
        self.ExitButton = tk.Button(self,text="Exit",bg="orange",fg='black',command=Exit)
        self.ExitButton.pack()
        # NightMode button later

        # Pack()



class CourseEntryWindow(tk.Tk,Course):
    def __init__(self):
        super().__init__()

        self.title("ClassGradeSoftware_v1.0beta")
        #self.attributes('-fullscreen', True)
        #self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.geometry("500x500")
        self.configure(bg="purple")

        def Exit():
            sys.exit()

        def Submit():
            print("Submit clicked")
            newCourse = Course(self.EnterCourseName.get(),str(self.EnterMaxStudents.get()),0)
            print(newCourse.toString())
            User.SampleCourse = newCourse

            self.destroy()

        # Labels
        self.CourseNameLabel = tk.Label(self,text="Enter the course name:")
        self.MaxStudentsLabel = tk.Label(self,text="Enter the maximum number of students:")

        # Entry Boxes
        self.EnterCourseName = tk.Entry(self,bg="blue")
        self.EnterMaxStudents = tk.Entry(self,bg="green")


        # Buttons
        self.SubmitButton = tk.Button(self,text="Submit",command=Submit)
        self.ExitButton = tk.Button(self, text="Exit", bg="orange", fg='black', command=Exit)

        # Pack on the screen
        self.CourseNameLabel.pack()
        self.EnterCourseName.pack()
        self.MaxStudentsLabel.pack()
        self.EnterMaxStudents.pack()
        self.SubmitButton.pack()
        self.ExitButton.pack()



class StudentEntryWindow(tk.Tk,Student,User,Course):
    def __init__(self):
        super().__init__()
        self.title("ClassGradeSoftware_v1.0beta")
        #self.attributes('-fullscreen', True)
        #self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.geometry("500x500")
        self.configure(bg="green")

        def Exit():
            sys.exit()

        def Submit():
            newStudent = Student(str(self.EnterFirstName.get()),str(self.EnterLastName.get()),str(self.EnterStudentNumber.get()),
                                 str(self.EnterGradeValue.get()),User.SampleCourse)
            #print(newStudent.toString())
            User.SampleCourse.StudentList.append(newStudent)
            User.SampleCourse.numStudents=len(User.SampleCourse.StudentList)
            #print(User.SampleCourse.toString())
            self.EnterFirstName.delete(0,'end')
            self.EnterLastName.delete(0,'end')
            self.EnterStudentNumber.delete(0,'end')
            self.EnterGradeValue.delete(0,'end')




        # Entry Boxes
        self.EnterFirstName = tk.Entry(self,bg="blue")
        self.EnterLastName = tk.Entry(self,bg="red")
        self.EnterStudentNumber = tk.Entry(self,bg="orange")
        self.EnterGradeValue = tk.Entry(self)

        # Labels
        self.FirstNameLabel = tk.Label(self,text="Enter First Name:")
        self.LastNameLabel = tk.Label(self,text="Enter Last Name: ")
        self.StudentNumberLabel = tk.Label(self,text="Enter Student Number: ")
        self.GradeLabel = tk.Label(self,text="Enter grade value: ")

        # Buttons
        self.ExitButton = tk.Button(self, text="Exit", bg="orange", fg='black', command=Exit)
        self.SubmitButton = tk.Button(self, text="Submit", command=Submit)
        self.PrintButton = tk.Button(self,text="Print Class List",command=User.SampleCourse.printClassList)


        # Pack
        self.FirstNameLabel.pack()
        self.EnterFirstName.pack()
        self.LastNameLabel.pack()
        self.EnterLastName.pack()
        self.StudentNumberLabel.pack()
        self.EnterStudentNumber.pack()
        self.GradeLabel.pack()
        self.EnterGradeValue.pack()
        self.SubmitButton.pack()
        self.PrintButton.pack()
        self.ExitButton.pack()









def RunProgram(): # add parameters and functionality later
    pass



if __name__ == "__main__":
    #OpeningWindow().mainloop()
    CourseEntryWindow().mainloop()
    StudentEntryWindow().mainloop()
