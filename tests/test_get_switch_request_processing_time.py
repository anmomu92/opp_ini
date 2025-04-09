import opp_ini as oi

topo = oi.Topology()
sw = oi.Switch()
app = oi.Application()

simulation = oi.Simulation()
simulation.set_root_dir("RLFT")


print("Root directory of the current simulation is ", simulation.get_root_dir())

switch = oi.get_switch_request_processing_time(simulation)

print(switch)

