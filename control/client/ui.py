# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
from ...constant.clientConstant import *

def FullScreenUI(isOpen):
    """
    全屏UI 玩家无法移动 GUI界面隐藏
    :param isOpen: 是否开启
    :return: 无
    """
    clientApi.HideHudGUI(isOpen)
    OperationComp.SetCanAll(not isOpen)
