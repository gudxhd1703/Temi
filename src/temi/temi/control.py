import rclpy as rp
from rclpy.node import Node

from temi_msgs.msg import Ultrasonic, MotorControl, BluetoothData

stop = 0
speed_change = 10
left = 3
right = 4
transformer = 5
class Control(Node):

    def __init__(self):
        super().__init__('control')
        self.publisher = self.create_publisher(MotorControl,'motorcontorl',10)
        self.ultrasonic_data = [None] * 4  # Initialize storage for ultrasonic data
        self.bluetooth_data = None  # Initialize storage for bluetooth data
        self.subscription_ultrasonic = [self.create_subscription(
            Ultrasonic,
            'ultrasonic'+str(i),
            self.control_callback,
            10) for i in range(4)]
        self.subscripton_bluetooth = self.create_subscription(BluetoothData,'bluetooth_data', self.control_callback,10)

    def control_callback(self):
        motor_msg = MotorControl()
        ultrasonic_msg = Ultrasonic()
        bluetooth_msg = BluetoothData()

        if ultrasonic_msg.data < 10:  ## 거리수정해야함
            motor_msg.velocity = 0
        elif bluetooth_msg.data == 1:
            if -9<motor_msg.velocity < 0:
                motor_msg.velocity
            elif 0< motor_msg.velocity:    
                motor_msg.velocity += speed_change
        
        elif bluetooth_msg.data == 2:
            if -9<motor_msg.velocity < 0:
                motor_msg.velocity
            elif 0< motor_msg.velocity:    
                motor_msg.velocity += speed_change    
                        
    ##### 수정
        elif bluetooth_msg.data == left: ## 좌회전
            motor_msg.velocity = 0
            self.wheel_control(left)

        elif bluetooth_msg.data == right: ## 우회전
            motor_msg.velocity = 0
            self.wheel_control(right)

        elif bluetooth_msg.data == transformer:
            motor_msg.velocity = 0
            self.wheel_control(transformer)
        self.publisher.publish(motor_msg)
     
    def wheel_control(self, direction):
        motor_msg = MotorControl()
        if direction == left:
            motor_msg.direction_fr = 0
            motor_msg.direction_fl = 0
            motor_msg.direction_br = 0
            motor_msg.direction_bl = 0
            
        elif direction == right:   
            motor_msg.direction_fr = 0
            motor_msg.direction_fl = 0
            motor_msg.direction_br = 0
            motor_msg.direction_bl = 0    
        elif direction == transformer:
            motor_msg.direction_fr = 0
            motor_msg.direction_fl = 0
            motor_msg.direction_br = 0
            motor_msg.direction_bl = 0    
        self.publisher.publish(motor_msg)
    ##### 수정   


def main(args=None):
 
    rp.init(args=args)

    control_node = Control()
    try:
        rp.spin(control_node)
    except KeyboardInterrupt:
        pass
    finally:
        control_node.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()
