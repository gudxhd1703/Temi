import bluetooth as bt

class BluetoothCommunication:
    def __init__(self):
        self.address = "5C:CB:99:9E:7C:75"  # Replace with your device's Bluetooth address
        self.port = bt.PORT_ANY
        self.host = ""  # Optionally, enter Bluetooth controller MAC address directly
        self.uuid = "00001101-0000-1000-8000-00805F9B34FB" 
        self.server_sock = bt.BluetoothSocket(bt.RFCOMM)
        self.server_sock.bind((self.host, self.port))
        self.server_sock.listen(1)
        self.server_sock.settimeout(10)
        bt.advertise_service(
            self.server_sock, "Temi",
            service_id=self.uuid,
            service_classes=[self.uuid, bt.SERIAL_PORT_CLASS],
            profiles=[bt.SERIAL_PORT_PROFILE],
        )
        print('Waiting for connection from Android device')
        self.client_sock, self.client_info = self.server_sock.accept()
        print(f'Accepted connection from {self.client_info}')

    def receive_data(self):
        while True:
            try:
                data = self.client_sock.recv(1024)  # Adjust buffer size as needed
                try:
                    message = data.decode("utf-8")
                    print('Received:', message)
                except UnicodeDecodeError:
                    print('Received data could not be decoded as UTF-8.')
            except bt.BluetoothError:
                break

    def __del__(self):
        self.client_sock.close()
        self.server_sock.close()
        print('Closed Bluetooth connection')

def main():
    bluetooth_communication = BluetoothCommunication()
    try:
        bluetooth_communication.receive_data()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()