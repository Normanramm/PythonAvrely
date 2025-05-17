import speedtest


st = speedtest.Speedtest()

ds = st.download()
us = st.upload()
ping = st.results.ping
def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


# Readable
print(f'Скорость загрузки: {humansize(ds)}')
print(f'Скорость отдачи: {humansize(us)}')
print(f'Задержка (ping): {ping} м/с')