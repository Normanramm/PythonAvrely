import sounddevice as sd
import soundfile as sf
from moviepy.audio.AudioClip import AudioArrayClip
import tkinter as tk
import pyautogui
import cv2
import numpy as np
import threading
from moviepy.editor import *


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
        fs = 44100  # Частота дискретизации
        duration = 10  # Продолжительность записи в секундах

        # Начинаем запись звука
        my_recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        # Создаем объект для записи видео
        output_filename = 'screen_capture_with_audio.mp4'
        output_video = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (1920, 1080))

        # Записываем видео с экрана
        while self.recording:
            screenshot = pyautogui.screenshot()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            output_video.write(frame)

        # Останавливаем запись звука
        sd.stop()

        # Сохраняем аудио в файл
        sf.write('audio_capture.wav', my_recording, fs)

        # Загружаем видеофайл и добавляем аудио
        video_clip = VideoFileClip(output_filename)
        audio_clip = AudioArrayClip(my_recording, fps=fs)
        final_clip = video_clip.set_audio(audio_clip)

        # Сохраняем видео с аудио
        output_filename_final = 'screen_capture_with_audio_final.mp4'
        final_clip.write_videofile(output_filename_final, codec='libx264')


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()







