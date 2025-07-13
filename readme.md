# ConsoleLib文档

## 目录

<!-- TOC -->
* [ConsoleLib文档](#consolelib文档)
  * [目录](#目录)
  * [constant](#constant)
  * [control / 控制](#control--控制)
    * [FullScreenUI](#fullscreenui)
  * [item / 物品](#item--物品)
    * [HaveItem](#haveitem)
  * [message / 消息](#message--消息)
    * [SendLocalMessage](#sendlocalmessage)
    * [SendGlobalMessage](#sendglobalmessage)
    * [SendMessageToPlayer](#sendmessagetoplayer)
  * [title / 标题](#title--标题)
    * [SetMiddleTitle](#setmiddletitle)
  * [playerId / 玩家ID](#playerid--玩家id)
    * [GetPlayerIdByPlayerName](#getplayeridbyplayername)
    * [GetPlayerIdByPlayerName](#getplayeridbyplayername-1)
    * [GetPlayerIdByDimensionId](#getplayeridbydimensionid)
    * [IsIdPlayerId](#isidplayerid)
      * [服务端](#服务端)
      * [客户端](#客户端)
  * [time / 时间](#time--时间)
    * [GetCurrentTime](#getcurrenttime)
    * [GetDay](#getday)
      * [服务端接口](#服务端接口)
      * [客户端接口](#客户端接口)
    * [GetTimeOfDay](#gettimeofday)
      * [服务端接口](#服务端接口-1)
      * [客户端接口](#客户端接口-1)
  * [position / 位置](#position--位置)
    * [GetDistanceToSecondTargetPointFromPlayer](#getdistancetosecondtargetpointfromplayer)
      * [服务端接口](#服务端接口-2)
      * [客户端接口](#客户端接口-2)
  * [command / 指令](#command--指令)
    * [IsRunByPlayer](#isrunbyplayer)
<!-- TOC -->

## constant

constant储存了组件工厂```clientApi.GetEngineCompFactory()```的组件 避免重复获取
还储存了一些量 如```serverApi.GetMinecraftEnum()```
需要注意的是 一些constant需要传入玩家ID

示例:

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *

for pid in serverApi.GetPlayerList():
    print NameComp(pid).GetName()
```

## control / 控制

### FullScreenUI

客户端

method in consoleLib.control.client.ui

* 描述
  
  全屏UI 玩家无法移动 GUI界面隐藏

* 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值 |
  | ------ | ---- | ---- | --- |
  | isOpen | bool | 是否开启 |     |

* 返回值
  
  无

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.clientApi import FullScreenUI

FullScreenUI(True)
```

## item / 物品

### HaveItem

服务端

method in consoleLib.item.haveItem

* 描述
  
  判断玩家是否有指定物品

* 参数
  
  | 参数名      | 数据类型 | 描述    | 默认值 |
  | -------- | ---- | ----- | --- |
  | pid      | str  | 玩家ID  |     |
  | itemName | str  | 物品标识符 |     |

* 返回值
  
  无

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *
from consoleLib.serverApi import HaveItem

print HaveItem(serverApi.GetPlayerList()[0], 'minecraft:diamond')
```

## message / 消息

### SendLocalMessage

客户端

method in consoleLib.message.client.leftCornerNotify

* 描述
  
  客户端发送一条消息

 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值  |
  |--------|------|------|------|
  | msg    | str  | 消息内容 |      |
  | header | str  | 消息头  | 空字符串 |
  | color  | str  | 颜色   | 白色   |

* 返回值
  
  | 数据类型 | 描述   |
  | ---- | ---- |
  | bool | 是否成功 |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.clientApi import SendLocalMessage

SendGlobalMessage('游戏即将开始', header='系统>>')
# 结果: 系统>>游戏即将开始
```

### SendGlobalMessage

服务端

method in consoleLib.message.server.leftCornerNotify

* 描述
  
  聊天框发送一条消息

 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值  |
  |--------|------|------|------|
  | msg    | str  | 消息内容 |      |
  | header | str  | 消息头  | 空字符串 |
  | color  | str  | 颜色   | 白色   |

* 返回值
  
  | 数据类型 | 描述   |
  | ---- | ---- |
  | bool | 是否成功 |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *
from consoleLib.serverApi import SendGlobalMessage

SendGlobalMessage('游戏即将开始', color=ENUM.ColorCode.MINECOIN_GOLD)
```

### SendMessageToPlayer

服务端

method in consoleLib.message.server.leftCornerNotify

* 描述
  
  给指定玩家发送消息

* 参数
  
  | 参数名   | 数据类型 | 描述        | 默认值 |
  | ----- | ---- | --------- | --- |
  | pid   | str  | 接收消息的玩家ID |     |
  | msg   | str  | 消息内容      |     |
  | header | str  | 消息头  | 空字符串 |
  | color | str  | 颜色        | 白色  |

* 返回值
  
  无

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *
from consoleLib.serverApi import SendMessageToPlayer

SendMessageToPlayer(serverApi.GetPlayerList()[0], 'example_sentence', color=ENUM.ColorCode.RED)
```

## title / 标题

### SetMiddleTitle

服务端

method in consoleLib.message.server.title

* 描述
  
  设置大标题 相当于title指令

* 参数
  
  | 参数名        | 数据类型 | 描述      | 默认值   |
  | ---------- | ---- | ------- | ----- |
  | title      | str  | 主标题     | 黑色    |
  | subtitle   | str  | 副标题     | 黑色    |
  | pid        | str  | 执行的玩家ID | None  |
  | showOutput | bool | 是否显示输出  | False |

* 返回值
  
  无

* 备注
  
  只设置subtitle而不设置title美观度更高

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *
from consoleLib.serverApi import SetMiddleTitle

SetMiddleTitle('倒计时开始', '321', serverApi.GetPlayerList()[0], False)
```

## playerId / 玩家ID

### GetPlayerIdByPlayerName

服务端

method in consoleLib.playerId.server.getPlayerId

* 描述
  
  通过玩家名字 获取玩家Id

* 参数
  
  | 参数名  | 数据类型 | 描述  | 默认值 |
  | ---- | ---- | --- | --- |
  | name | str  | 玩家名 |     |

* 返回值
  
  | 数据类型     | 描述                          |
  | -------- | --------------------------- |
  | str/None | 匹配到玩家ID返回玩家ID(str) 否则返回None |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import GetPlayerIdByPlayerName

print GetPlayerIdByPlayerName('Console')
```

### GetPlayerIdByPlayerName

服务端

method in consoleLib.playerId.server.getPlayerId

* 描述
  
  通过指定UID 获取玩家ID

* 参数
  
  | 参数名 | 数据类型 | 描述      | 默认值 |
  | --- | ---- | ------- | --- |
  | uid | int  | 玩家网易UID |     |

* 返回值
  
  | 数据类型     | 描述                          |
  | -------- | --------------------------- |
  | str/None | 匹配到玩家ID返回玩家ID(str) 否则返回None |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import GetPlayerIdByUid

print GetPlayerIdByUid(-12345678987654321)
```
### GetPlayerIdByDimensionId

服务端

method in consoleLib.playerId.server.getPlayerId

* 描述
  
  获取指定维度中所有的玩家

* 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- | ---- |------| --- |
  | dimensionId | int  | 维度ID |     |

* 返回值
  
  | 数据类型              | 描述                  |
  |-------------------|---------------------|
  | list\[str\]或者list | 玩家列表 没有玩家在此维度则返回空列表 |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import GetPlayerIdByUid

print GetPlayerIdByUid(-12345678987654321)
```

### IsIdPlayerId

#### 服务端

method in consoleLib.playerId.server.isPlayerId

* 描述
  
  判断实体id是不是玩家id

* 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- |------|------| --- |
  | eid | str  | 实体id |     |

* 返回值
  
  | 数据类型 | 描述      |
  |------|---------|
  | bool | 是否是玩家id |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import IsPlayerId

print IsPlayerId(114514)
```

#### 客户端

method in consoleLib.playerId.client.isPlayerId

* 描述
  
  判断实体id是不是玩家id

* 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- |------|------| --- |
  | eid | str  | 实体id |     |

* 返回值
  
  | 数据类型 | 描述      |
  |------|---------|
  | bool | 是否是玩家id |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.clientApi import IsPlayerId

print IsPlayerId(114514)
```

## time / 时间

### GetCurrentTime

服务端 客户端

method in consoleLib.time.all.currentRealTime

* 描述
  
  获取当前时间信息

* 参数
  
  无

* 返回值
  
  | 数据类型 | 描述                  |
  | ---- | ------------------- |
  | dict | 年 月 日 时 分 秒 微秒 时区信息 |

* 备注
  
  无需区分```serverApi```和```clientApi``` 直接调用即可

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.commonApi import GetCurrentTime

print GetCurrentTime()
```

### GetDay

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.gameTime

* 描述
  
  获取从游戏开始经过的游戏天数

* 参数
  
  | 参数名  | 数据类型 | 描述                                 | 默认值  |
  | ---- | ---- | ---------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内经过的游戏天数 不传返回从游戏开始经过的游戏天数 | None |

* 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 天数  |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import GetDay

print GetDay(24000) # 结果: 1 (表示经过了1天)
```

#### 客户端接口

method in consoleLib.time.client.gameTime

* 描述
  
  获取从游戏开始经过的游戏天数

* 参数
  
  | 参数名  | 数据类型 | 描述                                 | 默认值  |
  | ---- | ---- | ---------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内经过的游戏天数 不传返回从游戏开始经过的游戏天数 | None |

* 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 天数  |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.clientApi import GetDay

print GetDay() # 结果: 游戏实际天数
```

### GetTimeOfDay

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.gameTime

* 描述
  
  获取当前游戏天内的帧数

* 参数
  
  | 参数名  | 数据类型 | 描述                              | 默认值  |
  | ---- | ---- | ------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内游戏天内的帧数 不传返回当前游戏天内的帧数 | None |

* 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 帧数  |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import GetTimeOfDay

print GetTimeOfDay()
```

#### 客户端接口

method in consoleLib.time.client.gameTime

* 描述
  
  获取当前游戏天内的帧数

* 参数
  
  | 参数名  | 数据类型 | 描述                              | 默认值  |
  | ---- | ---- | ------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内游戏天内的帧数 不传返回当前游戏天内的帧数 | None |

* 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 帧数  |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.clientApi import GetTimeOfDay

print GetTimeOfDay()
```

## position / 位置

### GetDistanceToSecondTargetPointFromPlayer

服务端 客户端

#### 服务端接口

method in consoleLib.position.server.getDistance

* 描述
  
  计算从玩家开始到玩家朝向指定位置第二个点的距离

* 参数
  
  | 参数名      | 数据类型 | 描述            | 默认值 |
  | -------- | ---- | ------------- | --- |
  | playerId | str  | 玩家ID          |     |
  | end      | int  | 第二个点的距离       |     |
  | count    | int  | 点位数量 即分成多少个坐标 |     |

* 返回值
  
  | 数据类型 | 描述          |
  | ---- | ----------- |
  | list | 坐标列表 错误时为[] |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.serverConstant import *
from consoleLib.serverApi import GetDistanceToSecondTargetPointFromPlayer

print GetDistanceToSecondTargetPointFromPlayer(serverApi.GetPlayerList()[0], 10, 1)
```

#### 客户端接口

method in consoleLib.position.client.getDistance

* 描述
  
  计算从玩家开始到玩家朝向指定位置第二个点的距离

* 参数
  
  | 参数名      | 数据类型 | 描述            | 默认值                          |
  | -------- | ---- | ------------- | ---------------------------- |
  | end      | int  | 第二个点的距离       |                              |
  | count    | int  | 点位数量 即分成多少个坐标 |                              |
  | playerId | str  | 玩家ID          | clientApi.GetLocalPlayerId() |

* 返回值
  
  | 数据类型 | 描述          |
  | ---- | ----------- |
  | list | 坐标列表 错误时为[] |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.constant.clientConstant import *
from consoleLib.clientApi import GetDistanceToSecondTargetPointFromPlayer

print GetDistanceToSecondTargetPointFromPlayer(10, 1, PLAYER_ID)
```
## command / 指令

### IsRunByPlayer

服务端

method in consoleLib.command.server.origin

* 描述
  
  判断自定义指令是否由玩家运行

* 参数
  
  | 参数名  | 数据类型 | 描述  | 默认值 |
  | ---- |------| --- | --- |
  | originArgs | dict | CustomCommandTriggerServerEvent事件触发后的原始数据 |     |

* 返回值
  
  | 数据类型 | 描述      |
  |------|---------|
  | bool | 是否由玩家运行 |

* 示例

```python
# -*- coding: utf-8 -*-
from consoleLib.serverApi import IsRunByPlayer

@Listen
def CustomCommandTriggerServerEvent(self, args):
  print IsRunByPlayer(args)
```

