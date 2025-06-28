# -*- coding: utf-8 -*-
def IsRunByPlayer(originArgs):
    """
    判断自定义指令是否由玩家运行
    :param originArgs: CustomCommandTriggerServerEvent事件触发后的原始数据
    :return: 是否由玩家运行
    :rtype: bool
    """
    return originArgs['origin'].has_key('entityId')