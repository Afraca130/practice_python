import sys

n = int(sys.stdin.readline())
dp = [i-1 for i in range(n+1)]

for i in range(1, n+1):
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i-1]+1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1, dp[i])
    else:
        dp[i] = min(dp[i], dp[i-1]+1)

print(dp[n])


# def function(n):
#     result = 0
#     if n == 1:
#         return result

#     result = function(n-1) + 1
#     if n % 3 == 0:
#         result = min(function(n//3)+1, result)
#     if n % 2 == 0:
#         result = min(function(n//2)+1, result)

#     return result


# print(function(int(input())))
