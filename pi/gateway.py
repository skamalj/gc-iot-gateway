import paho.mqtt.client as mqtt
import ssl 
import jwt
import datetime


# [START iot_mqtt_jwt]
def create_jwt(project_id, private_key_file, algorithm):
   
    token = {
            # The time that the token was issued at
            'iat': datetime.datetime.utcnow(),
            # The time the token expires.
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440),
            # The audience field should always be set to the GCP project id.
            'aud': project_id
    }

    # Read the private key file.
    with open(private_key_file, 'r') as f:
        private_key = f.read()

    print('Creating JWT using {} from private key file {}'.format(
            algorithm, private_key_file))

    return jwt.encode(token, private_key, algorithm=algorithm)
# [END iot_mqtt_jwt]


def error_str(rc):
    """Convert a Paho error to a human readable string."""
    return '{}: {}'.format(rc, mqtt.error_string(rc))


def on_connect(client, unused_userdata, unused_flags, rc):
    """Callback for when a device connects."""
    print('on_connect', mqtt.connack_string(rc))


def on_disconnect(unused_client, unused_userdata, rc):
    """Paho callback for when a device disconnects."""
    print('on_disconnect', error_str(rc))


def on_publish(unused_client, unused_userdata, unused_mid):
    """Paho callback when a message is sent to the broker."""
    print('on_publish')


def on_message(unused_client, unused_userdata, message):
    """Callback when the device receives a message on a subscription."""
    payload = str(message.payload)
    print('Received message \'{}\' on topic \'{}\' with Qos {}'.format(
            payload, message.topic, str(message.qos)))

def detach_device(client, device_id):
    """Detach the device from the gateway."""
    # [START detach_device]
    detach_topic = '/devices/{}/detach'.format(device_id)
    print('Detaching: {}'.format(detach_topic))
    client.publish(detach_topic, '{}', qos=1)
    # [END detach_device]


def attach_device(client, device_id, auth):
    """Attach the device to the gateway."""
    # [START attach_device]
    attach_topic = '/devices/{}/attach'.format(device_id)
    
    attach_payload = '{{"authorization" : "{}"}}'.format(auth)
    client.publish(attach_topic, attach_payload, qos=1)
    
    print(attach_topic + ' '+ attach_payload)
    # [END attach_device]

def get_client(
        project_id, cloud_region, registry_id, device_id, private_key_file,
        algorithm, ca_certs, mqtt_bridge_hostname, mqtt_bridge_port):
    """Create our MQTT client. The client_id is a unique string that identifies
    this device. For Google Cloud IoT Core, it must be in the format below."""
    client_id=('projects/{}/locations/{}/registries/{}/devices/{}'
                       .format(
                               project_id,
                               cloud_region,
                               registry_id,
                               device_id))
    print(client_id)
    client = mqtt.Client(client_id)

    # With Google Cloud IoT Core, the username field is ignored, and the
    # password field is used to transmit a JWT to authorize the device.
    client.username_pw_set(
            username='unused',
            password=create_jwt(
                    project_id, private_key_file, algorithm))

    # Enable SSL/TLS support.
    client.tls_set(ca_certs=ca_certs, tls_version=ssl.PROTOCOL_TLSv1_2)

    # Register message callbacks. https://eclipse.org/paho/clients/python/docs/
    # describes additional callbacks that Paho supports. In this example, the
    # callbacks just print to standard out.
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    # Connect to the Google MQTT bridge.
    client.connect(mqtt_bridge_hostname, mqtt_bridge_port)
    
        

    # This is the topic that the device will receive configuration updates on.
    mqtt_config_topic = '/devices/{}/config'.format(device_id)

    # Subscribe to the config topic.
    client.subscribe(mqtt_config_topic, qos=1)

    # The topic that the device will receive commands on.
    mqtt_command_topic = '/devices/{}/commands/#'.format(device_id)

    # Subscribe to the commands topic, QoS 1 enables message acknowledgement.
    print('Subscribing to {}'.format(mqtt_command_topic))
    client.subscribe(mqtt_command_topic, qos=0)

    return client
           
