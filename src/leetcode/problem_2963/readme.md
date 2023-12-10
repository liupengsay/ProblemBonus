
# Title
Another LeetCode 2962

# From
[LeetCode 2962. Count Subarrays Where Max Element Appears at Least K Times](https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
)

# Description

You are given an non-empty positive integer array **nums** with length **n** and a positive integer **k**.

Return the number of subarrays where **the maximum element of that subarray** appears **at least k** times in that subarray.

A subarray is a **contiguous sequence** of elements within an array.

# InputFormat
The first line contains two integers $n$ and $k$($1<=n<=10^5, 1<=k<=10^5$), denoting the
length of the non-empty positive integer array and the times which the maximum element of that subarray must appears at least in that subarray.

The second line contains an non-empty positive integer array $nums$, with length $n$($1 <= nums[i] <= 10^6$, $1 <= i <= n$).

# OutputFormat
print a single interger denoting the number of subarrays where the maximum element of that subarray appears at least $k$ times in that subarray.

# Example
## input1
5 2
1 3 2 3 3
## output1
6
## input2
4 3
1 4 2 1
## output2
0

# Note
### Explanation1:
The subarrays which contain the max element of that subarray at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

### Explanation2:
No subarray which contains the max element of that subarray at least 3 times.

### Standard procedures and test cases
[Another LeetCode 2962](https://github.com/liupengsay/ProblemBonus/tree/main/src/leetcode/problem_2962)