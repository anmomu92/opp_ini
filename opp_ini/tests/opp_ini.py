##############
# Imports
##############

import os
import glob
import shutil

# Data structures
from enum import Enum

# Appearance
from pprint import pprint

#############
# Constant
#############
SAURON_ROOT = os.environ["SAURON_ROOT"]

#############
# Classes 
#############

# Base classes
class Simulation:
    """
    This class represents a simulation
    It contains methods to write and read simulations
    """
    
    def __init__(self):
        self.root_dir = ""
        self.config = ""

    ###########
    # Setters 
    ###########
    def set_root_dir(self, topology_name):
        self.root_dir = SAURON_ROOT + "/simulations/" + topology_name

    def set_config(self, *args):
        for i in range(len(args)):
            self.config = self.config + args[i]

    ###########
    # Getters 
    ###########
    def get_root_dir(self):
        return self.root_dir
    
    def get_config(self):
        return self.config


class Topology:
    """
    This class represents a generic topology
    It has attributes and methods common to every topology
    It is the base class of other more specific classes
    Current derived classes that have been implemented:
        - RLFT
        - Torus
            - Torus2D
    """

    def __init__(self):
        self.name = "rlft"
        self.network = "RLFT"
        self.channel_distance = 5
        self.nodes = 0

    ###########
    # Setters 
    ###########
    def set_channel_distance(self, distance):
        self.channel_distance = distance

    ###########
    # Getters
    ###########
    def get_name(self):
        return self.name
    
    def get_channel_distance(self):
        return self.channel_distance
    
    def get_network(self):
        return self.network


    def get_nodes(self):
        return self.nodes

class Switch:
    """
    This class represents a generic switch
    It has attributes and methods common to every topology
    It is the base class of other more specific classes
    """
    ####################
    # Class attributes
    ####################
    
    def __init__(self):
        pass
        self.architecture = "IB-NDR"
        self.arbiter = "Arbiter_ThreePhased"
        self.voq = "false"
        self.routing = "xy"
        self.bubble = True
        self.request_processing_time = 6  # in nanoseconds

    ###########
    # Setters
    ###########
    def set_architecture(self, architecture):
        self.architecture= architecture
        
    def set_arbiter(self, arbiter):
        self.arbiter = arbiter

    def set_voq(self, voq):
        self.voq = voq
        
    def set_routing(self, routing):
        self.routing= routing

    def set_bubble(self, bubble):
        self.bubble = bubble
        
    def set_request_processing_time(self, request_processing_time):
        self.request_processing_time= request_processing_time


    ###########
    # Getters
    ###########
    def get_name(self):
        return self.name
   
    def get_arbiter(self):
        return self.arbiter

    def get_voq(self):
        return self.voq
    
    def get_routing(self):
        return self.routing
    
    def get_bubble(self):
        return self.bubble
    
    def get_request_processing_time(self):
        return self.request_processing_time

class Application:
    """
    This class represents a generic application 
    It has attributes and methods common to every application 
    It is the base class of other more specific applications 
    """
    ####################
    # Class attributes
    ####################
    name = "Application"
    message_size = 0 
    initial_load = 0
    final_load = 0
    steps = 0
    file_name = "R"
    
    def __init__(self):
        pass

    ###########
    # Setters
    ###########
    def set_message_size(self, msg_size):
        self.message_size = msg_size 

    def set_load(self, initial=0, final=100, steps=0):
        self.initial_load = initial
        self.final_load = final
        self.steps = steps
 
    def set_filename(self, filename):
        self.file_name = filename

    ###########
    # Getters
    ###########
    def get_name(self):
        return self.name
   
    def get_msg_size(self):
        return self.message_size

    def get_initial_load(self):
        return self.initial_load

    def get_final_load(self):
        return self.final_load
    
    def get_steps(self):
        return self.steps

    def get_filename(self):
        return self.filename

# Derived classes from topology

class RLFT(Topology):
    """
    This is a class representing a Real Life Fat Tree topology

    :param Topology: the parent class topology
    """
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.name = "rlft"
        self.network = "RLFT"
        self.arity = 2
        self.stages = 2

    def set_nodes(self, arity, stages):
        self.arity = arity
        self.stages = stages
        self.nodes = 2*(pow(arity, stages))

    def get_arity(self):
        return self.arity

    def get_stages(self):
        return self.stages
    
    def get_nodes(self):
        return self.nodes

class Torus(Topology):
    """
    This is a class representing a Torus of generic dimension

    :param Topology: the parent class topology
    """
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.name = "torus"
        self.dimensions = 2

    def get_dimensions(self):
        return self.dimensions

class Torus2D(Torus):
    """
    This is a class representing a Torus of two dimensions 

    :param Topology: the parent class topology
    """
    
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.network = "Torus2D"
        self.dim0 = 2
        self.dim1 = 2

    def set_nodes(self, dim0, dim1):
        self.dim0 = dim0
        self.dim1 = dim1
        self.nodes = (dim0*dim1)


# Derived classes from switch
class IB_NDR(Switch):
    """
    This is a class representing the IB_NDR switch architecture 

    :param Switch: the parent switch class
    """
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.name = "ib_ndr"

class BXI3(Switch):
    """
    This is a class representing the BXI3 switch architecture 

    :param Switch: the parent switch class
    """
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.name = "bxi3"

# Derived classes from Application
class Synthetic(Application):
    """
    This class represents a synthetic application 
    It has attributes and methods common to every synthetic application 
    It is derived from a generic application
    It is the base class of other more specific synthetic applications 
    
    :param Application: the parent application class
    """

    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.name = "SyntheticApplication"


########
# Enum
########
class Topologies(Enum):
    DragonflyAbsolute = 1
    DragonflyCircular = 2
    DragonflyHammingGraph = 3
    DragonflyPalmTree = 4
    FatXaryXtree = 5
    Hypercube = 6
    KNSXary2direct1indirect = 7
    KNSXary2directXindirect = 8
    KNSXary3direct1indirect = 9
    Megafly_topgen = 10
    Mesh2D = 11
    Mesh3D = 12
    Mesh4D = 13
    NHosts1Switch = 14
    NHosts2Switches = 15
    PGFT = 16
    PGFT_Cell = 17
    RLFT = 18
    RLFT_tables = 19
    ShuffleXstageXexchange = 20
    SlimFly = 21
    Torus2D = 22
    Torus3D = 23
    Torus3D_Energy = 24

class SwArchs(Enum):
    # Input Queue (IQ)
    IB_QDR = 1
    IB_DDR = 2
    IB_EDR = 3
    IB_NDR = 4
    # Combined Input-Output Queue (CIOQ)
    PORT_PFC = 5
    BXI3 = 6 
    BXI3_JESUS = 7 

class Applications(Enum):
    S = 1           # Synthetic

##########
# Methods
##########

def list_topologies(topologies):
    for topology in Topologies:
        topologies.append(topology.name)

def list_switch_architectures(sw_archs):
    for sw_arch in SwArchs:
        sw_archs.append(sw_arch.name)

def list_applications(apps):
    for app in Applications:
        apps.append(app.name)

#def write_topology(topology):

def check_configuration(simulation, config_name="[Config"):
    """
    It checks if there is a configuration defined in the omnetpp.ini file
    
    :param simulation: the simulation folder to be checked
    :param config_name: the name of the configuration to be checked. The default value checks if there is any configuration
    :returns: True if the configuration was found. Prints "Not Found" otherwise
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    
    # Open the file and search for the target line
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                return True 
        else:
            print("Not Found") 

def get_configurations(simulation):
    """
    It retrieves all the configurations within the omnetpp.ini file
    
    :param simulation: the simulation folder to be checked
    :returns: A list of the configurations located in the omnetpp.ini file. Prints "Nothing Found" if no configurations where found
    """
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    config_name = "[Config"
    configs = []
    
    # Open the file and search for the target line
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                configs.append(line[8:line.index("]")])
        else:
            print("Nothing Found") 

    return configs

def get_switch_architecture(simulation):
    """
    It retrieves the current switch architecture in use
    
    :param simulation: the simulation folder to be checked
    :returns: a string with the current switch architecture being used
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    config_name="[Config portConfig]"
    
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                next_line = next(file, None)
                if next_line:
                    next_line = next_line.strip()
                    # Check if the line starts with "extends="
                    if next_line.startswith("extends="):
                        return next_line.split("=", 1)[1]  # Return everything after "extends="
                return None
        
def get_switch_routing(simulation):
    """
    It retrieves the current switch routing algorithm in use
    
    :param simulation: the simulation folder to be checked
    :returns: a string with the current switch routing algorithm being used
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    config_name="**.routingAlgorithm"
    
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                line = line.strip().replace(" ", "")
                return line.split("=", 1)[1]
            
def get_switch_arbiter(simulation):
    """
    It retrieves the current switch arbiter in use
    
    :param simulation: the simulation folder to be checked
    :returns: a string with the current switch arbiter being used
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    config_name="**.SW[*].arbiter.typename"
    
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                line = line.strip().replace(" ", "")
                return line.split("=", 1)[1]
            
def get_switch_request_processing_time(simulation):
    """
    It retrieves the current switch request processing time in use
    
    :param simulation: the simulation folder to be checked
    :returns: a string with the current switch request processing time
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    config_name="**.requestProcessingTime"
    
    with open(opp_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                line = line.strip().replace(" ", "")
                return line.split("=", 1)[1]
            
def set_default_configuration(simulation, topology):
    """
    It writes a default omnetpp.ini file
    
    :param simulation: the simulation folder where to write the file
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini" 
    backup_path = f"{opp_file}.bak"
    topology_name = topology.get_name()
    network_name = topology.get_network()
    channel_distance = topology.get_channel_distance()

    lines = [
            "[General]\n",
            f"network = {network_name}\n",
            "\n",
            "#warmup-period=0.00025s\n",
            "\n",
            "cmdenv-status-frequency = 5s\n",
            "sim-time-limit = 0.002000001s\n",
            "cmdenv-interactive=true\n",
            "#Net\n",
            f"**.topology = \"topology_name\"\n",
            "#**.arity = ${arity=2}\n",
            "#**.numStages = ${numStages=3}\n",
            "#**.numNodes = ${numNodes = int(2*pow(${arity},${numStages}))}\n",
            f"**.channelDistance = {channel_distance}m\n",
            "\n",
            "#Routing and Arbitration\n",
            "**.routingAlgorithm = \"destro\"\n",
            "**.H[*].arbiter.typename = \"Arbiter_TwoPhased\"\n",
            "#**.SW[*].arbiter.typename = \"Arbiter_TwoPhased\"\n",
            "**.requestProcessingTime = 6ns",
            "\n",
            "\n",
            "#Logging\n",
            "**.logInterval = 10us\n",
            "\n",
            "**.sysMng.**.result-recording-modes = default, +vector,+histogram\n",
            "**.sys.app*-**.result-recording-modes = default, +vector,+histogram\n",
            "\n",
            "# Stats to record per node - we have to indicate the stat that we want to recollect\n",
            "#**.H[127].throughput.\n",
            "**.H[*].**.scalar-recording = false\n",
            "**.SW[*].**.scalar-recording = false\n",
            "**.param-recording = false\n",
            "\n",
            "#Port Configurations\n",
            "include ../TrafficConfigurations/PortPFC.ini\n",
            "include ../TrafficConfigurations/originalPort.ini\n",
            "\n",
            "\n",
            "# Port configuration for IQ switch\n",
            "[Config portConfig] #Note that the config included extends from General and portConfig, change the next extend to test other technologies\n",
            "#extends=IB-NDR  # IQ\n",
            "extends=bxi3	# CIOQ\n",
            "\n",
            "#Queuing schemes configurations\n",
            "include ../TrafficConfigurations/indirect/schemes.ini\n",
            "\n",
            "#Traffic generation modes\n",
            "include ../TrafficConfigurations/indirect/random.ini\n",
            "include ../TrafficConfigurations/indirect/hotspot.ini\n",
            "include ../TrafficConfigurations/indirect/victim.ini\n",
            "include ../TrafficConfigurations/indirect/local.ini\n",
            "include ../TrafficConfigurations/indirect/storage.ini\n",
            "include ../TrafficConfigurations/indirect/ebb.ini\n",
            "include ../TrafficConfigurations/indirect/ebb_hs.ini\n",
            "include ../TrafficConfigurations/indirect/zipf1.ini\n",
            "include ../TrafficConfigurations/indirect/sla3.ini\n",
            "include ../TrafficConfigurations/indirect/ptrans.ini\n",
            "include ../TrafficConfigurations/indirect/natRing.ini\n",
            "include ../TrafficConfigurations/indirect/graph500.ini\n",
            "\n"
            ]
    
    
    # Check if the file exists
    if os.path.exists(opp_file):
        # Create a backup
        shutil.copy(opp_file, backup_path)
        print(f"Backup created: {backup_path}")
    
    # Write the default file
    with open(opp_file, "w") as file:
        #print(lines, file=file)
        file.writelines(lines)
        
    print(f"File {opp_file} written successfully")
    
def add_new_configuration(simulation, topology, switch, applicacion):
    """
    It adds a new configuration in the omnetpp.ini file
    
    :param simulation: the simulation folder where the omnetpp.ini file is located
    """
    
    opp_file = simulation.get_root_dir() + "/omnetpp.ini"
    config_name = simulation.get_config()
    
    # Topology parameters
    arity = str(topology.get_arity())
    stages = str(topology.get_stages())
    nodes = str(topology.get_nodes())
    
    # Switch parameters
    voq = switch.get_voq()
    arbiter = switch.get_arbiter()
    
    lines = [
            f"[Config {config_name}]\n",
            "extends=portConfig\n",
            "\n",
            "# Network\n"
            ]
    
    match topology.get_network():
        case "RLFT":
            lines.append("**.arity = ${arity=", f"{arity}", "}\n")
            lines.append("**.numStages = ${numStages={stages}}\n")
            lines.append("**.numNodes = int(2*pow(${{arity}},${{numStages}}))\n")
            lines.append("\n")
        case "Torus2D":
            lines.append("**.nD0 = ${nD0=2}\n")
            lines.append("**.nD1 = ${nD1=2}\n")
            lines.append("**.nodesInEachDim = ${nD0} ${nD1}\n")
            lines.append("**.numNodes = ${numNodes=${nD0}*${nD1}}\n")
            lines.append("\n")
            
            
    lines.append("# Switch\n")
    lines.append("#**.SW[*].virtualOutputQueues = {voq}\n")
    lines.append("**.SW[*].arbiter.typename = \"{arbiter}\"\n")
    lines.append("\n")
    lines.append("# Applications\n")
    lines.append("# These are defined in the configuration file of the specific traffic configuration\n")
    lines.append("**.firstLog = 0.00000s\n")
    lines.append("\n")
    lines.append("**.numApps = 2\n")
    lines.append("**.app[*].typename = \"SyntheticApplication\"\n")
    lines.append("**.app[*].msgSize = ${header}B+${data}B\n")
    lines.append("**.app[*].load = ${load=10..100 step 10}\n")
    lines.append("**.app[0].fileName = \"../TrafficConfigurations/files/synthetic/traffic_8_75_1_2_hotspot.in\"\n")
    lines.append("**.app[1].fileName = \"../TrafficConfigurations/files/synthetic/traffic_8_75_1_2_victim.in\"\n")
    lines.append("#**.app[0].msgForStats = 10000\n")
    lines.append("\n")
    lines.append("# Queueing scheme\n")
    lines.append("**.congestionControlTechnique = \"1q\"\n")
    lines.append("**.numQueues = 1\n")
    lines.append("\n")
    
    
    # Append new configuration
    with open(opp_file, "a") as file:
        file.writelines(lines)
