import utime
from umqtt.robust import MQTTClient
import parseargs

class esp:
    key = ''
    cert = ''
    device_id = ''
    mqtt_server = ''
    mqtt_port = 8883
    sensor = ''

    def __init__(self):
        args = parseargs.parse_args()
        self.device_id = args.device_id
        self.mqtt_server = args.mqtt_server
        self.mqtt_port = args.mqtt_port

        # Read key and certificate files into variable for passing to MQTTClient function
        with open(args.client_key_file) as f:
            self.key = f.read()
        with open(args.client_crt_file) as f:
            self.cert = f.read()     

    def set_sensor(self, sensor):
        self.sensor = sensor

    def connect(self, client):
     i = 0
     while 1:
        try:
            return client.connect(False)
        except OSError as e:
            print(e)
            i += 1
            print("Waiting to connect for " + str(i) + " seconds")
            utime.sleep(i)   

    def senddata(self):
       c = MQTTClient(client_id=self.device_id,server=self.mqtt_server,port=self.mqtt_port, ssl=True, 
                     keepalive=4000,ssl_params={'key': self.key,'cert':self.cert,'server_side':False})
       self.connect(c)

       while True:
          temp_reading = self.sensor.read()
          mqtt_topic = b"/home/sensor/" + self.device_id
          print('Sending temperature reading: ' + str(temp_reading) + ' to topic '+ str(mqtt_topic))
          c.publish(b"/home/sensor/" + self.device_id, str(temp_reading))
          utime.sleep(60)
