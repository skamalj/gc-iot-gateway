import argparse
import os

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=(
            'Example Google Cloud IoT Core MQTT device connection code.'))
    parser.add_argument(
            '--mqtt_server',
            default='192.168.1.8',
            required=False,
            help='Local mqtt server to connect to')
    parser.add_argument(
            '--mqtt_port',
            default=8883,
            required=False )
    parser.add_argument(
            '--device_id', 
            default='tempsensor',
            required=False,
            help='Device id of sensor in GCP cloud')
    parser.add_argument(
            '--client_key_file',
            default='esp_key.der',
            required=False,
            help='Client key file in der format')
    parser.add_argument(
            '--client_crt_file', 
            default='esp_crt.der', 
            required=False, 
            help='client certificate in der format')                       
    return parser.parse_args()
