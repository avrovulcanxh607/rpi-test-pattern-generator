import RPi.GPIO as GPIO
import time
import subprocess, os
import signal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TXT_switch = 26 # pin 18
TXT_LED = 23 # pin 16
TCD_switch = 6 # pin 31
MUS_switch = 5 # pin 29

GPIO.setup(TXT_switch,GPIO.IN)
GPIO.setup(TXT_LED,GPIO.OUT)
GPIO.setup(TCD_switch,GPIO.IN)
GPIO.setup(MUS_switch,GPIO.IN)

try:

   txt = 0
   tcd = 0
   mus = 0
   while True :
      if GPIO.input(TXT_switch)==0 and txt == 0:
         string = "/home/pi/vb2" 
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         GPIO.output(TXT_LED,GPIO.HIGH)
         txt = 1
         while GPIO.input(TXT_switch)==0:
             time.sleep(0.1)
      if GPIO.input(TXT_switch)==0 and txt == 1:
         txt = 0
         string = "/home/pi/vb2s"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         GPIO.output(TXT_LED,GPIO.LOW)
         while GPIO.input(TXT_switch)==0:
             time.sleep(0.1)
      if GPIO.input(TCD_switch)==0 and tcd == 0:
         string = "sudo fbi -T 1 -noverbose /home/pi/'Test C'.bmp -a"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         tcd = 1
         while GPIO.input(TCD_switch)==0:
             time.sleep(0.1)
      if GPIO.input(TCD_switch)==0 and tcd == 1:
         string = "sudo fbi -T 1 -noverbose /home/pi/'test'.bmp -a"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         tcd = 2
         while GPIO.input(TCD_switch)==0:
             time.sleep(0.1)
      if GPIO.input(TCD_switch)==0 and tcd == 2:
         string = "sudo fbi -T 1 -noverbose /home/pi/i1.png -a"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         tcd = 0
         while GPIO.input(TCD_switch)==0:
             time.sleep(0.1)
      if GPIO.input(MUS_switch)==0 and mus == 0:
         string = "sudo /home/pi/music"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         mus = 1
         while GPIO.input(MUS_switch)==0:
             time.sleep(0.1)
      if GPIO.input(MUS_switch)==0 and mus == 1:
         string = "sudo killall music && sudo killall aplay"
         p=subprocess.Popen(string,shell=True, preexec_fn=os.setsid)
         mus = 0
         while GPIO.input(MUS_switch)==0:
             time.sleep(0.1)



except KeyboardInterrupt:
  GPIO.cleanup()
