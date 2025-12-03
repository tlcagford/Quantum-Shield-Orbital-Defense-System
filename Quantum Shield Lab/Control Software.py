# config/quantum_lab_config.yaml
system:
  name: "Quantum-Shield-Lab-001"
  
instruments:
  laser:
    manufacturer: "Cobolt"
    model: "06-DPL"
    wavelength: 532  # nm
    max_power: 100  # mW
  
  microwave:
    manufacturer: "Rigol"
    model: "DSG3060A"
    frequency_range: [300e6, 6e9]  # Hz
    power_range: [-20, 20]  # dBm
  
  detector:
    manufacturer: "IDQuantique"
    model: "ID230"
    dark_count: <100  # counts/s
    dead_time: 50  # ns
  
  daq:
    manufacturer: "National Instruments"
    model: "PCIe-6363"
    sampling_rate: 2e6  # Hz
    resolution: 16  # bits
