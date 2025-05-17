import speedtest

class SpeedTest:
    def __init__(self):
        self.st = speedtest.Speedtest()

    def test(self):
        self.ds = self.st.download()
        self.us = self.st.upload()
        self.ping = self.st.results.ping

        return self.ds, self.us, self.ping

    def humansize(self, nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes) - 1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    def print_results(self):
        ds, us, ping = self.test()
        print(f'Скорость загрузки: {self.humansize(ds)}')
        print(f'Скорость отдачи: {self.humansize(us)}')
        print(f'Задержка (ping): {ping} м/с')


speed_test = SpeedTest()
print('Идет загрузка!')
speed_test.print_results()
print('Загрузка завершена!')