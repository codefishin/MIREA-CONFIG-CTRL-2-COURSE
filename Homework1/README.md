### Шаг 1 - Клонирование репозитория
Клонируйте репозиторий для запуска программы.
```
cd <директория проекта>
git clone <URL>
```
### Шаг 2 - Установка
Установите pytest и toml.
```
pip install pytest
pip install toml
```
### Шаг 3 - Создание виртуальное окружение
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
### Шаг 4 - Структура проекта
Проект содержит следующие файлы:
```
emulator.py # Программа
config.toml # Конфиг
test.py # Тестировщик
virtual_fs.zip # Файловая система
```
### Шаг 5 - Запуск тестов
```
pytest test.py
```
![image](https://github.com/user-attachments/assets/91ef94ed-9d16-4fb6-98bb-139c15e44290)
