# metrics/dashboard.py
class QuantumShieldMetrics:
    """Track and visualize system performance metrics"""
    
    metrics = {
        'quantum_advantage_ratio': [],
        'detection_latency': [],
        'false_alarm_rate': [],
        'system_uptime': [],
        'quantum_state_fidelity': [],
        'entanglement_rate': []
    }
    
    def record_metric(self, metric_name, value):
        """Record performance metric"""
        if metric_name in self.metrics:
            self.metrics[metric_name].append({
                'timestamp': time.time(),
                'value': value
            })
    
    def generate_performance_report(self):
        """Generate performance analysis report"""
        report = {}
        for metric, values in self.metrics.items():
            if values:
                recent = values[-100:]  # Last 100 measurements
                report[metric] = {
                    'current': recent[-1]['value'],
                    'average': np.mean([v['value'] for v in recent]),
                    'trend': self._calculate_trend(recent)
                }
        return report
