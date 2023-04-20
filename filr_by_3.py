fil = open(r'C:\Users\Abhinav\Desktop\file.txt', 'r')
content = fil.read()
nums = content.split()
for i in nums:
    if int(i)%3 == 0:
        print(i)
fil.close()
