import rclpy
from rclpy.node import Node
from temi.msg import Ultrasonic


class UltrasonicSubscriber(Node):

    def __init__(self):
         super().__init__('ultrasonic_subscriber')
         # 4개의 토픽 구독 (각각의 초음파 센서에 대응)
         self.subscription = [self.create_subscription(
            Ultrasonic,
            'ultrasonic'+str(i),
            self.listener_callback,
            10) for i in range(4)]
         self.subscription

    def listener_callback(self, msg):
        distance = msg.data
        # 거리가 10cm 미만이면 경고 메시지 출력 
        if distance < 10.0: 
             print('Warning: Object is too close! Distance:', distance, 'cm')


def main(args=None):
    rclpy.init(args=args)

    ultrasonic_subscriber = UltrasonicSubscriber()

    rclpy.spin(ultrasonic_subscriber)


if __name__ == '__main__':
     main()

