import datetime
import peri0
from time import sleep
import time
from appJar import gui
from multiprocessing import Process

buzzer = peri0.Buzzer()
now = datetime.datetime.now()
fnd = peri0.Fnds()
clcd = peri0.CharLcd()
led = [peri0.Led(1), peri0.Led(2)]

us = peri0.UltraSonic()

def Ultrasonic():
    while True :
        try :
            n = 0
            buzzer.set_tempo(120)
            dist = us.measure_average(delay = 20 * peri0.MS)
            print(dist)
            if (dist >= 2 and dist <= 4):
                n = 100
                fnd.set_num(n)
                clud.puts("집가자")
            elif (dist >= 5 and dist <= 6):
                n = 75
                fnd.set_num(n)
                led_on_i()
                sleep(5)
                led_off_i()
                buzzer.tone(4, "SOL", 1/4)
                buzzer.tone(4, "SOL", 1/4)
            elif (dist >= 7 and dist <=10):
                n = 50
                fnd.set_num(n)
                buzzer.tone(4, "SOL", 1/4)
            elif (dist > 10 and dist <= 14):
                n = 25
                fnd.set_num(n)
                led_on_i()
                sleep(5)
                led_off_i()
                
        except KeyboardInterrupt:
            fnd.stop()
def led_on_i():      
    led[0].on()
    led[1].on()
    
def led_off_i():    
    led[0].off()
    led[1].off()
       
def time():
    while True:
        now = datetime.datetime.now()
        h = now.hour
        m = now.minute
        s = now.second
        clcd.clear()
        clcd.puts("%dh %dm %ds " % (h, m, s))
        sleep(0.5)

p1 = Process(target=time)
p2 = Process(target=Ultrasonic)

p1.start()
p2.start()
p1.join()
p2.join()