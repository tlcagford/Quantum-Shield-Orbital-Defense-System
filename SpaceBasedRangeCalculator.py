class SpaceBasedRangeCalculator:
    """Calculate detection ranges from space"""
    
    def __init__(self):
        # Space-based system parameters
        self.parameters = {
            'orbit_altitude': 500e3,      # 500 km LEO
            'aperture_diameter': 1.0,     # 1 meter telescope
            'wavelength': 1.55e-6,        # 1550 nm (standard comms)
            'quantum_efficiency': 0.85,   # Better in vacuum
            'detection_probability': 0.99, # Higher required for space
            'false_alarm_rate': 1e-9,     # Much lower required
            'integration_time': 1.0,      # 1 second (can be longer)
            'photon_rate': 1e8,           # 100 MHz (higher in space)
            'background_temperature': 2.7, # Cosmic microwave background (K)
            'pointing_accuracy': 1e-6,    # 1 μrad pointing
            'quantum_advantage': 4.0,     # 6 dB advantage realizable
        }
        
        # Space targets
        self.targets = {
            'hypersonic_missile': {
                'cross_section': 0.01,    # 0.01 m² (stealthy)
                'speed': 5000,           # 5 km/s
                'altitude': 50e3,        # 50 km
            },
            'stealth_aircraft': {
                'cross_section': 0.001,   # 0.001 m² (very stealthy)
                'speed': 300,            # 300 m/s
                'altitude': 10e3,        # 10 km
            },
            'small_drone': {
                'cross_section': 0.001,   # 0.001 m²
                'speed': 50,             # 50 m/s
                'altitude': 0.1e3,       # 100 m
            },
            'satellite': {
                'cross_section': 1.0,     # 1 m²
                'speed': 7500,           # 7.5 km/s
                'altitude': 500e3,       # 500 km
            },
            'icbm_warhead': {
                'cross_section': 0.1,     # 0.1 m²
                'speed': 7000,           # 7 km/s
                'altitude': 200e3,       # 200 km
            }
        }
    
    def calculate_space_range(self, target_name):
        """Calculate detection range from space"""
        
        params = self.parameters.copy()
        target = self.targets[target_name]
        
        # Calculate aperture area
        A_r = np.pi * (params['aperture_diameter']/2)**2
        
        # Total photons in integration time
        N_total = params['photon_rate'] * params['integration_time']
        
        # Quantum advantage
        quantum_factor = params['quantum_advantage']
        
        # Background photon rate in space (much lower)
        # Using Planck's law for background
        background_photons = self.calculate_space_background()
        
        # Maximum range calculation for space
        # Simplified free-space quantum radar equation
        numerator = (N_total * params['quantum_efficiency'] * 
                    target['cross_section'] * A_r * quantum_factor)
        
        denominator = (4 * np.pi * params['wavelength']**2 * 
                      (np.log(1/(1-params['detection_probability'])) + 
                       background_photons))
        
        R_max = (numerator / denominator) ** 0.25
        
        return R_max
    
    def calculate_space_background(self):
        """Calculate background photon rate in space"""
        
        # Cosmic microwave background at 2.7K
        # Very low for optical wavelengths
        h = 6.626e-34      # Planck's constant
        k = 1.381e-23      # Boltzmann constant
        c = 3e8            # Speed of light
        T = 2.7            # CMB temperature
        
        wavelength = self.parameters['wavelength']
        frequency = c / wavelength
        
        # Blackbody radiation formula
        # Number of photons per mode
        photons_per_mode = 1 / (np.exp(h*frequency/(k*T)) - 1)
        
        # For optical, this is essentially 0 (CMB negligible at optical)
        return photons_per_mode * 1e-6  # Tiny factor
    
    def calculate_all_space_ranges(self):
        """Calculate ranges for all space targets"""
        
        results = {}
        
        for target_name in self.targets.keys():
            range_km = self.calculate_space_range(target_name) / 1000
            
            # Account for orbital altitude (slant range)
            altitude = self.targets[target_name]['altitude']
            orbital_altitude = self.parameters['orbit_altitude']
            
            # Slant range = sqrt(h_sat² + h_target² - 2*h_sat*h_target*cosθ)
            # Simplified: straight line distance
            if altitude < orbital_altitude:
                # Looking down at Earth target
                slant_range = np.sqrt(orbital_altitude**2 - altitude**2)
                ground_range = np.sqrt(slant_range**2 - (orbital_altitude - altitude)**2)
            else:
                # Looking at space target
                slant_range = np.abs(orbital_altitude - altitude)
                ground_range = 0
            
            detection_range = min(range_km, slant_range/1000)
            
            # Calculate warning time
            speed = self.targets[target_name]['speed']
            if detection_range > 0:
                warning_time = detection_range * 1000 / speed  # seconds
            else:
                warning_time = 0
            
            results[target_name] = {
                'maximum_range_km': round(detection_range, 1),
                'slant_range_km': round(slant_range/1000, 1),
                'ground_range_km': round(ground_range/1000, 1) if ground_range > 0 else 'N/A',
                'warning_time_s': round(warning_time, 1),
                'quantum_advantage_factor': self.parameters['quantum_advantage'],
                'orbit_altitude_km': self.parameters['orbit_altitude']/1000,
                'target_altitude_km': altitude/1000,
            }
        
        return results

# Calculate space-based ranges
space_calculator = SpaceBasedRangeCalculator()
space_ranges = space_calculator.calculate_all_space_ranges()
