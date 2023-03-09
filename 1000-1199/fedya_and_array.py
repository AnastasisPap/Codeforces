# https://codeforces.com/problemset/problem/1793/B

def main():
    n = int(input())
    
    for test in range(n):
        x, y = map(int, input().split())
        
        ans = [str(y + i) for i in range(x-y)] + [str(x-i) for i in range(x-y)]
        print(2 * (x-y))
        print(' '.join(ans))


if __name__ == '__main__':
    main()