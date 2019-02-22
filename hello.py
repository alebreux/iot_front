from flask import Flask
import subprocess
import RPi.GPIO as GPIO
from time import sleep
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World !"


@app.route('/lumiere/allume/<int:valeurlum>')
def lumiereAllume(valeurlum):
    pin=0
    print(valeurlum)
    if valeurlum==1:
        pin=5
    elif valeurlum==2:
        pin=6
    elif valeurlum==3:
        pin=13
    if pin!=0:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

        GPIO.output(pin, GPIO.HIGH)
        time.sleep(5)

        GPIO.output(pin, GPIO.LOW)

        GPIO.cleanup()
    print(valeurlum, pin)
    return 'True %s' % pin


@app.route('/lumiere/eteint/<int:valeurlum>')
def lumiereEteint(valeurlum):
    return 'False %s' % valeurlum


@app.route('/volet/ouvre/<int:valeurVolet>')
def voletOuvre(valeurVolet):
    GPIO.setmode(GPIO.BCM)
    Motor1A = 23
    Motor1B = 24
    Motor1E = 25

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    print("Turning motor on")

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

    sleep(5)
    print("stopping motor")
    GPIO.output(Motor1E,GPIO.LOW)

    GPIO.cleanup()
    return 'True %s' % valeurVolet


@app.route('/volet/ferme/<int:valeurVolet>')
def voletFerme(valeurVolet):
    GPIO.setmode(GPIO.BCM)
    Motor1A = 23
    Motor1B = 24
    Motor1E = 25

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    print("Turning motor on")

    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

    sleep(5)
    print("stopping motor")
    GPIO.output(Motor1E,GPIO.LOW)

    GPIO.cleanup()
    return 'False %s' % valeurVolet
