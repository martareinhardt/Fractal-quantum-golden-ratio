import matplotlib
# Use the 'Agg' backend to prevent the script from waiting for a graphical interface.
# This is crucial for running the code in headless environments (like GitHub tests).
matplotlib.use('Agg') 
import numpy as np
import matplotlib.pyplot as plt
import os

# --- Setup ---
# Define the Golden Ratio (Phi)
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

n_terms = 15 # Keep this number small for fast execution
fib_sequence = generate_fibonacci(n_terms)

# --- Ratio Calculation and Output ---
ratios = []
for i in range(2, n_terms):
    if fib_sequence[i-1] != 0:
        ratio = fib_sequence[i] / fib_sequence[i-1]
        ratios.append(ratio)
        if i >= 3: # Skip the first few for cleaner output
             print(f"F({i}) / F({i-1}) = {fib_sequence[i]} / {fib_sequence[i-1]} = {ratio:.16f}")

# --- Plot Generation (Saving to File) ---
# Create the directory if it doesn't exist to prevent IO errors
output_dir = '1_mathematical_foundation'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
plt.figure(figsize=(10, 6))
plt.plot(ratios, 'o-', label='F(n) / F(n-1) Ratio')
plt.axhline(PHI, color='red', linestyle='--', label=f'Golden Ratio (Φ ≈ {PHI:.3f})')
plt.title('Convergence of Fibonacci Ratios to the Golden Ratio (Phi)')
plt.xlabel('Iteration (n)')
plt.ylabel('Ratio Value')
plt.legend()
plt.grid(True)

# Save the plot file and explicitly close the figure to free up resources.
plot_path = os.path.join(output_dir, 'fibonacci_convergence_plot.png')
plt.savefig(plot_path)
plt.close() 

print(f"\nPlot saved successfully to: {plot_path}")

# Note: The plt.show() command is intentionally omitted to prevent timeouts.
