import pytest
import toml
from emulator import ShellEmulator

def emulator():
    config = toml.loads("""username = "A"
    hostname = "B"
    vfs_path = "virtual_fs.zip"
    """)
    return ShellEmulator(config)

# ls start
def test_error_ls(capsys):
    e = emulator()
    e.ls("a")
    captured = capsys.readouterr()
    assert "ls: cannot access 'a': No such file or directory\n" in captured.out

def test_ls_no_input(capsys):
    e = emulator()
    e.ls("")
    captured = capsys.readouterr()
    assert "secret.txt\ntask.txt\nhello\n" in captured.out

def test_ls_input(capsys):
    e = emulator()
    e.ls("hello")
    captured = capsys.readouterr()
    assert "buried.txt\n" in captured.out
# ls end

# cd start
def test_cd(capsys):
    e = emulator()
    e.cd("")
    captured = capsys.readouterr()
    assert "" in captured.out

def test_cd_hello(capsys):
    e = emulator()
    e.cd("hello")
    e.pwd()
    captured = capsys.readouterr()
    assert "hello\n" in captured.out
def test_cd_hello_no_action(capsys):
    e = emulator()
    e.cd("hello")
    captured = capsys.readouterr()
    assert "" in captured.out
# cd end

# pwd start
def test_pwd(capsys):
    e = emulator()
    e.pwd()
    captured = capsys.readouterr()
    assert "/\n" in captured.out

def test_pwd_with(capsys):
    e = emulator()
    e.cd("hello")
    e.pwd()
    captured = capsys.readouterr()
    assert "hello\n" in captured.out
def test_pwd_back_and_forth(capsys):
    e = emulator()
    e.cd("hello")
    e.pwd()
    e.cd("/")
    captured = capsys.readouterr()
    assert "/\n" in captured.out
# pwd end

def test_setup(capsys):
    e = emulator()
    e.printEnum()
    captured = capsys.readouterr()
    assert "A B virtual_fs.zip" in captured.out
