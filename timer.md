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
