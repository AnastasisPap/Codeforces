from math import gcd

def main():
    c = int(input())

    for test in range(c):
        n = int(input())
        a = list(map(int, input().split()))

        maxGCD = 1
        total = sum(a)
        leftSum = 0
        for i in range(n-1):
            leftSum += a[i]
            rightSum = total - leftSum
            maxGCD = max(gcd(leftSum, rightSum), maxGCD)

        print(maxGCD)


if __name__ == '__main__':
    main()