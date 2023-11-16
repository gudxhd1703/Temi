#pip3 install adafruit-circuitpython-servokit

from adafruit_servokit import ServoKit #for motor_driver
import time

servo_kit = ServoKit(channels=16)
servo_kit.frequency = 50

servo_kit.servo[0].set_pulsewidth_range(500, 2500)
servo_kit.servo[0].channel = 1
servo_kit.servo[1].set_pulsewidth_range(500, 2500)
servo_kit.servo[1].channel = 7
servo_kit.servo[2].set_pulsewidth_range(500, 2500)
servo_kit.servo[2].channel = 8
servo_kit.servo[3].set_pulsewidth_range(500, 2500)
servo_kit.servo[3].channel = 25
        
while 1:  
    servo_kit.update()                     #실제로는 이때 모터가 돌아감
        
    print("왼쪽위 : ",servo_kit.servo[0].angle,"오른쪽위 : ",servo_kit.servo[1].angle)    #유저를 위한 에코
    print("왼쪽아래 : ",servo_kit.servo[2].angle,"오른쪽아래 : ",servo_kit.servo[3].angle)
        
 #각도 조정용 함수 키보드에서 qw(왼쪽상) er(오른쪽상)
#                      as(왼쪽하) df(오른쪽하)를 사용해서 4바퀴 각각 적당한 각도를 찾기 위함

    input = input("Enter to set angle : ")
    if input == "q" or "w":
        if input == "q":
            servo_kit.servo[0].angle += 1                  #각도는 동경 기준 (왼쪽이 + ,오른쪽이 -)
        else:
            servo_kit.servo[0].angle -= 1
            
    if input == "e" or "r":
        if input == "e":
            servo_kit.servo[1].angle += 1
        else:
            servo_kit.servo[1].angle -= 1
                    
    if input == "a" or "s":
        if input == "a":
            servo_kit.servo[2].angle += 1
        else:
            servo_kit.servo[2].angle -= 1
                    
    if input == "d" or "f":
        if input == "d":
            servo_kit.servo[3].angle += 1
        else:
            servo_kit.servo[3].angle -= 1
    time.sleep(0.5)

