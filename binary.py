binary = list(map(int, input('list Items:').split()))
binary.sort
n = int(input("Enter number to be found"))
flag = 0
low = 0
high = len(binary)-1
while low <= high:
    mid = (low+high)//2
    if binary[mid]==n:
        flag = 1
        break
    elif binary[mid]<n:
        low = mid+1
    else:
        high = mid-1
    
if flag==1:
    print('The number Exist')
else:
    print('The number Does not Exist')