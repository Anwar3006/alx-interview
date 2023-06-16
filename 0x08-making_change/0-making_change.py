#!/usr/bin/python3
"""
Coin Change Problem.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total.
    """
    amount = total
    if total <= 0:
        return 0
    # create list to house the number of coins needed for each amount
    # from 1 to the amount
    DP_amount = [float('inf') for _ in range(amount + 1)]
    # set 0th index to 0(0 requires 0 coins)
    DP_amount[0] = 0

    # loop through each amount
    for amt in range(1, amount + 1):
        for coin in coins:
            if coin <= amt:
                DP_amount[amt] = min(DP_amount[amt], DP_amount[amt - coin] + 1)
    return DP_amount[amount] if DP_amount[amount] != float('inf') else -1
