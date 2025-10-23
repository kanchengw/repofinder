GitHub 仓库信息查询工具
项目概述
项目背景
本项目是一款基于 GitHub API 的仓库信息查询工具，核心目标是通过简洁的交互的方式，快速获取指定 GitHub 仓库的关键信息。项目采用 Git 分支管理、Docker 容器化、单元测试 等标准化开发技术，确保代码结构清晰、部署便捷、功能可靠，模拟真实工作场景下的项目开发与交付流程。
项目目标
实现通过 GitHub 用户名和仓库名，查询仓库核心信息的基础功能
采用规范的 Git 分支管理策略，保障项目迭代有序进行
结合 Docker 实现应用容器化部署，确保多环境运行一致性
编写测试用例验证核心功能，降低线上功能故障风险
技术栈
开发语言：Python 3.12
核心依赖：
requests：用于 GitHub API 调用，获取仓库数据
python-dotenv：加载本地环境变量（.env 文件），管理敏感配置
pytest：编写和执行单元测试，验证功能正确性
容器化工具：Docker
版本控制：Git + GitHub
API 接口：GitHub REST API v3
功能说明
核心功能
查询指定 GitHub 仓库并格式化输出以下信息：
仓库名称
星标数（对应 API 字段：stargazers_count）
复刻数（对应 API 字段：forks_count）
最后更新时间
待迭代功能（feature 分支开发）
新增仓库作者信息展示
恢复仓库描述信息展示
项目结构
repo-finder/
├── repofinder.py          # 主程序代码（核心功能实现）
├── test.py                # 测试文件（单元测试 + 整体测试）
├── requirements.txt       # 项目依赖清单（列出所有第三方库）
├── Dockerfile             # Docker 构建配置（容器化部署）
├── .dockerignore          # Docker 构建忽略文件（排除无需打包的文件）
├── .gitignore             # Git 忽略文件（避免敏感/自动生成文件提交）
└── .env                   # 环境变量文件（存储 GITHUB_TOKEN，本地配置不提交）

环境配置与使用方法
本地运行
克隆仓库
git clone git@github.com:你的用户名/你的仓库名.git
cd repo-finder  # 进入项目根目录

安装依赖
pip install -r requirements.txt

配置环境变量
在项目根目录创建 .env 文件，添加内容：
GITHUB_TOKEN=你的GitHub个人访问令牌

令牌生成指南：GitHub 个人访问令牌生成教程（需勾选 public_repo 权限）
运行程序
python repofinder.py

按照终端提示输入 GitHub 用户名和仓库名，即可获取查询结果。
Docker 运行
构建 Docker 镜像
docker build -t repo-finder .  # 镜像名称为 repo-finder

启动容器（挂载本地 .env 文件）
Windows 系统：
docker run -v %cd%/.env:/app/.env repo-finder

Mac/Linux 系统：
docker run -v $(pwd)/.env:/app/.env repo-finder

测试运行
确保已安装测试依赖（若未安装）：
pip install pytest

执行测试用例：
pytest test.py -v  # -v 显示详细测试日志

分支管理
分支结构
分支名称
功能定位
合并来源
合并目标
main
主分支（稳定可部署版本）
staging
无
staging
预发布分支（测试验证）
dev
main
dev
开发分支（功能集成）
feature/*
staging
feature/*
功能分支（单个功能开发）
无（基于 dev 创建）
dev

注意事项
敏感信息保护：GITHUB_TOKEN 存储在 .env 文件中，已添加到 .gitignore，禁止提交至 GitHub；若不慎提交，需立即在 GitHub 作废该令牌并重新生成
版本兼容：项目基于 Python 3.12 开发，本地运行时建议使用相同版本，避免语法或依赖兼容性问题
API 调用限制：GitHub API 存在调用频率限制（未登录用户每小时 60 次，登录用户每小时 5000 次），使用个人令牌可提升限制额度，避免高频次连续调用导致报错
分支规范：禁止直接在 main/staging/dev 分支修改代码，所有功能开发必须在 feature/* 分支进行
