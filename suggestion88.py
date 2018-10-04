"""
建议88：使用multiprocessing克服GIL的缺陷

进程之间的通信优先考虑Pipe和Queue，而不是Lock,Event,Condition,Semaphore等 同步原语。
使用Queue进行进程之间的通信的时候，传输的对象必须是可以序列化的，否则put操作会导致PicklingError。
multiprocessing.Pipe([duplex])，其中dumplex默认为True，表示为双向管道，否则为单向。它返回
一个Connection对象的组(conn1, conn2)，分别代表管道两端。它不支持进程安全，只适用在两个进程间通信，
性能更好。
"""

from multiprocessing import Process, Pipe, Queue
import time


def reader_pipe(pipe):
    # 这里用output_p端
    output_p, input_p = pipe
    input_p.close()  # 关闭一端，另一端接收数据
    while True:
        try:
            msg = output_p.recv()  # noqa
        except EOFError:
            break


def writer_pipe(count, input_p):
    # 这里用input_p端
    for i in range(0, count):
        input_p.send(i)


def reader_queue(queue):
    while True:
        msg = queue.get()
        if (msg == 'DONE'):
            break


def writer_queue(count, queue):
    for ii in range(0, count):
        queue.put(ii)
    queue.put('DONE')


# if __name__ == '__main__':
#     print('testing for pipe:')
#     for count in [10**3, 10**4, 10**5]:
#         output_p, input_p = Pipe()
#         reader_p = Process(target=reader_pipe, args=((output_p, input_p), ))  # 拷贝一份pipe
#         reader_p.start()

#         _start = time.time()
#         output_p.close()  # 当前进程的管道，关闭一端，往另一端发送数据
#         writer_pipe(count, input_p)
#         input_p.close()
#         reader_p.join()
#         print('Sending %s numbers to Pipe() took %s seconds' % (count, (time.time() - _start)))

#     print('testing for queue:')
#     for count in [10**3, 10**4, 10**5]:
#         queue = Queue()
#         reader_p = Process(target=reader_queue, args=((queue), ))
#         reader_p.daemon = True
#         reader_p.start()

#         _start = time.time()
#         writer_queue(count, queue)
#         reader_p.join()
#         print('Sending %s numbers to Queue() took %s seconds' % (count, time.time() - _start))
"""
尽量避免资源共享。如果不可避免，可以通过multiprocessing.Value 和 multiprocessing.Array
或者 multiprocessing.sharedctypes来实现内存共享，也可以通过服务器进程管理器Manager()来
实现数据和状态的共享。
共享内存方式更快，效率更高，但Manager()使用起来更加方便，并且支持本地和远程内存共享。
"""
import time
from multiprocessing import Process, Value


def func(val):
    for i in range(10):
        time.sleep(0.1)
        with val.get_lock():  # 必须加锁同步
            val.value += 1


if __name__ == '__main__':
    v = Value('i', 0)
    processList = [Process(target=func, args=(v, )) for i in range(10)]
    for p in processList:
        p.start()
    for p in processList:
        p.join()
    print(v.value)
