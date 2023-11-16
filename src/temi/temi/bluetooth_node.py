import rclpy
from rclpy.node import Node
from temi_msgs.msg import BluetoothData
import bluetooth as bt

class BluetoothCommunicationNode(Node):
    def __init__(self):
        super().__init__('bluetooth_communication_node')
        self.address = "5C:CB:99:9E:7C:75"  # Replace with your Android's Bluetooth address
        self.port = 1  # Bluetooth port may vary device to device
        self.host = "" # '블루투스 컨트롤러 맥 주소'를 직접 입력해도 됨  
        # 확인후 수정   https://hybridego.net/entry/raspberry-pi-bluetoothctl-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-%EB%B8%94%EB%A3%A8%ED%88%AC%EC%8A%A4
        self.uuid = "00001101-0000-1000-8000-00805F9B34FB" 
        self.publisher_ = self.create_publisher(BluetoothData, 'bluetooth_data', 10)
        self.timer_period = 0.5  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.server_sock = bt.BluetoothSocket(bt.RFCOMM)
        self.server_sock.bind((self.host, self.port))   ##   server_sock.bind(("", bluetooth.PORT_ANY))  자동으로 포트번호 선택하게 하는 법
        self.server_sock.listen(1)
        bt.advertise_service(
            self.server_sock, "Temi",
            service_id = self.uuid,
            service_classes = [ self.uuid, bt.SERIAL_PORT_CLASS ],
            profiles = [ bt.SERIAL_PORT_PROFILE ],
        )
        self.get_logger().info('Waiting for connection from Android device')
        self.client_sock, self.client_info = self.server_sock.accept()
        self.get_logger().info(f'Accepted connection from {self.client_info}')

    def timer_callback(self):
        data = self.client_sock.recv(1024)  # Buffer size may vary based on your needs
        try:
            try:
                message = data.decode("utf-8")  ## ascii일수도 decode 안해도 될수도
                self.get_logger().info('Publishing: "%s"' % message)
                msg = BluetoothData()
                msg.data = message
            except UnboundLocalError:
                self.get_logger().error('Received data could not be decoded as UTF-8.')
            self.publisher_.publish(msg)

        except:
            pass
        
    def __del__(self):
        self.client_sock.close()
        self.server_sock.close()
        self.get_logger().info('Closed Bluetooth connection')

def main(args=None):
    rclpy.init(args=args)
    bluetooth_communication_node = BluetoothCommunicationNode()
    try:
        rclpy.spin(bluetooth_communication_node)
    except KeyboardInterrupt:
        pass
    finally:   
        bluetooth_communication_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
