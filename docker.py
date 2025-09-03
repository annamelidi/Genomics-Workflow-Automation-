"""
Simple script to run all steps in order.
"""

import os

scripts = ["data_loading_exploration.py", "preproces.py", "visuals.py"]

for script in scripts:
    print(f"\nRunning {script}...")
    os.system(f"python scripts/{script}")
