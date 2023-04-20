def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = int(input("enter num"))
if num < 0:
   print("Factorial doesnot exixt for negetive numbers")
elif num == 0:
   print("The factorial is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))