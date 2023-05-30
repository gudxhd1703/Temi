from setuptools import find_packages
from setuptools import setup

package_name = 'Temi'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kim',
    maintainer_email='gudxhd1703@gmail.com',
    maintainer='add',
    maintainer_email='jeongwoo5058@naver.com',
    maintainer='add',
    maintainer_email='kkt161@daum.net',
    maintainer='add',
    maintainer_email='hidan0327@naver.com',
    keywords=['ROS'],
    description='ROS2 Variable width rc car with raspberry pi4',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
