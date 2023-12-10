
# Title
Another LeetCode 2963

# From
[LeetCode 2963. Count the Number of Good Partitions](https://leetcode.com/contest/weekly-contest-375/problems/count-the-number-of-good-partitions/)

# Description

You are given a **0-indexed** array nums consisting of positive integers.

A partition of an array into one or more **contiguous** subarrays is called **good** if every subarray is **non-empty** and contains **distinct** numbers.

Print the **total number** of good partitions of nums.

Since the answer may be large, print it modulo **$10^9 + 7$**.

# InputFormat
The first line contains a integer $n$($1<=n<=10^5$), denoting the
length of the non-empty positive integer array.

The second line contains a positive integer array $nums$, with length $n$($1 <= nums[i] <= 10^9$, $0 <= i < n$).

# OutputFormat
print a single interger denoting the total number of good partitions of nums.

# Example
## input1
4
1 2 3 4
## output1
8
## input2
4
1 1 1 1
## output2
1
## input3
4
1 2 1 3
## output3
6
# Note
### Explanation1:
The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).
### Explanation2:
The only possible good partition is: ([1], [1], [1], [1]).
### Explanation3:
The 6 possible good partitions are: ([1], [2], [1], [3]), ([1], [2], [1,3]), ([1], [2,1,3]), ([1], [2,1], [3]), ([1,2], [1,3]), ([1,2], [1], [3]), 

### Standard procedures and test cases
[Another LeetCode 2963](https://github.com/liupengsay/ProblemBonus/tree/main/src/leetcode/another_2963)