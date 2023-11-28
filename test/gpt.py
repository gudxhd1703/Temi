import time
import busio
from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

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


angle = 90 
center_angle = 15
try:
    while True:
    	
            rotate_servo(servo0, 90)
            rotate_servo(servo1, 110)
            rotate_servo(servo2, 110)
            rotate_servo(servo3, 90)
            rotate_servo(servo4, center_angle)


except KeyboardInterrupt:
    print('exit')
    
finally:
    pca.deinit()
