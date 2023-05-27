import pydirectinput
import threading
import tkinter as tk
import tkinter.font as font
import time
from utils import thread_killer

class Bot(tk.Tk):
    def __init__(self):
        super().__init__()
        # VERSION
        self.VERSION = "1.0"

        # FLAGS
        self.ATTACK_FLAG = False

        # INPUTS
        self.skill_input = tk.StringVar()
        self.delay_input = tk.StringVar()

        # DEFAULT INPUT
        self.skill_input = "z2"
        self.delay_input = "1000"

        # TEXT BOXES
        self.skill_text_box_label = tk.Label(self, text="BUTTON")
        self.skill_text_box_label.grid(row=0, column=1)

        self.skill_text_box = tk.Entry(self, textvariable=self.skill_input)
        self.skill_text_box.grid(row=1, column=1)
        self.skill_text_box.insert(tk.END, self.skill_input)

        self.delay_text_box_label = tk.Label(self, text="DELAY(ms)")
        self.delay_text_box_label.grid(row=2, column=1)

        self.delay_text_box = tk.Entry(self, textvariable=self.delay_input)
        self.delay_text_box.grid(row=3, column=1)
        self.delay_text_box.insert(tk.END, self.delay_input)

        # TKINTER WINDOW
        self.geometry("215x295")
        self.title(f"OH_MACRO_v{self.VERSION}")

        # BUTTONS
        self.buttonFont = font.Font(size=10)
        self.start_button = tk.Button(self, text="START", height=3, width=20, command=self.start)
        self.stop_button = tk.Button(self, text="STOP", height=3, width=20, command=self.stop)

        # BUTTON GRID
        self.start_button.grid(row=4, column=1, pady=(5, 5))
        self.stop_button.grid(row=5, column=1, pady=(5, 5))

        # STATUS
        self.status = tk.Label(self, text="STOPPED", bg="red", height=5, width=30)
        self.status.grid(row=6, column=0, columnspan=3, pady=(5, 5))

    def retrieve_input(self):
        self.skill_input = self.skill_text_box.get()
        self.delay_input = self.delay_text_box.get()

    def start(self):
        self.MACRO_FLAG= True
        self.skill_text_box.config(state="disabled")
        self.delay_text_box.config(state="disabled")
        self.update()
        self.retrieve_input()
        self.status.config(text="RUNNING", bg="green")
        self.run_macro_thread()


    def stop(self):
        self.status.config(text="STOPPED", bg="red")
        self.update()
        self.stop_attack_threads()
        self.skill_text_box.config(state="normal")
        self.delay_text_box.config(state="normal")

    def run_macro_thread(self):
        self.macro_thread = threading.Thread(target=self.macro)
        self.macro_thread.start()

    def stop_attack_threads(self):
        self.MACRO_FLAG = False
        thread_killer(self.macro_thread)
 
    def macro(self):
        while self.MACRO_FLAG:
            for char in self.skill_input:
                pydirectinput.keyDown(char)
                pydirectinput.keyUp(char)
            time.sleep(int(self.delay_input) / 1000)
