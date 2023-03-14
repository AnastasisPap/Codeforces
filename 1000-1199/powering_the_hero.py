# https://codeforces.com/problemset/problem/1800/C2
import heapq

def main():
    t = int(input())

    for c in range(t):
        n = int(input())
        cards = list(map(int, input().split()))

        total = 0
        heap = []
        for card in cards:
            if card == 0 and len(heap) > 0:
                total += -1 * heapq.heappop(heap)
            elif card > 0:
                heapq.heappush(heap, -card)
        
        print(total)


if __name__ == '__main__':
    main()