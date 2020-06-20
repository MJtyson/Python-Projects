#!/usr/bin/env python
# coding: utf-8

# In[24]:


import PySimpleGUI as sg
import webbrowser as wb
from datetime import *

sg.theme('GreenMono') 
sg.ChangeLookAndFeel('GreenMono')

layout = [[sg.Text('Persistent window')],
          [sg.Text('Value A'),sg.InputText(key='-IN-'),sg.Text('Value A'),sg.InputText(key='-IN2-')],
          [sg.Button('Read'), sg.Exit()],
         [sg.Text('Enter Url'),sg.InputText(key='-URL-'),sg.Button('open')]]   

date_ = datetime.now()
now_ = date_.split(' ')
window = sg.Window('Window that stays open', layout, now_[0]) 

event, values = window.read()

text_input, text2 = values['-IN-'], values['-IN2-']
sg.popup('You entered', text_input, text2)

url = values['-URL-']
wb.open(url)
window.close()


# In[19]:


print(date_.split(' '))


# In[24]:


sg.theme('GreenMono')


# In[11]:


dir(sg)


# In[12]:


import PySimpleGUI as sg
sg.theme('DarkBlue')

win_W = 300
win_H = 300
filename = None
startup = True

#file funtions
file_new = 'New   (CTRL+N)'
file_open = 'Open (CTRL+O)'
file_save = 'Save (CTRL+S)'


FileMenu =[['File',[file_new, file_open, file_save, 'Save As', 'Exit  (Alt+F4)']],
                  ['Tools', ['Word count']],
                  ['Help', ['About']]]

layout = [[sg.Menu(FileMenu)],
          [sg.Text('>New File<', font=('Arial', '12'), size=(win_W, 1), key='-INFO-')],
          [sg.Multiline(font=('Arial', '12'), size=(win_W, win_H), key='-BODY-')]]
          
window = sg.Window('NotePad', layout=layout, margins = (0,0), resizable = True,return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['-BODY-'].expand(expand_x =True, expand_y=True)

        
def new_file() -> str:
    window['-BODY-'].update(value='')
    window['-INFO-'].update(value = '> New File <')
    filename = None
    return filename

def open_file() ->str:
    try:
        filename: str = sg.popup_get_file('Open', no_window = True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename,tuple):
        with (filename, 'r') as f:
            window['-BODY-'].update(value=f.read())
        window['-INFO-'].update(value=filename)
    return filename
    
def savefile(filename: str):
    if filename not in (None, ''):
        with (filename, 'w') as f:
            f.write(values.get('-BODY-'))
        window['-INFO-'].update(value=filename)
    else:
        save_file_as()
    
def save_file_as() ->str:
    try:
        filename: str = sg.popup_get_file('Save File',save_as = True, no_window = True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename,tuple):
        with (filename, 'w') as f:
            f.write(values.get('-BODY-'))
        window['-INFO-'].update(value=filename)
    return filename
    
    
def word_count():
    words = [w for w in values['-BODY-'].split(' ') if w != '\n']
    word_count_ = len(words)
    sg.PopupQuick('word count:{:,d}'.format(word_count_), auto_close = True)
    
def about_me():
    sg.PopupQuick('ALL aboutthe programming', auto_close = False)
   
while True:
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    
    if event in (file_new, 'n:78'):
        filename = new_file()
    
    if event in (file_open, 'o:79'):
        filename  = open_file()
    
    if event in (file_save, 's:83'):
        savefile(filename)
          
    if event in ('Save As',):
        filename = save_file_as()
        
    if event in ('Word count',):
        word_count()
    
    if event in ('About',):
        about_me()





# In[ ]:





# In[6]:


import PySimpleGUI as sg 
sg.ChangeLookAndFeel('BrownBlue') # change style

WIN_W: int = 90
WIN_H: int = 25
filename:str = None

# string variables to shorten loop and menu code
file_new: str = 'New............(CTRL+N)'
file_open: str = 'Open..........(CTRL+O)'
file_save: str = 'Save............(CTRL+S)'

menu_layout: list = [['File', [file_new, file_open, file_save, 'Save As', '---', 'Exit']],
                     ['Tools', ['Word Count']],
                     ['Help', ['About']]]

layout: list = [[sg.Menu(menu_layout)],
                [sg.Text('> New file <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
                [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_')]]

window: object = sg.Window('Notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)

def new_file() -> str:
    ''' Reset body and info bar, and clear filename variable '''
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    filename = None
    return filename

def open_file() -> str:
    ''' Open file and update the infobar '''
    try:
        filename: str = sg.popup_get_file('Open File', no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

def save_file(filename: str):
    ''' Save file instantly if already open; otherwise use `save-as` popup '''
    if filename not in (None, ''):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    else:
        save_file_as()

def save_file_as() -> str:
    ''' Save new file or save existing file with another name '''
    try:
        filename: str = sg.popup_get_file('Save File', save_as=True, no_window=True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename, tuple):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    return filename

def word_count():
    ''' Display estimated word count '''
    words: list = [w for w in values['_BODY_'].split(' ') if w!='\n']
    word_count: int = len(words)
    sg.PopupQuick('Word Count: {:,d}'.format(word_count), auto_close=False)

def about_me():
    sg.PopupQuick('"All great things have small beginnings" - Peter Senge', auto_close=False)

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    if event in (file_new, 'n:78'):
        filename = new_file()
    if event in (file_open, 'o:79'):
        filename = open_file()
    if event in (file_save, 's:83'):
        save_file(filename)
    if event in ('Save As',):
        filename = save_file_as()   
    if event in ('Word Count',):
        word_count() 
    if event in ('About',):
        about_me()


# In[ ]:




