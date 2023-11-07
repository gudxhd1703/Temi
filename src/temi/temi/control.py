import rclpy as rp
from rclpy.node import Node

from temi_msgs.msg import Ultrasonic, MotorControl

class Control(Node):

    def __init__(self):
        super().__init__('control')
        self.publisher = self.create_publisher(MotorControl,'motorcontorl',10)
        timer_period = 0.3
        self.subscription = [self.create_subscription(
            Ultrasonic,
            'ultrasonic'+str(i),
            self.listener_callback,
            10) for i in range(4)]
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        motor_msg = MotorControl()
        ultrasonic_msg = Ultrasonic()

        if ultrasonic_msg.data < 10:  ## 거리수정해야함
            motor_msg.velocity = 0

def main(args=None):

