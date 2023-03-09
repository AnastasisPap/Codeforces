def main():
    c = int(input())

    for test in range(c):
        n = int(input())

        start, end = n*n, 1
        useStart = True
        reverse = False
        matrix = [[None for _ in range(n)] for row in range(n)]

        for i in range(n):
            row = reversed(range(n)) if reverse else range(n)
            for j in row:
                if useStart:
                    matrix[i][j] = str(start)
                    start -= 1
                else:
                    matrix[i][j] = str(end)
                    end += 1
                useStart = not useStart
            reverse = not reverse
    
        print('\n'.join([' '.join(row) for row in matrix]))

if __name__ == '__main__':
    main()