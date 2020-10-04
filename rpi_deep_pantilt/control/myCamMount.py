import Adafruit_PCA9685
import time
global pwm

pwmHz = 50

if pwmHz == 50:
    print("Servos running on 50 Hz")
    # pan settings
    convertTominRangePan = 90
    convertTomaxRangePan = -90
    originalMinPan = 500
    originalMaxPan = 250
    # tilt settings
    convertTominRangeTilt = 90
    convertTomaxRangeTilt = -90
    originalMinTilt = 270
    originalMaxTilt = 550

# Run sudo i2cdetect -y 1 to view your detected i2c addresses.

pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(pwmHz)

def translate(toPosition, convertTominRange, convertTomaxRange, originalMin, originalMax):
    leftSpan = convertTomaxRange - convertTominRange
    rightSpan = originalMax - originalMin
    valueScaled = float(toPosition - convertTominRange) / float(leftSpan)
    return int(originalMin + (valueScaled * rightSpan))

def moveToPosition(channel, position, panOrTilt):
    if panOrTilt == "pan":
        pwm.set_pwm(channel, 0, translate(position, convertTominRangePan, convertTomaxRangePan, originalMinPan, originalMaxPan))
    if panOrTilt == "tilt":
        pwm.set_pwm(channel, 0, translate(position, convertTominRangeTilt, convertTomaxRangeTilt, originalMinTilt, originalMaxTilt))

def resetServo(channel):
    pwm.set_pwm(channel, 0, 0)