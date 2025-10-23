# GitHub 仓库信息查询工具

## 项目概述

### 项目背景

本项目是一款基于 GitHub API 的仓库信息查询工具，核心目标是通过简洁的交互方式，快速获取指定 GitHub 仓库的关键信息。项目采用 Git 分支管理、Docker 容器化、单元测试等标准化开发技术，确保代码结构清晰、部署便捷、功能可靠，模拟真实工作场景下的项目开发与交付流程。

### 项目目标

- 实现通过 GitHub 用户名和仓库名，查询仓库核心信息的基础功能
- 采用规范的 Git 分支管理策略，保障项目迭代有序进行
- 结合 Docker 实现应用容器化部署，确保多环境运行一致性
- 编写测试用例验证核心功能，降低线上功能故障风险

## 技术栈

- &zwnj;**开发语言**&zwnj;: Python 3.12
- &zwnj;**核心依赖**&zwnj;:
  - `requests`: 用于 GitHub API 调用，获取仓库数据
  - `python-dotenv`: 加载本地环境变量（`.env` 文件），管理敏感配置
  - `pytest`: 编写和执行单元测试，验证功能正确性
- &zwnj;**容器化工具**&zwnj;: Docker
- &zwnj;**版本控制**&zwnj;: Git + GitHub
- &zwnj;**API 接口**&zwnj;: GitHub REST API v3

## 功能说明

### 核心功能

查询指定 GitHub 仓库并格式化输出以下信息：

- 仓库名称
- 星标数
- 复刻数
- 最后更新时间

repo-finder/
├── repofinder.py       # 主程序代码（核心功能实现）
├── test.py             # 测试文件（单元测试 + 整体测试）
├── requirements.txt    # 项目依赖清单（列出所有第三方库）
├── Dockerfile          # Docker 构建配置（容器化部署）
├── .dockerignore       # Docker 构建忽略文件（排除无需打包的文件）
├── .gitignore          # Git 忽略文件（避免敏感/自动生成文件提交）
└── .env                # 环境变量文件（存储 GITHUB_TOKEN，本地配置不提交）

# 环境配置与使用方法

## 本地运行

### 1. 克隆仓库
```bash
git clone git@github.com:你的用户名/你的仓库名.git
cd repo-finder  # 进入项目根目录

### 2. 安装依赖
```bash
pip install -r requirements.txt

### 3. 配置环境变量
```bash
GITHUB_TOKEN=你的个人访问令牌

### 4. 运行程序
```bash
python repofinder.py   
# 按照提示输入你的GITHUB用户名和搜索的仓库名即可完成查询

## Docker运行

### 1. 构建Docker镜像
```bash
docker build -t repo-finder .

### 2. 启动容器
```bash
docker run -v %cd%/.env:/app/.env repo-finder

## 测试运行

### 1. 安装依赖
```bash
pip install pytest

### 2. 运行测试
```bash
pytest test.py -v   # -v 显示详细测试日志


