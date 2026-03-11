# 第 2 课：初探 FreeCAD —— 代码召唤几何体

> **"在虚无的数字空间中，用代码创造有形的实体。"**

---

## 📐 物理/数理原理

### 拓扑几何基础

在数学的**拓扑学**中，任何复杂的三维物体都可以被拆解为最基本的拓扑几何体：
- **正方体 (Box)**：由长、宽、高决定
- **球体 (Sphere)**：由半径决定
- **圆柱体 (Cylinder)**：由半径和高度决定
- **圆锥体 (Cone)**：由半径和高度决定

这些基本形状就像是数字世界的"原子"，通过组合和运算，可以构建出任何复杂的模型。

### 参数化思维

**参数化设计**是 3D 建模的核心思想：
- 不是用鼠标"画"出一个形状
- 而是用**参数**（数字）来**定义**一个形状
- 改变参数 = 改变模型

例如：
- `半径 = 10` → 小球
- `半径 = 50` → 大球
- 只需修改一个数字，模型瞬间改变！

---

## 💻 FreeCAD 脚本

让我们在坐标原点 `(0, 0, 0)` 召唤一个基础球体：

```python
import Part

# 在坐标原点召唤一个半径为 10 的球体
my_sphere = Part.makeSphere(10)

# 将球体添加到当前文档并显示出来
Part.show(my_sphere)

# 刷新视觉缓存，让 3D 视图更新
App.ActiveDocument.recompute()
```

### 代码详解

| 代码 | 说明 |
|------|------|
| `import Part` | 导入 Part 模块（FreeCAD 的零件设计模块） |
| `Part.makeSphere(10)` | 创建一个半径为 10mm 的球体几何 |
| `Part.show(...)` | 将几何体显示在 3D 视图中 |
| `App.ActiveDocument.recompute()` | 重新计算并刷新 3D 视图 |

---

## 📋 实验报告

### 观察记录

运行代码后：
1. ✅ 3D 视图中央出现了一个灰色的**球体**
2. ✅ 球体位于坐标原点 `(0, 0, 0)`
3. ✅ 左侧"组合视图"中出现了一个名为 `Sphere` 的对象
4. ✅ 球体的半径是 10mm

### 交互操作

在 3D 视图中试试这些操作：

| 操作 | 快捷键/方法 |
|------|------------|
| 旋转视角 | `Shift` + 鼠标右键拖动 |
| 平移视角 | `Shift` + 鼠标中键拖动 |
| 缩放视角 | 鼠标滚轮滚动 |
| 选择对象 | 鼠标左键点击 |
| 切换视图 | 数字键 `1`=前视图 `3`=右视图 `5`=顶视图 `7`=等轴测 |

### 参数实验

尝试修改参数，观察变化：

```python
# 实验一：改变半径
my_sphere = Part.makeSphere(20)  # 更大的球
Part.show(my_sphere)

# 实验二：创建不同形状
my_box = Part.makeBox(10, 10, 10)    # 正方体
Part.show(my_box)

my_cylinder = Part.makeCylinder(5, 20)  # 细长圆柱
Part.show(my_cylinder)
```

---

## 🛠️ 制作指南

### 完整脚本

```python
# 导入必要的模块
import Part
import FreeCAD as App

# 创建球体
my_sphere = Part.makeSphere(10)

# 显示球体
Part.show(my_sphere)

# 刷新视图
App.ActiveDocument.recompute()

# 打印成功信息
App.Console.PrintMessage("✅ 球体创建成功！\n")
App.Console.PrintMessage("📍 半径：10mm\n")
```

### 保存你的第一个模型

```python
# 保存文档
App.ActiveDocument.saveAs("/tmp/MyFirstSphere.FCStd")
App.Console.PrintMessage("💾 文档已保存到：/tmp/MyFirstSphere.FCStd\n")
```

---

## 🚀 拓展挑战

### 挑战 1：创建复合形状

创建一个"雪人"（三个球体堆叠）：

```python
import Part
from FreeCAD import Vector

# 头部
head = Part.makeSphere(8)
head_obj = App.ActiveDocument.addObject("Part::Feature", "Head")
head_obj.Shape = head
head_obj.Placement.Base = Vector(0, 0, 22)

# 身体
body = Part.makeSphere(12)
body_obj = App.ActiveDocument.addObject("Part::Feature", "Body")
body_obj.Shape = body
body_obj.Placement.Base = Vector(0, 0, 10)

# 底座
base = Part.makeSphere(16)
base_obj = App.ActiveDocument.addObject("Part::Feature", "Base")
base_obj.Shape = base

App.ActiveDocument.recompute()
```

### 挑战 2：探索更多几何体

FreeCAD 的 Part 模块提供了丰富的几何体创建函数：

```python
# 圆锥体
cone = Part.makeCone(10, 5, 20)  # (半径1, 半径2, 高度)
Part.show(cone)

# 楔形
wedge = Part.makeWedge(10, 15, 20, 5, 10, 10)
Part.show(wedge)

# 棱柱（正多边形的柱体）
prism = Part.makePrism(Part.makePolygon([Vector(0,0,0), Vector(10,0,0), Vector(10,10,0), Vector(0,10,0)]), 5)
Part.show(prism)
```

### 挑战 3：查看对象属性

```python
# 获取球体对象
sphere_obj = App.ActiveDocument.getObject("Sphere")

# 查看属性
print("对象名称：", sphere_obj.Name)
print("对象类型：", sphere_obj.TypeId)
print("包围盒：", sphere_obj.Shape.BoundBox)
print("体积：", sphere_obj.Shape.Volume)
print("表面积：", sphere_obj.Shape.Area)
```

---

## 💡 知识点总结

| 概念 | 说明 |
|------|------|
| `Part.makeSphere(r)` | 创建半径为 r 的球体 |
| `Part.makeBox(x, y, z)` | 创建长宽高分别为 x, y, z 的长方体 |
| `Part.makeCylinder(r, h)` | 创建半径为 r、高度为 h 的圆柱体 |
| `Part.show(shape)` | 将几何体显示在 3D 视图中 |
| `recompute()` | 重新计算并刷新 3D 视图 |
| `Vector(x, y, z)` | 三维向量，表示空间中的点或方向 |

---

## 🎯 下一课预告

在下一课中，我们将学习**变量**的力量——用变量控制几何体的大小和位置，体验真正的参数化设计！

👉 **继续学习：[第 3 课：控制台的魔法](../chap2/03-控制台的魔法.md)**
