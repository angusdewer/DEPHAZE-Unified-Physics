import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from core.constants import PHI, PHI2, PHI3, BISTABLE_DRAG

def run_alpha_derivation():
    print("--- DEPHAZE PROOF: FINE-STRUCTURE CONSTANT (ALPHA) ---")
    
    # 1. TOPOLOGICAL DERIVATION
    # Ideal Cycle (360 degrees) distributed by Golden Surface (Phi^2)
    # Minus the Bistable Projection Drag (2/Phi^3)
    calculated_inverse = (360.0 / PHI2) - BISTABLE_DRAG
    
    # 2. REFERENCE (CODATA 2018)
    measured_inverse = 137.035999
    
    print(f"Structure: (360 / Phi^2) - (2 / Phi^3)")
    print(f"Calculated: {calculated_inverse:.6f}")
    print(f"Measured:   {measured_inverse:.6f}")
    print(f"Accuracy:   {100 * (1 - abs(calculated_inverse - measured_inverse)/measured_inverse):.6f}%")
    print("------------------------------------------------------")

if __name__ == "__main__":
    run_alpha_derivation()
