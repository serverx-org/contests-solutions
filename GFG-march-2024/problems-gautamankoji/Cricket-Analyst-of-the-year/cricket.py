for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    res = [1]*n
    for a in range(1, n):
        for b in range(a):
            if res[a] < res[b] + 1 and l[a] > l[b]:
                res[a] = res[b] + 1
    print(max(res))