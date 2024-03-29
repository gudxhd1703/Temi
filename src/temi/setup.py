from setuptools import find_packages
from setuptools import setup

package_name = 'temi'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','PyBluez','RPi.GPIO','adafruit_servokit'],
    zip_safe=True,
    maintainer='Kim,Park,Kwon,Choi',
    maintainer_email='gudxhd1703@gmail.com, jeongwoo5058@naver.com, kkt161@daum.net, hidan0327@naver.com',
    keywords=['ROS2'],
    description='ROS2 Variable width rc car with raspberry pi4',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor = temi.dcmotor_node:main',
            'control = temi.control_node:main',
            'ultrasonic_pub = temi.ultrasonic_node:main',
            'bluetooth= temi.bluetooth_node:main'
        ],
    },
)
