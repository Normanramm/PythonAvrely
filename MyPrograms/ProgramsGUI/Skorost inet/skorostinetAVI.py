import speedtest

st = speedtest.Speedtest()

st.get_servers()

best_server = st.get_best_server()

download_speed = st.download() / 1_000_000
upload_speed = st.upload() / 1_000_000
ping = st.results.ping

print(f"Скорость загрузки: {download_speed:.2f} Мбит/с")
print(f"Скорость отдачи: {upload_speed:.2f} Мбит/с")
print(f"Задержка (ping): {ping} мс")
#auto-py-to-exe через это делается запуск в файл
#pyinstaller название файла --one file