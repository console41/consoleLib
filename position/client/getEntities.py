# -*- coding: utf-8 -*-
from ..common.getDistance import GetEuclideanDistance
from ...constant.clientConstant import *


def GetNearestEntity(point, exceptedList=[]):
    """
    获取离当前一点最近的实体
    :param point:坐标
    :param exceptedList: 需要排除的实体id列表
    :return: 字典 eid为实体id列表(可能有距离相同的实体) 没有实体则为{} distance为距离
    """
    entities = clientApi.GetEngineActor().keys()
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
    :return: 字典 eid为玩家id列表(可能有距离相同的玩家) 没有玩家则为{} distance为距离
    """
    players = clientApi.GetPlayerList()
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
