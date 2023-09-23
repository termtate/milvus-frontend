# ui层

## 架构
使用mvi架构。
- view订阅viewmodel的State状态，根据State的数据渲染界面，并且在需要通知viewmodel时调用viewmodel公开的方法。
- viewmodel需要公开State状态，并且公开被`asyncSlot()`装饰的async函数，提供给view作为事件的回调。同时处理好回调之后数据的改变，结合其他模块生成新的State。
- view的代码应该尽量简洁，不要过多处理业务逻辑，在遇到需要外部数据的的情况下就调用viewmodel的函数。不要在view层内修改State状态。
![mvi示意图](/images/OIP-C.jfif)  
使用mvi架构的好处：
- 分担view职责：分离业务逻辑到viewmodel里，view只需要做数据的展示工作，不需要关心数据是怎么来的
- 方便测试：要模拟任意时刻的界面只需要改变提供的State状态即可
- pyside很难实现数据的双向绑定，所以没有采用mvvm架构


## UI设计
使用 qt designer 打开assets/main.ui进行ui设计，在保存时会自动生成.py代码。注意要在生成的代码中修改`import qrc1_rc`为`import assets.qrc1_rc`.  
使用[qt-material库](https://github.com/UN-GCPDS/qt-material/tree/master)进行ui的美化.

## 外部模块依赖
使用[injector模块](https://github.com/python-injector/injector)的依赖注入功能，在构造函数上使用`@inject`装饰器，并且写上要注入类的类型注解即可以使用外部模块，具体示例参考injector模块的readme.md。

## 防止界面卡顿
为了防止网络请求等io请求造成界面的卡顿或者无响应，ui层使用[qasync模块](https://github.com/CabbageDevelopment/qasync/)结合协程，协程解决网络请求的卡顿，qasync模块实现了pyside和协程的兼容，只需要在async函数前添加装饰器即可作为按钮的回调函数，最后按照要求启动qt界面即可。  
协程只能解决网络IO的阻塞情况，对于计算密集型的代码（比如机器学习）只能新开启一个进程运行，才能避免阻塞
