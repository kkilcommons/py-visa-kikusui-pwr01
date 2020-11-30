# a wrapper to be used with pyvisa specfically for the kikusui PWR-01 series DC power supply

# a PWR-01 class

# methods - function associated with a class

class Pwr_01:
    
    def __init__(self, instrument, serial_no, model_no):
        self.serial_no = serial_no
        self.model_no = model_no
        self.instrument = instrument

        # case set max values based on model number

    def set_voltage(self, voltage):
        self.instrument.write('VOLTage {}'.format(voltage))

    



