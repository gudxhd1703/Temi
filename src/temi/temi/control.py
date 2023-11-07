import rclpy as rp
from rclpy.node import Node

from temi_msgs.msg import Ultrasonic, MotorControl

class Control(Node):

    def __init__(self):
        super().__init__('control')
        self.publisher = self.create_publisher(MotorControl,'motorcontorl',10)
        self.subscription = [self.create_subscription(
            Ultrasonic,
            'ultrasonic'+str(i),
            self.control_callback,
            10) for i in range(4)]

    def control_callback(self):
        motor_msg = MotorControl()
        ultrasonic_msg = Ultrasonic()

        if ultrasonic_msg.data < 10:  ## 거리수정해야함
            motor_msg.velocity = 0

        self.publisher_publish(motor_msg)

def main(args=None):
 
    rp.init(args=args)

    control_node = Control()
 
    rp.spin(control_node)
 
    control_node.shutdown()
    rp.shutdown()

if __name__ == '__main__':
    main()
