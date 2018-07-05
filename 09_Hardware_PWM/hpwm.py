import pigpio

pi1 = pigpio.pi()
pi1.write(12,1) # enable soll high
pi1.hardware_PWM(6, 800, 250000) # 800Hz 25% dutycycle


