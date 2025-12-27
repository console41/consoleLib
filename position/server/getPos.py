# -*- coding: utf-8 -*-

from ...constant.serverConstant import *


def GetPosFromPlayerRot(playerId, end, count):
    """
    计算玩家朝向向前指定距离的坐标
    :param playerId: 玩家ID
    :param end: 第二个点的距离
    :param count: 点位数量 即分成多少个坐标
    :return: 坐标列表
    """
    playerPos = PosComp(playerId).GetFootPos()
    if not playerPos:
        return []
    playerPos = (playerPos[0], playerPos[1] + 1.6, playerPos[2])

    rot = RotComp(playerId).GetRot()
    if not rot:
        return []
    direction = serverApi.GetDirFromRot(rot)
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


def GetPlayerHandPos(pid):
    """
    @author: 奈雪
    获取玩家手的坐标
    :param pid: 玩家ID
    :return: 玩家手的坐标
    """
    pos = PosComp(pid).GetPos()
    x, y, z = pos
    direction = serverApi.GetDirFromRot(RotComp(pid).GetRot())
    dirX, dirY, dirZ = direction
    ARM_HEIGHT_OFFSET = 0.3  # 手臂高度相对视角的偏移量
    ARM_SIDE_OFFSET = 0.3  # 手臂右边相对视角的偏移量
    ARM_LENGTH = 0.8  # 手臂的长度
    nX, nY, nZ = -dirZ * ARM_SIDE_OFFSET, (dirY - ARM_HEIGHT_OFFSET) * ARM_SIDE_OFFSET, (dirX) * ARM_SIDE_OFFSET
    handPos = (x + nX + dirX * ARM_LENGTH, y + nY + dirY * ARM_LENGTH, z + nZ + dirZ * ARM_LENGTH)
    return handPos