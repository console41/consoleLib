### minX minY minZ maxX maxY maxZ

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  X Y Z的最大(小)坐标

### minPoint maxPoint

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  最大(小)角点坐标

### width height depth

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  X Y Z轴方向长度

### centerX centerY centerZ

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  X  Y Z轴中心点坐标

### center

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  包围盒中心点三维坐标

### volume

attribute in consoleLib.maths.common.aabb.AABB

- 描述
  
  AABB体积

### 特殊用法

### \_\_contains__

method in consoleLib.maths.common.aabb.AABB

- 描述
  
  魔法方法
  
  用于判断一个坐标是否包含在该AABB内 也可判断一个AABB是否在另一个AABB内

- 示例
  
  ```python
  aabb = AABB((-1, -1, -1), (1, 1, 1))
  aabb1 = AABB((-0.5, -0.5 ,-0.5), (0.5, 0.5, 0.5))
  print (0, 0, 0) in aabb # True
  print aabb1 in aabb # True
  ```

### \_\_str__

method in consoleLib.maths.common.aabb.AABB

- 描述
  
  魔法方法
  
  在print的时候将实例转换成可读性更好的字符串

- 示例
  
  ```python
  aabb = AABB((-1, -1, -1), (1, 1, 1))
  print AABB
  # AABB(min=(-1.0,-1.0,-1.0), max=(1.0,1.0,1.0))
  ```

### \_\_eq__

method in consoleLib.maths.common.aabb.AABB

- 描述
  魔法方法
  使用 `==` 运算符比较两个实例时触发 判断两个AABB边界是否完全一致

- 示例
  
  ```python
  box1 = AABB((0, 0, 0), (2, 2, 2))
  box2 = AABB((0, 0, 0), (2, 2, 2))
  print box1 == box2
  # True
  ```

### \_\_ne__

method in consoleLib.maths.common.aabb.AABB

- 描述
  魔法方法
  使用 `!=` 运算符比较两个实例时触发 判断两个AABB边界是否不相同

- 示例
  
  ```python
  box1 = AABB((0, 0, 0), (2, 2, 2))
  box2 = AABB((1, 1, 1), (3, 3, 3))
  print box1 != box2
  # True
  ```
  
  > 
