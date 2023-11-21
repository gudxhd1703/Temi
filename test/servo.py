import time

from board import SCL, SDA
import busio

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

servo1 = servo.Servo(pca.channels[1])
servo2 = servo.Servo(pca.channels[2])
servo3 = servo.Servo(pca.channels[3])
servo4 = servo.Servo(pca.channels[4])
<<<<<<< HEAD


try:
    while True:
        servo1.angle = 90
        servo2.angle = 90
        servo3.angle = 0
        servo4.angle = 0
except KeyboardInterrupt:
    print("프로그램 종료")
finally:    
    pca.reset()
    pca.deinit()
=======
time.sleep(1)

# We sleep in the loops to give the servo time to move into position.
#try:
#    while True:
servo1.angle = 70
servo2.angle = 70
servo3.angle = 70
servo4.angle = 70
time.sleep(2)

#except KeyboardInterrupt:
pca.deinit()
>>>>>>> 442fc30 (test)
   
# You can also specify the movement fractionally.

