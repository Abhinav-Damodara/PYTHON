string = input()
def swap():
  x = string[0]
  y = string[-1]
  afterswap = y + string[1:-1] + x
  print(afterswap)
swap()