
#> This just shows what pixel the mouse is currently hovering over.
#> This is mostly used to assign pixels in run_me.py
#> Kill the program with ctrl-c.

#! python3
import pyautogui, time
print('Press Ctrl-C to quit.')
time.sleep(2)
try:
    while True:
        # Get and print the mouse coords
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        #! Run this section if you want the screenshot and color check
        # pixelColor = pyautogui.screenshot().getpixel((x, y))
        # positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        # positionStr += ', ' + str(pixelColor[1]).rjust(3)
        # positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
