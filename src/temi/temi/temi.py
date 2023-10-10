import rclpy as rp
from rclpy.node import Node
import RPi.GPIO as GPIO
from time import sleep

from temi_msgs.msg import MotorControl

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 13  #33 pin

#GPIO PIN
IN1 = 19  #35 pin
IN2 = 26  #37 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)

    # 100khz 로 PWM 동작 시킴
    pwm = GPIO.PWM(EN, 100)

    # 우선 PWM 멈춤.
    pwm.start(0)
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)

    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)

    #뒤로
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    #모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
    pwmA = setPinConfig(ENA, IN1, IN2)

    if ch == 'CH1':
        setMotorContorl(pwmA, IN1, IN2, speed, stat)

class Temi(Node):

    def __init__(self):
        super().__init__('temi')
        self.publisher = self.create_publisher(MotorControl,'motorcontrol',10)
        timer_period = 0.3
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = MotorControl()
        setMotor(CH1,msg.velocity, msg.direction_fr)
        setMotor(CH1,msg.velocity, msg.direction_fl)
        setMotor(CH1,msg.velocity, msg.direction_br)
        setMotor(CH1,msg.velocity, msg.direction_bl)
     


def main(args=None):

    rp.init(args=args)

# GPIO 모드 설정
    GPIO.setmode(GPIO.BCM)
    
    temi_node = Temi()
    rp.spin(temi_node)

    temi_node.destroy_node()
    GPIO.cleaup()
    rp.shutdown()
    


if __name__ == '__main__' :
    main()
