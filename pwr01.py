# a wrapper to be used with pyvisa specfically for the kikusui PWR-01 series DC power supply

# a PWR-01 class

# methods - function associated with a class

class Pwr_01:
    
    def __init__(self, instrument):
        self.serial_no = 1
        self.model_no = 2
        self.instrument = instrument

        # case set max values based on model number

    def set_voltage(self, voltage):
        self.instrument.write('VOLTage{}'.format(voltage))
    
    def read_voltage(self):
        return(self.instrument.query('VOLT?'))

    def output(self, signal):
        if signal:
            self.instrument.write('OUTP ON')
        else:
            self.instrument.write('OUTP OFF')
