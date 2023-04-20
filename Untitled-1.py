class Abhinav:
    def __init__(self, rno, name, g, ano):
        self.rno = rno
        self.name = name
        self.g = g
        self.ano = ano
class Puppy(Abhinav):
    def __init__(self, ano, bank, branch, rno, name, g):
        self.ano = ano
        self.bank = bank
        self.branch = branch
        Abhinav.__init__(self, rno, name, g, ano)
repeat = int(input("No of students data to be entered:"))
students = list()
for i in range(repeat):
    x = int(input("Enter Rollno: "))
    y = input("Enter Student Name: ")
    z = int(input("Enter Student Grade: "))
    a = int(input("Enter Student Aadharno: "))
    s1 = Abhinav(x, y, z, a)
    students.append(s1)
print(str("Rollno:")+"\t", str("Name:")+"\t", str("Grade:")+"\t", str("Aadharno:")+"\t",)
for i in range(repeat):
    print(str(students[i].rno)+"\t", str(students[i].name)+"\t", str(students[i].g)+"\t", str(students[i].ano)+"\t")