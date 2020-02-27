from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
import time

keyboard = keyboardController()
mouse = mouseController()


#	What you want to type
text = "+m kill corp"
#	How often you want to type (Seconds * Minutes * Hours)
secs = (60 * 23 * 1)
#In order for this to work for you, you must first find the cordinates you want to use
#Mouse Position (Bring Discord Up from task bar cords, Click on chat box cords)
#Use the Mouse_Position.py Script to find the cordinates you will need for this part.
x,y = -1358, 1067
x1,y1 = -1029, 849


def useMouse(x,y,x1,y1):

	pos = mouse.position # Storing old mouse position
	(old_x,old_y) = pos

	mouse.position = (x,y) # Click program on task bar
	mouse.press(Button.left)
	mouse.release(Button.left)

	mouse.position = (x1, y1) # Click on chatbox
	mouse.press(Button.left)
	mouse.release(Button.left)

	mouse.position = (old_x,old_y) # Moves Mouse back to original position

def Type(text):

	keyboard.type(text)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)


counter = 0
##MAIN
while(True):

	print('{}{}{}'.format("We're up and running. \nCurrently we've completed " , counter, " runs."))	

	useMouse(x, y, x1, y1)
	time.sleep(2)
	Type(text)
	time.sleep(secs)
	counter += 1

	