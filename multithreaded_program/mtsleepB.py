#!/usr/bin/env python

import _thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, "at:", ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()  #得到锁对象
        lock.acquire()  #取得锁，相当于“把锁锁上”
        locks.append(lock)  #一旦锁被锁上后，就可以添加到锁列表中

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all DONE at:', ctime())


if __name__ == '__main__':
    main()
