# -*- coding: utf-8 -*-
import threading


def AddTimer(interval, function, args=(), kwargs={}):
    """
    添加一次性定时器 使用Python标准库threading编写
    :param interval: 定时器触发延迟时间
    :param function: 要执行的函数
    :param args: 函数的位置参数
    :param kwargs: 函数的关键字参数
    :return: 一次性计时器实例
    """
    return OneShotTimer(interval, function, args, kwargs)


def AddRepeatedTimer(interval, function, args=(), kwargs={}):
    """
    添加重复定时器 使用Python标准库threading编写
    :param interval: 定时器触发间隔时间
    :param function: 要执行的函数
    :param args: 函数的位置参数
    :param kwargs: 函数的关键字参数
    :return: 重复计时器实例
    """
    return RepeatedTimer(interval, function, args, kwargs)


class BaseTimer(object):
    def __init__(self, interval, function, args=(), kwargs={}):
        self.interval = interval  # type: float | int
        self.function = function  # type: function
        self.args = args
        self.kwargs = kwargs
        # 计时器
        self.timer = None  # 主计时器
        self.pauseTimer = None  # 用于自动恢复的计时器
        # 状态
        self.cancelled = False
        self.paused = False

    def Execute(self):
        if not self.cancelled:
            self.function(*self.args, **self.kwargs)

    def Start(self):
        """
        启动定时器
        :return: 返回自身 支持链式调用
        """
        if self.cancelled or (self.timer and self.timer.is_alive()):
            return
        self.timer = threading.Timer(self.interval, self.Execute)
        self.timer.start()
        return self

    def Cancel(self):
        """
        取消定时器 此操作不可逆
        """
        self.cancelled = True
        if self.timer and self.timer.is_alive():
            self.timer.cancel()
        self.timer = None
        if self.pauseTimer and self.pauseTimer.is_alive():
            self.pauseTimer.cancel()
        self.pauseTimer = None

    def Pause(self, resumeTime=None):
        """
        暂停定时器 并在指定时间后自动恢复
        :param resumeTime: 指定暂停的时间 默认为 None 表示不会自动恢复
        """
        if self.timer and self.timer.is_alive() and not self.paused:
            self.timer.cancel()
            self.paused = True
        if resumeTime is not None:
            # 再新建一个定时器来恢复
            self.pauseTimer = threading.Timer(resumeTime, self.Resume)
            self.pauseTimer.start()

    def Resume(self):
        """
        恢复已暂停的定时器
        """
        if self.paused and not self.cancelled:
            self.paused = False
            self.timer = threading.Timer(self.interval, self.Execute)
            self.timer.start()
            # 判断自动恢复的计时器是否存在/存活
            if self.pauseTimer and self.pauseTimer.is_alive():
                self.pauseTimer.cancel()
            self.pauseTimer = None


class OneShotTimer(BaseTimer):
    def __init__(self, interval, function, args=(), kwargs={}):
        super(OneShotTimer, self).__init__(interval, function, args, kwargs)


class RepeatedTimer(BaseTimer):
    def __init__(self, interval, function, args=(), kwargs={}):
        super(RepeatedTimer, self).__init__(interval, function, args, kwargs)

    def Execute(self):
        if not self.cancelled:
            self.function(*self.args, **self.kwargs)
            if not self.cancelled:
                # 自动重复
                self._timer = threading.Timer(self.interval, self.Execute)
                self._timer.start()
