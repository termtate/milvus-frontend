# milvus-frontend

## 运行前准备

1. [安装rye](https://rye-up.com/guide/installation/)
2. 运行milvus
3. 运行[后端](https://github.com/termtate/milvus-fastapi/)
4. 控制台输入 `rye sync`

## 运行
1. 下载[PaddleOCR-json程序](https://github.com/hiroi-sora/PaddleOCR-json/releases/tag/v1.3.0)并解压到当前目录
2. `rye run main`


## 打包

1. 运行 `rye run pack`
2. 将 .venv\paddle\libs 文件夹复制粘贴到 out\main.dist\paddle 文件夹内
3. 将 .venv\qt_material 文件夹中的 fonts、resources、themes 文件夹和 material.css.template 文件复制粘贴到 out\main.dist\qt_material 文件夹内（如果没有 qt_material 文件夹就新建一个）
4. 将 .venv\LAC 文件夹下的lac_model、rank_model、seg_model 文件夹复制粘贴到 out\main.dist\LAC 文件夹内（如果没有 LAC 文件夹就新建一个）
5. 下载[PaddleOCR-json程序](https://github.com/hiroi-sora/PaddleOCR-json/releases/tag/v1.3.0)并解压到 out\main.dist 文件夹内