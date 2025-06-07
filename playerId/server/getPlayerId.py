# -*- coding: utf-8 -*-

from ...constant.serverConstant import *


def GetPlayerIdByPlayerName(name):
    """
    通过玩家名字 获取玩家Id
    :param name 玩家名
    :return: 匹配到玩家ID返回玩家ID(str) 否则返回None
    """
    for pid in serverApi.GetPlayerList():
        if name == NameComp(pid).GetName():
            return pid
    return None


def GetPlayerIdByUid(uid):
    """
    通过指定UID 获取玩家ID
    :param uid
    :return: 匹配到玩家ID返回玩家ID(str) 否则返回None
    """
    for pid in serverApi.GetPlayerList():
        getUid = HttpComp.GetPlayerUid(pid)
        if uid == getUid:
            return pid
    return None
