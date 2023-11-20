import time
import Adafruit_PCA9685

# SG92R를 컨트롤하기 위한 클래스
class SG90_92R_Class:
    # mPin : GPIO Number (PWM)
    # mPwm : PWM컨트롤러용 인스턴스
    # m_Zero_offset_duty

    def __init__(self, Channel, ZeroOffset):
        self.mChannel = Channel
        self.m_ZeroOffset = ZeroOffset

        # Adafruit_PCA9685 초기화
        # address : PCA9685의 I2C Channel 0x40
        self.mPwm = Adafruit_PCA9685.PCA9685(address = 0x40)
        # 50Hz로 설정하셔야 하지만 60Hz로 하시는게 좀더 좋습니다.
        self.mPwm.set_pwm_freq(60)

    # 서보모터 위치 설정
    def SetPos(self, pos):
        pulse = (512 - 102) * pos / 180 + 102 + self.m_ZeroOffset
        self.mPwm.set_pwm(self.mChannel, 0, int(pulse))
    # 종료처리
    def Cleanup(self):
        # 서보모터를 90도로 재설정
        time.sleep(1)


# 여기가 시작하는 메인 입니다.
if __name__ == '__main__':
    Servo_1 = SG90_92R_Class(Channel = 4, ZeroOffset = -10)
    Servo_2 = SG90_92R_Class(Channel = 5, ZeroOffset = -10)
    Servo_3 = SG90_92R_Class(Channel = 6, ZeroOffset = -10)
    Servo_4 = SG90_92R_Class(Channel = 7, ZeroOffset = -10)

    
    try:
        while True:
#            angle = 100
            angle = int(input('angle:' ))
#            Servo_1.SetPos(angle)
#            Servo_2.SetPos(angle)
#            Servo_3.SetPos(angle)
            Servo_4.SetPos(angle)
#           Servo.SetPos(45)
#            time.sleep(25)
#            Servo.SetPos(30)
#           time.sleep(5)
#           servo.SetPos(90)

    # Ctrl + C키를 누르면 종료 됩니다.
    except KeyboardInterrupt:
        print("Ctrl + C")

    except Exception as e:
        print(str(e))

    finally:
        Servo_1.Cleanup()
        Servo_2.Cleanup()
        Servo_3.Cleanup()
        Servo_4.Cleanup()
        print("exit program")
