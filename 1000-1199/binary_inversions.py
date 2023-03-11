# https://codeforces.com/problemset/problem/1760/E
def calcScore(a):
    res = 0
    currOnes = 0

    for i in range(len(a)):
        if a[i] == 0: res += currOnes
        else: currOnes += 1

    return res

def main():
    c = int(input())

    for t in range(c):
        n = int(input())
        a = list(map(int, input().split()))

        leftmostZero = 0 
        while  leftmostZero < n and a[leftmostZero] != 0: leftmostZero += 1
        rightmostOne = n - 1
        while rightmostOne >= 0 and a[rightmostOne] != 1: rightmostOne -= 1

        leftArr = [val for val in a]
        leftScore = -1
        if leftmostZero < n: 
            leftArr[leftmostZero] = 1
            leftScore = calcScore(leftArr)
        rightArr = [val for val in a]
        rightScore = -1
        if rightmostOne >= 0:
            rightArr[rightmostOne] = 0
            rightScore = calcScore(rightArr)

        print(max(calcScore(a), rightScore, leftScore))


if __name__ == '__main__':
    main()