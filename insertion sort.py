def insertionsort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j>=0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
data = [16, 228, 52, 12, 108, 48, 50, 200]
insertionsort(data)
print("Sorted array in Ascending Order: ")
print(data)