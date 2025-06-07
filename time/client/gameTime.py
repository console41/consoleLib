# -*- coding: utf-8 -*-


from ...constant.clientConstant import *


def __GetTime():
    """
    :return: 当前游戏所过帧数
    :rtype: int
    """
    return TimeComp.GetTime()


def GetDay(time=None):
    """
    获取从游戏开始经过的游戏天数
    :param time: 传入数字则计算帧数内经过的游戏天数 不传返回从游戏开始经过的游戏天数
    :return: 天数
    :rtype: int
    """
    if time:
        return time / 24000
    time = __GetTime()
    return time / 24000


def GetTimeOfDay(time=None):
    """
    获取当前游戏天内的帧数
    :param time: 传入数字则计算帧数内游戏天内的帧数 不传返回当前游戏天内的帧数
    :return: 帧数
    :rtype: int
    """
    if time:
        return time % 24000
    time = __GetTime()
    return time % 24000
