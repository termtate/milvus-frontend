# milvus-frontend

## 运行前准备

1. [安装rye](https://rye-up.com/guide/installation/)
2. 运行milvus
3. 控制台输入 `rye sync`

## 运行
1. 下载[PaddleOCR-json程序](https://github.com/hiroi-sora/PaddleOCR-json/releases/tag/v1.3.0)并解压到当前目录
2. `rye run main`


## 打包

1. 运行 `rye run pack`（很可能需要科学上网）（预计时间3个小时左右）
2. 
3. 下载[PaddleOCR-json程序](https://github.com/hiroi-sora/PaddleOCR-json/releases/tag/v1.3.0)并解压到 out\main.dist 文件夹内


## 项目架构


![依赖关系示意图](images/modules.png)
- `main` 入口文件main.py
- `ui` ui层，提供gui界面，处理用户输入
- `ml` 机器学习相关模块，负责将导入的病历解析为数据库表中数据
- `db` milvus模块的业务封装，负责表的定义、分表、提供增删改查接口工作。
- `ppocr` 负责图片转文字(ocr)功能
- `milvus` `pymilvus`库的封装，负责简化milvus数据库的连接和增删改查、自动生成向量字段等功能
- `common` 包含全局设置、数据格式的定义
  
各模块通过[injector模块](https://github.com/python-injector/injector)进行依赖注入