'''
 Find the median of two arrays.

    Args:
        nums1: The first array.
        nums2: The second array.

    Returns:
    The median of the two arrays.
'''

def find_median(arr1: list[int], arr2: list[int]) -> float:
    if not arr1 and not arr2:
        raise ValueError("Both input arrays are empty")

    merged = sorted(arr1+arr2)
    total_len = len(merged)

    if total_len % 2 == 1:
        return float(merged[total_len // 2])

    middle1 = merged[total_len // 2 -1]
    middle2 = merged[total_len // 2]

    return (float(middle1) + float(middle2)) / 2.0


def main():
    pass
