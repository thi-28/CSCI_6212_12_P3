import time
import math
import pandas as pd
import matplotlib.pyplot as plt


def egg_drop_min_moves(m, n):
    dp = [0] * (m + 1)
    moves = 0
    while dp[m] < n:
        moves += 1
        for eggs in range(m, 0, -1):
            dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
    return moves

def run_experiment():

    ns = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**12]

    m = 100 

    REPETITIONS = 100_000 
    
    experimental = []
    theoretical = []

    print(f"Running experiment (m={m}, reps={REPETITIONS:,})...")

    for n in ns:
        start = time.time()
        for _ in range(REPETITIONS):
            egg_drop_min_moves(m, n)
        end = time.time()

        avg_time = (end - start) / REPETITIONS
        experimental.append(avg_time)

        theoretical.append(math.log(n, 2))

    # Normalize values 0–1
    exp_min, exp_max = min(experimental), max(experimental)
    theo_min, theo_max = min(theoretical), max(theoretical)

    eps = 1e-12 
    exp_norm = [(x - exp_min) / (exp_max - exp_min + eps) for x in experimental]
    theo_norm = [(x - theo_min) / (theo_max - theo_min + eps) for x in theoretical]

    # Create DataFrame
    df = pd.DataFrame({
        'n': ns,
        'Experimental (avg sec)': experimental,
        'Theoretical log2(n)': theoretical,
        'Experimental (Norm)': exp_norm,
        'Theoretical (Norm)': theo_norm
    })

    # ===== Numerical Output =====
    print("\nOUTPUT NUMERICAL DATA (UN-NORMALISED)")
    print(df[['n', 'Experimental (avg sec)', 'Theoretical log2(n)']], "\n")

    print("OUTPUT NUMERICAL DATA (NORMALISED) ")
    print(df[['n', 'Experimental (Norm)', 'Theoretical (Norm)']], "\n")

    # Graph 1 - Unnormalized

    plt.figure(figsize=(8,5))
    plt.plot(df['n'], df['Experimental (avg sec)'], 'bo-', label='Experimental (avg sec)')
    plt.plot(df['n'], df['Theoretical log2(n)'], 'ro-', label='Theoretical log2(n)')
    plt.xscale('log')
    plt.xlabel("Input Size n (log scale)")
    plt.ylabel("Time / Value")
    plt.title("Egg Dropping (m=100) - Unnormalized Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

    #GRaph 2 - Normalised

    plt.figure(figsize=(8,5))
    plt.plot(df['n'], df['Experimental (Norm)'], 'bo-', label='Experimental (Normalized)')
    plt.plot(df['n'], df['Theoretical (Norm)'], 'ro-', label='Theoretical (Normalized)')
    plt.xscale('log')
    plt.xlabel("Input Size n (log scale)")
    plt.ylabel("Normalized Value")
    plt.title("Egg Dropping (m=100) - Normalized Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

    return df


# Run experiment
df_results = run_experiment()