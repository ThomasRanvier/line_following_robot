import bbio as io
from ir_sensor import IR_sensor

IR_SENSOR_PINS = [io.AIN0, io.AIN1, io.AIN2, io.AIN3]
ir_sensors = IR_sensor(IR_SENSOR_PINS)
while True:
    ir_values = ir_sensors.get_values()
    print '(', ir_values[0], ir_values[1], ir_values[2], ir_values[3], ')'#, ir_values[4], ir_values[5], ir_values[6], ir_values[7], ')'
