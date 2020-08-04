n = int(input())
if n == 0:
    n = 1
else:
    for i in range(1, n):
        n = i*n
print(n)
