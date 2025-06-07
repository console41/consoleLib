# -*- coding: utf-8 -*-

from ...constant.clientConstant import *


def GetDistanceToSecondTargetPointFromPlayer(end, count, playerId=PLAYER_ID):
    """
    计算从玩家开始到玩家朝向指定位置第二个点的距离
    :param end: 第二个点的距离
    :param count: 点位数量 即分成多少个坐标
    :param playerId: 玩家ID 默认本地玩家ID
    :return: 坐标列表
    """
    playerPos = COMPONENT_FACTORY.CreatePos(playerId).GetFootPos()
    if not playerPos:
        return []
    playerPos = (playerPos[0], playerPos[1] + 1.6, playerPos[2])

    rot = COMPONENT_FACTORY.CreateRot(playerId).GetRot()
    if not rot:
        return []
    direction = clientApi.GetDirFromRot(rot)
    endPos = (
        playerPos[0] + direction[0] * end,
        playerPos[1] + direction[1] * end,
        playerPos[2] + direction[2] * end
    )

    xd = playerPos[0] - endPos[0]
    yd = playerPos[1] - endPos[1]
    zd = playerPos[2] - endPos[2]
    xStep = xd / (count + 1)
    yStep = yd / (count + 1)
    zStep = zd / (count + 1)
    linePos = []
    while count > 0:
        pos = (
            endPos[0] + xStep * count,
            endPos[1] + yStep * count,
            endPos[2] + zStep * count
        )
        linePos.append(pos)
        count -= 1

    return linePos
