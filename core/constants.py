"""
DEPHAZE CORE CONSTANTS
----------------------
The source of truth. No magic numbers.
All physical derivations originate from these geometric invariants.
"""
import numpy as np

# 1. THE SEED
PHI = (1.0 + np.sqrt(5.0)) / 2.0  # The Golden Ratio (1.618...)

# 2. THE TOPOLOGY
PHI2 = PHI ** 2   # Surface Topology (Expansion)
PHI3 = PHI ** 3   # Volumetric Topology (Projection / The Master Key)
PHI5 = PHI ** 5   # Stability Horizon (Hyper-surface)

# 3. THE DYNAMICS
# The "Friction" of existence. The cost of projecting from timeless Omega0 to temporal Psi.
BISTABLE_DRAG = 2.0 / PHI3  

# 4. UNIVERSAL SCALING
# Used for Galaxy Rotation (C) and Cosmology
UPSILON_GEO = 7.5e-4
