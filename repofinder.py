import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_repo_info(owner, repo):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    repo_data = response.json()
    
    return {
        "仓库名称": repo_data["name"],
        "星标数": repo_data["stargazers_count"],
        "复刻数": repo_data["forks_count"],
        "最后更新时间": repo_data["updated_at"],
        "仓库说明": repo_data.get("description", "无说明")
    }

def display_info(info):
    print("=" * 50)
    for key, value in info.items():
        print(f"{key}: {value}")
    print("=" * 50)

if __name__ == "__main__":
    owner = input("请输入仓库作者用户名: ")
    repo = input("请输入仓库名: ")
    
    try:
        repo_info = get_repo_info(owner, repo)
        display_info(repo_info)
    except Exception as e:
        print(f"查询失败: {str(e)}")