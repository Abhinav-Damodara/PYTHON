smallest = None
print ('Before')
for value in [9, 41, 12, 3, 74, 15, 1, 0] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print ('After', smallest)