import bluetooth
import rclpy as rp
import rclpy.node as Node
from temi_msgs.msg import BluetoothData

class BluetoothNode(Node):

    def __init__(self):
        super().__init__('bluetooth_node')
        self.publisher = self.create_publisher(BluetoothData, 'bluetooth_data', 10)
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]
        bluetooth.advertise_service(self.server_sock, "SampleServer", service_id=bluetooth.SERVICE_ID, service_classes=[bluetooth.SERVICE_ID, bluetooth.SERIAL_PORT_CLASS], profiles=[bluetooth.SERIAL_PORT_PROFILE])
        print("Waiting for connection on RFCOMM channel %d" % self.port)
        self.client_sock, self.client_info = self.server_sock.accept()
        print("Accepted connection from ", self.client_info)
        timer_period = 0.02
        self.bluetooth_timer = self.create_timer(timer_period, self. bluetooth_callback)

    def bluetooth_callback(self):
        try:
            data = self.client_sock.recv(1024)
            if len(data) == 0: break
            print("received [%s]" % data)
            msg = BluetoothData()
            # TODO: Parse the received data and populate the msg fields
            self.publisher.publish(msg)
        except IOError:
            pass

    def shutdown(self):
        self.client_sock.close()
        self.server_sock.close()
        print("Disconnected")

def main(args=None):
    rp.init(args=args)
    bluetooth_node = BluetoothNode()
    rp.spin(bluetooth_node)
    bluetooth_node.shutdown()
    rp.shutdown()

if __name__ == '__main__':
    main()