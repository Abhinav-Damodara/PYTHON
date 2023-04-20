# Concept: String and List

# Calculator

'''
You all have used a calculator. It is quite useful when we have simple and also complex calculations.

In general calculators

we will give 
25+345
30-20
30/4
and other operations to perform simple math calculations

Let us do the same thing where you will receive an input like the below

"25+345"

or "30-20"

Your task is to write a program that detects the symbol mentioned and performs the operations on the two operands and returns an integer answer
'''

import unittest

def calculator(expression):
  ans = 0
  cal=['+','-','*','/']
  for i in range (0,len(expression)):
      if expression[i] in cal:
          n1 = int(expression[0:i])
          n2 = int(expression[i+1:len(expression)])
          if expression[i]=='+':
              ans = n1 + n2
          if expression[i]=='-':
              ans = n1 - n2
          if expression[i]=='*':
              ans = n1 * n2
          if expression[i]=='/':
              ans = n1 / n2
  return ans

# DO NOT TOUCH THE BELOW CODE

class Dict_to_list(unittest.TestCase):
  def test_01(self):
    self.assertEqual(calculator("5+4"), 9)

  def test_02(self):
    self.assertEqual(calculator("54+46"), 100)

  def test_03(self):
    self.assertEqual(calculator("545-42"), 503)

  def test_04(self):
    self.assertEqual(calculator("5346/2"), 2673)


if __name__ == '__main__':
  unittest.main(verbosity=2)