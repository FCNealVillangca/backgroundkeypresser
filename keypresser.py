
from time import sleep
import win32gui, win32ui, win32con, win32api, os

def main():
    window_name = "0x9026a"
    hwnd = win32gui.FindWindow(None, window_name)
    hwnd = get_inner_windows(hwnd)['MuhRO']
    win = win32ui.CreateWindowFromHandle(hwnd)

    command_list(hwnd)

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)

def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds

def click_skill(x,y, hwnd):
    win32api.SetCursorPos((960,540))
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x,y)) 
    sleep(.1)
    win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(x,y))

def command_list(hwnd):

    i = 1
    while i != 50:
        print(i)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x70, 0)
        sleep(0.5)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x70, 0)
        sleep(0.5)
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x71, 0)
        sleep(0.5)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x71, 0)
        sleep(1)
        i += 1
    os.system('cls')
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x78, 0)
    sleep(0.5)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x78, 0)
    sleep(0.5)

while True:   
    main()


