# -*- coding: utf-8 -*-
from ..common.getDistance import GetEuclideanDistance
from ...constant.clientConstant import *


def GetEntityListSortedByDistance(pos, exceptedList=None):
    """
    按离某点的距离由近到远排序指定维度内的实体ID 并获取距离
    :param pos: 坐标
    :param exceptedList: 需要排除的实体ID列表
    :return: 包含元组的列表 元组的第1个元素为实体ID 第2个元素为距离
    """
    result = []
    if exceptedList is None:
        exceptedList = []
    # 这里的GetEngineActor只返回本地玩家所在维度的已加载实体
    # 而不是服务端所有维度的已加载实体
    entities = clientApi.GetEngineActor().keys()
    for i in exceptedList:
        entities.remove(i)
    for eid in entities:
        distance = GetEuclideanDistance(PosComp(eid).GetPos(), pos)
        result.append((eid, distance))
    result.sort(key=lambda x: x[1])
    return result
