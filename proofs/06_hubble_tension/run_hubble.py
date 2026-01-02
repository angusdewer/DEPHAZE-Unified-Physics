import sys
import os

# --- BANK ELÉRÉSE ---
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

# --- KONSTANSOK ---
from core.constants import PHI5

def run_hubble_solution():
    print("--- DEPHAZE PROOF: HUBBLE TENSION (H0) ---")
    
    # 1. BEMENETI ADAT (Korai Univerzum / Ősállapot)
    # Forrás: Planck Collaboration 2018 (CMB mérés)
    H0_Early_CMB = 67.4  # km/s/Mpc
    
    # 2. DEPHAZE GEOMETRIAI SKÁLÁZÁS
    # A Protonnál már használtuk: Phi^5 a "Stabilitási Horizont".
    # A táguló téridő a "Mostani" (Lokális) állapotban ennyivel "lazább" vagy skálázottabb.
    # Scaling Factor = 1 + (1 / Phi^5)
    
    scaling_factor = 1.0 + (1.0 / PHI5)
    
    # 3. ELŐREJELZÉS (Lokális Univerzumra)
    H0_Local_Predicted = H0_Early_CMB * scaling_factor
    
    # 4. VALÓSÁG (Lokális Mérés)
    # Forrás: Riess et al. 2022 (SH0ES Team / Hubble Space Telescope)
    # A legpontosabb lokális mérés: 73.04 +/- 1.04
    H0_Local_Measured = 73.04
    
    # KIÍRÁS
    print(f"Early Universe (Planck CMB):   {H0_Early_CMB} km/s/Mpc")
    print(f"Phi^5 Stability Scaling:       {scaling_factor:.5f} (1 + 1/Phi^5)")
    print("-" * 50)
    print(f"DEPHAZE PREDICTED H0 (Local):  {H0_Local_Predicted:.2f} km/s/Mpc")
    print(f"MEASURED H0 (SH0ES/Riess):     {H0_Local_Measured:.2f} km/s/Mpc")
    print("-" * 50)
    
    diff = abs(H0_Local_Predicted - H0_Local_Measured)
    # Mivel a mérésnek van hibahatára (+/- 1.04), megnézzük, beleesünk-e.
    in_range = diff < 1.04
    
    print(f"Difference:                    {diff:.2f}")
    print(f"Within Measurement Error?      {'YES' if in_range else 'NO'}")
    print(f"Accuracy:                      {100 * (1 - diff/H0_Local_Measured):.2f}%")
    print("\nConclusion: The 'Tension' is not an error. It is the geometric scaling")
    print("between the Compact (Early) and Relaxed (Late) topology via Phi^5.")

if __name__ == "__main__":
    run_hubble_solution()