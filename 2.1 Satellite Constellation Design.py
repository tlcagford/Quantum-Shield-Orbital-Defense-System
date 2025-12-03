class QuantumShieldSatellite:
    """Design of individual quantum sensing satellite"""
    
    def __init__(self):
        self.specifications = {
            'bus': {
                'size': 'SmallSat class (200-500 kg)',
                'power': '1-2 kW (solar panels)',
                'lifetime': '5-7 years',
                'orbit': 'Sun-synchronous LEO (500-600 km)',
                'pointing_accuracy': '0.001° (3.6 arcseconds)',
                'stability': '< 0.001°/s jitter',
            },
            'quantum_payload': {
                'sensor_type': 'Entangled photon quantum radar',
                'wavelength': '1550 nm (eye-safe, low atmospheric loss)',
                'aperture': '1.0 meter diameter telescope',
                'photon_source': 'PPKTP or PPLN crystal pumped by laser',
                'entanglement_rate': '100-1000 MHz pairs',
                'detectors': 'Superconducting nanowire single photon detectors',
                'cooling': 'Cryocooler to 0.8K for detectors',
                'quantum_memory': 'Rare-earth doped crystal (Pr:YSO)',
                'coherence_time': '> 1 second in space',
            },
            'classical_payloads': {
                'thermal_imager': 'Mid-wave IR (3-5 μm)',
                'visible_camera': 'High-resolution (0.5 m GSD)',
                'hyperspectral': '400-2500 nm, 10 nm resolution',
                'ais_receiver': 'Automatic Identification System',
                'adsb_receiver': 'Aircraft transponder monitoring',
            },
            'quantum_communication': {
                'qkd_system': 'BB84 or E91 protocol',
                'entanglement_distribution': 'To ground and other satellites',
                'key_rate': '1-10 kbps secure key',
                'pointing_requirements': 'μrad accuracy',
            }
        }
    
    def calculate_payload_mass(self):
        """Calculate mass budget for quantum payload"""
        
        mass_breakdown = {
            'optical_telescope': 150,      # kg (1 meter lightweight)
            'cryocooler_system': 80,       # kg (0.8K cooler)
            'laser_system': 20,            # kg (pump laser + PPLN)
            'detector_system': 15,         # kg (SNSPD array)
            'quantum_control': 25,         # kg (electronics)
            'thermal_control': 30,         # kg (radiators, heat pipes)
            'data_processing': 40,         # kg (FPGA/GPU computers)
            'structure': 100,              # kg (optical bench, mounts)
            'contingency': 40,             # kg (30% contingency)
            
            'total': 500,                  # kg
        }
        
        return mass_breakdown
    
    def calculate_power_budget(self):
        """Calculate power requirements"""
        
        power_breakdown = {
            'cryocooler': 300,            # Watts (0.8K operation)
            'pump_laser': 100,            # Watts (10W output @ 775nm)
            'detector_bias': 50,          # Watts (SNSPD operation)
            'quantum_control': 150,       # Watts (electronics cooling)
            'data_processing': 200,        # Watts (FPGA/GPU operations)
            'pointing_system': 100,       # Watts (reaction wheels, star trackers)
            'thermal_control': 150,       # Watts (heaters, controllers)
            'communications': 200,         # Watts (X-band downlink)
            
            'peak_power': 1250,           # Watts
            'average_power': 800,         # Watts
        }
        
        return power_breakdown

class SatelliteConstellation:
    """Design of full satellite constellation"""
    
    def __init__(self):
        self.configurations = {
            'minimal': {
                'satellites': 6,
                'orbits': 2,
                'planes': 3,
                'altitude': 500,
                'inclination': 97.6,  # Sun-synchronous
                'revisit_time': '2 hours',
                'coverage': '60% of Earth surface',
                'cost': '$300M',
            },
            'operational': {
                'satellites': 24,
                'orbits': 6,
                'planes': 4,
                'altitude': 600,
                'inclination': 'Mixed (SSO + equatorial)',
                'revisit_time': '30 minutes',
                'coverage': '95% of Earth surface',
                'cost': '$1.2B',
            },
            'strategic': {
                'satellites': 72,
                'orbits': 12,
                'planes': 6,
                'altitude': 'Mixed (LEO + MEO)',
                'inclination': 'Full global coverage',
                'revisit_time': '5 minutes',
                'coverage': '100% continuous',
                'cost': '$3.5B',
            }
        }
    
    def calculate_coverage(self, constellation_type='operational'):
        """Calculate coverage statistics"""
        
        config = self.configurations[constellation_type]
        
        # Simplified coverage calculation
        satellites = config['satellites']
        altitude_km = config['altitude']
        
        # Field of view for quantum sensor
        # Assuming 1 m aperture at 1550 nm gives 1.9 μrad diffraction limit
        diffraction_limit = 1.22 * 1.55e-6 / 1.0  # radians
        fov_rad = diffraction_limit * 1000  # Practical FOV
        
        # Ground footprint at nadir
        earth_radius = 6371  # km
        satellite_height = altitude_km
        nadir_angle = fov_rad / 2
        
        # Calculate ground swath width
        ground_swath = 2 * (earth_radius + satellite_height) * np.sin(nadir_angle)
        
        # Satellite orbital period
        period_minutes = 2 * np.pi * np.sqrt((earth_radius + satellite_height)**3 / 3.986e5) / 60
        
        # Coverage calculations
        total_earth_area = 4 * np.pi * earth_radius**2
        daily_coverage_per_sat = ground_swath * 2 * np.pi * earth_radius * (24 * 60 / period_minutes)
        
        total_daily_coverage = daily_coverage_per_sat * satellites
        coverage_fraction = total_daily_coverage / total_earth_area
        
        return {
            'ground_swath_km': round(ground_swath, 1),
            'orbital_period_min': round(period_minutes, 1),
            'daily_coverage_per_sat_km2': round(daily_coverage_per_sat, 0),
            'total_daily_coverage_km2': round(total_daily_coverage, 0),
            'coverage_fraction': round(coverage_fraction, 3),
            'revisit_time_hours': round(24 / (satellites * coverage_fraction), 2)
        }
