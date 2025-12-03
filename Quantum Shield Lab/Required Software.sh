# Core quantum control software
git clone https://github.com/qutech/qlib
git clone https://github.com/PrincetonUniversity/PrincetonInstruments
git clone https://github.com/lukin-group/qdmpy

# Install Python environment
conda create -n quantum-shield python=3.9
conda activate quantum-shield

# Install dependencies
pip install numpy scipy matplotlib qutip
pip install pyvisa pyqt5 pyserial
pip install qiskit pennylane

# Install instrument control
pip install python-ivi python-usbtmc
