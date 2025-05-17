import tkinter as tk
import pyautogui
import cv2
import numpy as np
import threading

class ScreenRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Screen Recorder")

        self.start_button = tk.Button(self.master, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.recording = False

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.record_screen).start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def record_screen(self):
        screen_width, screen_height = pyautogui.size()
        screen_resolution = (screen_width, screen_height)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_filename = 'screen_capture.mp4'
        out = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_resolution)

        while self.recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)

        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()
