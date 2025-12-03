class SpaceBasedAdvantages:
    """Unique advantages of space-based quantum sensing"""
    
    ADVANTAGES = {
        'altitude': {
            'leo': '300-2000 km altitude',
            'coverage': '~1000 km diameter field of view',
            'persistence': 'Continuous monitoring capability',
        },
        'atmosphere': {
            'no_atmospheric_loss': 'No absorption/scattering',
            'no_turbulence': 'Perfect beam propagation',
            'clear_line_of_sight': 'No obstructions',
        },
        'physics': {
            'longer_coherence': 'Lower decoherence in vacuum',
            'stable_temperature': '4K background temperature',
            'no_vibration': 'Microgravity environment',
        },
        'strategic': {
            'global_coverage': 'Multiple orbits provide global access',
            'difficult_to_counter': 'Space assets hard to attack',
            'strategic_high_ground': 'Dominates terrestrial systems',
        }
    }
    
    def calculate_space_advantages(self, terrestrial_performance):
        """Quantify improvements in space"""
        
        improvements = {
            'range_improvement': {
                'factor': 5,  # 5x range improvement in space
                'reason': 'No atmospheric attenuation',
            },
            'sensitivity_improvement': {
                'factor': 10,  # 10x better sensitivity
                'reason': 'Lower noise, better thermal environment',
            },
            'coherence_time': {
                'factor': 100,  # 100x longer coherence
                'reason': 'Vacuum reduces decoherence',
            },
            'detection_probability': {
                'improvement': '+0.2',  # 20% better P_d
                'reason': 'Clear line of sight',
            }
        }
        
        return improvements
