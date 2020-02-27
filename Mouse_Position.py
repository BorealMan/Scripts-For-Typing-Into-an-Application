from pynput.mouse import Button, Controller as mouseController

mouse = mouseController()

print('The current pointer position is {0}'.format(mouse.position))

