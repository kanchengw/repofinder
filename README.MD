GitHub 仓库信息查询工具
项目概述
项目背景
本项目是一款基于 GitHub API 的仓库信息查询工具，核心目标是通过简洁的交互方式，快速获取指定 GitHub 仓库的关键信息。项目采用 Git 分支管理、Docker 容器化、单元测试等标准化开发技术，确保代码结构清晰、部署便捷、功能可靠，模拟真实工作场景下的项目开发与交付流程。

项目目标
实现通过 GitHub 用户名和仓库名，查询仓库核心信息的基础功能
采用规范的 Git 分支管理策略，保障项目迭代有序进行
结合 Docker 实现应用容器化部署，确保多环境运行一致性
编写测试用例验证核心功能，降低线上功能故障风险
技术栈
‌开发语言‌: Python 3.12
‌核心依赖‌:
requests: 用于 GitHub API 调用，获取仓库数据
python-dotenv: 加载本地环境变量（.env 文件），管理敏感配置
pytest: 编写和执行单元测试，验证功能正确性
‌容器化工具‌: Docker
‌版本控制‌: Git + GitHub
‌API 接口‌: GitHub REST API v3
功能说明
核心功能
查询指定 GitHub 仓库并格式化输出以下信息：

仓库名称
星标数（对应 API 字段：stargazers_count）
复刻数（对应 API 字段：forks_count）
最后更新时间
使用说明
安装依赖
bash
Copy Code
pip install -r requirements.txt
配置环境变量
创建 .env 文件并添加您的 GitHub 访问令牌（如果需要）：

bash
Copy Code
GITHUB_TOKEN=your_github_access_token
运行程序
bash
Copy Code
python main.py
使用 Docker 运行
bash
Copy Code
docker build -t github-repo-info .
docker run -it --rm github-repo-info
贡献指南
欢迎提交 Pull Request 或 Issue 来改进本项目。请遵循以下步骤：

Fork 本项目
创建您的分支 (git checkout -b feature/AmazingFeature)
提交您的更改 (git commit -m 'Add some AmazingFeature')
推送至分支 (git push origin feature/AmazingFeature)
创建一个新的 Pull Request
许可证
本项目采用 MIT 许可证 发布。
