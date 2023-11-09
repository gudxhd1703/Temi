import rclpy
from rclpy.node import Node
from temi_msgs.msg import Ultrasonic

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# 초음파 센서의 TRIG 및 ECHO 핀에 연결된 GPIO 번호 설정
TRIG = [22,23,24,25] 
ECHO = [27,28,29,30]

class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_publisher')
        # 4개의 토픽 생성 (각각의 초음파 센서에 대응)
        self.publisher_ = [self.create_publisher(Ultrasonic, 'ultrasonic'+str(i), 10) for i in range(4)]
        timer_period = 0.5  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        
        for i in range(4): # 각 초음파 센서에 대해 반복
            GPIO.setup(TRIG[i],GPIO.OUT)
            GPIO.setup(ECHO[i],GPIO.IN)

            GPIO.output(TRIG[i], False)
            time.sleep(0.5)

            GPIO.output(TRIG[i], True)
            time.sleep(0.00001)
            GPIO.output(TRIG[i], False)

            while GPIO.input(ECHO[i])==0:
                pulse_start = time.time()

            while GPIO.input(ECHO[i])==1:
                pulse_end = time.time()

           # 초음파가 반사되어 돌아오는 시간을 이용하여 거리 계산 
            distance_cm= round((pulse_end - pulse_start) * 34300 / 2 , 2 )

            msg=Ultrasonic()
            msg.data=distance_cm
           # 해당 거리 정보를 토픽으로 발행 
            self.publisher_[i].publish(msg)


def main(args=None):
    rclpy.init(args=args)

    ultrasonic_publisher=UltrasonicPublisher()

    rclpy.spin(ultrasonic_publisher)
    GPIO.cleanup()
    ultrasonic_publisher.destroy_node()

if __name__ == '__main__':
    main()

