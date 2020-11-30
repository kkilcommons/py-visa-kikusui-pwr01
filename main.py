# the main file to test the different wrappers 

import pyvisa as visa
import pwr01

rm = visa.ResourceManager('@py')
print(rm.list_resources())

instrument = rm.open_resource('COM2')

PWR_01_A = pwr01.Pwr_01(instrument, '123456', 'PWR401ML')

PWR_01_A.set_voltage(40)


