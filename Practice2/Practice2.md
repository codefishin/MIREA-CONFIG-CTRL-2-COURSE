## Задание 1
```
pip install matplotlib
pip show matplotlib
```
![image](https://github.com/user-attachments/assets/c42c018b-af4e-46e7-b10c-544310f448f2)
## Задание 2
```
git clone https://github.com/expressjs/express.git
cd express
cat package.json
```
![image](https://github.com/user-attachments/assets/2537af27-478b-4a47-8e24-ac589def9f99)

## Задание 3
```
pip install pipdeptree
pipdeptree --packages matplotlib
```
![image](https://github.com/user-attachments/assets/8d92922a-71f4-45f3-92e6-f20c5b3915bc)
```
digraph G {
    node [shape=box];

    express -> "accepts";
    express -> "body-parser";
    express -> "content-disposition";
    express -> "content-type";
    express -> "cookie";
    express -> "cookie-signature";
    express -> "debug";
    express -> "depd";
    express -> "encodeurl";
    express -> "etag";
    express -> "finalhandler";
    express -> "fresh";
    express -> "http-errors";
    express -> "merge-descriptors";
    express -> "methods";
    express -> "mime-types";
    express -> "on-finished";
    express -> "once";
    express -> "parseurl";
    express -> "qs";
    express -> "range-parser";
    express -> "router";
    express -> "safe-buffer";
    express -> "send";
    express -> "serve-static";
    express -> "setprototypeof";
    express -> "statuses";
    express -> "type-is";
    express -> "utils-merge";
    express -> "vary";
}
```
![image](https://github.com/user-attachments/assets/769e46ed-e46d-4cea-acc5-1dc1e8c21d9c)

```
digraph G {
    node [shape=box];


    matplotlib -> "contourpy" -> "numpy";
    matplotlib -> "cycler";
    matplotlib -> "fonttools";
    matplotlib -> "kiwisolver";
    matplotlib -> "numpy";
    matplotlib -> "packaging";
    matplotlib -> "pillow";
    matplotlib -> "pyparsing";
    matplotlib -> "python-dateutil" -> six;
}
```
![image](https://github.com/user-attachments/assets/c571fd90-fe60-40d9-9da3-463a94375ad5)

## Задание 4
```
include "globals.mzn";  % all_different

% Массив кол-ва 10 и чисел от 0 до 100
array[1..10] of var 0..100: ticket;

% Все различны
constraint all_different(ticket);

% Сумма первых трёх цифр должна быть равна сумме последних трёх цифр
constraint ticket[1] + ticket[2] + ticket[3] = ticket[4] + ticket[5] + ticket[6] + ticket[7] + ticket[8] + ticket[9] + ticket[10];

% Минимизируем сумму трёх цифр (чтобы найти минимальный билет)
var int: sum_3_digits = ticket[1] + ticket[2] + ticket[3];

% Найти минимальную сумму
solve minimize sum_3_digits;
```
![image](https://github.com/user-attachments/assets/b3f437a5-ec17-411d-8c5f-cfd91c0db24b)

## Задание 5
```
enum VersionsMenu = { menu_v1_0_0, menu_v1_1_0, menu_v1_2_0, menu_v1_3_0, menu_v1_4_0, menu_v1_5_0 };
enum VersionsDropdown = { dropdown_v1_8_0, dropdown_v2_0_0, dropdown_v2_1_0, dropdown_v2_2_0, dropdown_v2_3_0 };
enum VersionsIcons = { icons_v1_0_0, icons_v2_0_0 };

var VersionsMenu: menu_version;
var VersionsDropdown: dropdown_version;
var VersionsIcons: icons_version;

constraint
    if menu_version = menu_v1_5_0 then dropdown_version in {dropdown_v2_3_0, dropdown_v2_2_0} /\ icons_version = icons_v2_0_0
    elseif menu_version = menu_v1_4_0 then dropdown_version in {dropdown_v2_2_0, dropdown_v2_1_0} /\ icons_version = icons_v2_0_0
    elseif menu_version = menu_v1_3_0 then dropdown_version in {dropdown_v2_1_0, dropdown_v2_0_0} /\ icons_version = icons_v1_0_0
    elseif menu_version = menu_v1_2_0 then dropdown_version in {dropdown_v2_0_0, dropdown_v1_8_0} /\ icons_version = icons_v1_0_0
    elseif menu_version = menu_v1_1_0 then dropdown_version = dropdown_v1_8_0 /\ icons_version = icons_v1_0_0
    else dropdown_version = dropdown_v1_8_0 /\ icons_version = icons_v1_0_0
    endif;

solve minimize menu_version;
```
![image](https://github.com/user-attachments/assets/e0d1b9b8-ed7a-4317-832a-09a2c1e4a33d)

## Задание 6
```
% Версии для каждого пакета
enum VersionsFoo = { foo_v1_0_0, foo_v1_1_0 };
enum VersionsLeft = { left_v1_0_0 };
enum VersionsRight = { right_v1_0_0 };
enum VersionsShared = { shared_v1_0_0, shared_v2_0_0 };
enum VersionsTarget = { target_v1_0_0, target_v2_0_0 };
enum VersionsRoot = { root_v1_0_0 };

% Переменные
var VersionsFoo: foo_version;
var VersionsLeft: left_version;
var VersionsRight: right_version;
var VersionsShared: shared_version;
var VersionsTarget: target_version;
var VersionsRoot: root_version;

% root от foo и target
constraint
    root_version = root_v1_0_0 /\
    foo_version in {foo_v1_0_0, foo_v1_1_0} /\
    target_version in {target_v2_0_0};

% foo 1.1.0 от left и right
constraint
    if foo_version = foo_v1_1_0 then
        left_version = left_v1_0_0 /\
        right_version = right_v1_0_0
    else
        true
    endif;

% left 1.0.0 от shared >= 1.0.0
constraint
    if left_version = left_v1_0_0 then
        shared_version in {shared_v1_0_0, shared_v2_0_0}
    else
        true
    endif;

% right 1.0.0 от shared < 2.0.0
constraint
    if right_version = right_v1_0_0 then
        shared_version = shared_v1_0_0
    else
        true
    endif;

% shared 1.0.0 от target >= 1.0.0
constraint
    if shared_version = shared_v1_0_0 then
        target_version in {target_v1_0_0, target_v2_0_0}
    else
        true
    endif;

solve satisfy;
```
![image](https://github.com/user-attachments/assets/cdf28f3e-93bf-4211-aa71-d5961661079d)

## Задание 7
```
# Структура данных для хранения пакетов и их зависимостей
packages = {
    'root': {
        '1.0.0': {
            'dependencies': {
                'foo': '^1.0.0',
                'target': '^2.0.0'
            }
        }
    },
    'foo': {
        '1.1.0': {
            'dependencies': {
                'left': '^1.0.0',
                'right': '^1.0.0'
            }
        },
        '1.0.0': {
            'dependencies': {}
        }
    },
    'left': {
        '1.0.0': {
            'dependencies': {
                'shared': '>=1.0.0'
            }
        }
    },
    'right': {
        '1.0.0': {
            'dependencies': {
                'shared': '<2.0.0'
            }
        }
    },
    'shared': {
        '2.0.0': {
            'dependencies': {}
        },
        '1.0.0': {
            'dependencies': {
                'target': '^1.0.0'
            }
        }
    },
    'target': {
        '2.0.0': {
            'dependencies': {}
        },
        '1.0.0': {
            'dependencies': {}
        }
    }
}


# Функция проверки совместимости версии пакетов
def check_dependencies(package, version, resolved, packages):
    # Если пакет уже добавлен в решение, пропускаем
    if package in resolved:
        return True

    # Получаем зависимости для указанной версии
    dependencies = packages[package][version]['dependencies']

    for dep_pkg, dep_version in dependencies.items():
        # Проверка совместимости версии зависимостей
        if not resolve_version(dep_pkg, dep_version, packages, resolved):
            return False

    # Добавляем текущий пакет в решенные
    resolved[package] = version
    return True


# Функция выбора совместимой версии
def resolve_version(package, version_range, packages, resolved):
    # Для простоты обрабатываем только некоторые форматы версий
    if version_range.startswith('^'):
        min_version = version_range[1:]  # Минимальная версия для диапазона "^"
        for version in packages[package]:
            if version >= min_version and package not in resolved:
                if check_dependencies(package, version, resolved, packages):
                    return True
    return False


# Основная функция для решения задачи
def solve(packages):
    resolved = {}
    root_version = '1.0.0'  # Задаем корневую версию
    if check_dependencies('root', root_version, resolved, packages):
        print("Решение найдено:", resolved)
    else:
        print("Решение не найдено")


solve(packages)
```

![image](https://github.com/user-attachments/assets/6935b951-1ad0-48e7-a104-8db6437e39e1)

