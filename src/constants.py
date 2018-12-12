import bbio as io
from bbio.libraries.RotaryEncoder import RotaryEncoder

"""
File containing all useful constants that are used in the code
"""

MAX_SPEED = 80
RIGHT_MOTOR = io.PWM2B
LEFT_MOTOR = io.PWM2A
RIGHT_ENCODER = RotaryEncoder.EQEP2b
LEFT_ENCODER = RotaryEncoder.EQEP1
IR_SENSOR_SPI = io.SPI0
IR_SENSOR_CS = 0
IR_SENSOR_FREQ = 50000
IR_SENSOR_THRESHOLD = 300
IR_SENSOR_DEFAULT_ACTIVATIONS = [0, 0, 0, 1, 1, 0, 0, 0]
IR_SENSOR_NO_ACTIVATIONS = [0, 0, 0, 0, 0, 0, 0, 0]
IR_SENSOR_WEIGHTS = [-9, -6, -3, -1, 1, 3, 6, 9]
IR_SENSOR_MAX_WEIGHT = 12
SCALE_SPEED = 1.0 / 12.0
LIMITS = (0, 255)
PAUSE_MS = 10
PAUSE_S = PAUSE_MS / 1000.0
ENCODER_FREQ = 100
KP = 1.00726
KI = 18.38404
ENCODER_OUTPUT_GAIN = 255.0 / 8000.0
