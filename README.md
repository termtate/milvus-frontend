# milvus-frontend

## 运行前准备

1. 安装rye
   1. 下载rye (https://rye-up.com/guide/installation/)
   2. [添加 `%USERPROFILE%\.rye\shims` 到 Path 环境变量](https://rye-up.com/guide/installation/#add-shims-to-path)
2. 运行milvus
3. 运行[后端](https://github.com/termtate/milvus-fastapi/)

## 运行
1. `rye sync`
2. `rye run python src/main.py`