import os
import unittest
from github_api import create_repository, check_repository_exists, delete_repository
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

class TestGitHubAPI(unittest.TestCase):
    def setUp(self):
        """Создание репозитория перед каждым тестом."""
        self.repo_name = os.getenv('REPO_NAME')
        # Убедитесь, что репозиторий не существует перед созданием
        if check_repository_exists(self.repo_name):
            delete_repository(self.repo_name)

    def tearDown(self):
        """Удаление репозитория после каждого теста."""
        if check_repository_exists(self.repo_name):
            delete_repository(self.repo_name)

    def test_create_repository(self):
        """Тестирование создания репозитория."""
        response = create_repository(self.repo_name)
        print(f"Create response status: {response.status_code}")
        #print(f"Create response body: {response.json()}")
        self.assertEqual(response.status_code, 201, "Не удалось создать репозиторий")
        # Проверяем, что репозиторий действительно создан
        exists = check_repository_exists(self.repo_name)
        self.assertTrue(exists, "Репозиторий не найден после создания")

    def test_check_repository_exists(self):
        """Тестирование проверки наличия репозитория."""
        # Создаем репозиторий для проверки
        create_repository(self.repo_name)
        exists = check_repository_exists(self.repo_name)
        self.assertTrue(exists, "Репозиторий не найден после создания")

    def test_delete_repository(self):
        """Тестирование удаления репозитория."""
        # Создаем репозиторий перед удалением
        create_repository(self.repo_name)
        response = delete_repository(self.repo_name)
        print(f"Delete response status: {response.status_code}")
        self.assertEqual(response.status_code, 204, "Не удалось удалить репозиторий")
        # Проверяем, что репозиторий действительно удален
        exists = check_repository_exists(self.repo_name)
        self.assertFalse(exists, "Репозиторий все еще существует после удаления")

if __name__ == "__main__":
    unittest.main()
