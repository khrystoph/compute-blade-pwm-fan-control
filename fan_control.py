#! /usr/bin/env python3
from gpiozero import PhaseEnableMotor
import time
import signal
import sys

# The Noctua PWM control actually wants 25 kHz (kilo!), see page 6 on:
# https://noctua.at/pub/media/wysiwyg/Noctua_PWM_specifications_white_paper.pdf

PWM_FREQ = 25           # [Hz] PWM frequency

FAN_PIN = 12            # BCM pin used to drive PWM fan
TACH_PIN = 13           
WAIT_TIME = 1           # [s] Time to wait between each refresh

OFF_TEMP = 40           # [°C] temperature below which to stop the fan
MIN_TEMP = 45           # [°C] temperature above which to start the fan
MAX_TEMP = 70           # [°C] temperature at which to operate at max fan speed
FAN_LOW = 1
FAN_HIGH = 100
FAN_MAX = 100
FAN_GAIN = float(FAN_HIGH - 0) / float(MAX_TEMP - MIN_TEMP)


def getCpuTemperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        return float(f.read()) / 1000


def handleFanSpeed(fan:PhaseEnableMotor, temperature:float):
    if temperature > MIN_TEMP:
        delta = min(temperature, MAX_TEMP) - MIN_TEMP
        fan.forward(FAN_LOW + delta * FAN_GAIN)
        
    elif temperature < OFF_TEMP:
        fan.stop()


try:
    signal.signal(signal.SIGTERM, lambda *args: sys.exit(0))
    fan = PhaseEnableMotor(FAN_PIN, TACH_PIN, pwm=True)
    while True:
        handleFanSpeed(fan, getCpuTemperature())
        time.sleep(WAIT_TIME)

except KeyboardInterrupt:
    exit()
