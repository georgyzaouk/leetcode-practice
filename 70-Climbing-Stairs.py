
def ClimbingStairs(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


if __name__ == "__main__":

    # test case 1
    n1 = 2
    print(ClimbingStairs(n1))

    # test case 2
    n2 = 3
    print(ClimbingStairs(n2))

    # test case 3
    n3 = 5
    print(ClimbingStairs(n3))