n = int(input())
a = sorted(map(int, input().split()))
print(min(a[2 * i + n] for i in range(n)))
