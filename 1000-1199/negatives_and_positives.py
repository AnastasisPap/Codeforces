# https://codeforces.com/problemset/problem/1791/E

def main():
    k = int(input())

    for test in range(k):
        n = int(input())
        a = list(map(int, input().split()))

        neg_count = 0
        biggest_neg = float('-inf')
        smallest_pos = float('inf')
        hasZero = False
        total = 0
        for num in a:
            if num < 0:
                neg_count += 1
                biggest_neg = max(biggest_neg, num)
            elif num == 0: hasZero = True
            else:
                smallest_pos = min(smallest_pos, num)
            total += abs(num)


        if neg_count % 2 == 0 or hasZero: print(total)
        else: 
            total = total + 2 * (-smallest_pos if abs(biggest_neg) > smallest_pos else biggest_neg)
            print(total)

if __name__ == '__main__':
    main()