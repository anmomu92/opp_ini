"""opp_ini - Tools for managing the OMNet++ configuration configuration file."""

__version__ = "0.1.0"

import os
import shutil

# Data structures
from enum import Enum

# Appearance
# from pprint import pprint

# ----- Constants ----- #
# SAURON_ROOT = os.environ["SAURON_ROOT"]

try:
    SAURON_ROOT = os.environ["SAURON_ROOT"]
except KeyError:
    SAURON_ROOT = None
    if __name__ == "__main__":
        raise RuntimeError("SAURON_ROOT is required to run this program.")


# ----- Classes ----- #


# Base


class Simulation:
    """A class representing a simulation.

    This class provides functionality to add/remove configuration parameters in the omnetpp.ini file.
    It holds instances of interconnection network elements (topology, switch, application).

    Attributes:
        root_dir (str): Path to the root of the simulation within the SAURON file system.
        topology (Topology): Topology to be simulated.
        switch (Switch): Switch to be simulated.
        app (Application): Application to be simulated.
    """

    def __init__(self):
        """Initializes the Simulation with default values."""
        self.root_dir = ""
        self.topology = Topology()
        self.switch = Switch()
        self.app = Application()

    def __del__(self):
        """Deletes the simulation."""
        print(
            f"Simulation with root directory {self.root_dir} is being destroyed"
        )

    # ----- Setters ----- #

    def set_root_dir(self, topology_name: str):
        """
        Sets the root directory of the simulation.

        Args:
            topology_name (str): The name of the topology to be simulated.
        """
        self.root_dir = SAURON_ROOT + "/simulations/" + topology_name

    def set_topo(self, topo: "Topology"):
        """
        Sets the topology.

        Args:
            topo (Topology): The object containing topology parameters.
        """
        self.topology = topo

    def set_sw(self, sw: "Switch"):
        """
        Sets the switch.

        Args:
            sw (Switch): The object containing switch parameters.
        """
        self.switch = sw

    def set_app(self, app: "Application"):
        """
        Sets the application.

        Args:
            app (Application): The object containing application parameters.
        """
        self.app = app

    ###########
    # Getters
    ###########
    def get_root_dir(self) -> str:
        """
        Gets the root directory of the simulation.

        Returns:
            str: The name of the root directory of the simulation.
        """
        return self.root_dir


class Topology:
    """A class representing a topology in a simulation.

    This class provides functionality to add/remove topology parameters.

    Attributes:
        name (str): Name of the topology.
        network (str): Name of the simulation folder the omnetpp_ini file is located.
        channel_distance (int): Distance of the channels in the topology.
        nodes (int): The number of nodes that the topology contains.
    """

    def __init__(self):
        """Initializes the topology with default values."""
        self.name = "rlft"
        self.network = "RLFT"
        self.channel_distance = 5
        self.nodes = 0

    def __del__(self):
        """Deletes the topology"""
        print(f"Topology with name {self.name} is being destroyed")

    ###########
    # Setters
    ###########
    def set_channel_distance(self, distance: int):
        """
        Sets the distance of the channels.

        Args:
            distance (int): The distance in meters.
        """
        self.channel_distance = distance

    ###########
    # Getters
    ###########
    def get_name(self) -> str:
        """
        Gets the name of the topology.

        Returns:
            str: The name of the topology.
        """
        return self.name

    def get_channel_distance(self) -> int:
        """
        Gets the distance of the channels.

        Returns:
            int: The distance of the channels.
        """
        return self.channel_distance

    def get_network(self) -> str:
        """
        Gets the name of the network.

        Returns:
            str: The name of the network.
        """
        return self.network

    def get_nodes(self) -> int:
        """
        Gets the number of nodes.

        Returns:
            int: The number of nodes.
        """
        return self.nodes


class Switch:
    """A class representing a switch in a simulation.

    This class provides functionality to add/remove switch parameters.

    Attributes:
        architecture (str): Architecture of the switch.
        arbiter (str): Arbiter used by the switch.
        voq (bool): Whether the switch uses VOQs or not.
        queue_scheme (str): Queue scheme used in the switch.
        bubble (bool): Whether the switch uses bubble or not.
        request_processing_time (int): Time it takes the switch to process requests.
    """

    # Class attributes
    def __init__(self):
        """Initializes the switch with default values."""
        self.architecture = "IB_DDR"
        self.arbiter = "Arbiter_TwoPhased"
        self.voq = False
        self.queue_scheme = "1q"
        self.num_queues = 1
        self.routing = "xy"
        self.bubble = False
        self.request_processing_time = 6  # in nanoseconds

    def __del__(self):
        """Deletes the switch"""
        print(
            f"Switch with architecture {self.architecture} is being destroyed"
        )

    # ----- Setters ----- #

    def set_architecture(self, architecture: str):
        """
        Sets the architecture of the switch.

        Args:
            architecture (str): Architecture of the switch
        """
        self.architecture = architecture

    def set_arbiter(self, arbiter: str):
        """
        Sets the arbiter of the switch.

        Args:
            architecture (str): Architecture of the switch.
        """
        self.arbiter = arbiter

    def set_voq(self, voq: bool):
        """
        Sets if VOQs are active.

        Args:
            voq (bool): True if active, False if inactive.
        """
        self.voq = voq

    def set_queue_scheme(self, queue_scheme: str):
        """
        Sets queueing scheme.

        Args:
            queue_scheme (str): Queue scheme.
        """
        self.queue_scheme = queue_scheme

    def set_num_queues(self, num_queues: int):
        """
        Sets the number of queues of the queueing scheme.

        Args:
            num_queues (str): Number of queues.
        """
        self.num_queues = num_queues

    def set_routing(self, routing: str):
        """
        Sets the routing algorithm of the switch.

        Args:
            routing (str): Routing algorithm.
        """
        self.routing = routing

    def set_bubble(self, bubble: bool):
        """
        Sets the bubbles.

        Args:
            bubble (bool): True if active, False if inactive.
        """
        self.bubble = bubble

    def set_request_processing_time(self, request_processing_time: int):
        """
        Sets the request processing time.

        Args:
            request_processing_time (int): Time it takes the switch to process each request.
        """
        self.request_processing_time = request_processing_time

    # ----- Getters ----- #

    def get_architecture(self) -> str:
        """
        Gets the name of the switch architecture.

        Returns:
            str: Name of the switch architecture.
        """
        return self.architecture

    def get_arbiter(self) -> str:
        """
        Gets the name of the switch arbiter.

        Returns:
            str: Name of the switch arbiter.
        """
        return self.arbiter

    def get_voq(self) -> bool:
        """
        Checks if VOQs are active.

        Returns:
            bool: True if active, False if inactive.
        """
        return self.voq

    def get_queue_scheme(self) -> str:
        """
        Gets the queue scheme.

        Returns:
            str: Name of the switch queue scheme.
        """
        return self.queue_scheme

    def get_num_queues(self) -> int:
        """
        Gets the number of queues used by the queue scheme.

        Returns:
            int: Number of queues in the queue scheme.
        """
        return self.num_queues

    def get_routing(self) -> str:
        """
        Gets the name of the routing algorithm used by the switch.

        Returns:
            str: Name of the switch routing algorithm.
        """
        return self.routing

    def get_bubble(self) -> bool:
        """
        Checks if bubble is active.

        Returns:
            bool: True if active, False if inactive.
        """
        return self.bubble

    def get_request_processing_time(self) -> int:
        """
        Gets the request processing time of the switch.

        Returns:
            int: Time it takes the switch to process a request.
        """
        return self.request_processing_time


class Application:
    """A class representing an application in a simulation.

    This class provides functionality to add/remove application parameters.

    Attributes:
        name (str): Name of the application.
        message_size (int): Size of the message.
        initial_load (int): Initial load of the simulation, if steps is greater than one.
        final_load (int): Final load of he simulation, if steps is greater than one.
        steps (int): Number of steps performed during the simulations, with increasing load.
        file_name (str): Type of application.
    """

    def __init__(self):
        """Initializes the application with default values."""
        self.name = "Application"
        self.message_size = 0
        self.initial_load = 0
        self.final_load = 0
        self.steps = 0
        self.file_name = "R"

    def __del__(self):
        "Deletes the application."
        print(f"Application with name {self.name} is being destroyed")

    # ----- Setters ----- #

    def set_message_size(self, msg_size: int):
        """
        Sets the size of the messages sent by the application.

        Args:
            msg_size (int): Size of the message.
        """
        self.message_size = msg_size

    def set_load(self, initial=0, final=100, steps=0):
        """
        Sets the loads of the application.

        Args:
            initial (int): Initial load.
            final (int): Final load.
            steps (int): Number of steps.
        """
        self.initial_load = initial
        self.final_load = final
        self.steps = steps

    def set_filename(self, filename: str):
        """
        Sets the type of application.

        Args:
            filename (str): Type of application.
        """
        self.file_name = filename

    # ----- Getters ----- #

    def get_name(self) -> str:
        """
        Gets the name of the application.

        Returns:
            str: Name of the application.
        """
        return self.name

    def get_msg_size(self) -> int:
        """
        Gets the size of the message sent by the application.

        Returns:
            str: Message size of the application.
        """
        return self.message_size

    def get_initial_load(self) -> int:
        """
        Gets the initial load of the simulation.

        Returns:
            int: Initial load.
        """
        return self.initial_load

    def get_final_load(self) -> int:
        """
        Gets the final load of the simulation.

        Returns:
            int: Final load.
        """
        return self.final_load

    def get_steps(self) -> int:
        """
        Gets the steps that will be perform during the simulation.

        Returns:
            int: Steps to be performed during the simulation.
        """
        return self.steps

    def get_filename(self) -> str:
        """
        Gets the type of application.

        Returns:
            str: Type of application.
        """
        return self.file_name


# Derived from Topology


class RLFT(Topology):
    """A class representing a RLFT topology.

    This class provides functionality to add/remove RLFT-specific parameters.

    Attributes:
        name (str): Name of the topology.
        network (str): Name of the simulation folder the omnetpp_ini file is located.
        channel_distance (int): Distance of the channels in the topology.
        arity (int): Half of the number of ports of the switch.
        stages (int): Number of staes of the network.
        nodes (int): The number of nodes that the topology contains.
    """

    def __init__(self, parent=None):
        """Initializes the RLFT topology with default values."""
        super().__init__()
        self.parent = parent
        self.name = "rlft"
        self.network = "RLFT"
        self.arity = 0
        self.stages = 0
        self.nodes = 0

    # ----- Setters ----- #

    def set_arity(self, arity: int):
        """
        Sets the arity of the RLFT network.

        Args:
            arity (int): Arity of the network.
        """
        self.arity = arity
        self.set_nodes(self.arity, self.stages)

    def set_stages(self, stages: int):
        """
        Sets the number of stages of the RLFT network.

        Args:
            stages (int): Number of stages of the network.
        """
        self.stages = stages
        self.set_nodes(self.arity, self.stages)

    def set_nodes(self, arity: int, stages: int):
        """
        Sets the number of nodes of the RLFT network.

        Args:
            arity (int): Arity of the network.
            stages (int): Number of stages of the network.
        """
        self.arity = arity
        self.stages = stages
        self.nodes = 2 * (pow(arity, stages))

    # ----- Getters ----- #

    def get_arity(self) -> int:
        """
        Gets the arity of the RLFT network.

        Returns:
            int: Arity of the network.
        """
        return self.arity

    def get_stages(self) -> int:
        """
        Gets the number of stages of the RLFT network.

        Returns:
            int: Number of stages of the network.
        """
        return self.stages

    def get_nodes(self) -> int:
        """
        Gets the number of nodes of the RLFT network.

        Returns:
            int: Number of nodes of the network.
        """
        return self.nodes


class Torus(Topology):
    """A class representing a Torus topology.

    This class provides functionality to add/remove Torus-specific parameters.

    Attributes:
        name (str): Name of the topology.
        dimensions (int): The number of dimensions that the topology contains.
    """

    def __init__(self, parent=None):
        """Initializes the Torus topology with default values"""
        super().__init__()
        self.parent = parent
        self.name = "torus"
        self.dimensions = 0

    def get_dimensions(self) -> int:
        """
        Gets the number of dimensions of the torus network.

        Returns:
            int: Number of dimensions of the torus.
        """
        return self.dimensions


class Torus2D(Torus):
    """A class representing a Torus2D topology.

    This class provides functionality to add/remove Torus2D-specific parameters.

    Attributes:
        network (str): Network name.
        dim1 (int): Size of dimension 1.
        dim2 (int): Size of dimension 2.
    """

    def __init__(self, parent=None):
        """Initializes the torus2D network with default values."""
        super().__init__()
        self.parent = parent
        self.network = "Torus2D"
        self.dim1 = 0
        self.dim2 = 0

    # ----- Setters ----- #

    def set_dim1(self, dim1: int):
        """
        Sets the size of dimension 1 of the Torus2D network.

        Args:
            dim1 (int): Size of the dimension 1.
        """
        self.dim1 = dim1
        self.set_nodes(self.dim1, self.dim2)

    def set_dim2(self, dim2: int):
        """
        Sets the size of dimension 2 of the Torus2D network.

        Args:
            dim2 (int): Size of the dimension 2.
        """
        self.dim2 = dim2
        self.set_nodes(self.dim1, self.dim2)

    def set_nodes(self, dim1: int, dim2: int):
        """
        Sets the number of nodes of the Torus2D network.

        Args:
            dim1 (int): Size of the dimension 1.
            dim2 (int): Size of the dimension 2.
        """
        self.nodes = dim1 * dim2

    # ----- Getters ----- #

    def get_dim1(self) -> int:
        """
        Gets the size of dimension 1 of the Torus2D network.

        Returns:
            int: Size of dimension 1 of the Torus2D.
        """
        return self.dim1

    def get_dim2(self) -> int:
        """
        Gets the size of dimension 2 of the Torus2D network.

        Returns:
            int: Size of dimension 2 of the Torus2D.
        """
        return self.dim2

    def get_nodes(self) -> int:
        """
        Gets the number of nodes of the Torus2D network.

        Returns:
            int: Size of dimension 1 of the Torus2D.
        """
        return self.nodes


# Derived from Switch


class IB_NDR(Switch):
    """A class representing an IB_NDR switch in a simulation.

    This class provides functionality to add/remove IB_NDR switch parameters.

    Attributes:
        architecture (str): Architecture of the switch.
    """

    def __init__(self, parent=None):
        """Initializes the IB_NDR switch with default values."""
        super().__init__()
        self.parent = parent
        self.architecture = "IB_NDR"


class BXI3(Switch):
    """A class representing an IB_NDR switch in a simulation.

    This class provides functionality to add/remove IB_NDR switch parameters.

    Attributes:
        architecture (str): Architecture of the switch.
    """

    def __init__(self, parent=None):
        """Initializes the BXI3 switch with default values."""
        super().__init__()
        self.parent = parent
        self.architecture = "BXI3"


# Derived from Application
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


# Enum


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


class SwArbiters(Enum):
    # Input Queue (IQ)
    Aging = 1
    WRR = 2
    RR = 3


class Applications(Enum):
    S = 1  # Synthetic


class CongestionTechniques(Enum):
    oneq = 1
    voqnet = 2
    voqsw = 3
    obqa = 4
    flow2sl = 5
    dbbm = 6
    bbq = 7
    vftree = 8
    xflow2sl = 9


class RoutingAlgorithms(Enum):
    destro = 1


# ----- Methods ----- #


def list_topologies(topologies):
    for topology in Topologies:
        topologies.append(topology.name)


def list_switch_architectures(sw_archs):
    for sw_arch in SwArchs:
        sw_archs.append(sw_arch.name)


def list_switch_arbiters(sw_arbiters):
    for sw_arb in SwArbiters:
        sw_arbiters.append(sw_arb.name)


def list_switch_queue_schemes(sw_queue_schemes):
    for sw_queue in CongestionTechniques:
        sw_queue_schemes.append(sw_queue.name)


def list_switch_routing_algorithms(sw_routing_algorithms):
    for sw_algorithm in RoutingAlgorithms:
        sw_routing_algorithms.append(sw_algorithm.name)


def list_applications(apps):
    for app in Applications:
        apps.append(app.name)


def list_congestion_control_technique(apps):
    for congestion in CongestionTechniques:
        apps.append(congestion.name)


# def check_configuration(simulation, config_name="[Config"):
#     """
#     It checks if there is a configuration defined in the omnetpp.ini file
#
#     :param simulation: the simulation folder to be checked
#     :param config_name: the name of the configuration to be checked. The default value checks if there is any configuration
#     :returns: True if the configuration was found. Prints "Not Found" otherwise
#     """
#
#     opp_file = simulation.get_root_dir() + "/omnetpp.ini"
#
#     # Open the file and search for the target line
#     with open(opp_file, "r") as file:
#         for line_number, line in enumerate(file, start=1):
#             if config_name in line:
#                 return True
#         else:
#             print("Not Found")


def check_configuration(simulation) -> str:
    """
    It returns the name of the configuration from omnetpp.ini.

    Args:
        simulation (Simulation): the simulation folder to be checked.

    Returns:
        str: the name of the configuration.
    """
    opp_file = os.path.join(simulation.get_root_dir(), "omnetpp.ini")
    config_name = "# Configuration:"

    try:
        with open(opp_file, "r") as file:
            for line in file:
                if config_name in line:
                    start_idx = line.find(config_name) + len(config_name)
                    end_idx = len(line) - 1
                    if end_idx != -1:
                        return line[start_idx:end_idx].strip()
        return "Nothing Found"
    except FileNotFoundError:
        return f"Error: File {opp_file} not found"


# ----- Getters ----- #


def get_configuration(simulation) -> str:
    """
    It retrieves the first configuration within the omnetpp.ini file.

    Args:
        simulation (Simulation): the simulation folder to be checked.

    Returns:
        str: The first configuration found in the omnetpp.ini file. Prints "Nothing Found" if no configurations where found
    """
    opp_file = os.path.join(simulation.get_root_dir(), "omnetpp.ini")
    config_name = "[Config"

    try:
        with open(opp_file, "r") as file:
            for line in file:
                if config_name in line:
                    start_idx = line.find(config_name) + len(config_name)
                    end_idx = line.find("]", start_idx)
                    if end_idx != -1:
                        return line[start_idx:end_idx].strip()
        return "Nothing Found"
    except FileNotFoundError:
        return f"Error: File {opp_file} not found"


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
    with open(opp_file, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                configs.append(line[8 : line.index("]")])
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
    config_name = "[Config portConfig]"

    with open(opp_file, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                next_line = next(file, None)
                if next_line:
                    next_line = next_line.strip()
                    # Check if the line starts with "extends="
                    if next_line.startswith("extends="):
                        return next_line.split("=", 1)[
                            1
                        ]  # Return everything after "extends="
                return None


def get_switch_routing(simulation):
    """
    It retrieves the current switch routing algorithm in use

    :param simulation: the simulation folder to be checked
    :returns: a string with the current switch routing algorithm being used
    """

    opp_file = simulation.get_root_dir() + "/omnetpp.ini"
    config_name = "**.routingAlgorithm"

    with open(opp_file, "r") as file:
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
    config_name = "**.SW[*].arbiter.typename"

    with open(opp_file, "r") as file:
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
    config_name = "**.requestProcessingTime"

    with open(opp_file, "r") as file:
        for line_number, line in enumerate(file, start=1):
            if config_name in line:
                line = line.strip().replace(" ", "")
                return line.split("=", 1)[1]


# ----- Setters ----- #


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
        f'**.topology = "topology_name"\n',
        "#**.arity = ${arity=2}\n",
        "#**.numStages = ${numStages=3}\n",
        "#**.numNodes = ${numNodes = int(2*pow(${arity},${numStages}))}\n",
        f"**.channelDistance = {channel_distance}m\n",
        "\n",
        "#Routing and Arbitration\n",
        '**.routingAlgorithm = "destro"\n',
        '**.H[*].arbiter.typename = "Arbiter_TwoPhased"\n',
        '#**.SW[*].arbiter.typename = "Arbiter_TwoPhased"\n',
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
        "\n",
    ]

    # Check if the file exists
    if os.path.exists(opp_file):
        # Create a backup
        shutil.copy(opp_file, backup_path)
        print(f"Backup created: {backup_path}")

    # Write the default file
    with open(opp_file, "w") as file:
        # print(lines, file=file)
        file.writelines(lines)

    print(f"File {opp_file} written successfully")


def set_new_configuration(simulation):
    """
    It adds a new configuration in the omnetpp.ini file.

    Args:
        simulation (Simulation): The simulation folder where the omnetpp.ini file is located.
    """

    opp_file = simulation.get_root_dir() + "/omnetpp.ini"
    config_name = set_configuration_name(simulation)

    # ----------- Topology parameters ----------- #
    network_name = simulation.topology.get_network()
    topology_name = simulation.topology.get_name()
    channel_distance = simulation.topology.get_channel_distance()

    # Switch parameters
    architecture = simulation.switch.get_architecture()
    voq = simulation.switch.get_voq()
    arbiter = simulation.switch.get_arbiter()
    routing = simulation.switch.get_routing()
    queue_scheme = simulation.switch.get_queue_scheme()
    num_queues = simulation.switch.num_queues()

    # ----- Configuration ----- #
    lines = [
        "[General]\n",
        f"# Configuration: {config_name}\n",
        f"network = {network_name}\n",
        "\n",
        "#warmup-period=0.00025s\n",
        "\n",
        "cmdenv-status-frequency = 5s\n",
        "sim-time-limit = 0.002000001s\n",
        "cmdenv-interactive=true\n",
        "#Net\n",
        f'**.topology = "{topology_name}"\n',
    ]

    match simulation.topology.get_network():
        case "RLFT":
            arity = str(simulation.topology.get_arity())
            stages = str(simulation.topology.get_stages())

            lines.append(f"**.arity = ${{arity={arity}}}\n")
            lines.append(f"**.numStages = ${{numStages={stages}}}\n")
            lines.append(
                "**.numNodes = ${numNodes = int(2*pow(${arity},${numStages}))}\n"
            )
            lines.append("\n")
        case "Torus2D":
            dim0 = str(simulation.topology.get_dim1())
            dim1 = str(simulation.topology.get_dim2())
            lines.append(f"**.nD0 = ${{nD0={dim0}}}\n")
            lines.append(f"**.nD1 = ${{nD1={dim1}}}\n")
            lines.append(f"**.nodesInEachDim = ${{{dim0}}} ${{{dim1}}}\n")
            lines.append("**.numNodes = ${numNodes=${nD0}*${nD1}}\n")
            lines.append("\n")

    lines.append(f"**.channelDistance = {channel_distance}m\n")
    lines.append("\n")
    lines.append("#Routing and Arbitration\n")
    lines.append(f'**.routingAlgorithm = "{routing}"\n')
    lines.append('**.H[*].arbiter.typename = "Arbiter_TwoPhased"\n')
    lines.append(f'**.SW[*].arbiter.typename = "{arbiter}"\n')
    lines.append("**.requestProcessingTime = 6ns")
    lines.append("\n")
    lines.append("\n")
    lines.append("#Logging\n")
    lines.append("**.logInterval = 10us\n")
    lines.append("\n")
    lines.append(
        "**.sysMng.**.result-recording-modes = default, +vector,+histogram\n"
    )
    lines.append(
        "**.sys.app*-**.result-recording-modes = default, +vector,+histogram\n"
    )
    lines.append("\n")
    lines.append(
        "# Stats to record per node - we have to indicate the stat that we want to recollect\n"
    )
    lines.append("#**.H[127].throughput.\n")
    lines.append("**.H[*].**.scalar-recording = false\n")
    lines.append("**.SW[*].**.scalar-recording = false\n")
    lines.append("**.param-recording = false\n")
    lines.append("\n")
    lines.append("# Queueing scheme\n")
    lines.append(f'**.congestionControlTechnique = "{queue_scheme}"\n')
    lines.append(f"**.numQueues = {num_queues}\n")
    lines.append("\n")
    lines.append("#Port Configurations\n")
    lines.append("include ../TrafficConfigurations/PortPFC.ini\n")
    lines.append("include ../TrafficConfigurations/originalPort.ini\n")
    lines.append("\n")
    lines.append("\n")
    lines.append("# Port configuration for IQ switch\n")
    lines.append(
        "[Config portConfig] #Note that the config included extends from General and portConfig, change the next extend to test other technologies\n"
    )
    lines.append("#IB-NDR = IQ\n")
    lines.append("#BXI3 = CIOQ\n")
    lines.append(f"extends={architecture}	# CIOQ\n")
    lines.append("\n")
    lines.append("#Queuing schemes configurations\n")
    lines.append("include ../TrafficConfigurations/indirect/schemes.ini\n")
    lines.append("\n")
    lines.append("#Traffic generation modes\n")
    lines.append("include ../TrafficConfigurations/indirect/random.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/hotspot.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/victim.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/local.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/storage.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/ebb.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/ebb_hs.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/zipf1.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/sla3.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/ptrans.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/natRing.ini\n")
    lines.append("include ../TrafficConfigurations/indirect/graph500.ini\n")
    lines.append("\n")

    # Check if the file exists
    if os.path.exists(opp_file):
        backup_configuration(simulation)

    # Append new configuration
    with open(opp_file, "w") as file:
        file.writelines(lines)


def set_configuration_name(simulation) -> str:
    """
    Sets the name of the configuration file.

    Args:
        - simulation (Simulation): the simulation that contains the fields of the configuration file.

    Returns:
        - str: the name of the configuration.
    """
    configuration = ""

    if simulation is not None:
        if not isinstance(simulation, Simulation):
            raise TypeError("Argument must be a string")
        else:
            if simulation.topology is None:
                raise TypeError("Topology not added to simulation")
            if simulation.switch is None:
                raise TypeError("Switch not added to simulation")
            if simulation.app is None:
                raise TypeError("Application not added to simulation")
            if simulation.topology.get_name() == "":
                raise ValueError("Topology name not set")
            if simulation.topology.get_nodes() == 0:
                raise ValueError("Topology nodes not set")
            if simulation.switch.get_architecture() == "":
                raise ValueError("Switch architecture not set")
            if simulation.switch.get_arbiter() == "":
                raise ValueError("Switch arbiter not set")
            if simulation.switch.get_queue_scheme() == "":
                raise ValueError("Switch queue scheme not set")
            if simulation.switch.get_num_queues() == 0:
                raise ValueError("Switch number of queues not set")

            # Concatenate name fields
            configuration += simulation.topology.get_network()
            configuration += "-"
            configuration += str(simulation.topology.get_nodes()) + "N"

            configuration += "_"
            configuration += (
                simulation.switch.get_architecture().replace("_", "").upper()
            )
            configuration += "-"
            configuration += simulation.switch.get_arbiter()
            configuration += "-"
            configuration += simulation.switch.get_queue_scheme()
            configuration += "-"
            configuration += str(simulation.switch.get_num_queues()) + "Q"

            configuration += "_"

            # TODO: Concatenate relevant app fields to configuration name
    return configuration


def backup_configuration(simulation):
    """
    Backups the current omnetpp.ini file in the root of the simulation directory

    Args:
        - simulation (Simulation): the simulation that contains the fields of the configuration file.
    """
    opp_file = simulation.get_root_dir() + "/omnetpp.ini"
    backup_file = (
        simulation.get_root_dir()
        + "/"
        + check_configuration(simulation)
        + ".bak"
    )

    if not os.path.exists(backup_file):
        shutil.copy2(opp_file, backup_file)
    else:
        print(f" {backup_file} file already exists.")
