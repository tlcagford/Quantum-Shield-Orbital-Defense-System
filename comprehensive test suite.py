# tests/test_quantum_shield.py
import pytest
from core.quantum_radar_sim import QuantumRadarSimulator

class TestQuantumShield:
    
    def test_quantum_advantage(self):
        """Verify quantum illumination provides advantage"""
        simulator = QuantumRadarSimulator()
        classical_detection = simulator.classical_detection_rate()
        quantum_detection = simulator.quantum_detection_rate()
        
        assert quantum_detection > classical_detection, \
            "Quantum advantage not achieved"
    
    def test_decoherence_compensation(self):
        """Test decoherence mitigation effectiveness"""
        simulator = QuantumRadarSimulator()
        uncompensated = simulator.run_with_decoherence(mitigation=False)
        compensated = simulator.run_with_decoherence(mitigation=True)
        
        assert compensated.fidelity > uncompensated.fidelity * 1.5, \
            "Decoherence compensation ineffective"
