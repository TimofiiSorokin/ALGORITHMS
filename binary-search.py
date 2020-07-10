# bubble sort
# for fun >>> https://www.youtube.com/watch?v=lyZQPjUT5B4 <<<

# def binary_search(some_list, item):
#     low = 0
#     high = len(mylist) - 1
#
#     while low <= high:
#         mid = (low + high)
#         guess = some_list[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None


def binary_search(mylist, search, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if search == mylist[mid]:
            return mid
        elif search < mylist[mid]:
            return binary_search(mylist, search, low, mid - 1)
        else:
            return binary_search(mylist, search, mid + 1, high)



mylist = [1, 3, 5, 8, 9, 12, 15, 22, 33, 44, 55]
search = 3
low = 0
high = len(mylist) - 1


print(binary_search(mylist, search, low, high))

