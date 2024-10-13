### Задание 2
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
```
### Задание 5
```
```
