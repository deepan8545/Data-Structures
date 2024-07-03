"""
In the "Kth Largest Element in an Array" problem, we are provided with an array of integers nums and an integer k. The objective is to determine the kth largest element in this array.

For example, with the array nums = [3,2,1,5,6,4] and k = 2, the expected answer is 5 since 5 is the second largest element in the array.

"""
'''
 This function rearranges the elements in the input list 'elements' such that
    all elements greater than or equal to the chosen pivot are on the right side
    of the pivot, and all elements smaller than the pivot are on the left side.
'''
def partition(arr: list[int], low:int, high,int) -> int:
    pivot = arr[high]
    i = low -1
    for k in range(low,high):
        i += 1
        arr[i], arr[k] = arr[k], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


#Using Sorted mechanism
# def find_kth_largest(arr: list[int], k: int) -> int:
#     return sorted(arr)[-k]

def find_kth_largest(arr: list[int], k: int) -> int:
    if not arr:
        return -1

    if not isinstance(k,int):
        raise ValueError("The K position should be an integer")

    if not 1 <= k <= len(arr):
        raise ValueError("K position is outside index")

    low, high = 0, len(arr) - 1
    while low <= high:

        if low > len(arr) - 1 or high < 0:
            return -1

        pivot_index = partition(arr, low, high)

        if pivot_index == k - 1:
            return arr[pivot_index]

        elif pivot_index > k - 1:
            high = pivot_index - 1

        else:
            low = pivot_index + 1

    return -1

def main():
    arr = [int(input(f"Enter {i}th element") for i in range(5))]
    find_kth_largest(arr, k=int(input("Enter the k pos")))

