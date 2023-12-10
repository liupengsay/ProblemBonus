from typing import List


def standard_procedure(nums: List[int]) -> int:
    n = len(nums)
    mod = 10 ** 9 + 7

    dp = [0] * (n + 1)
    pre = [0] * (n + 1)
    dp[0] = pre[0] = 1

    dct = dict()
    ind = -1
    for i in range(n):
        pre[i + 1] = (pre[i] + dp[i]) % mod
        if nums[i] in dct and dct[nums[i]] > ind:
            ind = dct[nums[i]]
        cur = (pre[i + 1] - pre[ind + 1]) % mod
        dp[i + 1] = cur
        dct[nums[i]] = i
    return dp[-1]


def brute_force(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        dct = set()
        cur = 0
        for j in range(i, -1, -1):
            if nums[j] in dct:
                break
            dct.add(nums[j])
            cur += dp[j]
            cur %= mod
        dp[i + 1] = cur
    return dp[-1]


def brute_force_2(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0] = 1
    mod = 10 ** 9 + 7
    for i in range(n):
        cur = 0
        for j in range(i, -1, -1):
            if len(set(nums[j:i + 1])) < i - j + 1:
                break
            cur += dp[j]
            cur %= mod
        dp[i + 1] = cur
    return dp[-1]
