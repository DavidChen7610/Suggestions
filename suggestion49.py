import os
import queue
import threading
import requests


class DownloadThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            print(self.name + ' begin download ' + url + '...')
            self.download_file(url)
            self.queue.task_done()
            print(self.name + ' download completed!!!')

    def download_file(self, url):
        import re

        ret = re.findall('www.(.+?).com', url)
        urlhandler = requests.get(url)
        fname = ret[0] + '.html'
        with open(fname, 'w') as f:
            f.write(urlhandler.text)


if __name__ == '__main__':
    urls = ['https://www.163.com', 'http://www.qq.com', 'http://www.sohu.com']
    q = queue.Queue()

    for i in range(5):
        t = DownloadThread(q)
        t.setDaemon(True)
        t.start()

    for url in urls:
        q.put(url)

    q.join()
