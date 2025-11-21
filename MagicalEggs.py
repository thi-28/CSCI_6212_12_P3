def egg_drop(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    moves = 0
    while dp[m][moves] < n:
        moves += 1
        for eggs in range(1, m + 1):
            dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1
    return moves


def first_drop_floor(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    moves = 0
    while dp[m][moves] < n:
        moves += 1
        for eggs in range(1, m + 1):
            dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1
    first_floor = dp[m - 1][moves - 1] + 1
    return moves, first_floor

if __name__ == "__main__":
    m = int(input("Enter number of eggs: "))
    n = int(input("Enter number of floors: "))

    moves, first_floor = first_drop_floor(m, n)
    print(f"Minimum moves required: {moves}")
    print(f"First floor to drop from: {first_floor}")