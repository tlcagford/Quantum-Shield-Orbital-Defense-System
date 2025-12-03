# Clone and set up test environment
git clone https://github.com/tlcagford/Quantum-Shield
cd Quantum-Shield/loop_test

# Install dependencies
pip install -r requirements.txt

# Set up hardware
python setup_hardware.py --mode basic

# Run initial loop test
python basic_loop_test.py --iterations 100

# Generate report
python generate_report.py --output basic_test_report.pdf
