import speedtest
import time


class PySpeedTest:
    def __init__(self) -> None:
        self.test = speedtest.Speedtest()
        self.better_server = self.test.get_best_server()
        self.location = self.better_server['country']
        self.start = time.time()

    def download_speed(self):
        self.download_speed = self.test.download()/1024/1024
        return self.download_speed

    def upload_speed(self):
        self.upload_speed = self.test.upload()/1024/1024
        return self.upload_speed

    def ping(self):
        self.ping = self.test.results.ping
        return self.ping

    def display(self):
        print("\nINTERNET SPEED TEST\n")
        print(f"Location: {self.location}")

        download = self.download_speed()
        print(f"download: {download:.2f} Mbps")

        upload = self.upload_speed()
        print(f"Upload: {upload:.2f} Mbps")

        ping_ = self.ping()
        print(f"Ping: {ping_:.1f} ms")

        self.end = time.time()
        self.run_time = self.end - self.start


test = PySpeedTest()
test.display()
