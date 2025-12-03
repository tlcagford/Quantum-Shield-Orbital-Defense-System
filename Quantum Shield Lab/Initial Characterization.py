# characterization/initial_test.py
import numpy as np
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager
from instruments import LaserController, MWGenerator, PhotonCounter

def measure_fluorescence():
    """Basic fluorescence measurement"""
    
    # Initialize instruments
    laser = LaserController('COM3', power=10)  # 10 mW
    mw = MWGenerator('TCPIP0::192.168.1.100::INSTR')
    counter = PhotonCounter('Dev1')
    
    # Sweep microwave frequency
    frequencies = np.linspace(2.7e9, 3.0e9, 301)
    counts = []
    
    for f in frequencies:
        mw.set_frequency(f)
        mw.set_power(10)  # dBm
        
        # Laser pulse
        laser.on()
        time.sleep(1e-3)
        laser.off()
        
        # Count photons
        photon_count = counter.read_counts(integration_time=0.1)
        counts.append(photon_count)
    
    # Plot ODMR spectrum
    plt.figure(figsize=(10,6))
    plt.plot(frequencies/1e9, counts, 'b-')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Fluorescence (counts)')
    plt.title('NV Center ODMR Spectrum')
    plt.grid(True)
    plt.savefig('data/odmr_initial.png')
    
    return frequencies, counts
