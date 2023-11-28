#sudo apt install -y bluez bluetooth libbluetooth-dev python3-pip && python3 -m pip install pybluez
#sudo apt install -y pkg-config libboost-python-dev libboost-thread-dev libglib2.0-dev python3-dev && python3 -m pip install pybluez\[ble\]
#https://wiki.loliot.net/docs/lang/python/libraries/python-pybluez/


import bluetooth
import busio
from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = bluetooth.PORT_ANY  # RFCOMM 포트
server_sock.bind(("", port))
server_sock.listen(1)
server_sock.settimeout(10)
bluetooth.advertise_service(server_sock, "SampleServer",
                            service_id="00001101-0000-1000-8000-00805F9B34FB",
                            service_classes=["00001101-0000-1000-8000-00805F9B34FB"],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

servo0 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
servo1 = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)
servo2 = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2500)
servo3 = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2500)
servo4 = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2500)


def rotate_servo(servo_motor, angle):
    servo_motor.angle = angle



try:
    while True:
    	
    
        data = client_sock.recv(1024)
        
        if not data:
            break
        data_decode = data.decode("utf-8")
        print("Received [%s]" % data_decode)
        client_sock.send("servo: [%s]  % data_decode")
        angle = int(data_decode)
        rotate_servo(servo0, angle)
        rotate_servo(servo1, angle)
        rotate_servo(servo2, angle)
        rotate_servo(servo3, angle)
        rotate_servo(servo4, angle)

except OSError:
    pass
except KeyboardInterrupt :
    print("Program terminated by user")
finally:
    client_sock.close()
    server_sock.close()
    print("Disconnected.")


