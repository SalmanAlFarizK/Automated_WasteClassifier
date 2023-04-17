from pyfirmata import Arduino,SERVO
from time import sleep
import threading

com_port='COM4'
pin1 = 9
pin2 = 10


board=Arduino(com_port)

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
flag = 0


def rotateServo(pin):
    c_pin = None
    if pin == 1:
        c_pin = pin1
    elif pin == 2:
        c_pin = pin2
    else:
        return

    for i in range(0, 180):
        board.digital[c_pin].write(i)
        sleep(.0000001)
    sleep(.01)
    for i in range(180, 1, -1):
        board.digital[c_pin].write(i)
        sleep(.0000001)
    return

# def rotateServo(pin, i):
#     board.digital[pin].write(i)

# while True:
#     flag = int(input("enter a value"))
#     if flag==1:
#         for i in range(0,180):
#             rotateServo(pin1,i)
#         for i in range(180,1,-1):
#             rotateServo(pin1,i)
#     if flag==2:
#         for i in range(0,180):
#             rotateServo(pin2,i)
#         for i in range(180,1,-1):
#             rotateServo(pin2,i)
#     else:
#         rotateServo(pin1, 0)
#         rotateServo(pin2, 0)
