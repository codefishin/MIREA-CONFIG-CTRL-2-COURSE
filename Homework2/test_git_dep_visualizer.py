import unittest
from unittest.mock import patch, MagicMock
import subprocess  # Добавляем импорт
from main import get_commits, generate_dot_code, build_dependency_graph

class TestGitDependencyVisualizer(unittest.TestCase):

    @patch('subprocess.run')
    def test_get_commits(self, mock_run):
        # Настраиваем mock для успешного выполнения команды
        mock_completed_process = subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout="commit1\ncommit2\ncommit3",
            stderr=""
        )
        mock_run.return_value = mock_completed_process

        commits = get_commits("path/to/repo", "v1.0")
        self.assertEqual(commits, ["commit1", "commit2", "commit3"])
        mock_run.assert_called_with(
            ['git', '-C', 'path/to/repo', 'rev-list', '--reverse', 'v1.0'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    @patch('subprocess.run')
    def test_build_dependency_graph(self, mock_run):
        # Настраиваем mock для получения родителей коммитов
        def subprocess_side_effect(cmd, stdout, stderr, text):
            commit_hash = cmd[-1]
            parents_map = {
                "commit1": "",
                "commit2": "commit1",
                "commit3": "commit2"
            }
            stdout_data = parents_map.get(commit_hash, "")
            return subprocess.CompletedProcess(args=cmd, returncode=0, stdout=stdout_data, stderr="")

        mock_run.side_effect = subprocess_side_effect

        commits = ["commit1", "commit2", "commit3"]
        edges = build_dependency_graph("path/to/repo", commits)
        expected_edges = [("commit1", "commit2"), ("commit2", "commit3")]

        # Преобразуем хэши до 7 символов
        expected_edges = [(p[:7], c[:7]) for p, c in expected_edges]
        self.assertEqual(edges, expected_edges)

    def test_generate_dot_code(self):
        commits = ["commit1", "commit2"]
        edges = [("commit1", "commit2")]
        dot_code = generate_dot_code(commits, edges)

        # Проверяем, что сгенерированный код содержит необходимые части
        self.assertIn('rankdir=LR;', dot_code)
        self.assertIn('node [shape=box];', dot_code)
        self.assertIn('"commit1" -> "commit2";', dot_code)

if __name__ == "__main__":
    unittest.main()
