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
    print(f"{'n':>12} {'Experimental (avg sec)':>25} {'Theoretical log₂(n)':>25} {'Ratio':>10}")
    print("-" * 75)
    for i, n in enumerate(ns):
        ratio = experimental[i] / theoretical[i] if theoretical[i] > 0 else 0
        print(f"{n:>12} {experimental[i]:>25.6f} {theoretical[i]:>25.6f} {ratio:>10.2f}")

    print("\nOUTPUT NUMERICAL DATA (NORMALISED)")
    print(f"{'n':>12} {'Experimental (Norm)':>25} {'Theoretical (Norm)':>25} {'Ratio':>10}")
    print("-" * 75)
    for i, n in enumerate(ns):
        ratio = exp_norm[i] / theo_norm[i] if theo_norm[i] > 0 else 0
        print(f"{n:>12} {exp_norm[i]:>25.6f} {theo_norm[i]:>25.6f} {ratio:>10.2f}")

    # Graph 1 - Unnormalized (Both Experimental and Theoretical)
    plt.figure(figsize=(8, 6))
    
    # Experimental data
    plt.plot(df['n'], df['Experimental (avg sec)'], 'ro-', linewidth=2, markersize=6, label='Experimental Runtime (avg sec)')
    
    # Theoretical log₂(n) reference
    plt.plot(df['n'], df['Theoretical log2(n)'], 'bs--', linewidth=2, markersize=6, label='Theoretical log₂(n)')
    
    plt.xscale('log')
    plt.xlabel('n (log scale)')
    plt.ylabel('Value (seconds for experimental, log₂(n) for theoretical)')
    plt.title('Egg Dropping (m=100) - Runtime vs Theoretical log₂(n)')
    plt.grid(True, which='both', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show(block=False)

    # Graph 2 - Normalized (Both Experimental and Theoretical)
    plt.figure(figsize=(8, 6))
    
    # Experimental data
    plt.plot(df['n'], df['Experimental (Norm)'], 'ro-', linewidth=2, markersize=6, label='Experimental Runtime (Normalized)')
    
    # Theoretical log₂(n) reference
    plt.plot(df['n'], df['Theoretical (Norm)'], 'bs--', linewidth=2, markersize=6, label='Theoretical log₂(n) (Normalized)')
    
    plt.xscale('log')
    plt.xlabel('n (log scale)')
    plt.ylabel('Normalized Value (0-1 scale)')
    plt.title('Egg Dropping (m=100) - Normalized Comparison')
    plt.grid(True, which='both', alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

    return df


# Run experiment
df_results = run_experiment()