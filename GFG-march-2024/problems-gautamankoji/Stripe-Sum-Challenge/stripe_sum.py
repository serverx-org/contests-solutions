for _ in range(int(input())):
    n = int(input())
    cmprt = list(map(int, input().split()))
    oneTwo = cmprt.count(1) + cmprt.count(2)
    threeFour = cmprt.count(3) + cmprt.count(4)
    print((oneTwo//2)*2 + threeFour*2 if oneTwo % 2 == 0 else -1)
