
def search(nums: list[int], target: int) -> int:

    low = 0
    high = len(nums) - 1

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if nums[mid] == target:
            return mid

        # If x is greater, ignore left half
        elif nums[mid] < target:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


if __name__ == "__main__":

    # test case 1
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums, target))

    # test case 2
    nums = [-1,0,3,5,9,12]
    target = 2
    print(search(nums, target))