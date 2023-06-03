#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """Is winner"""
    prime_cache = [False, False] + [True] * (max(nums) - 1)

    # Generate a cache of prime numbers up to the maximum number in nums
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if prime_cache[i]:
            for j in range(i * i, max(nums) + 1, i):
                prime_cache[j] = False

    # Helper function to check if a number is prime
    def is_prime(num):
        return prime_cache[num]

    # Count the number of rounds won by Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play x rounds of the game
    for n in nums:
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the winner based on the number of rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
