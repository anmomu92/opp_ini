import opp_ini as oi

topo = oi.RLFT(oi.Topology())
topo.set_nodes(3,3)

sw = oi.Switch()
app = oi.Application()

simulation = oi.Simulation()
simulation.set_root_dir("RLFT")
simulation.set_config("ConfiguracionPrueba")

print("Root directory of the current simulation is ", simulation.get_root_dir())

oi.add_new_configuration(simulation, topo, sw, app)
