import os
import sys

import opp_ini as oi

# Get the parent directory (A)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

simulation = oi.Simulation()
simulation.set_root_dir("RLFT")

configuration = ""

print("Root directory of the current simulation is ", simulation.get_root_dir())

if oi.check_configuration(simulation):
    configuration = oi.get_configuration(simulation)

print(f"Configuration {configuration} retrieved\n")
