# ui层

## 架构
使用mvi架构。
- view订阅viewmodel的State状态，根据State的数据渲染界面，并且在需要通知viewmodel时调用viewmodel公开的方法。
- viewmodel公开被`asyncSlot()`装饰的async函数，提供给view作为事件的回调。同时处理好回调之后数据的改变，结合其他模块生成新的数据。
- view的代码应该尽量简洁，不要过多处理业务逻辑，在遇到需要外部数据的的情况下就调用viewmodel的函数，不要在view层内修改State状态。
![mvi示意图](/assets/OIP-C.jfif)


## 外部模块依赖
使用injector模块的依赖注入功能，在构造函数上使用`@inject`装饰器，并且写上要注入类的类型注解即可以使用外部模块。

## 防止界面卡顿
为了防止网络请求等io请求造成界面的卡顿或者无响应，ui层使用qasync模块结合协程，协程解决网络请求的卡顿，qasync模块实现了pyside和协程的兼容，只需要在async函数前添加装饰器即可作为按钮的回调函数，最后按照要求启动qt界面即可。
