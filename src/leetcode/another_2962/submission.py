import random
from collections import defaultdict
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


def standard_procedure(nums: List[int], k: int) -> int:
    n = len(nums)
    ans = 0

    post_max = [n] * n
    pre_max = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[i] >= nums[stack[-1]]:
            post_max[stack.pop()] = i
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[i] > nums[stack[-1]]:
            pre_max[stack.pop()] = i
        stack.append(i)

    dct = defaultdict(list)
    for i in range(n):
        dct[nums[i]].append(i)

    for num in dct:
        lst = dct[num]
        m = len(lst)
        for j in range(k - 1, m):
            x = lst[j]
            if pre_max[x] < lst[j - k + 1]:
                left = lst[j - k + 1] - pre_max[x]
                right = post_max[x] - x
                ans += left * right
    return ans


def brute_force(nums: List[int], k: int) -> int:
    n = len(nums)
    ans = 0
    for i in range(n):
        cnt = defaultdict(int)
        ceil = 0
        for j in range(i, n):
            cnt[nums[j]] += 1
            if nums[j] > ceil:
                ceil = nums[j]
            if cnt[ceil] >= k:
                ans += 1
    return ans


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):
        n, k = ac.read_list_ints()
        assert 1 <= n <= 10 ** 5
        assert 1 <= k <= 10 ** 5
        nums = ac.read_list_ints()
        assert all(1 <= x <= 10 ** 6 for x in nums)
        assert len(nums) == n
        ans = standard_procedure(nums, k)
        ac.st(ans)
        return


Solution().main()
