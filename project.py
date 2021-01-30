import serial                                      # add Serial library for serial communication
import pyautogui
# add pyautogui library for programmatically controlling the mouse and keyboard.
import codecs
Arduino_Serial = serial.Serial('com5',9600)       # Initialize serial and Create Serial port object called Arduino_Serial
 
while 1:
    incoming_data = Arduino_Serial.readline() # read the serial data and print it as line
    data = str(codecs.decode(incoming_data))                   # print the incoming Serial data
    print(data)
    
    if 'Rewind' in data:                    # if incoming data is 'next'
        pyautogui.hotkey('pgdn')           # perform "ctrl+pgdn" operation which moves to the next tab
        
    if 'Forward' in data:                # if incoming data is 'previous'
        pyautogui.hotkey('pgup')           # perform "ctrl+pgup" operation which moves to the previous tab

    if 'vdown' in data:                    # if incoming data is 'down'
        pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        #pyautogui.scroll(-100) 
         
    if 'vup' in data:                      # if incoming data is 'up'
        pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        #pyautogui.scroll(100)
        
    if 'change' in data:                  # if incoming data is 'change'
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
    data = "";                            # clears the data
