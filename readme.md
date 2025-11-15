# ConsoleLib文档

## 目录

<!-- TOC -->
* [ConsoleLib文档](#consolelib文档)
  * [目录](#目录)
  * [constant](#constant)
  * [control / 控制](#control--控制)
    * [FullScreenUI](#fullscreenui)
  * [item / 物品](#item--物品)
    * [CreateItemDict](#createitemdict)
    * [HaveItem](#haveitem)
  * [message / 消息](#message--消息)
    * [SendLocalMessage](#sendlocalmessage)
    * [SendGlobalMessage](#sendglobalmessage)
    * [SendMessageToPlayer](#sendmessagetoplayer)
  * [title / 标题](#title--标题)
    * [SetMiddleTitle](#setmiddletitle)
  * [playerId / 玩家ID](#playerid--玩家id)
    * [GetPlayerIdByPlayerName](#getplayeridbyplayername)
    * [GetPlayerIdByPlayerUid](#getplayeridbyplayeruid)
    * [GetPlayerIdByDimensionId](#getplayeridbydimensionid)
    * [IsIdPlayerId](#isidplayerid)
      * [服务端接口](#服务端接口)
      * [客户端接口](#客户端接口)
  * [time / 时间](#time--时间)
    * [AddTimer](#addtimer)
      * [服务端接口](#服务端接口-1)
      * [客户端接口](#客户端接口-1)
    * [AddRepeatedTimer](#addrepeatedtimer)
      * [服务端接口](#服务端接口-2)
      * [客户端接口](#客户端接口-2)
    * [Start](#start)
      * [服务端接口](#服务端接口-3)
      * [客户端接口](#客户端接口-3)
    * [Pause](#pause)
      * [服务端接口](#服务端接口-4)
      * [客户端接口](#客户端接口-4)
    * [Cancel](#cancel)
      * [服务端接口](#服务端接口-5)
      * [客户端接口](#客户端接口-5)
    * [GetDay](#getday)
      * [服务端接口](#服务端接口-6)
      * [客户端接口](#客户端接口-6)
    * [GetTimeOfDay](#gettimeofday)
      * [服务端接口](#服务端接口-7)
      * [客户端接口](#客户端接口-7)
  * [position / 位置](#position--位置)
    * [GetEuclideanDistance](#geteuclideandistance)
    * [GetNearestEntity](#getnearestentity)
      * [服务端接口](#服务端接口-8)
      * [客户端接口](#客户端接口-8)
    * [GetNearestPlayer](#getnearestplayer)
      * [服务端接口](#服务端接口-9)
      * [客户端接口](#客户端接口-9)
    * [GetPosFromPlayerRot](#getposfromplayerrot)
      * [服务端接口](#服务端接口-10)
      * [客户端接口](#客户端接口-10)
    * [GetPlayerHandPos](#getplayerhandpos)
  * [random / 随机数](#random--随机数)
    * [CanEventHappenByProbability](#caneventhappenbyprobability)
  * [command / 指令](#command--指令)
    * [IsRunByPlayer](#isrunbyplayer)
<!-- TOC -->

## constant

constant储存了组件工厂```clientApi.GetEngineCompFactory()```的组件 避免重复获取
还储存了一些量 如```serverApi.GetMinecraftEnum()```
需要注意的是 一些constant需要传入玩家ID

示例:

```python
# --- coding: utf-8 ---
from consoleLib.constant.serverConstant import *

for pid in serverApi.GetPlayerList():
    print NameComp(pid).GetName()
```

## control / 控制

### FullScreenUI

客户端

method in consoleLib.control.client.ui

- 描述
  
  全屏UI 玩家无法移动 GUI界面隐藏

- 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值 |
  | ------ | ---- | ---- | --- |
  | isOpen | bool | 是否开启 |     |

- 返回值
  
  无

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import FullScreenUI
  
  FullScreenUI(True)
  ```

## item / 物品

### CreateItemDict

服务端 客户端

method in consoleLib.item.itemDict

- 描述
  
  构造物品信息字典

- 参数
  
  | 参数名            | 数据类型                    | 描述                                  | 默认值  |
  | -------------- | ----------------------- | ----------------------------------- | ---- |
  | newItemName    |                         | 必须设置 物品的identifier                  |      |
  | newAuxValue    |                         | 必须设置 物品附加值                          | 0    |
  | count          |                         | 必须设置 物品数量 设置为0时为空物品                 | 1    |
  | showInHand     |                         | 可选 是否显示在手上                          | True |
  | enchantData    | list\[tuple\[str, str]] | 可选 附魔数据                             | None |
  | modEnchantData | list\[tuple\[str, str]] | 可选 自定义附魔数据                          | None |
  | customTips     |                         | 可选 物品的自定义tips 修改该内容后会覆盖实例的组件        | ''   |
  | extraId        |                         | 可选 物品自定义标识符 可以用于保存数据 区分物品           | ''   |
  | userData       |                         | 可选 物品userData 用于灾厄旗帜、旗帜等物品 请勿随意设置该值 | None |
  | durability     |                         | 可选 物品耐久度 不存在耐久概念的物品默认值为0            | 0    |
  | itemName       |                         | 废弃 1.22及以前版本的旧identifier            | ''   |
  | auxValue       |                         | 废弃 1.22及以前版本的旧物品附加值                 | 0    |

- 返回值
  
  无

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.commonApi import CreateItemDict
  
  print CreateItemDict('console:item')
  # {'newAuxValue': 0, 'newItemName': 'console:item', 'count': 1}
  ```

### HaveItem

服务端

method in consoleLib.item.haveItem

- 描述
  
  判断玩家是否有指定物品

- 参数
  
  | 参数名      | 数据类型 | 描述    | 默认值 |
  | -------- | ---- | ----- | --- |
  | pid      | str  | 玩家ID  |     |
  | itemName | str  | 物品标识符 |     |

- 返回值
  
  无

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import HaveItem
  
  print HaveItem(serverApi.GetPlayerList()[0], 'minecraft:diamond')
  ```

## message / 消息

### SendLocalMessage

客户端

method in consoleLib.message.client.leftCornerNotify

- 描述
  
  客户端发送一条消息

- 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值  |
  | ------ | ---- | ---- | ---- |
  | msg    | str  | 消息内容 |      |
  | header | str  | 消息头  | 空字符串 |
  | color  | str  | 颜色   | 白色   |

- 返回值
  
  | 数据类型 | 描述   |
  | ---- | ---- |
  | bool | 是否成功 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import SendLocalMessage
  
  SendGlobalMessage('游戏即将开始', header='系统>>')
  # 结果: 系统>>游戏即将开始
  ```

### SendGlobalMessage

服务端

method in consoleLib.message.server.leftCornerNotify

- 描述
  
  聊天框发送一条消息

- 参数
  
  | 参数名    | 数据类型 | 描述   | 默认值  |
  | ------ | ---- | ---- | ---- |
  | msg    | str  | 消息内容 |      |
  | header | str  | 消息头  | 空字符串 |
  | color  | str  | 颜色   | 白色   |

- 返回值
  
  | 数据类型 | 描述   |
  | ---- | ---- |
  | bool | 是否成功 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import SendGlobalMessage
  
  SendGlobalMessage('游戏即将开始', color=ENUM.ColorCode.MINECOIN_GOLD)
  ```

### SendMessageToPlayer

服务端

method in consoleLib.message.server.leftCornerNotify

- 描述
  
  给指定玩家发送消息

- 参数
  
  | 参数名    | 数据类型 | 描述        | 默认值  |
  | ------ | ---- | --------- | ---- |
  | pid    | str  | 接收消息的玩家ID |      |
  | msg    | str  | 消息内容      |      |
  | header | str  | 消息头       | 空字符串 |
  | color  | str  | 颜色        | 白色   |

- 返回值
  
  无

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import SendMessageToPlayer
  
  SendMessageToPlayer(serverApi.GetPlayerList()[0], 'example_sentence', color=ENUM.ColorCode.RED)
  ```

## title / 标题

### SetMiddleTitle

服务端

method in consoleLib.message.server.title

- 描述
  
  设置大标题 相当于title指令

- 参数
  
  | 参数名        | 数据类型 | 描述      | 默认值   |
  | ---------- | ---- | ------- | ----- |
  | title      | str  | 主标题     | 黑色    |
  | subtitle   | str  | 副标题     | 黑色    |
  | pid        | str  | 执行的玩家ID | None  |
  | showOutput | bool | 是否显示输出  | False |

- 返回值
  
  无

- 备注
  
  只设置subtitle而不设置title美观度更高

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import SetMiddleTitle
  
  SetMiddleTitle('倒计时开始', '321', serverApi.GetPlayerList()[0], False)
  ```

## playerId / 玩家ID

### GetPlayerIdByPlayerName

服务端

method in consoleLib.playerId.server.getPlayerId

- 描述
  
  通过玩家名字 获取玩家Id

- 参数
  
  | 参数名  | 数据类型 | 描述  | 默认值 |
  | ---- | ---- | --- | --- |
  | name | str  | 玩家名 |     |

- 返回值
  
  | 数据类型     | 描述                          |
  | -------- | --------------------------- |
  | str/None | 匹配到玩家ID返回玩家ID(str) 否则返回None |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import GetPlayerIdByPlayerName
  
  print GetPlayerIdByPlayerName('Console')
  ```

### GetPlayerIdByPlayerUid

服务端

method in consoleLib.playerId.server.getPlayerId

- 描述
  
  通过指定UID 获取玩家ID

- 参数
  
  | 参数名 | 数据类型 | 描述      | 默认值 |
  | --- | ---- | ------- | --- |
  | uid | int  | 玩家网易UID |     |

- 返回值
  
  | 数据类型     | 描述                          |
  | -------- | --------------------------- |
  | str/None | 匹配到玩家ID返回玩家ID(str) 否则返回None |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import GetPlayerIdByUid
  
  print GetPlayerIdByUid(-12345678987654321)
  ```

### GetPlayerIdByDimensionId

服务端

method in consoleLib.playerId.server.getPlayerId

- 描述
  
  获取指定维度中所有的玩家

- 参数
  
  | 参数名         | 数据类型 | 描述   | 默认值 |
  | ----------- | ---- | ---- | --- |
  | dimensionId | int  | 维度ID |     |

- 返回值
  
  | 数据类型               | 描述                  |
  | ------------------ | ------------------- |
  | list\[str\]\| list | 玩家列表 没有玩家在此维度则返回空列表 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import GetPlayerIdByUid
  
  print GetPlayerIdByUid(-12345678987654321)
  ```

### IsIdPlayerId

#### 服务端接口

method in consoleLib.playerId.server.isPlayerId

- 描述
  
  判断实体id是不是玩家id

- 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- | ---- | ---- | --- |
  | eid | str  | 实体id |     |

- 返回值
  
  | 数据类型 | 描述      |
  | ---- | ------- |
  | bool | 是否是玩家id |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import IsIdPlayerId
  
  print IsPlayerId(6666666666666)
  ```

#### 客户端接口

method in consoleLib.playerId.client.isPlayerId

- 描述
  
  判断实体id是不是玩家id

- 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- | ---- | ---- | --- |
  | eid | str  | 实体id |     |

- 返回值
  
  | 数据类型 | 描述      |
  | ---- | ------- |
  | bool | 是否是玩家id |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import IsIdPlayerId
  
  print IsPlayerId(6666666666666)
  ```

## time / 时间

### AddTimer

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.timer

- 描述
  
  添加一次性定时器 使用Python标准库threading编写

- 参数
  
  | 参数名      | 数据类型     | 描述        | 默认值 |
  | -------- | -------- | --------- | --- |
  | interval | float    | 定时器触发延迟时间 |     |
  | function | function | 要执行的函数    |     |
  | args     | tuple    | 函数的位置参数   | ()  |
  | kwargs   | dict     | 函数的关键字参数  | {}  |

- 返回值
  
  | 数据类型         | 描述       |
  | ------------ | -------- |
  | OneShotTimer | 一次性计时器实例 |

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  from consoleLib.serverApi import AddTimer
  
  def CallBack(*args, **kwargs):
      print args, kwargs
  
  AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

#### 客户端接口

method in consoleLib.time.client.timer

- 描述
  
  添加一次性定时器 使用Python标准库threading编写

- 参数
  
  | 参数名      | 数据类型     | 描述        | 默认值 |
  | -------- | -------- | --------- | --- |
  | interval | float    | 定时器触发延迟时间 |     |
  | function | function | 要执行的函数    |     |
  | args     | tuple    | 函数的位置参数   | ()  |
  | kwargs   | dict     | 函数的关键字参数  | {}  |

- 返回值
  
  | 数据类型         | 描述       |
  | ------------ | -------- |
  | OneShotTimer | 一次性计时器实例 |

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  from consoleLib.clientApi import AddTimer
  
  def CallBack(*args, **kwargs):
      print args, kwargs
  
  AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

### AddRepeatedTimer

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.timer

- 描述
  
  添加重复定时器 使用Python标准库threading编写

- 参数
  
  | 参数名      | 数据类型     | 描述        | 默认值 |
  | -------- | -------- | --------- | --- |
  | interval | float    | 定时器触发间隔时间 |     |
  | function | function | 要执行的函数    |     |
  | args     | tuple    | 函数的位置参数   | ()  |
  | kwargs   | dict     | 函数的关键字参数  | {}  |

- 返回值
  
  | 数据类型          | 描述      |
  | ------------- | ------- |
  | RepeatedTimer | 重复计时器实例 |

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  from consoleLib.serverApi import AddRepeatedTimer
  
  def CallBack(*args, **kwargs):
      print args, kwargs
  
  AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

#### 客户端接口

method in consoleLib.time.client.timer

- 描述
  
  添加重复定时器 使用Python标准库threading编写

- 参数
  
  | 参数名      | 数据类型     | 描述        | 默认值 |
  | -------- | -------- | --------- | --- |
  | interval | float    | 定时器触发间隔时间 |     |
  | function | function | 要执行的函数    |     |
  | args     | tuple    | 函数的位置参数   | ()  |
  | kwargs   | dict     | 函数的关键字参数  | {}  |

- 返回值
  
  | 数据类型          | 描述      |
  | ------------- | ------- |
  | RepeatedTimer | 重复计时器实例 |

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  from consoleLib.clientApi import AddRepeatedTimer
  
  def CallBack(*args, **kwargs):
      print args, kwargs
  
  AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

### Start

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.timer.BaseTimer

- 描述
  
  启动定时器

- 参数
  
  无

- 返回值
  
  返回自身

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  timer = AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

#### 客户端接口

method in consoleLib.time.client.timer.BaseTimer

- 描述
  
  启动定时器

- 参数
  
  无

- 返回值
  
  返回自身

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  timer = AddTimer(1.0, CallBack, (1, 2, 3), {'playerId': -1}).Start()
  ```

### Pause

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.timer.BaseTimer

- 描述
  
  暂停定时器 并在指定时间后自动恢复

- 参数
  
  | 参数名        | 数据类型        | 描述                | 默认值  |
  | ---------- | ----------- | ----------------- | ---- |
  | resumeTime | float\|None | 指定暂停的时间 不传则不会自动恢复 | None |

- 返回值
  
  无返回值

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  
  # 暂停5秒 并在5秒后自动恢复
  timer.Pause(5)
  
  # 暂停5秒 但是提前被手动恢复
  timer.Pause(5)
  import time
  time.sleep(2)
  timer.Resume()
  ```

#### 客户端接口

method in consoleLib.time.client.timer.BaseTimer

- 描述
  
  暂停定时器 并在指定时间后自动恢复

- 参数
  
  | 参数名        | 数据类型        | 描述                | 默认值  |
  | ---------- | ----------- | ----------------- | ---- |
  | resumeTime | float\|None | 指定暂停的时间 不传则不会自动恢复 | None |

- 返回值
  
  无返回值

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  
  # 暂停5秒 但是提前被取消
  timer.Pause(5)
  import time
  time.sleep(2)
  timer.Cancel()
  ```

### Cancel

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.timer.BaseTimer

- 描述
  
  取消定时器 此操作不可逆

- 参数
  
  无

- 返回值
  
  无返回值

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  timer.Cancel()
  ```

#### 客户端接口

method in consoleLib.time.client.timer.BaseTimer

- 描述
  
  取消定时器 此操作不可逆

- 参数
  
  无

- 返回值
  
  无返回值

- 示例
  
  ```python
  # -*- coding: utf-8 -*-
  timer.Cancel()
  ```

### GetDay

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.gameTime

- 描述
  
  获取从游戏开始经过的游戏天数

- 参数
  
  | 参数名  | 数据类型 | 描述                                 | 默认值  |
  | ---- | ---- | ---------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内经过的游戏天数 不传返回从游戏开始经过的游戏天数 | None |

- 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 天数  |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import GetDay
  
  print GetDay(24000)  # 结果: 1 (表示经过了1天)
  ```

#### 客户端接口

method in consoleLib.time.client.gameTime

- 描述
  
  获取从游戏开始经过的游戏天数

- 参数
  
  | 参数名  | 数据类型 | 描述                                 | 默认值  |
  | ---- | ---- | ---------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内经过的游戏天数 不传返回从游戏开始经过的游戏天数 | None |

- 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 天数  |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import GetDay
  
  print GetDay()  # 结果: 游戏实际天数
  ```

### GetTimeOfDay

服务端 客户端

#### 服务端接口

method in consoleLib.time.server.gameTime

- 描述
  
  获取当前游戏天内的帧数

- 参数
  
  | 参数名  | 数据类型 | 描述                              | 默认值  |
  | ---- | ---- | ------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内游戏天内的帧数 不传返回当前游戏天内的帧数 | None |

- 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 帧数  |

- 示例

```python
# --- coding: utf-8 ---
from consoleLib.serverApi import GetTimeOfDay

print GetTimeOfDay()
```

#### 客户端接口

method in consoleLib.time.client.gameTime

- 描述
  
  获取当前游戏天内的帧数

- 参数
  
  | 参数名  | 数据类型 | 描述                              | 默认值  |
  | ---- | ---- | ------------------------------- | ---- |
  | time | int  | 传入数字则计算帧数内游戏天内的帧数 不传返回当前游戏天内的帧数 | None |

- 返回值
  
  | 数据类型 | 描述  |
  | ---- | --- |
  | int  | 帧数  |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import GetTimeOfDay
  
  print GetTimeOfDay()
  ```

## position / 位置

### GetEuclideanDistance

服务端 客户端

method in consoleLib.position.common.getDistance

- 描述
  
  计算两个三元组表示的点之间的欧几里得距离

- 参数
  
  | 参数名    | 数据类型                         | 描述      | 默认值 |
  | ------ | ---------------------------- | ------- | --- |
  | point1 | tuple\[float, float, float\] | 第1个点的坐标 |     |
  | point2 | tuple\[float, float, float\] | 第2个点的坐标 |     |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.commonApi import GetEuclideanDistance
  
  GetEuclideanDistance((0, 0, 0), (1, 1, 1))
  ```

### GetNearestEntity

#### 服务端接口

method in consoleLib.position.server.getEntities

- 描述
  
  获取离当前一点最近的实体

- 参数
  
  | 参数名          | 数据类型                         | 描述          | 默认值  |
  | ------------ | ---------------------------- | ----------- | ---- |
  | point        | tuple\[float, float, float\] | 坐标          |      |
  | exceptedList | list\[str\]                  | 需要排除的玩家id列表 | \[\] |

- 返回值
  
  | 数据类型                        | 描述        |
  | --------------------------- | --------- |
  | tuple\[list\[str\], float\] | 实体id列表和距离 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import GetNearestEntity
  
  eid, distance = GetNearestEntity(PosComp(serverApi.GetPlayerList()[0]).GetPos())
  ```

#### 客户端接口

method in consoleLib.position.client.getEntities

- 描述
  
  获取离当前一点最近的实体

- 参数
  
  | 参数名          | 数据类型                         | 描述          | 默认值  |
  | ------------ | ---------------------------- | ----------- | ---- |
  | point        | tuple\[float, float, float\] | 坐标          |      |
  | exceptedList | list\[str\]                  | 需要排除的玩家id列表 | \[\] |

- 返回值
  
  | 数据类型                        | 描述        |
  | --------------------------- | --------- |
  | tuple\[list\[str\], float\] | 实体id列表和距离 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import GetNearestEntity
  
  eid, distance GetNearestEntity((0, 0, 0))
  ```

### GetNearestPlayer

#### 服务端接口

method in consoleLib.position.server.getEntities

- 描述
  
  获取离当前一点最近的玩家

- 参数
  
  | 参数名          | 数据类型                         | 描述          | 默认值  |
  | ------------ | ---------------------------- | ----------- | ---- |
  | point        | tuple\[float, float, float\] | 坐标          |      |
  | exceptedList | list\[str\]                  | 需要排除的玩家id列表 | \[\] |

- 返回值
  
  | 数据类型                        | 描述        |
  | --------------------------- | --------- |
  | tuple\[list\[str\], float\] | 玩家id列表和距离 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import GetNearestPlayer
  
  pid, distance GetNearestPlayer(PosComp(serverApi.GetPlayerList()[0]).GetPos())
  ```

#### 客户端接口

method in consoleLib.position.client.getEntities

- 描述
  
  获取离当前一点最近的玩家

- 参数
  
  | 参数名          | 数据类型                         | 描述          | 默认值  |
  | ------------ | ---------------------------- | ----------- | ---- |
  | point        | tuple\[float, float, float\] | 坐标          |      |
  | exceptedList | list\[str\]                  | 需要排除的玩家id列表 | \[\] |

- 返回值
  
  | 数据类型                        | 描述        |
  | --------------------------- | --------- |
  | tuple\[list\[str\], float\] | 玩家id列表和距离 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.clientApi import GetNearestPlayer
  
  pid, distance GetNearestPlayer((0, 0, 0))
  ```

### GetPosFromPlayerRot

服务端 客户端

#### 服务端接口

method in consoleLib.position.server.getPos

- 描述
  
  计算玩家朝向向前指定距离的坐标

- 参数
  
  | 参数名      | 数据类型 | 描述            | 默认值 |
  | -------- | ---- | ------------- | --- |
  | playerId | str  | 玩家ID          |     |
  | end      | int  | 第二个点的距离       |     |
  | count    | int  | 点位数量 即分成多少个坐标 |     |

- 返回值
  
  | 数据类型 | 描述          |
  | ---- | ----------- |
  | list | 坐标列表 错误时为[] |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.serverApi import GetPosFromPlayerRot
  
  print GetPosFromPlayerRot(serverApi.GetPlayerList()[0], 10, 1)
  ```

#### 客户端接口

method in consoleLib.position.client.getPos

- 描述
  
  计算玩家朝向向前指定距离的坐标

- 参数
  
  | 参数名      | 数据类型 | 描述            | 默认值                          |
  | -------- | ---- | ------------- | ---------------------------- |
  | end      | int  | 第二个点的距离       |                              |
  | count    | int  | 点位数量 即分成多少个坐标 |                              |
  | playerId | str  | 玩家ID          | clientApi.GetLocalPlayerId() |

- 返回值
  
  | 数据类型 | 描述          |
  | ---- | ----------- |
  | list | 坐标列表 错误时为[] |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.clientConstant import *
  from consoleLib.clientApi import GetPosFromPlayerRot
  
  print GetPosFromPlayerRot(10, 1, PLAYER_ID)
  ```

### GetPlayerHandPos

服务端 客户端

method in consoleLib.position.common.getPos

- 描述
  
  获取玩家手的位置

- 参数
  
  | 参数名 | 数据类型 | 描述   | 默认值 |
  | --- | ---- | ---- | --- |
  | pid | str  | 玩家ID |     |

- 返回值
  
  | 数据类型                        | 描述     |
  | --------------------------- | ------ |
  | tuple\[float, float, float] | 玩家手的位置 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.constant.serverConstant import *
  from consoleLib.commonApi import GetPlayerHandPos
  
  print GetPlayerHandPos(serverApi.GetPlayerList[0])
  ```

## random / 随机数

### CanEventHappenByProbability

服务端 客户端

method in consoleLib.random.common.probability

- 描述
  
  判断事件是否以给定概率发生

- 参数
  
  | 参数名         | 数据类型  | 描述                  | 默认值 |
  | ----------- | ----- | ------------------- | --- |
  | probability | float | 0-1之间的浮点数 表示事件发生的概率 |     |

- 返回值
  
  | 数据类型 | 描述                    |
  | ---- | --------------------- |
  | bool | True表示事件发生 False表示不发生 |

- 示例
  
  ```python
  from consoleLib.commonApi import CanEventHappenByProbability
  
  if CanEventHappenByProbability(85%):
    print 'consolelib'
  ```

## command / 指令

### IsRunByPlayer

服务端

method in consoleLib.command.server.origin

- 描述
  
  判断自定义指令是否由玩家运行

- 参数
  
  | 参数名        | 数据类型 | 描述                                        | 默认值 |
  | ---------- | ---- | ----------------------------------------- | --- |
  | originArgs | dict | CustomCommandTriggerServerEvent事件触发后的原始数据 |     |

- 返回值
  
  | 数据类型 | 描述      |
  | ---- | ------- |
  | bool | 是否由玩家运行 |

- 示例
  
  ```python
  # --- coding: utf-8 ---
  from consoleLib.serverApi import IsRunByPlayer
  
  @Listen
  def CustomCommandTriggerServerEvent(self, args):
    print IsRunByPlayer(args)
  ```
