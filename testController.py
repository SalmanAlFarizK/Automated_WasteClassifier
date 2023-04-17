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


def rotateServo1(i):
    board.digital[pin1].write(i)

def rotateServo2(i):
    board.digital[pin2].write(i)

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
