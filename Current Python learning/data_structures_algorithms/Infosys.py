# Q1: While playing an RPG game, you were assigned to complete one of the hardest quests in this game.
# There are n monsters you’ll need to defeat in this quest. Each monster i is described with two
# integer numbers – poweri and bonusi. To defeat this monster, you’ll need at least poweri experience points. If
# you try fighting this monster without having enough experience points, you lose immediately. You will
# also gain bonusi experience points if you defeat this monster. You can defeat monsters in any order.
#
# The quest turned out to be very hard – you try to defeat the monsters but keep losing repeatedly. Your
# friend told you that this quest is impossible to complete. Knowing that, you’re interested, what is the
# maximum possible number of monsters you can defeat?
#
# (Question difficulty level: Hardest)
#
# Input:
#
# The first line contains an integer, n, denoting the number of monsters. The next
# line contains an integer, e, denoting your initial experience.
# Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, poweri,
# which represents power of the corresponding monster.
# Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer, bonusi,
# which represents bonus for defeating the corresponding monster.

# def rpgGameBonus(n, exp, monster_levels):
#     monster_levels.sort()
#     count = 0
#     for level in monster_levels:
#         if level[0] > exp:
#             break
#         exp += level[1]
#         count += 1
#
#     return count
#
#
# n = int(input("Monsters: "))
# exp = int(input("Experience: "))
# p = []; b = []
# for i in range(n):
#     p.append(int(input(f"Monster {i + 1}: ")))
#
# for i in range(n):
#     b.append(int(input(f"Monster {i + 1} bonus: ")))
#
# monster_levels = zip(p, b)
# print(rpgGameBonus(n, exp, list(monster_levels)))

# ================================================================================================================================
# Q2: Your birthday is coming soon and one of your friends, Alex, is thinking about
# a gift for you. He knows that you really like integer arrays with interesting properties.
# He selected two numbers, N and K and decided to write down on paper all integer arrays of
# length K (in form a[1], a[2], …, a[K]), where every number a[i] is in range from 1 to N, and,
# moreover, a[i+1] is divisible by a[i] (where 1 < i <= K), and give you this paper as a birthday present.
#
# Alex is very patient, so he managed to do this. Now you’re wondering, how many different arrays are written down on this paper?
#
# Since the answer can be really large, print it modulo 10000.
#
# Input:
#
# The first line contains an integer, n, denoting the maximum possible value in the arrays.
# The next line contains an integer, k, denoting the length of the arrays.

# def maxSumXor(n, k, nums):
#     maxSum = sum(nums)
#     for x in range(1, k + 1):
#         curr = 0
#         for num in nums:
#             curr += (x ^ num)
#         if curr > maxSum:
#             maxSum = curr
#
#     return maxSum
#
# n = int(input("N: "))
# k = int(input("K: "))
# nums = []
# for i in range(n):
#     nums.append(int(input(f"Num {i + 1}: ")))
# print(maxSumXor(n, k, nums))

# ================================================================================================================================
# Q3: You have to choose a set of integers S from the range [1, N-1] such that the product of
# integers in S is 1 modulo N. This means that if N=5, we can choose set S = [1,2,3] as the product is 6 and 6 modulo 5 is 1.
#
# Find the length of the biggest set S you can choose.
#
# Input Format
#
# The first line contains an integer N, denoting the given integer.
#
# Constraints  1<=N<= 5 * 10^5
#
# Sample Input 1
#
# 7
#
# Sample Output 1
#
# 5
#
# Explanation:
#
# We can choose set (1,2,3,4,5). Here product = 120 which mod 7 is 1

# def modOne(n):
#     def fact(n):
#         if n > 0:
#             return n * fact(n - 1)
#         else: return 1
#     for num in range(n - 1, 0, -1):
#         if fact(num) % n == 1:
#             return num
#     return 0
#
#
# n = int(input("N: "))
# print(modOne(n))

# ================================================================================================================================
# Q4: You are given an array of size N.
#
# An array A is considered a summer array if all the even values in A are on one side and odd values are on the other side.
#
# You are allowed to swap two adjacent elements in A in one operation. Find the
# minimum swap operations required to change A into a summer array.
#
# Input Format
#
# The first line contains an integer N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 <= i <= N) contains an integer describing A[i].
#
# Constraints 1<= N <= 10^5
#
# 1 <= A[i] <= 10^5
#
# Sample Input 1
#
# 3
#
# 1
#
# 2
#
# 2
#
# Sample Output 1
#
# 0
#
# Explanation:
#
# Here N=3 A= [1,2,2]. 0 swaps are required here as the odd number is already on the
# left and all the even number are already on the right

# def minSwaps(nums):
#     swaps = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums) - 1):
#             if nums[j] % 2 == 0 and nums[j + 1] % 2 != 0:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#                 swaps += 1
#                 break
#     return swaps
#
# n = int(input("N: "))
# nums = [int(input()) for _ in range(n)]
# print(minSwaps(nums))

# ================================================================================================================================
# Q4: You have an array A of N integers A1 A2 .. An. Find the longest increasing subsequence Ai1 Ai2 .. Ak
# (1 <= k <= N) that satisfies the following condition:
# For every adjacent pair of numbers of the chosen subsequence Ai[x] and Ai[x+1] (1 < x < k), the expression( Ai[x] & Ai[x+1] ) * 2 < ( Ai[x] | Ai[x+1] ) is true
#
# Note: ‘&’ is the bitwise AND operation, ‘ | ‘ is the bit-wise OR operation
#
# Input Format
#
# The first line contains an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing Ai.
# Sample Input 1
#
# 5
# 15
# 6
# 5
# 12
# 1
#
# Sample Output 1
#
# 2
#
# Explanation:
#
# One possible subsequence is: 5 12

# def longestConsecutiveSequence(nums):
#     seen, seq, maxSeq = set(nums), 0, 0
#     for num in nums:
#         if (num - 1) not in seen:
#             seq = 0
#             while (num + seq) in seen: seq += 1
#         maxSeq = max(maxSeq, seq)
#     return maxSeq
#
# n = int(input())
# nums = [int(input()) for _ in range(n)]
# print(longestConsecutiveSequence(nums))

