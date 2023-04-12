# Problem - 1

# Adds the consecutive numbers
# Basically x -> tends to add 1 + 2 + 3 + ... + x = x(x + 1)/2 and added with y ==> x(x + 1)/2 + y
# Time Complexity O(N)

# def func(x, y):
#     if x == 0:
#         return y
#     else:
#         return func(x - 1, x + y)
#
# print(func(5, 5))

# ================================================================================
# Problem - 2

# Selection Sort
# Searches for index that has minimum numbered element and swaps with the previous element encountered.
# Uses O(n^2) Time complexity

# def minIdx(arr, s, e):
#     smol = 99999999999
#     min_idx = 0
#     for i in range(s, e):
#         if smol > arr[i]:
#             smol = arr[i]
#             min_idx = i
#     return min_idx
#
# def selectionSort(arr, s, e):
#     if s >= e:
#         return
#     min_idx = minIdx(arr, s, e)
#     arr[s], arr[min_idx] = arr[min_idx], arr[s]
#     selectionSort(arr, s + 1, e)
#
# a = [34, 45, 1, 0, -1, 5]
# selectionSort(a, 0, len(a))
# print(a)

# ================================================================================
# Problem - 3

# Divides the input, which reduces the Time Complexity to O(log(N))

# def fun(n):
#     if n == 1:
#         return 0
#     else:
#         return 1 + fun(n // 2)
#
# print(fun(10))

# ================================================================================
# Problem - 4

# Divides the input, which reduces the Time Complexity to O(log(N))

# def fun(n):
#     if n == 1:
#         return 0
#     fun(n // 2)
#     print(n % 2, end=" ")
#
# fun(15)
# ================================================================================
# Problem - 5

# Time Complexity O(N)

# def fun(n):
#     i = 0
#     if n > 1:
#         fun(n - 1)
#     for i in range(n):
#         print(" * ", end="")
#
# fun(5)
# ================================================================================
# Problem - 6

# Time Complexity O(N)

# LIMIT = 1000
# def fun(n):
#     if n <= 0:
#         return
#     if n > LIMIT:
#         return
#     print(n, end=" ")
#     fun(2 * n)
#     print(n, end=" ")
#
# fun(5)

# ================================================================================
# Problem 6

# Time Complexity of O(2 ^ n)

# def fun(n):
#     if n > 0:
#         n -= 1
#         fun(n)
#         print(n, end=" ")
#         n -= 1
#         fun(n)
#
# fun(5)
# ================================================================================
# Problem 7

# Time Complexity of O(N)

# def fun(a, n):
#     if n == 1:
#         return a[0]
#     else:
#         x = fun(a, n - 1)
#     if x > a[n - 1]:
#         return x
#     else:
#         return a[n - 1]
#
# print(fun([12, 50, 21, 100, 5], 5))
# ================================================================================
# Problem 8

# Time Complexity of O(N)

# def fun(n):
#     if n % 2 == 1:
#         n += 1
#         return n - 1
#     else:
#         return fun(fun(n - 1))
#
# print(fun(200))
# ================================================================================
# Problem 9

# Time Complexity of log(a * b)

# def fun(a, b):
#     if b == 0:
#         return 1
#     if b % 2 == 0:
#         return fun(a * a, b // 2)
#
#     return fun(a * a, b // 2) * a
#
# a, b = 2, 4
# print(fun(a, abs(b)) if b >= 0 else abs(1 / fun(a, abs(b))))

# ================================================================================
# Problem 10

# Time Complexity of O(N)

# def fun(a):
#     if a > 100:
#         return a - 10
#     return fun(fun(a + 11))
#
# print(fun(99))
# ================================================================================
# Problem 11

# Time Complexity of O(2^n)

# def fun(s):
#     if len(s) == 0:
#         return
#     fun(s[1:])
#     fun(s[1:])
#     print(s[0], end=" ")
#
# fun('xyz')
# ================================================================================
# Problem 12

# fp = 0
# def fun(n):
#     global fp
#     if n <= 2:
#         fp = 1
#         return 1
#     t = fun(n - 1)
#     f = t + fp
#     fp = t
#     return f
#
# print(fun(8))
# ================================================================================
# Reach the target

# def solve(a, b, c, d):
#     if d == 0 and a == c:
#         return 'yes'
#     if d < 0:
#         return 'no'
#     if a <= c:
#         return solve(a + b, b, c, d - 1)
#     else:
#         return solve(a - b, b, c, d)
#
# t = int(input())
# res = []
# while t != 0:
#     a, b, c, d = [int(num) for num in input().split(" ")]
#     ans = solve(a, b, c, d)
#     res.append(ans)
#     t -= 1
#
# for ans in res:
#     print(ans)

# ================================================================================
# Geek-onacci series

# def series(a, b, c, n):
#     if n == 1:
#         return a
#     if n == 2:
#         return b
#     if n == 3:
#         return c
#     return series(a, b, c, n - 1) + series(a, b, c, n - 2) + series(a, b, c, n - 3)
#
# t = int(input())
# res = []
# while t != 0:
#     a, b, c, d = [int(num) for num in input().split(" ")]
#     ans = series(a, b, c, d)
#     res.append(ans)
#     t -= 1
#
# for ans in res:
#     print(ans)

# ================================================================================
# Geek's Garden similar to flood fill problem by leetcode

# count = 0
# def dfs(arr, r, c, count):
#     if r < 0 or r >= len(arr) or c < 0 or c >= len(arr[0]) or arr[r][c] == '0':
#         return
#     if arr[r][c] == '1':
#         count += 1
#         arr[r][c] = '0'
#         dfs(arr, r-1, c, count)
#         dfs(arr, r+1, c, count)
#         dfs(arr, r, c+1, count)
#         dfs(arr, r, c-1, count)
#         dfs(arr, r-1, c-1, count)
#         dfs(arr, r+1, c-1, count)
#         dfs(arr, r-1, c+1, count)
#         dfs(arr, r+1, c+1, count)
#
# t = int(input())
# res = []
# while t != 0:
#     row, col = map(int, input().split())
#     arr = []
#     for i in range(row):
#         arr.append(list(char for char in input()))
#     ans = 0
#     for i in range(row):
#         for j in range(col):
#             if arr[i][j] == '1':
#                 count = 0
#                 dfs(arr, i, j, count)
#                 ans = max(ans, count)
#     res.append(ans)
#     t -= 1
#
# print(res)

# ================================================================================
# Subsequences using Recursion

# def subseq(index, arr, l):
#     if index >= len(l):
#         print(arr)
#         return
#     arr.append(l[index])
#     subseq(index + 1, arr, l)
#     arr.pop()
#     subseq(index + 1, arr, l)
#
# subseq(0, [], [3,1,2,4,5])
