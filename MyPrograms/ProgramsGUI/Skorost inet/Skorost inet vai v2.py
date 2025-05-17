import tkinter as tk
from tkinter import messagebox
import speedtest


# cod speedtest
def run_speedtest():
    st = speedtest.Speedtest()
    try:
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
        result_label.config(text=f"Скорость загрузки: {download_speed:.2f} Mbps\nСкорость отдачи: {upload_speed:.2f} Mbps\nПинг:{ping:.2f} Mbps")
    except speedtest.SpeedtestError as e:
        messagebox.showerror("Ошибка", str(e))

# GUI
root = tk.Tk()
root.title("Замеритель скорости интернета VAI v.2")
root.geometry("500x200")

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=30)

run_button = tk.Button(root, text="Нажми и жди, будет результат", command=run_speedtest)
run_button.pack()

root.mainloop()

