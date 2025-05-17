import tkinter as tk
import pyautogui
import cv2
import numpy as np
import threading
import sounddevice as sd
import soundfile as sf

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
        threading.Thread(target=self.record_screen_and_audio).start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def record_screen_and_audio(self):
        screen_width, screen_height = pyautogui.size()
        screen_resolution = (screen_width, screen_height)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_filename = 'screen_capture_with_audio.mp4'
        out = cv2.VideoWriter(output_filename, fourcc, 20.0, screen_resolution)

        fs = 44100  # Частота дискретизации
        duration = 10  # Продолжительность записи в секундах

        # Начинаем запись звука
        my_recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        while self.recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            out.write(frame)

        # Останавливаем запись звука
        sd.stop()

        # Сохраняем аудио в файл
        sf.write('audio_capture.wav', my_recording, fs)

        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()

