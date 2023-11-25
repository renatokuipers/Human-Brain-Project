# Central place for all constants used in the project

# BrainSimulationProject Constants

# General Biological Constants
NEURON_RESTING_POTENTIAL = -70  # mV
ACTION_POTENTIAL_THRESHOLD = -55  # mV
MAX_NEURON_FIRE_RATE = 1000  # Hz

# Ion Channel Constants
NA_CONCENTRATION_OUT = 145  # mM
NA_CONCENTRATION_IN = 12  # mM
K_CONCENTRATION_OUT = 4  # mM
K_CONCENTRATION_IN = 155  # mM
CL_CONCENTRATION_OUT = 110  # mM
CL_CONCENTRATION_IN = 10  # mM

# Synaptic Transmission
SYNAPTIC_CLEFT_WIDTH = 20  # nm
NEUROTRANSMITTER_RELEASE_PROBABILITY = 0.5  # probability
MAX_SYNAPTIC_DELAY = 2.0  # ms

# Neuron Model Constants
MEMBRANE_RESISTANCE = 1e7  # Ohms
MEMBRANE_CAPACITANCE = 1e-6  # Farads

# Synapse Model Constants
SYNAPTIC_WEIGHT_RANGE = (0.0, 1.0)
SYNAPTIC_DECAY_CONSTANT = 0.5  # Time constant for synaptic decay

# Neurotransmitter Dynamics
GLUTAMATE_REUPTAKE_TIME = 0.5  # ms
GABA_REUPTAKE_TIME = 0.6  # ms

# Electrophysiological Properties
AXONAL_CONDUCTION_VELOCITY = 120  # m/s (range can be from 0.5 m/s to 120 m/s)

# Neural Coding
SPIKE_TIMING_PRECISION = 1  # ms

# Neural Network Dynamics
SMALL_WORLD_REWIRING_PROBABILITY = 0.1
SCALE_FREE_NETWORK_EXPONENT = 2.5

# Sensory Processing Constants
VISUAL_FIELD_SIZE = 180  # degrees
AUDITORY_FREQUENCY_RANGE = (20, 20000)  # Hz

# Cognitive Functions
WORKING_MEMORY_CAPACITY = 7  # items

# Emotional and Social Processing
EMOTIONAL_INTENSITY_SCALE = (0, 10)

# Pathology
ALZHEIMERS_PLAQUE_THRESHOLD = 30  # Arbitrary Units

# Whole Brain Dynamics
BRAIN_TOTAL_NEURONS = 86e9  # Estimated total number of neurons in human brain

# Consciousness
CONSCIOUSNESS_THRESHOLD = 0.5  # Arbitrary scale

# Miscellaneous
SIMULATION_TIME_STEP = 0.1  # ms
BRAIN_TEMPERATURE = 37  # Celsius
BRAIN_PH = 7.4
