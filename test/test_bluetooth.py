#sudo apt install -y bluez bluetooth libbluetooth-dev python3-pip && python3 -m pip install pybluez
#sudo apt install -y pkg-config libboost-python-dev libboost-thread-dev libglib2.0-dev python3-dev && python3 -m pip install pybluez\[ble\]
#https://wiki.loliot.net/docs/lang/python/libraries/python-pybluez/


import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = bluetooth.PORT_ANY  # RFCOMM 포트
server_sock.bind(("", port))
server_sock.listen(1)
server_sock.settimeout(10)
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
        data_decode = data.decode("utf-8")
        print("Received [%s]" % data_decode)
except OSError:
    pass
except KeyboardInterrupt :
    print("Program terminated by user")
finally:
    client_sock.close()
    server_sock.close()
    print("Disconnected.")


