# Quick drop-in usage for your projects:

# 1. Import the comparison class
from quantum_shield_comparison import QuantumShieldComparison

# 2. Instantiate the comparison
qs = QuantumShieldComparison()

# 3. Get any comparison table
print(qs.comparison_data['space_missile_defense'].to_string())

# 4. Or generate complete dashboard
create_comparison_dashboard()

# 5. Or embed in reports
html = generate_single_page_comparison()
