import rclpy as rp
from rclpy.node import Node
import RPi.GPIO as GPIO
from time import sleep

from temi.msg import Velocity

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWORD = 2

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

class Temi(Node):

    def __init__(self):
        super().__init__('temi')
        self.publisher = self.create_publisher(Velocity,'velocity',10)
        timer_period = 0.3
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback:
        msg = Velocity()
        
