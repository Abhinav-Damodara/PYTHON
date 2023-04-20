
def oneD_to_sorted2D(lst):
  lst.sort()
  t = []
  p = []
  for i in range(0,len(lst)):
    t.append(lst[i])
    if (i+1)%3==0:
      p.append(t)
      t = []


def find_max_min_dict(d1):
  x = 0
  y = 100000
  ans = []
  for i in d1.keys():
    for j in range(0,len(d1[i])):
      if d1[i][j] < y:
        min = i
        y = d1[i][j]
      if d1[i][j] > x :
        max = i
        x = d1[i][j]
  ans.append(max)
  ans.append(min)
  return ans