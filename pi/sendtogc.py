import paho.mqtt.client as mqtt
import time
import connect, parseargs
broker = '192.168.1.8'
port = 8883
gw_client = ''
local_client = ''
mqtt_topic = ''


def on_connect(client, user_data, flags, rc):
    print("Local mqtt client connected")


def on_disconnect(client, user_data, rc):
    print("Local mqtt client disconnected")


def on_message(client, userdata, message):
    global mqtt_topic
    print("Local mqtt recieved temp reading =" +
          str(message.payload.decode("utf-8")) +
          " on topic " +
          message.topic.decode("utf-8")
          )
    msg_payload =  str(message.payload.decode("utf-8"))  
    gw_client.publish(mqtt_topic,msg_payload,qos=1)


def create_local_client(client_name):
    client = mqtt.Client(client_name)
    client.on_message = on_message
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.tls_set(ca_certs='ca.crt', certfile='kamal.crt',keyfile='kamal.key')
    client.tls_insecure_set(True)
    client.connect(broker, port)
    client.subscribe(b"/home/sensor/+")
    return client

def create_gw_client():
    args = parseargs.parse_command_line_args()
    client = connect.get_client(
                args.project_id, args.cloud_region,
                args.registry_id, args.gateway_id, args.private_key_file,
                args.algorithm, args.ca_certs, args.mqtt_bridge_hostname,
                args.mqtt_bridge_port)
    connect.attach_device(client,args.device_id,'')    
    time.sleep(15)        
    return client

def main():
    global gw_client
    global local_client
    global mqtt_topic
    args = parseargs.parse_command_line_args()
    gw_client = create_gw_client()
    local_client = create_local_client('mosquitto-client')
    mqtt_topic = '/devices/{}/events/{}'.format(args.device_id,args.device_id)
    device_config_topic = '/devices/{}/config'.format(args.device_id)
    gw_client.subscribe(device_config_topic, qos=0)
    gw_client.loop_start()
    local_client.loop_forever()
