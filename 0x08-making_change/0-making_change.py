#!/usr/bin/python3
"""
Making Change module
"""



def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    dp = {}
    dp[0] = 0

    for i in range(1, total + 1):
        dp[i] = float('inf')
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
