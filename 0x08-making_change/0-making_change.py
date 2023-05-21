#!/usr/bin/python3
"""
MakeChange module
"""


def makeChange(coins, total):
    """To determine the fewest number of coins
    """
    if total <= 0:
        return 0
    remainder = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_index >= n:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1
    return coins_count
