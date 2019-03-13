import connectwifi
from publishtemp import esp
from readtemp import tempsensor

sensor = tempsensor()

connectwifi.do_connect()
esp_obj = esp()
esp_obj.set_sensor(sensor)
esp_obj.senddata()