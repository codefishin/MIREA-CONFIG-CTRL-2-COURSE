import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(description='Визуализация графа зависимостей git-коммитов.')
    parser.add_argument('--vizpath', required=True, help='Путь к программе для визуализации графов.')
    parser.add_argument('--repopath', required=True, help='Путь к анализируемому репозиторию.')
    parser.add_argument('--output', required=True, help='Путь к файлу-результату в виде кода.')
    parser.add_argument('--tag', required=True, help='Имя тега в репозитории.')
    return parser.parse_args()


def get_commits(repopath, tag):
    cmd = ['git', 'rev-list', '--reverse', tag]
    result = subprocess.run(cmd, cwd=repopath, stdout=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise Exception(f"Ошибка при получении списка коммитов для тега {tag}")
    commits = result.stdout.strip().split('\n')
    return commits


def build_dependency_graph(repopath, commits):
    graph = {}
    for commit in commits:
        cmd = ['git', 'log', '--pretty=%P', '-n', '1', commit]
        result = subprocess.run(cmd, cwd=repopath, stdout=subprocess.PIPE, text=True)
        parents = result.stdout.strip().split()
        graph[commit] = parents
    return graph


def generate_graphviz_code(graph):
    lines = ['digraph G {']
    for commit, parents in graph.items():
        for parent in parents:
            lines.append(f'    "{parent}" -> "{commit}";')
    lines.append('}')
    return '\n'.join(lines)


def save_output(output_path, code):
    with open(output_path, 'w') as f:
        f.write(code)
def main():
    args = parse_args()
    commits = get_commits(args.repopath, args.tag)
    graph = build_dependency_graph(args.repopath, commits)
    code = generate_graphviz_code(graph)
    print(code)
    save_output(args.output, code)

if __name__ == '__main__':
    main()
