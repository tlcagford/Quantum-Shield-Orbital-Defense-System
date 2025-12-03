# loop_test/troubleshooting.py
class LoopTestTroubleshooter:
    """Automated troubleshooting for loop test failures"""
    
    COMMON_ISSUES = {
        'no_detection': [
            'Check laser alignment',
            'Verify microwave frequency',
            'Confirm magnetic field generation',
            'Check photodetector connection',
            'Verify data acquisition settings'
        ],
        'high_false_alarms': [
            'Increase detection threshold',
            'Improve magnetic shielding',
            'Add signal averaging',
            'Implement adaptive thresholding',
            'Check for environmental interference'
        ],
        'slow_response': [
            'Optimize processing algorithm',
            'Reduce integration time',
            'Use parallel processing',
            'Implement predictive algorithms',
            'Upgrade hardware (FPGA/GPU)'
        ],
        'system_instability': [
            'Check power supply stability',
            'Monitor temperature',
            'Verify grounding',
            'Check for mechanical vibrations',
            'Update firmware/drivers'
        ]
    }
    
    def diagnose_issue(self, test_results):
        """Automatically diagnose issues from test results"""
        
        issues = []
        
        # Check detection performance
        if self.calculate_pd(test_results) < 0.5:
            issues.append(('no_detection', 'Low detection probability'))
        
        # Check false alarm rate
        if self.calculate_far(test_results) > 0.05:
            issues.append(('high_false_alarms', 'High false alarm rate'))
        
        # Check response time
        avg_response = self.calculate_avg_response_time(test_results)
        if avg_response > 1.0:  # >1 second
            issues.append(('slow_response', f'Slow response: {avg_response:.2f}s'))
        
        # Check system stability
        if self.check_stability_issues(test_results):
            issues.append(('system_instability', 'System stability issues'))
        
        # Generate troubleshooting steps
        recommendations = []
        for issue_code, description in issues:
            recommendations.append({
                'issue': description,
                'possible_causes': self.COMMON_ISSUES.get(issue_code, []),
                'diagnostic_steps': self.generate_diagnostic_steps(issue_code),
                'corrective_actions': self.generate_corrective_actions(issue_code)
            })
        
        return recommendations
