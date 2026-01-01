import sys
import os

# --- ÚTVONAL BEÁLLÍTÁSA (A BANK ELÉRÉSE) ---
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

# --- KONSTANSOK IMPORTÁLÁSA ---
from core.constants import PHI2, BISTABLE_DRAG

def run_lithium_solution():
    print("--- DEPHAZE PROOF: COSMOLOGICAL LITHIUM ---")
    
    # 1. BEMENETI ADATOK
    # Standard Model Prediction (Elméleti jóslat - ami hibás)
    Li_theory = 5.0  # x 10^-10
    
    # 2. DEPHAZE KORREKCIÓ
    # Dephaze Suppression: Surface Expansion (Phi^2) + Drag (2/Phi^3)
    # Ez a "geometriai ellenállás", ami gátolja a lítium képződését.
    suppression = PHI2 + BISTABLE_DRAG
    
    # 3. SZÁMÍTÁS (Zero-Fit)
    Li_corrected = Li_theory / suppression
    
    # 4. VALÓSÁG (Obszervált adat - Spite Plateau)
    Li_observed = 1.6  # x 10^-10
    
    # KIÍRÁS
    print(f"Standard Model Prediction: {Li_theory} (Túl sok)")
    print(f"Dephaze Suppression Factor: {suppression:.5f} (Phi^2 + Drag)")
    print("-" * 40)
    print(f"DEPHAZE PREDICTION:       {Li_corrected:.3f}")
    print(f"OBSERVED REALITY:         {Li_observed:.3f}")
    print("-" * 40)
    
    diff = abs(Li_corrected - Li_observed)
    accuracy = 100 * (1 - diff/Li_observed)
    print(f"MATCH ACCURACY:           {accuracy:.2f}%")

if __name__ == "__main__":
    # ITT VOLT A HIBA: .py NÉLKÜL KELL HÍVNI!
    run_lithium_solution()
