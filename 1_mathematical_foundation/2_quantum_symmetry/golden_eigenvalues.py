import numpy as np

# 1. Define the Golden Ratio (Phi) and its conjugate
PHI = (1 + np.sqrt(5)) / 2
# PHI_CONJUGATE is -1/Phi (for comparison)
PHI_CONJUGATE = (1 - np.sqrt(5)) / 2
print(f"Phi (Φ):                       {PHI:.16f}")
print(f"Phi Conjugate (-1/Φ):          {PHI_CONJUGATE:.16f}")
print("-" * 45)


# 2. Define the Fibonacci Transition Matrix (F)
fibonacci_matrix = np.array([
    [1, 1],
    [1, 0]
])
print("Fibonacci Transition Matrix F:")
print(fibonacci_matrix)


# 3. Calculate the Eigenvalues (Autovalores)
# These represent the fundamental resonant modes (observables) of the system.
eigenvalues = np.linalg.eigvals(fibonacci_matrix)

# 4. Display Results and Comparison
print("-" * 45)
print("Calculated Eigenvalues (λ₁ and λ₂):")
for i, lambda_val in enumerate(eigenvalues):
    print(f"  Eigenvalue {i + 1} (λ):         {lambda_val:.16f}")

print("-" * 45)

# Test the fundamental relationship: Eigenvalues are exactly Φ and -1/Φ
# Sort the eigenvalues for consistent comparison with [ -1/Φ, Φ ]
sorted_eigenvalues = np.sort(eigenvalues)
target_values = [PHI_CONJUGATE, PHI]

is_phi_close = np.isclose(sorted_eigenvalues, target_values)
print(f"Test: Are the eigenvalues [ -1/Φ, Φ ]? {is_phi_close.all()}")

# Conclusion for the README:
# The eigenvalues of this iterative matrix are PHI and -1/PHI, mathematically 
# connecting the constant of fractal growth to quantum system states.
