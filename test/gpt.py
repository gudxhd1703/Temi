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

def rotate_servo(servo_motor, angle):
    servo_motor.angle = angle

try:
    while True:
    	
     #   for angle in range(0,181,10):
            rotate_servo(servo0, 0)
            rotate_servo(servo1, 0)
            rotate_servo(servo2, 0)
            rotate_servo(servo3, 0)
          #  time.sleep(0.5)
       # for angle in range(181,0,10):
        #    rotate_servo(servo0, angle)
         #   rotate_servo(servo1, angle)
          #  rotate_servo(servo2, angle)
           # rotate_servo(servo3, angle)
           # time.sleep(0.5)

except KeyboardInterrupt:
    print('exit')
    
finally:
    pca.deinit()

