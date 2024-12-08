import unittest
from unittest.mock import patch, MagicMock
import subprocess
import main
class TestDependencyVisualizer(unittest.TestCase):
    @patch('subprocess.run')
    def test_get_commits(self, mock_run):
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = 'commit1\ncommit2\ncommit3\n'
        mock_run.return_value = mock_result

        commits = main.get_commits('/path/to/repo', 'v1.0')
        self.assertEqual(commits, ['commit1', 'commit2', 'commit3'])
        mock_run.assert_called_with(['git', 'rev-list', '--reverse', 'v1.0'], cwd='/path/to/repo', stdout=subprocess.PIPE, text=True)

    @patch('subprocess.run')
    def test_build_dependency_graph(self, mock_run):
        def side_effect(cmd, cwd, stdout, text):
            commit = cmd[-1]
            mock_result = MagicMock()
            if commit == 'commit1':
                mock_result.stdout = ''
            elif commit == 'commit2':
                mock_result.stdout = 'commit1'
            elif commit == 'commit3':
                mock_result.stdout = 'commit2'
            mock_result.returncode = 0
            return mock_result

        mock_run.side_effect = side_effect

        commits = ['commit1', 'commit2', 'commit3']
        graph = main.build_dependency_graph('/path/to/repo', commits)
        expected_graph = {
            'commit1': [],
            'commit2': ['commit1'],
            'commit3': ['commit2']
        }
        self.assertEqual(graph, expected_graph)

    def test_generate_graphviz_code(self):
        graph = {
            'commit1': [''],
            'commit2': ['commit1'],
            'commit3': ['commit2']
        }
        code = main.generate_graphviz_code(graph)
        expected_code = '''digraph G {
    "" -> "commit1";
    "commit1" -> "commit2";
    "commit2" -> "commit3";
}'''
        self.assertEqual(code.strip(), expected_code.strip())

    @patch('builtins.open')
    def test_save_output(self, mock_open):
        code = 'digraph G {}'
        main.save_output('/path/to/output.dot', code)
        mock_open.assert_called_with('/path/to/output.dot', 'w')

    def test_parse_args(self):
        test_args = ['--vizpath', '/path/to/viz', '--repopath', '/path/to/repo', '--output', '/path/to/output.dot', '--tag', 'v1.0']
        with patch('sys.argv', ['script.py'] + test_args):
            args = main.parse_args()
            self.assertEqual(args.vizpath, '/path/to/viz')
            self.assertEqual(args.repopath, '/path/to/repo')
            self.assertEqual(args.output, '/path/to/output.dot')
            self.assertEqual(args.tag, 'v1.0')

if __name__ == '__main__':
    unittest.main()
