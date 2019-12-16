# coding=utf-8
import time


class Timer:
    def __init__(self, timeout):
        self.timeout = timeout
        self.start = time.time()
        self.callback = None

    def done(self):
        return time.time() - self.start > self.timeout

    def on_timer_done(self, callback):
        self.callback = callback


timer1 = Timer(0.2)
timer1.on_timer_done(lambda: print('Job1 is done...'))

timer2 = Timer(0.1)
timer2.on_timer_done(lambda: print('Job2 is done...'))
timers = [timer1, timer2]

while True:
    for timer in timers:
        if timer.done():
            timer.callback()
            timers.remove(timer)

    if not timers:
        break
