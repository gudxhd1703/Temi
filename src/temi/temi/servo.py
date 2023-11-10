import rclpy as rp
from rclpy.node import Node
from temi_pkg_msg.msg import Servo #for ros2

from adafruit_servokit import ServoKit #for motor_driver

class servo_load(Node):

    def __init__(self,msg):
        super().__init__('servo_load')
        self.servo_kit = ServoKit(channels=16)
        self.servo_kit.frequency = 50
        self.pub_servo = self.create_publisher(Servo,"servo_ang",10) #토픽 이름 "servo_ang"
        self.timer = self.create.timer(1,servo_load) #타이머는 별도의 스레드로 ang_set_keyboard에 영향을 주지 않음
        
        self.servo_kit.servo[0].set_pulsewidth_range(500, 2500)
        self.servo_kit.servo[0].channel = 1
        self.servo_kit.servo[1].set_pulsewidth_range(500, 2500)
        self.servo_kit.servo[1].channel = 7
        self.servo_kit.servo[2].set_pulsewidth_range(500, 2500)
        self.servo_kit.servo[2].channel = 8
        self.servo_kit.servo[3].set_pulsewidth_range(500, 2500)
        self.servo_kit.servo[3].channel = 25
        
        msg.left_top = self.servo_kit.servo[0].angle        #제로리턴을 하지 않으므로 메세지를 최신화
        msg.right_top = self.servo_kit.servo[1].angle
        msg.left_bottom = self.servo_kit.servo[2].angle
        msg.right_bottom = self.servo_kit.servo[3].angle
        
    def servo_load(self,msg):
        
        self.servo_kit.servo[0].angle = msg.left_top    #메세지와 서보모터 내부변수의 최신화
                                                        #두번하는이유는 아래에서 키보드를 이용해서 바꿀수도 있지만, 외부에서 바뀔 가능성도 있기 때문
        self.servo_kit.servo[1].angle = msg.right_top
        self.servo_kit.servo[2].angle = msg.left_bottom
        self.servo_kit.servo[3].angle = msg.right_bottom
        
        self.servo_kit.update()                     #실제로는 이때 모터가 돌아감
        
        print("왼쪽위 : ",self.servo_kit.servo[0].angle,"오른쪽위 : ",self.servo_kit.servo[1].angle)    #유저를 위한 에코
        print("왼쪽아래 : ",self.servo_kit.servo[2].angle,"오른쪽아래 : ",self.servo_kit.servo[3].angle)
        
        
    def ang_set_keyboard(self,msg): #각도 조정용 함수 키보드에서 qw(왼쪽상) er(오른쪽상)
                                    #                      as(왼쪽하) df(오른쪽하)를 사용해서 4바퀴 각각 적당한 각도를 찾기 위함
        while 1:
            input = input("Enter to set angle : ")
            if input == "q" or "w":
                if input == "q":
                    self.servo_kit.servo[0].angle += 1                  #각도는 동경 기준 (왼쪽이 + ,오른쪽이 -)
                    msg.left_top = self.servo_kit.servo[0].angle
                else:
                    self.servo_kit.servo[0].angle -= 1
                    msg.left_top = self.servo_kit.servo[0].angle
            
            if input == "e" or "r":
                if input == "e":
                    self.servo_kit.servo[1].angle += 1
                    msg.right_top = self.servo_kit.servo[1].angle
                else:
                    self.servo_kit.servo[1].angle -= 1
                    msg.right_top = self.servo_kit.servo[1].angle
                    
            if input == "a" or "s":
                if input == "a":
                    self.servo_kit.servo[2].angle += 1
                    msg.left_bottom = self.servo_kit.servo[2].angle
                else:
                    self.servo_kit.servo[2].angle -= 1
                    msg.left_bottom = self.servo_kit.servo[2].angle
                    
            if input == "d" or "f":
                if input == "d":
                    self.servo_kit.servo[3].angle += 1
                    msg.right_bottom = self.servo_kit.servo[3].angle
                else:
                    self.servo_kit.servo[3].angle -= 1
                    msg.right_bottom = self.servo_kit.servo[3].angle

                    
                    
def main(args=None):
    rp.init(args=args)          #대충 킨다는 내용
    node = servo_load(Servo)
    rp.spin(node)
    node.destroy_node()
    
if __name__ == '__main__':
    main()
