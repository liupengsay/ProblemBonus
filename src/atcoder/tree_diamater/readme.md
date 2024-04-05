
# Title
最公平的划分

# From
企鹅笔试题拓展

# Description

给定一棵节点个数至少为$2$的边带权无根树，将树的任意一条边切断后将形成两棵树，求使得两棵树直径之差的绝对值最小的切断方案，并输出这个最小的直径之差绝对值。

# InputFormat
第一行为节点个数$n$，满足$2<=n<=2*10^5$

接下来的$n-1$行为边的信息，每行为使用空格分割的三个非负整数$u$ $v$ $w$，表示节点$u$和节点$v$之间有一条权值为$w$的边，节点编号从$0$开始，即有$0<=u<n$和$0<=v<n$，边的权值范围为$1<=w<=10^9$

# OutputFormat
输出一个整数，表示为所求切割方案最小的直径之差绝对值。

# Example
## input1
2
0 1 2
## output1
0
## input2
3
0 1 1
1 2 1
## output2
1

# Note
### Explanation1:
只有一条边，所以只有一种切割方案，切割后两棵树均为一个点，直径均为$0$，因此直径之差绝对值为$0$。

### Explanation2:
有两种切割方案，切割后两棵树直径为$0$和$1$或者$1$和$0$，因此直径之差绝对值为$1$。


### Standard Procedures and Test Cases
[Tree Diameter](https://github.com/liupengsay/ProblemBonus/tree/main/src/atcoder/tree_diameter)