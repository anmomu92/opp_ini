import os
import sys

import opp_ini as oi

# Get the parent directory (A)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

simulation = oi.Simulation()
simulation.set_root_dir("RLFT")

simulation.set_topo(oi.RLFT())
simulation.topology.set_nodes(2, 2)

simulation.set_sw(oi.IB_NDR())
simulation.switch.set_arbiter("WRR")
simulation.switch.set_queue_scheme("1q")
simulation.switch.set_num_queues("1")

simulation.set_app(oi.Application())

configuration = oi.set_configuration_name(simulation)

print("Root directory of the current simulation is ", simulation.get_root_dir())

print(f"Configuration {configuration} created\n")
