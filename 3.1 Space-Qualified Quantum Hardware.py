class SpaceQuantumHardware:
    """Space-qualified quantum sensing components"""
    
    def __init__(self):
        self.components = {
            'photon_pair_source': {
                'technology': 'Periodically Poled Potassium Titanyl Phosphate (PPKTP)',
                'wavelength': '1550 nm signal / 775 nm pump',
                'pair_rate': '100-1000 MHz',
                'entanglement_fidelity': '> 0.95',
                'space_qualification': 'Radiation-hardened, thermal stable',
                'mass': '2.5 kg',
                'power': '50 W',
                'lifetime': '> 7 years',
            },
            'single_photon_detectors': {
                'technology': 'Superconducting Nanowire Single Photon Detectors (SNSPD)',
                'efficiency': '> 0.85 at 1550 nm',
                'dark_count_rate': '< 100 counts/s',
                'timing_jitter': '< 20 ps',
                'cooling': '0.8-1.0 K required',
                'space_cryocooler': 'Stirling/pulse tube hybrid',
                'cooling_power': '300 W at 300K to 0.8K',
                'mass': '25 kg (including cryocooler)',
            },
            'quantum_memory': {
                'technology': 'Praseodymium-doped Yttrium Orthosilicate (Pr:YSO)',
                'storage_time': '> 1 second at 2K',
                'efficiency': '> 0.70',
                'multimode_capacity': '> 1000 modes',
                'space_adaptation': 'Magnetic shielding, thermal control',
                'mass': '15 kg',
                'power': '100 W',
            },
            'optical_telescope': {
                'aperture': '1.0 meter diameter',
                'material': 'Silicon carbide or beryllium',
                'wavefront_error': '< λ/20 rms',
                'pointing_stability': '< 0.1 μrad/10s',
                'thermal_stability': '< 1K gradient',
                'deployment': 'Foldable for launch, deploy in orbit',
                'mass': '150 kg',
            },
            'quantum_control_system': {
                'processor': 'Radiation-hardened FPGA + Quantum Control ASIC',
                'timing_resolution': '10 ps',
                'control_channels': '64 independent channels',
                'memory': '256 GB radiation-hardened',
                'interface': 'SpaceWire + SpaceFibre',
                'mass': '15 kg',
                'power': '150 W',
            }
        }
    
    def radiation_mitigation(self):
        """Radiation hardening strategies"""
        
        strategies = {
            'shielding': {
                'method': 'Tungsten and polyethylene composite',
                'thickness': '5-10 cm equivalent aluminum',
                'mass_penalty': '100-200 kg per satellite',
                'effectiveness': 'Reduces total ionizing dose by 90%',
            },
            'component_hardening': {
                'electronics': 'Radiation-hardened by design (RHBD)',
                'optics': 'Radiation-resistant coatings',
                'detectors': 'Annealing capability for radiation damage',
            },
            'error_correction': {
                'quantum': 'Surface code quantum error correction',
                'classical': 'Triple modular redundancy + EDAC',
                'data': 'Forward error correction (Reed-Solomon)',
            },
            'redundancy': {
                'critical_components': 'Dual or triple redundancy',
                'cold_sparing': 'Backup components powered off',
                'graceful_degradation': 'System operates at reduced capability',
            }
        }
        
        return strategies
