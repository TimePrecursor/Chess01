import emoji
import fcntl, termios, struct
import os
#from termcolor import cprint


emo = emoji.emojize
def clr():
  os.system('clear')
def terminal_size():
      th, tw, hp, wp = struct.unpack('HHHH',
          fcntl.ioctl(0, termios.TIOCGWINSZ,
          struct.pack('HHHH', 0, 0, 0, 0)))
      global width
      width = tw
      return tw, th
terminal_size()




print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print("\33[40m  ")
print("\33[7m  ")
print("\33[0m")
print


x_ = "h"
print(f"\033[20;20H{x_}")