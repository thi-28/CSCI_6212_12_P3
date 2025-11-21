# Egg Dropping Problem - Dynamic Programming Solution

This repository contains an implementation and analysis of the classic Egg Dropping Problem using dynamic programming. The solution finds the minimum number of moves required to determine the critical floor (the highest floor from which an egg can be dropped without breaking) given `m` eggs and `n` floors.

## Files

- `MagicalEggs.py` - Main implementation script with interactive input and verbose mode
- `MagicalEggs_Graph.py` - Experimental analysis script with runtime comparison and visualization

## Running Instructions

### Prerequisites

- Python 3.6 or higher
- Required packages: matplotlib, pandas

### Installation

```bash
pip install matplotlib pandas
```

### Running the Analysis

**Main Script:**
```bash
python MagicalEggs.py
```

**Graph Analysis:**
```bash
python MagicalEggs_Graph.py
```

## What the Script Does

### MagicalEggs.py
- Prompts user for number of eggs (`m`) and number of floors (`n`)
- Calculates the minimum number of moves required using dynamic programming
- Determines the optimal first floor from which to drop the first egg
- Optionally displays detailed step-by-step DP table construction in verbose mode
- Uses high-precision nanosecond timing to measure execution time

### MagicalEggs_Graph.py
- Executes the algorithm for input sizes: [10³, 10⁴, 10⁵, 10⁶, 10⁷, 10⁸, 10⁹, 10¹⁰, 10¹²]
- Uses `m = 100` eggs for all experiments
- Runs 100,000 repetitions per input size to get average runtime
- Compares experimental runtime with theoretical `log₂(n)` complexity
- Displays results in comparison tables showing:
  - Input size (n)
  - Experimental runtime (average seconds)
  - Theoretical log₂(n) values
  - Normalized values (0-1 scale)
  - Ratios between experimental and theoretical
- Generates two plots:
  - Unnormalized comparison: Experimental runtime vs Theoretical log₂(n)
  - Normalized comparison: Both values normalized to 0-1 scale

## Expected Output

**MagicalEggs.py:**
- Console output showing timing data, minimum moves, and optimal first floor
- Optional verbose output displaying DP table construction step-by-step

**MagicalEggs_Graph.py:**
- Console output showing numerical data tables (both normalized and unnormalized)
- Two matplotlib windows displaying comparison plots
- The plot windows will remain open until manually closed

## Note

The `MagicalEggs_Graph.py` script may take several minutes to complete due to the large number of repetitions (100,000 per input size) and very large input values (up to 10¹²). The plot windows will remain open until manually closed.

## Key Findings

This analysis demonstrates that the egg dropping algorithm exhibits logarithmic behavior with respect to the number of floors (`n`), approximately O(log₂(n)) when the number of eggs (`m`) is sufficiently large. The dynamic programming approach efficiently solves the problem by building up a table that tracks the maximum number of floors that can be tested with a given number of eggs and moves, using the recurrence relation: `dp[eggs][moves] = dp[eggs-1][moves-1] + dp[eggs][moves-1] + 1`.

## Course Information

- **Course**: CSCI 6212 - Design and Analysis of Algorithms
- **Assignment**: Project 3
- **Team**: 3
