
def rob(nums):
    dp = [0] * (len(nums)+1)
    dp[0] = 0
    dp [1] = nums[0]

    for i in range(2, len(dp)):
        w = nums[i-1]
        dp[i] = max( dp[i-1], dp[i-2]+w )

    return dp[-1]

if __name__ == "__main__":

    # test case 1
    nums = [1,2,3,1]
    print(rob(nums))

    # test case 2
    nums = [2,7,9,3,1]
    print(rob(nums))
