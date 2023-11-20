import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)

pca.frequency = 50

servo1 = servo.Servo(pca.channels[7])
#servo2 = servo.Servo(pca.channels[2])
#servo3 = servo.Servo(pca.channels[3])
#servo4 = servo.Servo(pca.channels[4])


# We sleep in the loops to give the servo time to move into position.
#try:
#    while True:
servo1.angle = 90
#servo2.angle = 90
#       servo3.angle = 0
#        servo4.angle = 0
#except KeyboardInterrupt:
pca.deinit()
   
# You can also specify the movement fractionally.

