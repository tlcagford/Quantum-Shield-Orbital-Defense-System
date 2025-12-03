# testing/field_test_protocol.py
class FieldTestProtocol:
    """Protocol for field testing quantum sensing system"""
    
    def __init__(self, test_site):
        self.test_site = test_site  # e.g., 'open_field', 'wooded_area'
        self.targets = self.define_test_targets()
        
    def define_test_targets(self):
        """Define standard test targets"""
        return [
            {
                'name': 'small_drone',
                'size': '30cm',
                'material': 'carbon_fiber',
                'magnetic_signature': 'weak',
                'speed_range': [1, 10]  # m/s
            },
            {
                'name': 'ground_vehicle',
                'size': '2m',
                'material': 'metal',
                'magnetic_signature': 'strong',
                'speed_range': [0.5, 5]  # m/s
            },
            {
                'name': 'person',
                'size': 'human',
                'material': 'organic',
                'magnetic_signature': 'very_weak',
                'speed_range': [0.5, 3]  # m/s
            }
        ]
    
    def run_field_test(self, target_type, conditions):
        """Execute field test with specified target"""
        
        # Set up quantum sensor array
        sensor_array = QuantumSensorArray()
        
        # Deploy target
        target = self.deploy_target(target_type)
        
        # Run detection sequence
        detection_log = []
        
        for distance in [100, 50, 25, 10]:  # meters
            print(f"Testing at {distance}m distance")
            
            # Move target to test distance
            target.position = distance
            
            # Run detection
            result = sensor_array.detect_target(
                target=target,
                integration_time=10,  # seconds
                conditions=conditions
            )
            
            detection_log.append({
                'distance': distance,
                'detection': result['detected'],
                'confidence': result['confidence'],
                'false_alarm': result['false_alarms']
            })
        
        # Calculate performance metrics
        performance = self.calculate_performance(detection_log)
        
        return {
            'target': target_type,
            'conditions': conditions,
            'detection_log': detection_log,
            'performance_metrics': performance
        }
