"""Functions for the cash register system based on greedy algorythm and dynamic programming"""


def find_coins_greedy(amount, denominations):
    """
    This function uses a greedy approach to find the number of coins
    needed for a given amount using available denominations.

    Args:
        amount: The amount of change to be given (integer).
        denominations: A list of available coin denominations (integers).

    Returns:
        A dictionary with coin denominations as keys and the number of coins
        needed as values.
    """
    coins = {}
    for denomination in denominations[
        ::-1
    ]:  # Loop through denominations in descending order (greedy)
        if amount >= denomination:
            coins[denomination] = (
                amount // denomination
            )  # Use as many coins as possible
            amount -= coins[denomination] * denomination
    return coins


def find_min_coins(amount, denominations):
    """
    This function uses dynamic programming to find the minimum number of
    coins needed for a given amount using available denominations.

    Args:
        amount: The amount of change to be given (integer).
        denominations: A list of available coin denominations (integers).

    Returns:
        A dictionary with coin denominations as keys and the number of coins
        needed for the minimum coin combination.
    """
    dp = [float("inf")] * (
        amount + 1
    )  # Initialize dp table with infinity (except dp[0] = 0)
    dp[0] = 0  # Base case: No change needed

    for coin in denominations:
        for i in range(coin, amount + 1):  # Iterate through possible amounts
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Update min coins needed

    # Reconstruct coin combination from dp table (optional)
    coins = {}
    i = amount
    while i > 0:
        for coin in denominations:
            if dp[i] == dp[i - coin] + 1:
                coins[coin] = coins.get(coin, 0) + 1
                i -= coin
                break
    return coins


# Usage example
coin_denominations = [1, 5, 10, 25, 50]

print(find_coins_greedy(367, coin_denominations))
print(find_min_coins(367, coin_denominations))
