# -*- coding: utf-8 -*-
from math import sqrt


def GetEuclideanDistance(point1, point2):
    """
    计算两个三元组表示的点之间的欧几里得距离
    :param point1: 第1个点的坐标
    :param point2: 第2个点的坐标
    :return: 两点之间的距离
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
