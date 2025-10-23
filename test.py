import os
import pytest
from repofinder import load_environment, fetch_repo_info, parse_repo_info

# 单元测试
def test_load_environment():
    """测试环境变量加载"""
    token = load_environment()
    assert isinstance(token, str)

def test_parse_repo_info():
    """测试信息解析"""
    raw_data = {
        "name": "test-repo",
        "stargazers_count": 100,
        "forks_count": 20,
        "updated_at": "2025-10-01"
    }
    parsed = parse_repo_info(raw_data)
    assert parsed["仓库名称"] == "test-repo"
    assert parsed["星标数"] == 100
    assert parsed["复刻数"] == 20

# 整体测试（调用真实API）
@pytest.mark.skipif(not os.getenv("GITHUB_TOKEN"), reason="需要GITHUB_TOKEN")
def test_fetch_repo_info_real():
    """测试真实API调用"""
    token = load_environment()
    data = fetch_repo_info("python", "cpython", token)
    assert data["name"] == "cpython"
    assert data["stargazers_count"] > 0