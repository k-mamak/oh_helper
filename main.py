import ctypes
import sys

from app import Bot
from utils import is_admin

if is_admin():
    if __name__ == "__main__":
        app = Bot()
        app.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
