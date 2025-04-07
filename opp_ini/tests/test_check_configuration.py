import opp_ini as oi

topo = oi.Topology()
sw = oi.Switch()
app = oi.Application()

simulation = oi.Simulation(topo, sw, app)
simulation.set_root_dir("RLFT")

print("Root directory of the current simulation is ", simulation.get_root_dir())

if(oi.check_configuration(simulation)):
    print("PASSED. A configuration was found.")
