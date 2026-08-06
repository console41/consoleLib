# -*- coding: utf-8 -*-
from ..common.getDistance import GetEuclideanDistance
from ...constant.serverConstant import *


def GetEntityListSortedByDistance(dimensionId, pos, exceptedList=None):
    """
    按离某点的距离由近到远排序指定维度内的实体ID 并获取距离
    :param dimensionId: 维度ID
    :param pos: 坐标
    :param exceptedList: 需要排除的实体ID列表
    :return: 包含元组的列表 元组的第1个元素为实体ID 第2个元素为距离
    """
    result = []
    if exceptedList is None:
        exceptedList = []
    entities = serverApi.GetEngineActor().keys()
    for i in exceptedList:
        entities.remove(i)
    for eid in entities:
        entityDimensionId = DimensionComp(eid).GetEntityDimensionId()
        if entityDimensionId == dimensionId:
            distance = GetEuclideanDistance(PosComp(eid).GetPos(), pos)
            result.append((eid, distance))
    result.sort(key=lambda x: x[1])
    return result

def GetPlayerListSortedByDistance(dimensionId, pos, exceptedList=None):
    """
    按离某点的距离由近到远排序指定维度内的玩家ID 并获取距离
    :param dimensionId: 维度ID
    :param pos: 坐标
    :param exceptedList: 需要排除的玩家ID列表
    :return: 包含元组的列表 元组的第1个元素为玩家ID 第2个元素为距离
    """
    result = []
    if exceptedList is None:
        exceptedList = []
    players = serverApi.GetPlayerList()
    for i in exceptedList:
        players.remove(i)
    for pid in players:
        playerDimensionId = DimensionComp(pid).GetEntityDimensionId()
        if playerDimensionId == dimensionId:
            distance = GetEuclideanDistance(PosComp(pid).GetPos(), pos)
            result.append((pid, distance))
    result.sort(key=lambda x: x[1])
    return result

