# https://codeforces.com/problemset/problem/1743/C
def main():
    t = int(input())

    for c in range(t):
        n = int(input())
        lids = input()
        vals = list(map(int, input().split()))

        total = 0
        currMin = float('inf')
        currSum = 0

        hasInit = False
        for i in range(n):
            if lids[i] == '0':
                hasInit = True
                total += max(currSum - currMin, 0)
                currSum = vals[i]
                currMin = vals[i]
            else:
                if hasInit:
                    currSum += vals[i]
                    currMin = min(currMin, vals[i])
                    if i == n-1:
                        total += max(currSum - currMin, 0)
                else:
                    total += vals[i]
        
        print(total)
            


if __name__ == '__main__':
    main()