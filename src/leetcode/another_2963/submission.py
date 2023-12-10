import random
from sys import stdin
from typing import List


class FastIO:
    def __init__(self):
        self.random_seed = random.randint(0, 10 ** 9 + 7)
        return

    @staticmethod
    def read_int():
        return int(stdin.readline().rstrip())

    @staticmethod
    def read_float():
        return float(stdin.readline().rstrip())

    @staticmethod
    def read_list_ints():
        return list(map(int, stdin.readline().rstrip().split()))

    @staticmethod
    def read_list_ints_minus_one():
        return list(map(lambda x: int(x) - 1, stdin.readline().rstrip().split()))

    @staticmethod
    def read_str():
        return stdin.readline().rstrip()

    @staticmethod
    def read_list_strs():
        return stdin.readline().rstrip().split()

    @staticmethod
    def st(x):
        return print(x)

    @staticmethod
    def lst(x):
        return print(*x)

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def ceil(a, b):
        return a // b + int(a % b != 0)

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre


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


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):
        n = ac.read_int()
        assert 1 <= n <= 10 ** 5
        nums = ac.read_list_ints()
        assert all(1 <= x <= 10 ** 9 for x in nums)
        assert len(nums) == n
        ans = standard_procedure(nums)
        ac.st(ans)
        return


Solution().main()
