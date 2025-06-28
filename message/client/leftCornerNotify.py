# -*- coding: utf-8 -*-
from ...constant.clientConstant import *

def SendLocalMessage(pid, msg, header, color=ENUM.ColorCode.WHITE):
    """
    给指定玩家发送消息
    (原SetClientMessage)
    :param header: 消息头 会被添加在msg的前面
    :param pid: 接收消息的玩家ID
    :param msg: 消息内容
    :param color: 颜色 默认白色
    :return: 无
    """
    TextNotifyComp.SetLeftCornerNotify(color+header+str(msg))
