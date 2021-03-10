from gpiozero import LED
from time import sleep
#      RED      YEL      GRE
s1 = [LED(21), LED(20), LED(16)]
s2 = [LED(12), LED(1), LED(7)]
s3 = [LED(8), LED(25), LED(24)]
s4 = [LED(23), LED(18), LED(15)]

def mig_LED(any1, any2):
    x = 0
    while x != 3:
        any1.on()
        any2.on()

        sleep(1)

        any1.off()
        any2.off()
    
        sleep(1)
        x += 1

def on_LED(any1, any2):
    any1.on()
    any2.on()

def off_LED(any1, any2):
    any1.off()
    any2.off()



while True:
    on_LED(s1[0], s2[0])

    on_LED(s3[2], s4[2])
    sleep(10)

    off_LED(s3[2], s4[2])

    mig_LED(s3[1],s4[1])
    on_LED(s3[0], s4[0])

    off_LED(s1[0], s2[0])
    on_LED(s1[2], s2[2])
    sleep(10)

    off_LED(s1[2], s2[2])
    mig_LED(s1[1], s2[1])
    off_LED(s3[0], s4[0])




