import rclpy
from rclpy.node import Node
from temi_msgs.msg import BluetoothData
import bluetooth

class BluetoothCommunicationNode(Node):
    def __init__(self):
        super().__init__('bluetooth_communication_node')
        self.publisher_ = self.create_publisher(BluetoothData, 'bluetooth_data', 10)
        self.timer_period = 0.5  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.bluetooth_address = "5C:CB:99:9E:7C:75"  # Replace with your Android's Bluetooth address
        self.port = 1  # Bluetooth port may vary device to device
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", self.port))   ##   server_sock.bind(("", bluetooth.PORT_ANY))  자동으로 포트번호 선택하게 하는 법
        self.server_sock.listen(1)
        self.get_logger().info('Waiting for connection from Android device')
        self.client_sock, self.client_info = self.server_sock.accept()
        self.get_logger().info(f'Accepted connection from {self.client_info}')

    def timer_callback(self):
        data = self.client_sock.recv(1024)  # Buffer size may vary based on your needs
        if data:
            message = data.decode("utf-8")
            self.get_logger().info('Publishing: "%s"' % message)
            msg = BluetoothData()
            msg.data = message
            self.publisher_.publish(msg)

    def __del__(self):
        self.client_sock.close()
        self.server_sock.close()
        self.get_logger().info('Closed Bluetooth connection')

def main(args=None):
    rclpy.init(args=args)
    bluetooth_communication_node = BluetoothCommunicationNode()
    rclpy.spin(bluetooth_communication_node)
    bluetooth_communication_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()