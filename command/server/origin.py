# -*- coding: utf-8 -*-
def IsRunByPlayer(args):
    """
    判断自定义指令是否由玩家运行
    :param args: CustomCommandTriggerServerEvent事件触发后的原始数据
    :return: 是否由玩家运行
    :rtype: bool
    """
    return 'entityId' in args['origin']
