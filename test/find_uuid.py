import bluetooth

def find_bluetooth_devices():
    devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(devices)))

    for addr, name in devices:
        print("Device Name: {}, Address: {}".format(name, addr))
        try:
            services = bluetooth.find_service(address=addr)
            for service in services:
                print(" Service Name: {}, Service ID: {}".format(service["name"], service["service-id"]))
        except Exception as e:
            print(" Could not find services for the device: ", e)

if __name__ == "__main__":
    find_bluetooth_devices()