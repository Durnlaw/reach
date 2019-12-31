import pyautogui as pya, time, pyperclip


#> When operating in Reach with the objective of finding an individual, noting that they signed a petition,
#> and then noting which petition they signed, use this program. The correct screen to run the program on
#> follows after clicking on an individual's name specifically.

#> The program will account for a person being entered in on a different petition and will not save their
#> file with the new data.

#! NOTE: The program was set up for a 3440x1440 monitor, the layout will need to be adjusted for others

#! This program runs in about 4 seconds. It has been slowed down on
#! purpose to make sure it doesn't outrun the browser.

#? User input could be added here if wanted.
pg_nmbr = '77'

#. Tab selection
pya.click(3137, -14)

#. Click inside the page and scroll down
pya.click(2951, 227)
pya.scroll(-20000)
time.sleep(.5)

# #. Yes button
pya.click(3338, 1079)
time.sleep(.25)

#> New plan. We enter the current number, and if it's not = then we 
#> delete that again and not save the page.
#. Click into the page number field
pya.click(2771, 1176)
time.sleep(.25)
pya.typewrite(pg_nmbr)
time.sleep(.25)

#! YOU NEED TO CHECK IF SOMETHING IS ALREADY HERE. IF STATEMENT NEEDED.
#. Build a function that sets up the copy paste
def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

#. double clicks on a position of the cursor
#// pya.doubleClick(pya.position())
pya.doubleClick(2771, 1176)

#. Create a variable to bring in the copied value
chk = copy_clipboard()

#. If the variable = the page number we made, then save and back out. If not, then 
#. don't save and back out. They were already entered.
if chk == pg_nmbr:
    #. Save button
    pya.click(3388, 111)
    time.sleep(1.2)
    pya.typewrite(['backspace'])
    time.sleep(.25)
    pya.typewrite(['backspace'])
    time.sleep(.25)
    pya.typewrite(['Tab', 'Tab', 'Tab'])
else:
    #. Anywhere not in a typing field
    pya.click(2629, 1087)
    time.sleep(2)
    pya.typewrite(['backspace'])
    time.sleep(.25)
    pya.typewrite(['backspace'])
    pya.click(2944, 588)
    time.sleep(.5)
    pya.click(2752, 588)
    time.sleep(.5)
    pya.typewrite(['Tab', 'Tab', 'Tab'])
