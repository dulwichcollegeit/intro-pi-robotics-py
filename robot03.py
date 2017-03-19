import RPi.GPIO as GPIO 
import time 

# Set the GPIO modes 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
# Set variables for the GPIO motor pins 
pinMotorAForwards = 9 
pinMotorABackwards = 10 
pinMotorBForwards = 7
pinMotorBBackwards = 8 

pinLineSensor = 25

# How many times to turn the pin on and off each second 
Frequency = 20 
# How long the pin stays on each cycle, as a percent 
DutyCycleA = 30 
DutyCycleB = 30 
# Setting the duty cycle to 0 means the motors will not turn 
Stop = 0 
# Set the GPIO Pin mode to be Output 
GPIO.setup(pinMotorAForwards, GPIO.OUT) 
GPIO.setup(pinMotorABackwards, GPIO.OUT) 
GPIO.setup(pinMotorBForwards, GPIO.OUT) 
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

GPIO.setup(pinLineSensor, GPIO.IN)

# Set the GPIO to software PWM at 'Frequency' Hertz 
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency) 
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency) 
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency) 
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
# Start the software PWM with a duty cycle of 0 (i.e. not moving) 
pwmMotorAForwards.start(Stop) 
pwmMotorABackwards.start(Stop) 
pwmMotorBForwards.start(Stop) 
pwmMotorBBackwards.start(Stop) 
# Turn all motors off 
def StopMotors(): 
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop) 
# Turn both motors forwards 
def Forwards(): 
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop)
# Turn both motors backwards 
def Backwards(): 
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB) 
# Turn left 
def Left(): 
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop) 
# Turn Right 
def Right(): 
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
# Detect Line
def IsOverBlack():
    if GPIO.input(pinLineSensor) == 0:
        return False
    else:
        return True

# Your code to control the robot goes below this line 
try:
    while True:
        if not IsOverBlack():
            Forwards()
        else:
            StopMotors()
            Right()
            time.sleep(0.2)
            StopMotors()


except KeyboardInterrupt:
    GPIO.cleanup()
