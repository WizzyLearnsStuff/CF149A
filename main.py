k = int(input())
a = map(int, input().split())

g = 0
c = 0
if k == 0:
    print(0)
    raise SystemExit

for i in sorted(a, reverse=True):
    g += i
    c += 1
    if g >= k:
        print(c)
        raise SystemExit
print(-1)
