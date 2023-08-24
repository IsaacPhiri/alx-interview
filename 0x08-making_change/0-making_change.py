#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the 
    # minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
