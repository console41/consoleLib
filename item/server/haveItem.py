# -*- coding: utf-8 -*-

from ...constant.serverConstant import *


def HaveItem(pid, itemName):
    """
    判断玩家是否有指定物品
    :param pid: 玩家ID
    :param itemName: 物品标识符 例: minecraft:dirt
    :return:
    """
    allItems = ItemComp(pid).GetPlayerAllItems(ENUM.ItemPosType.INVENTORY)
    for itemDict in allItems:
        if not itemDict:
            continue
        if itemDict['newItemName'] == itemName:
            return True
    return False
