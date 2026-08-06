# -*- coding: utf-8 -*-
from ..common.getDistance import GetEuclideanDistance
from ...constant.serverConstant import *


def GetNearestEntity(point, exceptedList=[]):
    """
    获取离当前一点最近的实体
    :param point:坐标
    :param exceptedList: 需要排除的实体id列表
    :return: 元组 第 1 个元素为玩家id列表 第 2 个元素为距离
    """
    entities = serverApi.GetEngineActor().keys()
    for i in exceptedList:
        entities.remove(i)
    entityDistances = {
        eid: GetEuclideanDistance(point, PosComp(eid).GetPos())
        for eid in entities
    }
    if not entityDistances:
        return {}
    minDistance = min(entityDistances.values())
    return [eid for eid, distance in entityDistances.items() if distance == minDistance], minDistance


def GetNearestPlayer(point, exceptedList=[]):
    """
    获取离当前一点最近的玩家
    :param point:坐标
    :param exceptedList: 需要排除的玩家id列表
    :return: 元组 第 1 个元素为玩家id列表 第 2 个元素为距离
    """
    players = serverApi.GetPlayerList()
    for i in exceptedList:
        players.remove(i)
    playerDistances = {
        eid: GetEuclideanDistance(point, PosComp(eid).GetPos())
        for eid in players
    }
    if not playerDistances:
        return {}
    minDistance = min(playerDistances.values())
    return [pid for pid, distance in playerDistances.items() if distance == minDistance], minDistance
