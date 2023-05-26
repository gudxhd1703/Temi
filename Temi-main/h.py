import RPi.GPIO as GPIO
import time

# 사용할 핀 번호 설정
AIN1_PIN = 17
AIN2_PIN = 27
PWMA_PIN = 22

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 출력 핀으로 설정
GPIO.setup(AIN1_PIN, GPIO.OUT)
GPIO.setup(AIN2_PIN, GPIO.OUT)
GPIO.setup(PWMA_PIN, GPIO.OUT)

# PWM 객체 생성
pwm = GPIO.PWM(PWMA_PIN, 100)  # 주파수를 100Hz로 설정

# 모터 구동 함수
def drive_motor(speed, direction):
    # 방향 제어
    if direction == 'forward':
        GPIO.output(AIN1_PIN, GPIO.HIGH)
        GPIO.output(AIN2_PIN, GPIO.LOW)
    elif direction == 'backward':
        GPIO.output(AIN1_PIN, GPIO.LOW)
        GPIO.output(AIN2_PIN, GPIO.HIGH)
    else:
        # 예외 처리: 정의되지 않은 방향일 경우 모터 정지
        GPIO.output(AIN1_PIN, GPIO.LOW)
        GPIO.output(AIN2_PIN, GPIO.LOW)

    # 속도 제어
    pwm.start(speed)

# 모터 정지
def stop_motor():
    GPIO.output(AIN1_PIN, GPIO.LOW)
    GPIO.output(AIN2_PIN, GPIO.LOW)
    pwm.stop()

# 모터 구동 예시
try:
    drive_motor(50, 'forward')  # 50% 속도로 정방향으로 회전
    time.sleep(2)  # 2초 동안 회전

    stop_motor()  # 모터 정지
    time.sleep(1)  # 1초 동안 대기

    drive_motor(30, 'backward')  # 30% 속도로 역방향으로 회전
    time.sleep(2)  # 2초 동안 회전

    stop_motor()  # 모터 정지

except KeyboardInterrupt:
    stop_motor()  # 프로그램 종료 시 모터 정지
    GPIO.cleanup()  # GPIO 설정 해제
