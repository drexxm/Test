print("welcome to GitHub By Buakaew")

n = 6
for i in range(n//2, n, 2):
    # Print spaces for the left side
    for j in range(1, n-i, 2):
        print(' ', end=' ')
    # Print stars for the left side
    for j in range(1, i+1):
        print('*', end=' ')
    # Print spaces in the middle
    for j in range(1, n-i+1):
        print(' ', end=' ')
    # Print stars for the right side
    for j in range(1, i+1):
        print('*', end=' ')
    print()

# Print the bottom part of the heart
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end=' ')
    for j in range(1, i*2):
        print('*', end=' ')
    print()

def print_smiley():
    smiley = [
        "      *****      ",
        "   **       **   ",
        "  *  O   O   *  ",
        " *     \_/     * ",
        " *               * ",
        "  *  \_____/   *  ",
        "   **       **   ",
        "      *****      "
    ]
    
    for line in smiley:
        print(line)

print_smiley()
