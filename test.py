import pytest
import os
import requests
from dotenv import load_dotenv
from repofinder import get_repo_info, display_info

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TEST_REPO = ("octocat", "Hello-World")

def test_token_configured():
    assert GITHUB_TOKEN is not None, "缺少GITHUB_TOKEN"

def test_get_repo_info_essential_fields():
    owner, repo = TEST_REPO
    info = get_repo_info(owner, repo)
    assert "仓库名称" in info
    assert "星标数" in info
    assert "仓库说明" in info
    assert info["仓库名称"] == repo

def test_display_info_output(capsys):
    test_info = {
        "仓库名称": "test",
        "星标数": 100,
        "仓库说明": "测试描述"
    }
    display_info(test_info)
    captured = capsys.readouterr()
    assert "仓库名称: test" in captured.out
    assert "仓库说明: 测试描述" in captured.out
    assert "=" * 50 in captured.out

def test_invalid_repo_error():
    with pytest.raises(requests.exceptions.HTTPError):
        get_repo_info("invalid", "invalid")