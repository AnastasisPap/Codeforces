# https://codeforces.com/problemset/problem/1762/B
import math

def main():
    c = int(input())

    for t in range(c):
        n = int(input())
        a = list(map(int, input().split()))
        newA = [[val, i+1] for i, val in enumerate(a)]
        newA.sort(key=lambda x: x[0])

        operations = []
        for i in range(1, n):
            if newA[i][0] % newA[i-1][0] != 0:
                x_i = newA[i-1][0] * math.ceil(newA[i][0]/newA[i-1][0]) - newA[i][0]
                newA[i][0] += x_i
                operations.append(f'{newA[i][1]} {x_i}')
        
        print(len(operations))
        for operation in operations:
            print(operation)


if __name__ == '__main__':
    main()