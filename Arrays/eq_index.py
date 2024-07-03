"""
Given a sequence arr[] of size n, this function returns
an equilibrium index (if any) or -1 if no equilibrium index exists.

The equilibrium index of an array is an index such that the sum of
elements at lower indexes is equal to the sum of elements at higher indexes.

"""

def eq_index(arr: list[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0

    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value


    return -1



if __name__ == "__main__":
    n = int(input("Enter number of elements"))
    arr = [int(input()) for x in range(n) ]

    print(eq_index(arr))