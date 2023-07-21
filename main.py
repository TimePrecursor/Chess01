import emoji
import fcntl, termios, struct
import os
import time
#import sys
ue1 = "\u001b[40m"
ue2 = "\u001b[47;1m "

def slep1():
  time.sleep(1)
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
clr1 = ""
clr2 = ""
#clr3 = u"\33[40m  \33[7m  \33[40m  \33[7m  \33[40m  \33[7m  \33[40m  \33[7m  "
rownumber = 0
columletter = 0
columletter1 = " "
alphabet = ["A", "B", "C", "D", 'E', 'F', 'G', 'H']


rownumber1 = 0
my_string = []
my_string2 = []
#def maker1():
columbletterlocation = int(-1)
global columbnumber
columbnumber = 0.00


for x in range(4):
  columbletterlocation = int(-1)
  columbnumber = 0.00
  rownumber1 = rownumber1 + 1
  for x in range(4):
    columbnumber =+ 0.02
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append((f"\u001b[40m {columbnumber3}{rownumber1}"))
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append(f"\u001b[47;1m {columbnumber3}{rownumber1}")
  my_string.append("")
  print(*my_string)
  columbletterlocation = -1
  my_string.clear()
  
  columbnumber = 0
  for x in range(4):
    columbnumber =+ 0.02
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append(("\u001b[40m   "))
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append("\u001b[47;1m   ")
  my_string.append("")
  print(*my_string)
  columbletterlocation = -1
  my_string.clear()
  rownumber1 = rownumber1 + 1
  columbnumber = 0
  for x in range(4):
    ez =+ 0.25
    columbnumber =+ float(0.25)
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append(f"\u001b[47;1m {columbnumber3}{rownumber1}")
    #my_string.append(u"\u001b[47;1m")
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append((f"\u001b[40m {columbnumber3}{rownumber1}"))
  my_string.append("")
  print(*my_string)
  columbletterlocation = -1
  my_string.clear()
  columbnumber = 0
  for x in range(4):
    ez =+ 0.25
    columbnumber =+ float(0.25)
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append("\u001b[47;1m   ")
    #my_string.append(u"\u001b[47;1m")
    columbletterlocation = int(columbletterlocation+1)
    columbnumber3 = str(alphabet[int(columbletterlocation)])
    my_string.append(("\u001b[40m   "))
  my_string.append("")
  print(*my_string)
  my_string.clear()
print("\n")
#maker1()
print("\n")


