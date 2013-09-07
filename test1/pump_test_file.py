#!python
import code
import Leap, sys
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import serial
import time
arduino = serial.Serial('/dev/cu.usbmodem1411', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
# arduino.open()
arduino.isOpen()
print("initialising")

userInput = raw_input("Enter code: ").upper()
print(userInput)
while True:
    if userInput == 'U':
       print('pump now flooding')
       arduino.write("U\n") # turns ONE MOTOR ON
       print "yoda"
       break

    elif userInput == 'D':
       print('pump now draining')
       arduino.write('D\n') # turns TWO MOTORS ON
       break

    else:
       print('pumps now off')
       arduino.write('N\n') # turns ALL OFF

       print "booo"
       break

# # STEPS

# # 1 RUN PROGRAMME, CHECK IF STATEMENT WORKS, TYPE 'ON', 'OFF'

# # 2 UNCOMMENT CONNECT AND CONFIRM ARDUINO SECTIONS

# # 3 UNCOMMENT arduino.write lines in if and else sections

# # 4 YOU CAN ALTER TIME MOTOR RUNS IN THE time.sleep(x) line

# # IMPORTS REQUIRED FOR LEAP/ARDUINO INTEGRATION
# import Leap, sys
# from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
# import serial
# import time

# # # CONNECT TO ARDUINO
# # arduino = serial.Serial('/dev/cu.usbmodem1421', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)

# # # CONFIRM ARDUINO AVAILABLE
# # # arduino.open() //arduino already open, not required in our case
# # arduino.isOpen()
# # time.sleep(5) # waiting the initialization...
# # print("initialising")


# # GET USER INPUT
# userInput = raw_input("Please enter 'ON' to turn motor on: ").lower()
# # print(userInput)

# # ACT ON USER INPUT
# # while True:
# if userInput == 'on':
#   print('pump now on')
#   time.sleep(20)
#   # arduino.write("Y\n") # turns ONE MOTOR ON
#   # break
# else:
#   print('pump will remain off')
#   time.sleep(3)
#   # arduino.write('N\n') # turns ALL OFF

# # PROGRAMME CONTROL
# # def main():

# # if __name__ == "__main__":
# #   main()