# -*- coding: utf-8 -*-
import random


def CanEventHappenByProbability(probability):
    """
    判断事件是否以给定概率发生
    :param probability: 0-1之间的浮点数 表示事件发生的概率
    :return True表示事件发生，False表示不发生
    """
    return random.random() <= probability
