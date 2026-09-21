
def lengthOfLIS_DP(self, nums: list[int]) -> int:

    dp = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp) if dp else 0
    

# better approach using binary search
def lengthOfLIS_BinarySearch(nums: list[int]) -> int:
    n = len(nums)
    ans = []

    # Initialize the answer list with the
    # first element of arr
    ans.append(nums[0])

    for i in range(1, n):
        if nums[i] > ans[-1]:
            # If the current number is greater than the last element of the answer list,
            # it means we have found a longer increasing subsequence.
            # Hence, we append the current number to the answer list.
            ans.append(nums[i])
        else:
            # If the current number is not greater than the last element of the answer list,
            # we perform a binary search to find the smallest element in the ANSWER list
            # that is greater than or equal to the current number.
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            # We update the element at the found position with the current number (from the nums list).
            # By doing this, we are maintaining a sorted order in the answer list.
            ans[low] = nums[i]

    # The length of the answer list
    # represents the length of the
    # longest increasing subsequence.
    return len(ans)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS_DP(None, nums))  # Output: 4
    print(lengthOfLIS_BinarySearch(nums))  # Output: 4
    print()

    nums = [0, 1, 0, 3, 2, 3]
    print(lengthOfLIS_DP(None, nums))  # Output: 4
    print(lengthOfLIS_BinarySearch(nums))  # Output: 4
    print()

    nums = [7, 7, 7, 7, 7, 7, 7]
    print(lengthOfLIS_DP(None, nums))  # Output: 1
    print(lengthOfLIS_BinarySearch(nums))  # Output: 1