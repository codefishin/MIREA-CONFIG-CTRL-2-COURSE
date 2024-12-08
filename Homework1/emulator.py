import os
import sys
import zipfile
import toml

class ShellEmulator:
    def __init__(self, config):
        self.username = config['username']
        self.hostname = config['hostname']
        self.vfs_path = config['vfs_path']
        self.history = []
        self.current_path = '/'
        self.zip_file = zipfile.ZipFile(self.vfs_path, 'r')
        self.file_structure = self._build_file_structure()

    def _build_file_structure(self):
        file_structure = {}
        for file_info in self.zip_file.infolist():
            path = '/' + file_info.filename
            parts = path.strip('/').split('/')
            cur = file_structure
            for part in parts:
                cur = cur.setdefault(part, {})
        return file_structure

    def printEnum(self):
        print(self.username, self.hostname, self.vfs_path)

    def run(self):
        while True:
            try:
                command = input(f"{self.username}@{self.hostname}:{self.current_path}$ ")
                self.history.append(command)
                if command.strip() == '':
                    continue
                parts = command.strip().split()
                cmd = parts[0]
                args = parts[1:]

                if cmd == 'exit':
                    self.exit()
                elif cmd == 'ls':
                    self.ls(args)
                elif cmd == 'cd':
                    self.cd(args)
                elif cmd == 'pwd':
                    self.pwd()
                elif cmd == 'history':
                    self.show_history()
                else:
                    print(f"{cmd}: command not found")
            except EOFError:
                self.exit()

    def exit(self):
        print("Exiting...")
        sys.exit(0)

    def ls(self, args):
        directory = self._get_directory(args)
        if directory:
            for name in directory.keys():
                print(name)
        else:
            print(f"ls: cannot access '{args}': No such file or directory")

    def cd(self, args):
        if not args:
            path = '/'
        else:
            path = self._resolve_path(args[0])
            path = path.replace('\\', '')
        if self._get_directory(path):
            self.current_path = path
        else:
            print(f"cd: no such file or directory: {args}")

    def pwd(self):
        print(self.current_path)

    def show_history(self):
        for idx, cmd in enumerate(self.history, 1):
            print(f"{idx}  {cmd}")

    def _resolve_path(self, path):
        if path.startswith('/'):
            return os.path.normpath(path)
        else:
            return os.path.normpath(os.path.join(self.current_path, path))

    def _get_directory(self, path):
        parts = path.strip('/').split('/')
        cur = self.file_structure
        for part in parts:
            if part == '':
                continue
            if part in cur:
                cur = cur[part]
            else:
                return None
        return cur

if __name__ == "__main__":
    config_path = 'config.toml'
    with open(config_path, 'r') as f:
        config = toml.load(f)
    emulator = ShellEmulator(config)
    emulator.run()
