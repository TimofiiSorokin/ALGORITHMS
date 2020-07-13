# find smallest min in arr

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


my_list = [5, 8, 33, 55, 2, 99]

print(findSmallest(my_list))  # находит индекс минимального числа
print(my_list[findSmallest(my_list)])  # находит значение минимального числа


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort(my_list))
