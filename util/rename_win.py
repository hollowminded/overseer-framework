import ctypes
def rename_window(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)