### Задание 1
```
git commit
git tag in
git branch first
git branch second
git commit
git checkout first
git commit
git checkout second
git commit
git commit
git checkout first
git commit
git checkout master
git commit
git merge first
git checkout second
git rebase master
git checkout master
git merge second
```
![image](https://github.com/user-attachments/assets/c33bac66-ee23-4bb7-9a92-7011ec11b763)
### Задание 2
```
$ cd /d/conf
$ mkdir local_rep
$ cd local_rep/
$ git init
$ git config user.name "stomp"
$ git config user.email "thisisnotarealemail@email.com"
$ echo "Hello world" > prog.py
$ git add prog.py
$ git status
$ git commit -m "first commit"
```
### Задание 3
```
$ cd /d/conf
$ git init --bare server.git
$ git remotr -v
$ git remote -v
$ git push server master
$ cd ..
$ cd code/
$ git config user.name "stomp"
$ git config user.email "thisisnotarealemail@email.com"
$ echo "Hello world" > readme.md
$ git add readme.md
$ git commit -m "Added readme.md
$ git push origin master
$ cd ../local_rep/
$ git pull server master
$ echo "Hello world2" > readme.md
$ git add readme.md
$ git commit -m "updated info"
$ git push server master
$ cd ../code/
$ git pull origin master
$ echo "Hello world3" > readme.md
$ git add readme.md
$ git commit -m "updated info, resolve conf"
$ git push origin master
```
### Задание 4
```
import subprocess
def list_git_objects():
    objects = subprocess.check_output(['git', 'rev-list', '--objects', '--all']).decode().splitlines()
    for line in objects:
        sha1, *path = line.split()
        print(f"Object SHA-1: {sha1}")
        try:
            content = subprocess.check_output(['git', 'cat-file', '-p', sha1]).decode()
            print(f"Contents of {sha1} ({' '.join(path) if path else 'no path'}):")
            print(content)
            print("-" * 40)
        except subprocess.CalledProcessError as e:
            print(f"Error reading object {sha1}: {e}")
            continue
list_git_objects()
```
