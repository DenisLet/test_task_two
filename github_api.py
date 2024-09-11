import os
import requests

# Загрузка переменных окружения из файла .env
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github.v3+json"
}

def create_repository(repo_name):
    """Создание нового публичного репозитория."""
    url = f"{BASE_URL}/user/repos"
    data = {"name": repo_name, "auto_init": True, "private": False}
    response = requests.post(url, headers=HEADERS, json=data)
    return response

def check_repository_exists(repo_name):
    """Проверка существования репозитория."""
    url = f"{BASE_URL}/repos/{os.getenv('GITHUB_USERNAME')}/{repo_name}"
    response = requests.get(url, headers=HEADERS)
    return response.status_code == 200

def delete_repository(repo_name):
    """Удаление репозитория."""
    url = f"{BASE_URL}/repos/{os.getenv('GITHUB_USERNAME')}/{repo_name}"
    response = requests.delete(url, headers=HEADERS)
    return response
