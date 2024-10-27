### Задание 1
```
local groups = [
  'ИКБО-%d-20' % i
  for i in std.range(1, 24)
];

local students = [
  { age: 19, group: groups[3], name: 'Иванов И.И.' },
  { age: 18, group: groups[4], name: 'Петров П.П.' },
  { age: 18, group: groups[4], name: 'Сидоров С.С.' },
  { age: 19, group: groups[2], name: 'Толстов А.Э.' },
];

{
  groups: groups,
  students: students,
  subject: 'Конфигурационное управление',
}
```
![image](https://github.com/user-attachments/assets/3fca12eb-482e-4c32-9223-9f1956f3721f)

### Задание 2
```
let generateGroup = λ(i : Natural) → "ИКБО-" ++ Natural/show i ++ "-20"

let numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 ]

let groupList = List/map Natural Text generateGroup numbers

let student1 = { age = 19, group = "ИКБО-4-20", name = "Иванов И.И." }

let student2 = { age = 18, group = "ИКБО-5-20", name = "Петров П.П." }

let student3 = { age = 18, group = "ИКБО-5-20", name = "Сидоров С.С." }

let student4 = { age = 18, group = "ИКБО-6-20", name = "aaa aaa" }

in  { groups = groupList
    , students = [ student1, student2, student3, student4 ]
    , subject = "Конфигурационное управление"
    }
```
### Задание 3
```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
E = E "0" | E "1" | "0" | "1"
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
![image](https://github.com/user-attachments/assets/b947d1e0-fa61-49d3-befc-7cd90119f63e)

### Задание 4
```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
E =  | ( E ) | { E }
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
![image](https://github.com/user-attachments/assets/e70d7c1e-8d4c-4471-b0c5-224c9dbdf164)


### Задание 5
```
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)

BNF = '''
E = E & T | T
T = ~ F | F
F = ( E ) | x | y
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
![image](https://github.com/user-attachments/assets/73f19521-1e02-455b-8d98-a7ed79ac66bb)
