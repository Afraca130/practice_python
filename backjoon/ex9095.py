case = int(input())
rp = list(0 for i in range(10))
rp[0] = 1
rp[1] = 2
rp[2] = 4
for i in range(3, 10):
    rp[i] = rp[i-3] + rp[i-2] + rp[i-1]

for i in range(0, case):
    n = int(input()) - 1
    print(rp[n])
