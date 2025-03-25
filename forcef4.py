import win32gui, win32process, psutil, os, ctypes
from ctypes import wintypes
from pynput import keyboard

alt_pressed = False
config_file = "forcef4.ini"

def create_config_file():
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            f.write("explorer\n")

def load_excluded_processes():
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            return [line.strip().lower() for line in f if line.strip()]
    return []

def is_process_critical(pid):
    hProcess = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
    if not hProcess: return False
    isCritical = wintypes.BOOL()
    result = ctypes.windll.kernel32.IsProcessCritical(hProcess, ctypes.byref(isCritical))
    ctypes.windll.kernel32.CloseHandle(hProcess)
    return bool(isCritical.value) and result != 0

def kill_process_and_children(pid):
    try:
        parent = psutil.Process(pid)
        excluded_processes = load_excluded_processes()
        if any(excluded in parent.name().lower() for excluded in excluded_processes) or is_process_critical(pid):
            return
        for child in parent.children(recursive=True): child.terminate()
        parent.terminate()
    except: pass

def kill_foreground_process():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        kill_process_and_children(pid)

def on_press(key):
    global alt_pressed
    if key in [keyboard.Key.alt_l, keyboard.Key.alt_r]: alt_pressed = True
    elif key == keyboard.Key.f4 and alt_pressed: kill_foreground_process()

def on_release(key):
    global alt_pressed
    if key in [keyboard.Key.alt_l, keyboard.Key.alt_r]: alt_pressed = False

create_config_file()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
