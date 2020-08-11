# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    mid = (start + end)//2
    if len(arr) <= 0:
        return -1

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid
        return binary_search(arr, target, start, end)
    elif arr[mid] < target:
        start = mid
        return binary_search(arr, target, start, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
