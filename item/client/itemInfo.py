# -*- coding: utf-8 -*-

from ...constant.serverConstant import *


def GetItemByTag(*tag):
    """
    根据物品标签获取物品
    :param tag: 物品标签 可为多个
    :return: 带有该标签的物品标识符列表(若传了多个标签 物品需同时带有这几种标签才会匹配上)
    """
    result = []
    itemComp = ItemComp(LEVEL_ID)
    allItems = itemComp.GetLoadItems()
    for itemName in allItems:
        itemTags = itemComp.GetItemTags(itemName)
        if all(t in itemTags for t in tag):
            result.append(itemName)
    return result
