# metrics/performance_tracking.py
class QuantumShieldMetrics:
    """Track and report system performance metrics"""
    
    KPIs = {
        'detection_range': {
            'target': '>100m for 30cm drone',
            'current': '0m',
            'unit': 'meters'
        },
        'probability_of_detection': {
            'target': '>0.95 at 50m',
            'current': '0.0',
            'unit': 'probability'
        },
        'false_alarm_rate': {
            'target': '<0.01 per hour',
            'current': 'N/A',
            'unit': 'events/hour'
        },
        'quantum_advantage': {
            'target': '>3dB improvement',
            'current': '0dB',
            'unit': 'dB'
        },
        'system_availability': {
            'target': '>0.99',
            'current': '0.0',
            'unit': 'probability'
        },
        'mean_time_between_failure': {
            'target': '>1000 hours',
            'current': 'N/A',
            'unit': 'hours'
        }
    }
    
    def measure_all_kpis(self, test_duration=168):  # 1 week test
        """Measure all KPIs over extended test period"""
        
        results = {}
        
        for kpi_name, kpi_spec in self.KPIs.items():
            measurement = self.measure_kpi(kpi_name, test_duration)
            
            results[kpi_name] = {
                'measured': measurement,
                'target': kpi_spec['target'],
                'status': self.evaluate_status(measurement, kpi_spec['target'])
            }
        
        return results
