# # ==========================================================
# # Sieve of eratosthenes
import math
# def sieve_eratosthenes(n):
#     primes = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#
#     for i in range(2, n + 1):
#         if primes[i]:
#             print(i, end=' ')
#
# sieve_eratosthenes(10)

# # Segmented Sieve's
# prime = []
# def simpleSieve(n):
#     primes = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if primes[p]:
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1
#
#     for i in range(2, n):
#         if primes[i]:
#             prime.append(i)
#             print(i, end=" ")
#
#
# def segmentedSieve(n):
#     # Compute all the primes smaller than or equal to the
#     # square root of n using the simple sieve
#
#     limit = int(math.floor(math.sqrt(n)) + 1)
#     simpleSieve(limit)
#
#     low = limit
#     high = limit * 2
#
#     while low < n:
#         if high >= n:
#             high = n
#
#         marking = [True for i in range(limit + 1)]
#
#         for i in range(len(prime)):
#             lowLimit = int(math.floor(low / prime[i]) * prime[i])
#             if lowLimit < low:
#                 lowLimit += prime[i]
#
#             for j in range(lowLimit, high, prime[i]):
#                 marking[j - low] = False
#
#         for i in range(low, high):
#             if marking[i - low]:
#                 print(i, end=' ')
#
#         low = low + limit
#         high = high + limit
#
# segmentedSieve(100)

# simpleSieve(20)
# print(prime)

# ========================================================
# Product of primes
# def prod_primes(l, r):
#     primes = [True] * (r - l + 1)
#     for i in range(2, math.floor(math.sqrt(r))):
#         j = max(i * i, (l/i) * i)
#         while (j <= r):
#             if (j-r <= r - l) & (j - l >= 0):
#                 primes[j - l] = False
#             j += i
#     ans = 1
#     for j in range(r - l):
#         if primes[j]:
#             ans = (ans * (j + l)) % 1000000007
#
#     return ans
# print(prod_primes(1, 10))

# ========================================================
# Add Binary
# def addBinary(a, b) -> str:
#     max_len = max(len(a), len(b))
#     a = a.zfill(max_len)
#     b = b.zfill(max_len)
#     result = ''
#     carry = 0
#     for i in range(max_len - 1, -1, -1):
#         r = carry
#         r += 1 if a[i] == '1' else 0
#         r += 1 if b[i] == '1' else 0
#         result = ('1' if r % 2 == 1 else '0') + result
#         carry = 0 if r < 2 else 1
#
#     if carry != 0:
#         result = "1" + result
#
#     return result.zfill(max_len)
#
#
# print(addBinary('11','1'))
# =======================================================
# Is Subsequence

# def isSub(s, t):
#     s=list(s)
#     p=len(t)-len(s)
#     for i in range(p):
#         s.append('')
#
#     t=list(t)
#
#     j=0
#
#     i=0
#
#     while(i<len(s) and j<len(t)):
#
#         if(s[i]==t[j]):
#             s[i]=''
#             i+=1
#             j+=1
#         else:
#             j+=1
#
#     x=s.count('')
#
#     if(x==len(s)):
#         return True
#     else:
#         return False
#
# print(isSub('abc', 'ahbgdc'))

# ==================================================
# Isomorphic strings

# def isomorphic(s, t):
#     mapST, mapTS = {}, {}
#
#     for c1, c2, in zip(s, t):
#         if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
#             return False
#         mapST[c1] = c2
#         mapTS[c2] = c1
#     return True
#
# print(isomorphic('egg', 'add'))
# ===================================================
# Finding the divisors

# def divisors(n: int):
#     i = 1
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             if n/i == i:
#                 print(i, end=" ")
#             else:
#                 print(i , int(n/i), end=" ")
#         i += 1
#
# divisors(10)
# ===================================================
# Count the total number of divisors

# def count_divisors(n: int) -> int:
#     i = 1
#     l = []
#     while i <= math.sqrt(n):
#         if n % i == 0:
#             if n / i == i:
#                 l.append(i)
#             else:
#                 l.append(i)
#                 l.append(int(n/i))
#         i += 1
#
#     return len(l)
#
# print(count_divisors(10))
# =================================================
# kth smallest factor

# def smallestFactor(n: int, k: int):
#     t = 0
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             t += 1
#             if t == k:
#                 return i
#     t += 1
#     if t == k:
#         return n
#     else:
#         return -1
#
# print(smallestFactor(10, 3))
# =================================================
# Array form of integer

# def array_form(n: [int], k: int):
#     str_l = [str(i) for i in n]
#     toInt = int("".join(str_l))
#     added = toInt + k
#     str_to_int = [int(i) for i in list(str(added))]
#     return str_to_int
#
# print(array_form([1, 2, 3], 334))
# =================================================
# All prime factors of n

# def prime_factors(n: int):
#     while n % 2 == 0:
#         print(2)
#         n = n / 2
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             print(i)
#             n = n / i
#
#     if n > 2:
#         print(n)
#
# prime_factors(6)

# ===================================================
# Least Prime Factor

# def leastPrimeFactor(n):
#     l = [0] * (n + 1)
#     l[1] = 1
#     for i in range(2, n + 1):
#         if l[i] == 0:
#             l[i] = i
#             for j in range(i * i, n + 1, i):
#                 if l[j] == 0:
#                     l[j] = i
#
#     return l[1:]
#
#
# print(leastPrimeFactor(12))

# ===================================================
# Largest Prime Number
# def largestPrime(n):
#     l = []
#     if n == 0:
#         return None
#     while n % 2 == 0:
#         l.append(2)
#         n = n / 2
#
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             l.append(i)
#             n = n / i
#
#     if n > 2:
#         l.append(n)
#
#     return int(max(l))
#
# print(largestPrime(6))

# ===================================================
# Prime Factorization using sieve O(log(n)) for multiple queries

# max_n = 100001
# spf = [0] * (max_n + 1)
#
# def least_prime():
#     spf[1] = 1
#     for i in range(2, max_n):
#         spf[i] = i
#
#     for i in range(4, max_n, 2):
#         spf[i] = 2
#
#     for i in range(3, math.ceil(math.sqrt(max_n))):
#         if spf[i] == i:
#             for j in range(i * i, max_n, i):
#                 if spf[j] == j:
#                     spf[j] = i
#
#
# def primeFactor(n):
#     res = set()
#     while n != 1:
#         res.add(spf[n])
#         n = n // spf[n]
#
#     return res
#
# least_prime()
# x = 100
# print(primeFactor(x))

# ===================================================
# Sum of all factors with O(N) and O(sqrt(N))
# def sum_factors(n):
#     sum = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             sum += i
#
#     return 1 + sum
#
# print(sum_factors(15))

# def sumFactor(n):
#     if n == 1:
#         return 1
#
#     sum = 0
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             if (n / i) == i:
#                 sum += (n/i)
#             else:
#                 sum += i + (n/i)
#
#     return 1 + n + int(sum)
#
# print(sumFactor(15))

# By using the formula
# def factor_sum(n):
#     sum = 1
#     if n == 1:
#         return 1
#
#     for i in range(2, int(math.sqrt(n)) + 1):
#         curr_sum = 1
#         curr_term = 1
#         while n % i == 0:
#             n = n / i
#             curr_term *= i
#             curr_sum += curr_term
#
#         sum *= curr_sum
#
#     if n > 2 :
#         sum = sum * (1 + n)
#
#     return sum
#
# print(factor_sum(30))
# ===============================================
# GCD or HCF of two numbers using the euclidean subtraction algorithm
# Has Time complexity of O(min(a, b))

# Iterative method
# def gcd(a: int, b: int) -> int:
#     min_num = min(a, b)
#     while min_num:
#         if a % min_num == 0 and b % min_num == 0:
#             break
#         min_num -= 1
#
#     return min_num
#
# print(gcd(36, 60))

# Recursive method
# def gcd(a: int, b: int) -> int:
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#
#     if a == b:
#         return a
#
#     if a > b:
#         return gcd(a - b, b)
#
#     return gcd(a, b - a)
#
# print(gcd(98, 56))

# Gcd using the extended euclidean algorithm
# Time complexity O(log(min(a, b)))
# def extented_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#
#     g, x1, y1 = extented_gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#
#     return g, x, y
#
#
# print(extented_gcd(98, 56))
# ====================================================
# Linear Diophantine equations

# def gcd(a, b):
#     if b == 0:
#         return a
#
#     return gcd(b, a % b)
# def linear(a, b, c):
#     return 1 if (c % gcd(a, b) == 0) else 0
#
# print(linear(3, 6, 9))

# ======================================================
# Least common multiple using GCD by O(log(min(a, b)))

# def gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#
#     g, x1, y1 = gcd(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#
#     return g, x, y
#
# def lcm(a, b):
#     return (a * b) // (gcd(a, b)[0])
#
# print(lcm(15, 25))

# =======================================================
# Maximum and minimum in an array using tournament method with O(n)
# def findSum(A,N):
#     max_num = A[0]
#     min_num = A[0]
#     if N == 1:
#         return A[0] + A[0]
#
#     elif N == 2:
#         if A[0] > A[1]:
#             max_num = A[0]
#             min_num = A[1]
#         else:
#             max_num = A[1]
#             min_num = A[0]
#
#         return max_num + min_num
#
#     for i in range(N):
#         if A[i] > max_num:
#             max_num = A[i]
#         elif A[i] < min_num:
#             min_num = A[i]
#
#     return max_num + min_num
#
# print(findSum([-2, 1, -4, 5, 3], 5))
# =========================================================
# Best time to buy stocks and sell stocks

# def buy_sell(l: [list]) -> int:
#     left, right = 0, 1
#     currProfit = 0
#     while right < len(l):
#         if l[left] < l[right]:
#             profit = l[right] - l[left]
#             currProfit = max(profit, currProfit)
#         else:
#             left = right
#         right += 1
#
#     return currProfit
#
# print(buy_sell([7,1,5,3,6,4]))

# ==========================================
# Counting frequencies of the elements

# def count(arr):
#     mp = {}
#     for i in range(len(arr)):
#         if arr[i] not in mp.keys():
#             mp[arr[i]] = 1
#         else:
#             mp[arr[i]] += 1
#
#     return mp
#
# print(count([10, 20, 20, 10, 10, 20, 5, 20]))

# Contains duplicates
# def isDuplicate(arr):
#     mp = set()
#     for i in arr:
#         if i not in mp:
#             mp.add(i)
#         else:
#             return True
#     return False
#
# print(isDuplicate([10, 20]))

# ================================================
# Two Sum
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i):
#             if nums[i] + nums[j] == target:
#                 return i, j
#     return -1
#
# print(two_sum([3, 3], 6))
# ===============================================
# Reverse integer
# def int_reverse(x):
#     if x >= 0:
#         l = list(str(x))[::-1]
#         if l[0] == "0":
#             return int("".join(l[1::]))
#         else:
#             return int("".join(l))
#
#     l = list(str(x))
#     sign = l[0]
#     l_rev = l[1::]
#     temp = l_rev[::-1]
#     if temp[0] == "0":
#         return int(sign + "".join(temp[1::]))
#     else:
#         return int(sign + "".join(temp))
#
# print(int_reverse(120))

# print(list(str(-123))[1::])
# ===============================================
# Longest palindrome

# def palindrome(s: str):
#     mp = {}
#
#     for char in s:
#         mp[char] = mp.get(char, 0) + 1
#
#     res, odd = 0, False
#
#     for key, count in mp.items():
#         if count % 2 == 0:
#             res += count
#         else:
#             odd = True
#             res = res + count - 1
#
#     if odd:
#         res += 1
#     return res
#
# print(palindrome('abccccdd'))
# ===============================================
# Number compression using Hashmap or unordered list
# def reduced_form(l):
#     temp = l
#     temp = sorted(temp)
#
#     mp = dict()
#     for i in range(len(l)):
#         mp[temp[i]] = i
#
#     for i in range(len(l)):
#         l[i] = mp[l[i]]
#
#     return l
#
# print(reduced_form([10, 40, 20]))
# ===============================================
# Kadane's Algorithm

# def max_subarray(l: list) -> int:
#     max_so_far = -99999999999999999999
#     max_ending_here = 0
#
#     for i in range(len(l)):
#         max_ending_here = max_ending_here + l[i]
#         if max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#         if max_ending_here < 0:
#             max_ending_here = 0
#
#     return max_so_far
#
#
# print(max_subarray([-1]))
# ===============================================
# String compression

# def compress(l: list) -> :
#     mp = {}
#     s = ""
#     for char in l:
#         if char not in mp:
#             mp[char] = 1
#         else:
#             mp[char] += 1
#
#     for key, val in mp.items():
#         if mp[key] == 1:
#             s += key
#         else:
#             s += key + str(val)
#
#     return len(s) if s else 0
#
# print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

# def compress(chars: list) -> int:
#     i = 0
#     to = 0
#     while i < len(chars):
#         j = i
#         while j < len(chars) and chars[j] == chars[i]:
#             j += 1
#
#         num = j - i
#         chars[to] = chars[i]
#         to += 1
#         if num > 1:
#             for digit in str(num):
#                 chars[to] = digit
#                 to += 1
#         i = j
#     chars = chars[:to]
#     return to
#
# print(compress([]))
# ===============================================
# def string_match(haystack, needle) -> int:
#
#     l = []
#     n, m = len(haystack), len(needle)
#
#     for i in range(n - m + 1):
#         count = 0
#         for j in range(m):
#             if haystack[i + j] != needle[j]:
#                 break
#             count += 1
#         if count == m:
#             l.append(i)
#
#     return l[0] if l else -1
#
#
# print(string_match('mississippi', 'issip'))
# ===============================================
# Count the number of sub arrays with fixed bounds

def count_sub(arr, minK, maxk):
    res = 0
    bad_index, left_index, right_index = -1, -1, -1

    for i, num in enumerate(arr):
        if not minK <= num <= maxk: bad_index = i
        if num == minK: left_index = i
        if num == maxk: right_index = i
        res += max(0, min(left_index, right_index) - bad_index)

    return res

print(count_sub([1,3,5,2,7,5], 1, 5))
    
