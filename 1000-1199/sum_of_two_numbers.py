# https://codeforces.com/problemset/problem/1788/B
import math

def main():
    c = int(input())

    for test in range(c):
        num = input()

        appendToY = True
        x = ['' for _ in range(len(num))]
        y = ['' for _ in range(len(num))]

        for i in range(len(num)):
            currDigit = int(num[i])

            x[i] = str(currDigit//2)
            y[i] = str(currDigit//2)

            if currDigit % 2 == 1:
                if appendToY: y[i] = str(int(y[i]) + 1)
                else: x[i] = str(int(x[i]) + 1)
                appendToY = not appendToY
            
        print(f"{int(''.join(x))} {int(''.join(y))}")

if __name__ == '__main__':
    main()