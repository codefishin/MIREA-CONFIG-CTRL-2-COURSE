### Шаг 1 - Клонирование репозитория
Клонируйте репозиторий для запуска программы.
```
git clone <URL>
cd <директория проекта>
```
### Шаг 2 - Вывод
Вывести в виде графа, имея сгенерированный код в формате Graphviz, можно на https://dreampuf.github.io/GraphvizOnline/#
### Шаг 3 - Установка
Установите unittest.
```
pip install unittest
```
### Шаг 4 - Создание виртуального окружения
### Для Windows:
```
python -m venv venv
venv\Scripts\activate
```
### Для MacOS/Linux:
```
python -m venv venv
source venv/bin/activate
```
### Шаг 5 - Vizpath
```
python main.py --vizpath /usr/bin/dot --repopath /path/to/repo --output /path/to/output.dot --tag v1.0
# Пример
```
### Шаг 6 - Тесты
```
python -m unittest test.py
```
Или
```
test.py 
```
![image](https://github.com/user-attachments/assets/8350878a-a7f2-43a9-b048-3eb326a2aa2c)
