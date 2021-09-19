import win32api, win32con
from pynput.mouse import Button, Controller
import time

mouse = Controller()

time.sleep(4)
print(mouse.position)
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 500, 500, 5, 0)
print(mouse.position)

# import autoit
# from pynput.mouse import Button, Controller
#
# mouse = Controller()
#
# time.sleep(3)
# print(mouse.position)
# time.sleep(1)
# autoit.mouse_move(2000,1900,5)
# time.sleep(1)
# print(mouse.position)

# mouse.move(200,200, absolute=True, duration=2)
# pydirectinput.move(300, None)
# pydirectinput.click()
# pyautogui.move(400, 200, 3)

#
#
# # Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))
#
# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))
#
# # Move pointer relative to current position
# mouse.move(50, -50)
#
# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click; this is different from pressing and releasing
# # twice on Mac OSX
# mouse.click(Button.left, 2)
#
# # Scroll two steps down
# mouse.scroll(0, 2)