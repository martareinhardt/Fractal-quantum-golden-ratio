import numpy as np

# 1. Define the Golden Ratio (Phi) and its conjugate
PHI = (1 + np.sqrt(5)) / 2
PHI_CONJUGATE = (1 - np.sqrt(5)) / 2  # Which is -1/Phi
print(f"Phi (Φ):                       {PHI:.16f}")
print(f"Phi Conjugate (-1/Φ):          {PHI_CONJUGATE:.16f}")
print("-" * 45)

# 2. Define the Fibonacci Transition Matrix (F)
# This matrix governs the linear growth (iteration) of the Fibonacci sequence.
# In Quantum Mechanics, similar matrices (Operators) govern system evolution.
# F transforms the state vector (F(n-1), F(n)) into (F(n), F(n+1))
fibonacci_matrix = np.array([
    [1, 1],
    [1, 0]
])

# 3. Calculate the Eigenvalues (Autovalores)
# Eigenvalues (λ) represent the measurable properties (observables, like Energy) 
# of the system governed by the matrix F.
eigenvalues = np.linalg.eigvals(fibonacci_matrix)

# 4. Display Results and Comparison
print(f"Calculated Eigenvalues (λ₁ and λ₂):")
for i, lambda_val in enumerate(eigenvalues):
    print(f"  Eigenvalue {i+1} (λ):         {lambda_val:.16f}")

print("-" * 45)

# Test the fundamental relationship: Eigenvalues are exactly Φ and -1/Φ
is_phi = np.isclose(np.abs(eigenvalues), [PHI, np.abs(PHI_CONJUGATE)])
print(f"Test 1: |λ₁| equals Φ?  {is_phi[0]}")
print(f"Test 2: |λ₂| equals 1/Φ? {is_phi[1]}")

# Conclusion for the README:
# The eigenvalues of this fundamental iterative matrix are PHI and -1/PHI.
# This mathematically connects the constant of fractal growth (Phi) to the 
# fundamental states (eigenvalues) of a linear system, forming a key bridge 
# to quantum mechanical mod
eling.
