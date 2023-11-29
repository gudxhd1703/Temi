import rclpy
from rclpy.node import Node
import threading

class MultiThreadedNode(Node):
    def __init__(self):
        super().__init__('multi_threaded_node')
        # Initialize threads for each node
        self.dc_motor_thread = threading.Thread(target=self.run_dc_motor_node)
        self.servo_thread = threading.Thread(target=self.run_servo_node)
        self.bluetooth_thread = threading.Thread(target=self.run_bluetooth_node)
        self.ultrasonic_thread = threading.Thread(target=self.run_ultrasonic_node)

        # Start threads
        self.dc_motor_thread.start()
        self.servo_thread.start()
        self.bluetooth_thread.start()
        self.ultrasonic_thread.start()

    def run_dc_motor_node(self):
        # Import and run the DC motor node logic
        import dc_motor_node
        dc_motor_node.main()

    def run_servo_node(self):
        # Import and run the servo node logic
        import servo_node
        servo_node.main()

    def run_bluetooth_node(self):
        # Import and run the Bluetooth node logic
        import bluetooth_node
        bluetooth_node.main()

    def run_ultrasonic_node(self):
        # Import and run the ultrasonic node logic
        import ultrasonic_node
        ultrasonic_node.main()

def main(args=None):
    rclpy.init(args=args)
    multi_threaded_node = MultiThreadedNode()
    rclpy.spin(multi_threaded_node)

    # Shutdown threads
    multi_threaded_node.dc_motor_thread.join()
    multi_threaded_node.servo_thread.join()
    multi_threaded_node.bluetooth_thread.join()
    multi_threaded_node.ultrasonic_thread.join()

    multi_threaded_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

