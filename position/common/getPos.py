# -*- coding: utf-8 -*-
from ...constant.serverConstant import *


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