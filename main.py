import time 
import os 
import sys

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"

bold = '\033[1m'
end = '\033[0m'

def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.2)


typewriter(bold + 'Travis: Hi John Hancock \n')
time.sleep(2)

typewriter(bold + 'John Hancock: Hi \n')
time.sleep(2)

typewriter(bold  + 'Travis: Oh hi John Matt! \n')
time.sleep(2)

typewriter(bold + 'John Matt: You idiot untie me!!! \n')
time.sleep(2)

typewriter(bold + 'John Hancock: Shut up! Were gonna make you talk, Programmer come here. \n')
time.sleep(2)

typewriter(bold +"Programer: what's up? \n")
time.sleep(2)

typewriter(bold +'John Hancock: You idiot I told you a biliion times! Get the X2G54 pro. \n')
time.sleep(2)

typewriter(bold + 'Programmer: Ok. Oof, why is this so heavy? \n')
time.sleep(2)

typewriter(bold + 'Travis: whoah hold up, whats with the Massive gadget? \n')
time.sleep(2)

typewriter(bold + 'John Hancock: You\'ll see \n')
time.sleep(2)

typewriter(bold + 'Travis: wait, what? \n')
time.sleep(2)

typewriter(bold + 'John Hancock: Shut up and watch. Programmer start the machine \n')
time.sleep(2)

typewriter(bold + 'Programmer: Yes sir! \n')
time.sleep(2)

typewriter(bold + 'John Matt: You tratior! \n')
time.sleep(2)

typewriter(bold + 'Travis: *Hits John Matt in the face \n')
time.sleep(2)

typewriter(bold + 'Travis: If you say something to Programmer like that again, it will be worse! \n')
time.sleep(2)

typewriter(bold + 'Programmer: please\n')
time.sleep(2)
q1 = input('What will programmer do, turn on the machine, or help John Matt? ')
typewriter(cyan + 'Tsunami:I wil be back...*disapears :/ \n')
time.sleep(2)

print(white)
