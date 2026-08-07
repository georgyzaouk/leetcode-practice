
def coinChange_Naive(coins: list[int], amount: int) -> int:
    # given a sorted list of coins
    coins.sort()

    if amount == 0:
        return 0

    # starting from the biggest coin
    current_sum = 0
    counter = 0

    i = len(coins)-1
    while i > -1:
        # add the coin to the current sum if it doesn't exceed the amount
        if current_sum + coins[i] <= amount:
            current_sum += coins[i]
            counter += 1

        # if the current sum exceeds the amount, move to the next smaller coin
        else:
            i -= 1

        # if the current sum equals the amount, return the counter
        if current_sum == amount:
            return counter

    # if the current sum doesn't equal the amount, return -1
    if current_sum != amount:
        return -1


def coinChange(coins: list[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    # test case 1
    coins = [1,2,5]
    amount = 11
    print(coinChange(coins, amount))

    # test case 2
    coins = [2]
    amount = 3
    print(coinChange(coins, amount))

    # test case 3
    coins = [1]
    amount = 0
    print(coinChange(coins, amount))

    # test case 51/189 (Naive/Greedy solution fails)
    coins = [186,419,83,408]
    amount = 6249
    print(coinChange(coins, amount))
