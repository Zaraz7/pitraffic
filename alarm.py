from gpiozero import LED
from time import sleep

reds = [LED(8), LED(12), LED(21), LED(23)] #, LED(20), LED(16)]

for led in reds:
    led.on()

while True:
    inp = input()
    if inp == 'e':
        break

