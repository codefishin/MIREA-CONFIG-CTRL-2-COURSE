import sys
import os
import subprocess
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Git Dependency Graph Visualizer")
    parser.add_argument('--graphviz_path', required=True, help="Path to the Graphviz dot program")
    parser.add_argument('--repo_path', required=True, help="Path to the Git repository")
    parser.add_argument('--output_file', required=True, help="Path to the output DOT code file")
    parser.add_argument('--tag_name', required=True, help="Name of the tag in the repository")
    return parser.parse_args()

def get_commits(repo_path, tag_name):
    cmd = ['git', '-C', repo_path, 'rev-list', '--reverse', tag_name]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error fetching commits: {result.stderr}")
        sys.exit(1)
    commits = result.stdout.strip().split("\n")
    return commits

def build_dependency_graph(repo_path, commits):
    edges = []
    commit_set = set(commits)
    for commit_hash in commits:
        cmd = ['git', '-C', repo_path, 'log', '--pretty=%P', '-n', '1', commit_hash]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error fetching parents for commit {commit_hash}: {result.stderr}")
            sys.exit(1)
        parents = result.stdout.strip().split()
        for parent_hash in parents:
            if parent_hash in commit_set:
                edges.append((parent_hash[:7], commit_hash[:7]))
    return edges

def generate_dot_code(commits, edges):
    dot = "digraph G {\n"
    dot += "    rankdir=LR;\n"
    dot += "    node [shape=box];\n"
    for commit_hash in commits:
        short_hash = commit_hash[:7]
        dot += f'    "{short_hash}";\n'
    for parent, child in edges:
        dot += f'    "{parent}" -> "{child}";\n'
    dot += "}\n"
    return dot

def main():
    args = parse_args()
    if not os.path.isfile(args.graphviz_path):
        print(f"Graphviz dot program not found at {args.graphviz_path}")
        sys.exit(1)

    if not os.path.isdir(args.repo_path):
        print(f"Repository not found at {args.repo_path}")
        sys.exit(1)

    commits = get_commits(args.repo_path, args.tag_name)
    if not commits:
        print(f"No commits found for tag {args.tag_name}")
        sys.exit(1)

    edges = build_dependency_graph(args.repo_path, commits)
    dot_code = generate_dot_code(commits, edges)

    with open(args.output_file, "w") as f:
        f.write(dot_code)
    print(f"DOT code has been written to {args.output_file}")

if __name__ == "__main__":
    main()
