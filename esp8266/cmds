
./generate-CA.sh
 cd /etc/mosquitto
    #$Copy ca and server files and configure mosquitto config  - mosquitto.conf
sudo systemctl start  mosquitto.service

./generate-CA.sh client rasp-pi


   mosquitto_sub -h 192.168.1.8  -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  
                    --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key


  mosquitto_sub -h raspberrypi -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key

  mosquitto_sub -h raspberrypi.local  -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key

 ./generate-CA.sh client esp

 openssl x509 -outform der -in esp.crt -out esp_crt.der

 openssl rsa -outform der -in esp.key -out esp_key.der

 openssl x509 -outform der -in ca.crt -out ca_crt.der

mosquitto_sub -h raspberrypi -t /home/sensor/tempsensor  --cafile ./ssl2/ca.crt -p 8883  --cert ./ssl2/rasp-pi.crt --key ./ssl2/rasp-pi.key
