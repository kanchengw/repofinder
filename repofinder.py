import os
import requests
from dotenv import load_dotenv

def load_environment():
    """加载本地环境变量（从.env文件中读取GITHUB_TOKEN）"""
    load_dotenv()
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        raise ValueError("请在.env文件中配置GITHUB_TOKEN环境变量")
    return github_token

def fetch_repo_info(owner: str, repo: str, token: str) -> dict:
    """
    调用GitHub API获取仓库信息
    :param owner: GitHub用户名
    :param repo: 仓库名
    :param token: GitHub个人访问令牌
    :return: 仓库信息字典（含星标数、更新时间等）
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def parse_repo_info(data: dict) -> dict:
    """
    解析API返回的仓库信息
    """
    return {
        "仓库名称": data.get("name", "未知"),
        "星标数": data.get("stargazers_count", 0),
        "复刻数": data.get("forks_count", 0),
        "最后更新时间": data.get("updated_at", "未知")
    }

def display_repo_info(info: dict) -> None:
    """打印格式化后的仓库信息"""
    print("=== GitHub仓库信息（初版） ===")
    for key, value in info.items():
        print(f"{key}: {value}")

def main():
    """主函数：串联所有功能流程"""
    try:
        token = load_environment()
        owner = input("请输入GitHub用户名：")
        repo = input("请输入仓库名：")
        raw_data = fetch_repo_info(owner, repo, token)
        parsed_info = parse_repo_info(raw_data)
        display_repo_info(parsed_info)
    except ValueError as ve:
        print(f"环境变量错误：{str(ve)}")
    except requests.exceptions.HTTPError as he:
        print(f"API请求错误：{str(he)}")
    except Exception as e:
        print(f"未知错误：{str(e)}")

if __name__ == "__main__":
    main()