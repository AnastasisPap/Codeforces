# https://codeforces.com/problemset/problem/1759/C
def solve(l, r, x, a, b):
    if a == b: return 0
    elif abs(a-b) >= x: return 1
    elif (abs(a-l) >= x and abs(l-b) >= x) or (abs(a-r) >= x and abs(r-b) >= x): return 2
    elif (abs(a-l) >= x and abs(l-r) >= x and abs(r-b) >= x) or (
        abs(a-r) >= x and abs(r-l) >= x and abs(l-b) >= x): return 3
    else: return -1

def main():
    t = int(input())

    for c in range(t):
        l, r, x = map(int, input().split())
        a, b = map(int, input().split())

        print(solve(l, r, x, a, b))

if __name__ == '__main__':
    main()