import pyautogui, keyboard, time, sys

pos1, pos2 = None, None

def set_pos1(): global pos1; pos1 = pyautogui.position()
def set_pos2(): global pos2; pos2 = pyautogui.position()

def press_mouse():
    while True:
        if keyboard.is_pressed(hotkeys[3]): break
        if pos1 and pos2:
            pyautogui.click(pos1[0], pos1[1])
            time.sleep(0.005)
            pyautogui.click(pos2[0], pos2[1])

if len(sys.argv) < 5:
    print("Usage: python dual_cursor_autoclicker.py <hotkey1> <hotkey2> <hotkey3> <hotkey4>")
    sys.exit()

hotkeys = sys.argv[1:5]
keyboard.add_hotkey(hotkeys[0], set_pos1)
keyboard.add_hotkey(hotkeys[1], set_pos2)
keyboard.add_hotkey(hotkeys[2], press_mouse)

keyboard.wait()
