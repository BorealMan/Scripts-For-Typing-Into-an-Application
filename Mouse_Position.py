from pynput.mouse import Button, Controller as mouseController

mouse = mouseController()

print('The current pointer position is {0}'.format(mouse.position))

pos = mouse.position

(x,y) = pos

print(x)
print(y)