from typing import List, Dict, Tuple


def ways_to_make_change(total: int) -> int:
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache: Dict[Tuple[int, int], int] = {}
    return ways_to_make_change_helper(total, coins, 0, cache)


def ways_to_make_change_helper(
    total: int,
    coins: List[int],
    index: int,
    cache: Dict[Tuple[int, int], int]
) -> int:
    # valid solution: exact match
    if total == 0:
        return 1

    # invalid path
    if total < 0 or index == len(coins):
        return 0

    key = (total, index)
    if key in cache:
        return cache[key]

    coin = coins[index]
    ways = 0

    # choose 0..max_count of current coin
    max_count = total // coin
    for count in range(max_count + 1):
        remaining = total - count * coin
        ways += ways_to_make_change_helper(
            remaining,
            coins,
            index + 1,
            cache
        )

    cache[key] = ways
    return ways