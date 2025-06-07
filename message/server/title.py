# -*- coding: utf-8 -*-


from ...constant.serverConstant import *


def SetMiddleTitle(title='§0', subtitle='§0', pid=None, showOutput=False):
    """
    设置大标题 相当于title指令
    :param title: 主标题 默认为 '§0'
    :param subtitle: 副标题 默认为 '§0'
    :param pid: 执行的玩家ID 默认为 None
    :param showOutput: 是否显示输出 默认为 '§0'
    :return: 无
    """
    RunCommand('/title @s title {}'.format(title), pid, showOutput)
    RunCommand('title @s subtitle {}'.format(subtitle), pid, showOutput)
