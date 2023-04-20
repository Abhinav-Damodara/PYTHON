smallest_so_far = -1
print('Before', smallest_so_far)
for the_num in [91, 411, 112, 113, -174, 151] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print (smallest_so_far, the_num)
print('After', smallest_so_far)