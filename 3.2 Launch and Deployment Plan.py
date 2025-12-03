class SpaceDeployment:
    """Launch and deployment strategy"""
    
    def __init__(self):
        self.deployment_phases = {
            'phase_1': {
                'timeline': 'Year 1-2',
                'objective': 'Technology demonstration',
                'satellites': '2-3 pathfinder satellites',
                'launch_vehicles': ['Falcon 9', 'Electron'],
                'cost': '$150-200M',
                'orbit': '500 km SSO',
                'capabilities': 'Basic quantum sensing, limited coverage',
            },
            'phase_2': {
                'timeline': 'Year 3-4',
                'objective': 'Initial operational capability',
                'satellites': '6-8 satellites',
                'launch_vehicles': ['Falcon 9', 'Ariane 6'],
                'cost': '$400-500M',
                'orbit': 'Mixed inclination LEO',
                'capabilities': 'Regional coverage, 2-hour revisit',
            },
            'phase_3': {
                'timeline': 'Year 5-7',
                'objective': 'Full operational capability',
                'satellites': '24-30 satellites',
                'launch_vehicles': ['Falcon Heavy', 'New Glenn', 'Vulcan'],
                'cost': '$1.2-1.5B',
                'orbit': 'Complete constellation with MEO/GEO',
                'capabilities': 'Global coverage, <30 minute revisit',
            },
            'phase_4': {
                'timeline': 'Year 8+',
                'objective': 'Enhanced capability',
                'satellites': 'Replacement and augmentation',
                'launch_vehicles': ['Fully reusable systems'],
                'cost': '$200-300M/year',
                'orbit': 'Optimized constellation',
                'capabilities': 'Continuous tracking, quantum networking',
            }
        }
    
    def calculate_launch_requirements(self, constellation_size=24):
        """Calculate launch manifest"""
        
        # Assuming 500 kg satellites
        satellite_mass = 500  # kg
        
        # Launch vehicle capabilities
        launch_vehicles = {
            'falcon_9': {
                'leo_capacity': 22800,  # kg to LEO
                'cost': '$67M',
                'max_satellites_per_launch': 45,  # Based on volume
            },
            'electron': {
                'leo_capacity': 300,    # kg to LEO
                'cost': '$7.5M',
                'max_satellites_per_launch': 1,
            },
            'falcon_heavy': {
                'leo_capacity': 63800,  # kg to LEO
                'cost': '$150M',
                'max_satellites_per_launch': 100,
            }
        }
        
        # Optimize launch manifest
        manifest = []
        remaining = constellation_size
        
        # Use Falcon Heavy for bulk launches
        while remaining > 0:
            if remaining >= 8:
                # Use Falcon Heavy
                manifest.append({
                    'vehicle': 'Falcon Heavy',
                    'satellites': min(8, remaining),
                    'cost': launch_vehicles['falcon_heavy']['cost'],
                })
                remaining -= 8
            else:
                # Use Falcon 9
                manifest.append({
                    'vehicle': 'Falcon 9',
                    'satellites': remaining,
                    'cost': launch_vehicles['falcon_9']['cost'],
                })
                remaining = 0
        
        total_cost = sum([m['cost'] for m in manifest])
        
        return {
            'total_satellites': constellation_size,
            'launch_manifest': manifest,
            'total_launches': len(manifest),
            'estimated_cost': f'${total_cost}M',
            'timeline': f'{len(manifest)*3} months (assuming 3 months between launches)',
        }
