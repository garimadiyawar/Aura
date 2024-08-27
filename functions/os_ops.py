import os
import subprocess as sp

paths = {
    'notion': "C:\\Users\\gdiya\\AppData\\Local\\Programs\\Notion\\Notion.exe",
    'chrome': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
    
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def open_notion():
    os.startfile(paths['notion'])
    
def open_chrome():
    os.startfile(paths['chrome'])
    
def open_cmd():
    os.system('start cmd')
    
def open_calculator():
    sp.Popen(paths['calculator'])