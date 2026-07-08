# -*- coding: utf-8 -*-
import copy


def CreateItemDict(newItemName, newAuxValue=0, count=1, showInHand=True, enchantData=None, modEnchantData=None,
                   customTips='', extraId='', userData=None, durability=0, itemName='', auxValue=0):
    """
    构造物品信息字典
    :param newItemName: 必须设置 物品的identifier
    :param newAuxValue: 必须设置 物品附加值
    :param count: 必须设置 物品数量 设置为0时为空物品
    :param showInHand: 可选 是否显示在手上
    :param enchantData: 可选 附魔数据 类型为列表 列表中每个元素为元组
    :param modEnchantData: 可选 自定义附魔数据 类型为列表 列表中每个元素为元组(str, int)
    :param customTips: 可选 物品的自定义tips 修改该内容后会覆盖实例的组件
    :param extraId: 可选 物品自定义标识符 可以用于保存数据 区分物品
    :param userData: 可选 物品userData 用于灾厄旗帜、旗帜等物品 请勿随意设置该值
    :param durability: 可选 物品耐久度 不存在耐久概念的物品默认值为0
    :param itemName: 废弃 1.22及以前版本的旧identifier
    :param auxValue: 废弃 1.22及以前版本的旧物品附加值
    :return: 物品信息字典
    """
    result = {}
    result['newItemName'] = newItemName
    result['newAuxValue'] = newAuxValue
    result['count'] = count
    if not showInHand:
        result['showInHand'] = showInHand
    if enchantData:
        result['enchantData'] = enchantData
    if modEnchantData:
        result['modEnchantData'] = modEnchantData
    if customTips:
        result['customTips'] = customTips
    if extraId:
        result['extraId'] = extraId
    if userData:
        result['userData'] = userData
    if durability:
        result['durability'] = durability
    if itemName:
        result['itemName'] = itemName
    if auxValue:
        result['auxValue'] = auxValue
    return result


def CreateEnchantItemBypass(itemDict, enchantment):
    """
    生成无视原版附魔等级和冲突限制的物品信息字典
    仅支持原版附魔 附魔等级x: -32767 <= x <= 32767 x为整数
    :param itemDict: 原物品信息字典
    :param enchantment: 附魔信息 key为附魔的数字ID value为附魔等级
    :return: 带有附魔信息的物品信息字典
    """
    itemDict = copy.deepcopy(itemDict)
    if 'enchantData' in itemDict:
        del itemDict['enchantData']
    if 'userData' not in itemDict or itemDict['userData'] is None:
        itemDict['userData'] = {}
    enchantments = itemDict['userData'].setdefault('ench', [])

    for _id, level in enchantment.items():
        safeLevel = max(-32767, min(32767, level))
        # 遍历已有附魔匹配ID 存在则修改等级
        for _enchantment in enchantments:
            if _enchantment["id"]["__value__"] == _id:
                _enchantment["lvl"]["__value__"] = safeLevel
                break
        else:
            # 无匹配则新增附魔条目
            enchantments.append({
                'id': {'__type__': 2, '__value__': _id},
                'lvl': {'__type__': 2, '__value__': safeLevel},
            })
    return itemDict
