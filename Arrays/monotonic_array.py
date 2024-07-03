"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
"""

def is_monotonic(nums: list[int]) -> bool:

    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(
        nums[i] >= nums[i + 1] for i in range(len(nums) - 1)
    )


if __name__ == "__main__":
    print(is_monotonic([1, 2, 2, 3]))  # Output: True
    print(is_monotonic([6, 5, 4, 4]))  # Output: True
    print(is_monotonic([1, 3, 2]))