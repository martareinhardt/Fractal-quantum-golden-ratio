import numpy as np

# --- Setup ---
# 1. Define the Golden Ratio (Phi)
PHI = (1 + np.sqrt(5)) / 2
print(f"Golden Ratio (Phi, Φ): {PHI:.16f}")
print("-" * 35)


# --- Fibonacci Sequence Generation ---
def generate_fibonacci(n_terms):
    """Generates the first n terms of the Fibonacci sequence."""
    if n_terms < 2:
        return [0] if n_terms == 1 else []

    a, b = 0, 1
    sequence = [a, b]
    for _ in range(n_terms - 2):
        a, b = b, a + b
        sequence.append(b)
    return sequence


n_terms = 15
fib_sequence = generate_fibonacci(n_terms)

# --- Ratio Calculation and Output ---
print("Calculating convergence ratio F(n) / F(n-1):")
ratios = []
for i in range(2, n_terms):
    if fib_sequence[i - 1] != 0:
        ratio = fib_sequence[i] / fib_sequence[i - 1]
        ratios.append(ratio)
        if i >= 3:
            print(
                f"F({i}) / F({i - 1}) = {fib_sequence[i]} / "
                f"{fib_sequence[i - 1]} = {ratio:.16f}"
            )

# Test the final calculated ratio against the true Phi
final_ratio = ratios[-1] if ratios else 0
is_close = np.isclose(final_ratio, PHI)
print("-" * 35)
print(f"Final calculated ratio: {final_ratio:.16f}")
print(f"Is the ratio close to Phi? {is_close}")

# Conclusion for the README:
# This script successfully demonstrates PHI as the limiting constant for 
# iterative growth patterns.
