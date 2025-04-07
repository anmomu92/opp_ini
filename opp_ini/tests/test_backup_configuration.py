import opp_ini as oi

simulation = oi.Simulation()
simulation.set_root_dir("RLFT")

print("Root directory of the current simulation is ", simulation.get_root_dir())

try:
    oi.backup_configuration(simulation)
    print("Configuration successfuly backed up")
except FileExistsError as FE:
    print(FE)
