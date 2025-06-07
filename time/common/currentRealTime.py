# -*- coding: utf-8 -*-
import datetime


def GetCurrentTime():
    """
    获取当前时间信息
    :return: 年 月 日 时 分 秒 微秒 时区信息
    """
    time = datetime.datetime.now()
    return {
        'year': time.year,
        'month': time.month,
        'day': time.day,
        'hour': time.hour,
        'second': time.second,
        'microsecond ': time.microsecond,
        'tzinfo': time.tzinfo
    }
