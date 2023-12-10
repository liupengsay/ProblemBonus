from collections import defaultdict
from typing import List


def count_subarrays(nums: List[int], k: int) -> int:
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


def count_subarrays_brute_force(nums: List[int], k: int) -> int:
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
