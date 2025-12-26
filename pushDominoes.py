def pushDominoes(dominoes: str) -> str:
    n = len(dominoes)
    left = [0] * n
    right = [0] * n

    prev = '.'
    count = 1

    # Left to right (R force)
    for i in range(n):
        if dominoes[i] == 'R':
            prev = 'R'
            count = 1
        elif dominoes[i] == 'L':
            prev = 'L'
        elif prev == 'R':
            right[i] = count
            count += 1

    prev = '.'
    count = 1

    # Right to left (L force)
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            prev = 'L'
            count = 1
        elif dominoes[i] == 'R':
            prev = 'R'
        elif prev == 'L':
            left[i] = count
            count += 1

    result = []

    for i in range(n):
        if right[i] == 0 and left[i] == 0:
            result.append(dominoes[i])
        elif right[i] == 0:
            result.append('L')
        elif left[i] == 0:
            result.append('R')
        elif right[i] == left[i]:
            result.append('.')
        elif left[i] > right[i]:
            result.append('R')
        else:
            result.append('L')

    return ''.join(result)


if __name__ == "__main__":
    tests = [
        "RR.L",
        ".L.R...LR..L..",
        "R....",
        "....L",
        "R.L",
        "...."
    ]

    for t in tests:
        print(f"Input:  {t}")
        print(f"Output: {pushDominoes(t)}")
        print("-" * 30)