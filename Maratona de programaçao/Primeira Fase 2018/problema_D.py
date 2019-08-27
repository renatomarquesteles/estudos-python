N = int(input())
res = 0
for i in range(N):
    bode = int(input())
    if bode == 2 or bode == 3:
        res += 1
print(res)
