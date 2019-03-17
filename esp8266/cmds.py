
./generate-CA.sh
 cd /etc/mosquitto
    #$Copy ca and server files and configure mosquitto config  - mosquitto.conf
sudo apt install -y mosquitto mosquitto-clients

sudo systemctl start  mosquitto.service

./generate-CA.sh client rasp-pi


   mosquitto_sub -h 192.168.1.8  -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  
                    --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key


  mosquitto_sub -h raspberrypi -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key

  mosquitto_sub -h raspberrypi.local  -t test-topic   --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-client.crt --key ./ssl2/rasp-client.key

mosquitto_pub -h raspberrypi.local -t test-topic  
--cafile ./ssl/ca.crt -m "Test message7" -p 8883 --cert ./ssl/rasp-client.crt --key ./ssl/rasp-client.key

 ./generate-CA.sh client esp

 openssl x509 -outform der -in esp.crt -out esp_crt.der

 openssl rsa -outform der -in esp.key -out esp_key.der

 openssl x509 -outform der -in ca.crt -out ca_crt.der

 wget https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh
 sudo apt install -y mosquitto mosquitto-clients


mosquitto_sub -h raspberrypi -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key
