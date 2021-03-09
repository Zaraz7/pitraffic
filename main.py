# import raspberry pi GPIO module
import RPi.GPIO as GP
from time import sleep

# setup pin 3 as output
ls = [3, 5, 7, 11, 13, 15]

for i in ls:
    GP.setup(i, GP.OUT)


# setup pin 3 as pulse width modulation output
# frequency = 2 hz (2 times per second)
#pwm = GP.PWM(5, 2)


while True:
        print('ON =', ls[0], ls[3])
        GP.output(ls[0], GP.HIGH)
        GP.output(ls[3], GP.HIGH)
        sleep(6)
        GP.output(ls[0], GP.LOW)
        GP.output(ls[3], GP.LOW)
        print('OFF =', ls[0], ls[3])
        print('ON =', ls[1], ls[4])
        GP.output(ls[1], GP.HIGH)
        GP.output(ls[4], GP.HIGH)
        sleep(3)
        GP.output(ls[1], GP.LOW)
        GP.output(ls[4], GP.LOW)
        print('OFF =', ls[1], ls[4])
        ls.reverse()

GP.cleanup()