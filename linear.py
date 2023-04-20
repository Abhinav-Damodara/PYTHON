def linear(items, n, key):
    for i in range(0, n):
        if(items[i]==key):
            return i
    return -1
items = [10, 20, 56, 26, 35, 61]
key = int(input('Enter the number to find: '))

n = len(items)
res = linear(items, n, key)
if res==-1:
    print('Element not found')
else:
    print('element found at index:',res)