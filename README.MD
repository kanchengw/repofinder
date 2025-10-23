# GitHub Repository Information Query Tool

## Project Overview

### Project Background

This project is a repository information query tool based on the GitHub API. Its core goal is to quickly retrieve key information of a specified GitHub repository through a concise interactive method. The project adopts standardized development technologies such as Git branch management, Docker containerization, and unit testing to ensure clear code structure, convenient deployment, and reliable functions, simulating the project development and delivery process in real work scenarios.

### Project Objectives

- Implement the basic function of querying core repository information through GitHub username and repository name
- Adopt a standardized Git branch management strategy to ensure orderly project iteration
- Achieve application containerization deployment with Docker to ensure consistency in multi-environment operation
- Write test cases to verify core functions and reduce the risk of online function failures

## Technology Stack

- &zwnj;**Programming Language**&zwnj;: Python 3.12
- &zwnj;**Core Dependencies**&zwnj;:
  - `requests`: Used for GitHub API calls to retrieve repository data
  - `python-dotenv`: Load local environment variables (`.env` file) to manage sensitive configurations
  - `pytest`: Write and execute unit tests to verify function correctness
- &zwnj;**Containerization Tool**&zwnj;: Docker
- &zwnj;**Version Control**&zwnj;: Git + GitHub
- &zwnj;**API Interface**&zwnj;: GitHub REST API v3

## Function Description

### Core Functions

Query the specified GitHub repository and format and output the following information:

- Repository Name
- Star Count
- Fork Count
- Last Update Time

# Environment Configuration and Usage Methods

## Local Run

### 1. Clone Repository
```bash
git clone git@github.com:Your Username/Your Repository Name.git
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```


### 3. Configure Environment Variables
```bash
GITHUB_TOKEN=Your Personal Access Token
```


### 4. Run
```bash
python repofinder.py   
# # Follow the prompts to enter the GitHub repository name to complete the query
```


## Docker Run

### 1. Build Docker Image
```bash
docker build -t repo-finder .
```


### 2. Run Container
```bash
docker run -v %cd%/.env:/app/.env repo-finder
```


## Run test

### 1. 安装依赖
```bash
pip install pytest request
```


### 2. Run
```bash
pytest test.py -v   # -v Show detailed test logs
```


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


# 环境配置与使用方法

## 本地运行

### 1. 克隆仓库
```bash
git clone git@github.com:你的用户名/你的仓库名.git
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```


### 3. 配置环境变量
```bash
GITHUB_TOKEN=你的个人访问令牌
```


### 4. 运行程序
```bash
python repofinder.py   
# 按照提示输入github仓库名即可完成查询
```


## Docker运行

### 1. 构建Docker镜像
```bash
docker build -t repo-finder .
```


### 2. 启动容器
```bash
docker run -v %cd%/.env:/app/.env repo-finder
```


## 测试运行

### 1. 安装依赖
```bash
pip install pytest request
```


### 2. 运行测试
```bash
pytest test.py -v   # -v 显示详细测试日志
```
