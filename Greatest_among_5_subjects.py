a = int(input('Enter the marks of maths :'))
b = int(input('Enter the marks of physics :'))
c = int(input('Enter the marks of english :'))
d = int(input('Enter the marks of Computer Science :'))
e = int(input('Enter the marks of Clad :'))
if a>b and a>c and a>d and a>e :
  print(a,'Marks which Obtained in Maths are the highest')
elif b>a and b>c and b>d and b>e :
  print(b,'Marks which Obtained in Physics are the highest')
elif c>a and c>b and c>d and c>e :
  print(c,'Marks which Obtained in English are the highest')
elif d>a and d>b and d>c and d>e :
  print(d,'Marks which Obtained in Computer Science are the highest')
elif e>a and e>b and e>c and e>d :
  print(e,'Marks which Obtained in Clad are the highest')