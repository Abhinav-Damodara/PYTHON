class Slist:
    def _init_(self, rno, name, g, ano):
        self.rno = rno
        self.name = name
        self.g = g
        self.ano = ano

class Alist(Slist):
    def _init_(self, ano, bank, branch, rno, name, g):
        self.bank = bank
        self.branch = branch
        Slist._init_(self, rno, name, g, ano)
        
class Blist(Alist):
    def _init_(self, bank, branch, ano, bal, rno, name, g):
        self.bal = bal
        Alist._init_(self, ano, bank, branch, rno, name, g)
        
# s1 = Slist(20, 'Puppy', 9, 2059)
st = int(input())
students = list()
aadhar = list()
bank = list()

for i in range(st):
    print("===================")
    r = int(input("Roll No: "))
    n = input("Name: ")
    g = int(input("Grade: "))
    a = int(input("Aadhar: "))
    b = input("Bank: ")
    br = input("Branch: ")
    bal = int(input("Balance: "))
    
    s1 = Slist(r, n, g, a)
    students.append(s1)
    a1 = Alist(a, b, br, r, n, g)
    aadhar.append(a1)
    b1 = Blist(b, br, a, bal, r, n, g)
    bank.append(b1)

print('\n')
print("RollNo"+"\t"+"Name"+"\t"+"Grade"+"\t"+"Aadhar")
for i in range(st):
    print(str(students[i].rno)+"\t"+str(students[i].name)+"\t"+str(students[i].g)+"\t"+str(students[i].ano))
print('\n')
print("Aadhar"+"\t"+"Bank"+"\t"+"Branch")
for i in range(st):
    print(str(aadhar[i].ano)+"\t"+str(aadhar[i].bank)+"\t"+str(aadhar[i].branch))
print('\n')
print("Bank"+"\t"+"Branch"+"\t"+"AccNo"+"\t"+"Balance")
for i in range(st):
    print(str(bank[i].bank)+"\t"+str(bank[i].branch)+"\t"+str(bank[i].ano)+"\t"+str(bank[i].bal))

print('\n')    
print("RollNo"+"\t"+"Name"+"\t"+"AccNo"+"\t"+"Branch")    
for i in bank:
    if i.bank == "SBI":
        print(str(i.rno)+'\t'+str(i.name)+'\t'+str(i.ano)+'\t'+str(i.branch)+'\t')