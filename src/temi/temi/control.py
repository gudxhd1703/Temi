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
        self.motor_data = [None]*4
        self.subscription_ultrasonic = [self.create_subscription(
            Ultrasonic,
            'ultrasonic'+str(i),
            self.ultrasonic_callback(i),
            10) for i in range(4)]
        self.subscripton_bluetooth = self.create_subscription(BluetoothData,'bluetooth_data', self.bluetooth_callback,10)
        self.motor_msg = MotorControl()

    def ultrasonic_callback(self, index):
        def callback(ultrasonic_msg):
            self.ultrasonic_data[index] = ultrasonic_msg
            self.control_logic()
        return callback
    
    def bluetooth_callback(self, bluetooth_msg):
        self.bluetooth_data = bluetooth_msg
        self.control_logic()
    
    def control_logic(self):

        # Check the ultrasonic data and adjust motor_msg accordingly
        for sensor_data in self.ultrasonic_data:
            if sensor_data is not None and sensor_data.data < 10:  # Example condition
                self.motor_msg.velocity = 0
                break

        # Check the bluetooth data and adjust motor_msg accordingly
        if self.bluetooth_data is not None:
            if self.bluetooth_data.data == 1:
                self.motor_msg.velocity += speed_change
            elif self.bluetooth_data.data == 2:
                self.motor_msg.velocity -= speed_change
            elif self.bluetooth_data.data == left:
                self.motor_msg.velocity = 0
                self.wheel_control(left)
            elif self.bluetooth_data.data == right:
                self.motor_msg.velocity = 0
                self.wheel_control(right)
            elif self.bluetooth_data.data == transformer:
                self.motor_msg.velocity = 0
                self.wheel_control(transformer)

        # Publish the motor command
        self.publisher.publish(self.motor_msg)
     
    def wheel_control(self, direction):
        if direction == left:
            self.motor_msg.direction_fr = 0
            self.motor_msg.direction_fl = 0
            self.motor_msg.direction_br = 0
            self.motor_msg.direction_bl = 0
            
        elif direction == right:   
            self.motor_msg.direction_fr = 0
            self.motor_msg.direction_fl = 0
            self.motor_msg.direction_br = 0
            self.motor_msg.direction_bl = 0    
        elif direction == transformer:
            self.motor_msg.direction_fr = 0
            self.motor_msg.direction_fl = 0
            self.motor_msg.direction_br = 0
            self.motor_msg.direction_bl = 0    
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
