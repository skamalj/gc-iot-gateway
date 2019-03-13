from machine import Pin
import onewire
import time, ds18x20

class tempsensor:

   def read(self):
     ow = onewire.OneWire(Pin(2))
     ds = ds18x20.DS18X20(ow)
     rom = ds.scan()[0]
     ds.convert_temp()
     time.sleep_ms(750)
     return ds.read_temp(rom)
