import argparse
import os

def parse_command_line_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=(
            'Example Google Cloud IoT Core MQTT device connection code.'))
    parser.add_argument(
            '--algorithm',
            default='RS256',
            choices=('RS256', 'ES256'),
            required=False,
            help='Which encryption algorithm to use to generate the JWT.')
    parser.add_argument(
            '--ca_certs',
            default='roots.pem',
            help=('CA root from https://pki.google.com/roots.pem'))
    parser.add_argument(
            '--cloud_region', default='asia-east1', help='GCP cloud region')
    parser.add_argument(
            '--device_id', default='tempsensor', required=False, help='Cloud IoT Core device id')
    parser.add_argument(
            '--gateway_id', default='my-gateway', required=False, help='Gateway identifier.')
    parser.add_argument(
            '--jwt_expires_minutes',
            default=120,
            type=int,
            help=('Expiration time, in minutes, for JWT tokens.'))
    parser.add_argument(
            '--mqtt_bridge_hostname',
            default='mqtt.googleapis.com',
            help='MQTT bridge hostname.')
    parser.add_argument(
            '--mqtt_bridge_port',
            choices=(8883, 443),
            default=8883,
            type=int,
            help='MQTT bridge port.')
    parser.add_argument(
            '--private_key_file',
            default='rsa_private.pem',
            required=False,
            help='Path to private key file.')
    parser.add_argument(
            '--project_id',
            default='my-iot-project-2019',
            help='GCP cloud project name')
    parser.add_argument(
            '--registry_id', 
            default='my-iot-registry', 
            required=False, 
            help='Cloud IoT Core registry id')
    parser.add_argument(
            '--mosquitto_key_file', 
            default='rasp-client.key', 
            required=False, 
            help='Key for local mqtt client')
    parser.add_argument(
            '--mosquitto_crt_file', 
            default='rasp-client.crt', 
            required=False, 
            help='Certificate for local mqtt client')  
    parser.add_argument(
            '--mosquitto_cacert_file', 
            default='ca.crt', 
            required=False, 
            help='CA certificate for local mqtt client') 
    parser.add_argument(
            '--mosquitto_broker', 
            default='192.168.1.9', 
            required=False, 
            help='Broker IP for local mqtt client') 
    parser.add_argument(
            '--mosquitto_port', 
            default=8883, 
            required=False, 
            help='Port for local mqtt service')                                                              
    return parser.parse_args()
