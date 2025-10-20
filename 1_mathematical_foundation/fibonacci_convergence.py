import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Golden Ratio (Phi)
# Phi is the positive solution to the quadratic equation x² - x - 1 = 0
PHI = (1 + np.sqrt(5)) / 2
print(f"Golden Ratio (Phi, Φ): {PHI:.16f}")
print("-" * 35)

# 2. Generate the Fibonacci Sequence
def generate_fibonacci(n_terms):
    """Generates the first n terms of the Fibonacci sequence."""
    a, b = 0, 1
    sequence = [a, b]
    for _ in range(n_terms - 2):
        a, b = b, a + b
        sequence.append(b)
    return sequence

n_terms = 15
fib_sequence = generate_fibonacci(n_terms)

# 3. Calculate the Ratio of Consecutive Terms (F(n) / F(n-1))
ratios = []
for i in range(3, n_terms):
    ratio = fib_sequence[i] / fib_sequence[i-1]
    ratios.append(ratio)
    print(f"F({i}) / F({i-1}) = {fib_sequence[i]} / {fib_sequence[i-1]} = {ratio:.16f}")

# 4. Visualize the Convergence
plt.figure(figsize=(10, 6))
plt.plot(ratios, 'o-', label='F(n) / F(n-1) Ratio')
plt.axhline(PHI, color='red', linestyle='--', label=f'Golden Ratio (Φ ≈ {PHI:.3f})')
plt.title('Convergence of Fibonacci Ratios to the Golden Ratio (Phi)')
plt.xlabel('Iteration (n)')
plt.ylabel('Ratio Value')
plt.legend()
plt.grid(True)
plt.savefig('1_mathematical_foundation/fibonacci_convergence_plot.png')
plt.show()

# Conclusion for the README:
# This script establishes PHI as the limiting constant for iterative, fractal-like growth patterns.
