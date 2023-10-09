import rclpy as rp
from rclpy.node import Node
import RPi.GPIO as GPIO
from time import sleep

from temi.msg import Velocity

class Temi(Node):

    def __init__(self):
        super().__init__('temi')
        self.publisher = self.create_publisher(Velocity,'velocity',10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback:
        msg = Velocity()
        
