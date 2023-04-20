def insertsort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j>=0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [8, 6, 4, 7, 9, 15, 18, 11, 23, 1, 2]
insertsort(data)
print("Sorted array in Ascending Order: ")
print(data)