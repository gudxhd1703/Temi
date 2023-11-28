import time
import busio
from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

import RPi.GPIO as GPIO
from time import sleep
import bluetooth

#DC모터
#모터 상태
STOP  = 0
FORWARD  = 1
BACKWORD = 2

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
ENB = 12  #32 pin
#GPIO PIN
IN1 = 19  #35 pin
IN2 = 26  #37 pin
IN3 = 5
IN4 = 6

# 핀 설정 함수
def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)

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
    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)

    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)
        
# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)
        
# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)
#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

#서보모터
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50
servo0 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
servo1 = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)
servo2 = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2500)
servo3 = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2500)
servo4 = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2500)
def rotate_servo(servo_motor, angle):
    servo_motor.angle = angle

angle = 108
center_angle = 15

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
            client_sock.send("1: 서보모터, 2: dc모터")
            data = client_sock.recv(1024)
            bluetooth_input = int(data)
            
            match bluetooth_input:  #1서보모터 2dc모터
                case 1: #서보모터
                    client_sock.send("1: 크랩워크, 2:폭변환")
                    data = client_sock.recv(1024)
                    bluetooth_input = int(data)
                    match bluetooth_input: #1크랩워크 2폭변환
                        case 1:   #크랩워크
                            client_sock.send("크랩워크를 위해 서보모터를 몇도로 돌릴까요? (추천 108도): ")
                            data = client_sock.recv(1024)
                            servo_angle_input = int(data)
                            
                            rotate_servo(servo0, servo_angle_input)
                            rotate_servo(servo1, servo_angle_input)
                            rotate_servo(servo2, servo_angle_input)
                            rotate_servo(servo3, servo_angle_input)
                            rotate_servo(servo4, center_angle)
                            
                        case 2:  #폭변환
                            client_sock.send("폭변환을 위해 서보모터를 몇도로 돌릴까요? (추천 108도): ")
                            data = client_sock.recv(1024)
                            servo_angle_input = int(data)
                            
                            rotate_servo(servo0,180- servo_angle_input)
                            rotate_servo(servo1,servo_angle_input)
                            rotate_servo(servo2,180- servo_angle_input)
                            rotate_servo(servo3, servo_angle_input)
                            rotate_servo(servo4, center_angle)
                    
                case 2:  #dc모터 # 1: front, 2: back
                    client_sock.send("얼마나 빠르게 돌까요? 추천(50): " )
                    data = client_sock.recv(1024)
                    dc_speed_input = int(data)
                    
                    setMotor(CH1, dc_speed_input, 2)
                    setMotor(CH2, dc_speed_input, 1)
                    client_sock.send("dc모터를 끄려면 아무거나 누르세요")
                    data = client_sock.recv(1024)
                    setMotor(CH1, 0, 2)
                    setMotor(CH2, 0, 1)
                case _:
                    continue

except KeyboardInterrupt:
    print('exit')
    
finally:
    pca.deinit()
    GPIO.cleanup()
    client_sock.close()
    server_sock.close()
    
    
