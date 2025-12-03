# calibration/magnetometer_calibration.py
import numpy as np
from scipy.optimize import curve_fit

def calibrate_magnetometer():
    """Calibrate NV center magnetometer sensitivity"""
    
    # Apply known magnetic fields
    field_strengths = np.linspace(-10e-6, 10e-6, 21)  # ±10 μT
    frequency_shifts = []
    
    for B in field_strengths:
        # Set Helmholtz coil current for desired field
        current = B / (0.8 * 100 * 0.01)  # N*I/R formula
        
        # Measure resonance frequency
        freq_shift = measure_resonance_shift(current)
        frequency_shifts.append(freq_shift)
    
    # Calculate gyromagnetic ratio
    # γ = 28 GHz/T for NV centers
    gyromagnetic_ratio = 28e9  # Hz/T
    
    # Fit linear relationship: Δf = γ * B
    def linear_fit(B, slope):
        return slope * B
    
    popt, pcov = curve_fit(linear_fit, field_strengths, frequency_shifts)
    measured_gamma = popt[0]
    
    # Calculate sensitivity
    # η = δB_min = δf_min / γ
    # where δf_min is minimum detectable frequency shift
    
    noise_floor = measure_frequency_noise()
    sensitivity = noise_floor / measured_gamma  # T/√Hz
    
    print(f"Measured γ: {measured_gamma/1e9:.2f} GHz/T")
    print(f"Sensitivity: {sensitivity*1e9:.2f} nT/√Hz")
    
    return sensitivity
