#project :- student managemant system

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
students=[]

def Add_student():
    name=input("enter the name :-")
    age=int(input("enter the age :-"))
    marks=int(input("enter the marks :-"))

    s=student(name,age,marks)
    students.append(s)
    print("student Added Succefully.....")

def View_student():
    if not students:
        print("no student found...")
    else:
        for s in students:
            print(f"Name :-{s.name}\nAge :-{s.age} \nMarks :-{s.marks}")
    
def Save_student():
    with open("student.txt","w") as file:
        for s in students:
            file.write(f"{s.name},{s.age},{s.marks}\n")
    print("student saved to file successfully....")
while True:
    print("1.add student | 2.view student | 3.Save student file | 4.Exit")
    ch=input("choose your option :-")
    if ch == "1":
        Add_student()
    elif ch == "2":
        View_student()
    elif ch == "3":
        Save_student()
    elif ch == "4":
        print("exiting program.....")
        break
    else:
        print("Invaild input")
