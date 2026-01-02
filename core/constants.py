"""
DEPHAZE CORE CONSTANTS
----------------------
The Source of Truth.
Zero fitting parameters. All values derived from a single geometric seed.
"""
import numpy as np

# ==========================================
# 1. THE SEED (The Most Irrational Number)
# ==========================================
PHI = (1.0 + np.sqrt(5.0)) / 2.0  # 1.6180339887...

# ==========================================
# 2. THE TOPOLOGICAL DIMENSIONS
# ==========================================
PHI2 = PHI ** 2   # 2D: Surface (Used for Alpha)
PHI3 = PHI ** 3   # 3D: Volume (Used for Drag)
PHI5 = PHI ** 5   # 5D: Stability Horizon (Used for Hubble & Proton) <-- EZ HIÁNYZOTT!

# ==========================================
# 3. THE DYNAMICS (Derived Mechanics)
# ==========================================
# The energy cost of projecting a non-closing spiral into 3D space.
BISTABLE_DRAG = 2.0 / PHI3  

# ==========================================
# 4. UNIVERSAL SCALING (Cosmology & Galaxies)
# ==========================================
# Derivation: The Volumetric (3rd power) projection of the Stability Horizon (Phi^5).
# Logic: (Phi^5)^-3 = Phi^-15
UPSILON_GEO = PHI ** -15  # Exact geometric value: ~0.000733...
