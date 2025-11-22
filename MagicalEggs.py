import time

def egg_drop(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    moves = 0
    while dp[m][moves] < n:
        moves += 1
        for eggs in range(1, m + 1):
            dp[eggs][moves] = dp[eggs - 1][moves - 1] + dp[eggs][moves - 1] + 1
    return moves


def first_drop_floor(m, n, verbose=False):
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    if verbose:
        print(f"\n{'='*70}")
        print(f"Calculating minimum moves for {m} eggs and {n} floors")
        print(f"{'='*70}")
        print(f"\nDP Table: dp[eggs][moves] = maximum floors we can test")
        print(f"Formula: dp[eggs][moves] = dp[eggs-1][moves-1] + dp[eggs][moves-1] + 1")
        print(f"  - dp[eggs-1][moves-1]: floors tested if egg breaks")
        print(f"  - dp[eggs][moves-1]: floors tested if egg doesn't break")
        print(f"  - +1: current floor being tested\n")

    moves = 0
    while dp[m][moves] < n:
        moves += 1
        if verbose:
            print(f"Move {moves}:")
        
        for eggs in range(1, m + 1):
            prev_break = dp[eggs - 1][moves - 1]
            prev_no_break = dp[eggs][moves - 1]
            dp[eggs][moves] = prev_break + prev_no_break + 1
            
            if verbose and eggs <= min(5, m):  # Show first 5 eggs to avoid too much output
                print(f"  dp[{eggs}][{moves}] = dp[{eggs-1}][{moves-1}] + dp[{eggs}][{moves-1}] + 1")
                print(f"                = {prev_break} + {prev_no_break} + 1 = {dp[eggs][moves]}")
        
        if verbose:
            print(f"  After move {moves}, with {m} eggs we can test up to {dp[m][moves]} floors")
            if dp[m][moves] < n:
                print(f"  (Need {n} floors, continuing...)\n")
            else:
                print(f"  (Reached {dp[m][moves]} >= {n} floors!)\n")
    
    first_floor = dp[m - 1][moves - 1] + 1
    
    if verbose:
        print(f"{'='*70}")
        print(f"Result Calculation:")
        print(f"  Minimum moves needed: {moves}")
        print(f"  First floor to drop from: dp[{m-1}][{moves-1}] + 1 = {dp[m-1][moves-1]} + 1 = {first_floor}")
        print(f"  (This is the optimal starting floor for the first drop)")
        print(f"{'='*70}\n")
    
    return moves, first_floor

if __name__ == "__main__":
    m = int(input("Enter number of eggs: "))
    n = int(input("Enter number of floors: "))
    show_working = input("Show detailed working? (y/n): ").lower().strip() == 'y'

    start_ns = time.perf_counter_ns()
    moves, first_floor = first_drop_floor(m, n, verbose=show_working)
    elapsed_ns = time.perf_counter_ns() - start_ns
    
    print(f"m={m:>5}  n={n:>5}  time={elapsed_ns:>12}ns  moves={moves:>5}  first_floor={first_floor:>5}")
    print(f"\nMinimum moves required: {moves}")
    print(f"First floor to drop from: {first_floor}")
