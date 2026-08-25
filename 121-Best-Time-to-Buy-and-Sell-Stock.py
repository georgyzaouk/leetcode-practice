
def maxProfit_brute_force(prices: list[int]) -> int:

    max_profit = 0

    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]

            if profit > max_profit:
                max_profit = profit

    return max_profit


def maxProfit(prices: list[int]) -> int:
    left = 0    # left = buy
    right = 1   # right = sell
    max_profit = 0

    while right < len(prices):

        if prices[right] <= prices[left]:
            left = right
            right += 1

        else:
            profit = prices[right] - prices[left]
            if profit > max_profit:     # can use max_profit = max(max_profit, profit) 
                max_profit = profit     # instead of if statement
            right += 1

        # or put the right+=1 outside the if-else block, 
        # since it will always increment regardless of the condition.

    return max_profit


if __name__ == "__main__":

    # test case 1
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))  # Output: 5

    # test case 2
    prices = [7,6,4,3,1]
    print(maxProfit(prices))  # Output: 0
