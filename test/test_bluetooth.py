import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 1  # RFCOMM 포트
server_sock.bind(("", port))
server_sock.listen(1)

bluetooth.advertise_service(server_sock, "SampleServer",
                            service_id="00001101-0000-1000-8000-00805F9B34FB",
                            service_classes=["00001101-0000-1000-8000-00805F9B34FB"],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE])

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print("Received [%s]" % data)
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()

