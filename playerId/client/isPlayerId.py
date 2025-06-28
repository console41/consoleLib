# -*- coding: utf-8 -*-
from ...constant.clientConstant import *


def IsIdPlayerId(eid):
    """
    判断实体id是不是玩家id
    :param eid: 实体id
    :return: 是否是玩家id
    :rtype: bool
    """
    return eid in clientApi.GetPlayerList()
