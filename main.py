# the main file to test the different wrappers 

import pyvisa as visa
import pwr01
import time

rm = visa.ResourceManager()
print(rm.list_resources())

instrument = rm.open_resource('USB0::0x0B3E::0x1049::XE001118::INSTR')

PWR_01_A = pwr01.Pwr_01(instrument)
# print(instrument.query('*IDN?'))
# instrument.write('VOLT 40')
# print(instrument.query('VOLT ?'))


PWR_01_A.set_voltage(40)
print(PWR_01_A.read_voltage())

PWR_01_A.output(1)
time.sleep(7)
PWR_01_A.output(0)
