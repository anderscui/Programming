
# Basics of PyQt

PyQt 的基础组件有：

* Widgets
* Layout managers
* Dialogs
* Main windows
* Applications
* Event loops
* Signals and slots

它们都由 `PyQt5.QtWidgets` 提供。

## Widgets

QWidget 是所有 UI 对象的基类。它们具有矩形外观，包含一系列属性和方法以定制其外观和行为。

它们还可以接收鼠标点击、按键和其它事件。当 widget 捕获到事件时，会发出一个 signal，标识其状态的改变。

常见的 widgets 包括：Buttons、Line Edits 等等。

## Layout Managers

可以通过 `.resize()/.move()` 手动调整组件的位置与大小，但更方便且易于维护的还是 Layout managers。

Layout managers 自动适配于 resize 和内容改变等事件。

## Dialogs

可以创建两类 apps：

* Main Window
* Dialog

## Main Windows

多数时候，我们使用的还是 Main Window 风格的应用。需要用到 `QMainWindow` 类。

## Applications

与 `应用` 对应的是 `QApplication`，这个类型也是任何 pyqt 应用的核心。app 类负责如下事情：

* 初始化和终止
* 提供事件循环和事件处理
* 处理大部分系统级和应用级的设置
* 提供了对于全局信息的访问
* 解析命令行参数
* 定义应用的外观
* 提供本地化能力

## Event Loop

GUI 应用都是事件驱动的。函数/方法作为对于用户行为的响应，如点击按钮、选择条目、按下键盘等等。

事件通常由 loop 处理。事件循环是一个无限循环，它等待下一个事件的发生，并将其分发下去。


