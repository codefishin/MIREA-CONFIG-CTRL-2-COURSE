### Описание
Преобразует текст из языка json в учебный конфигурационный язык
### Шаг 1 - Клонирование репозитория
Клонируйте репозиторий для запуска программы.
```
git clone <URL>
cd <директория проекта>
```
### Шаг 2 - Установка
Установите unittest.
```
pip install unittest
```
### Шаг 3 - Создание виртуального окружения
### Для Windows
```
python -m venv venv
venv\Scripts\activate
```
### Для MacOS/Linux
```
python -m venv venv
source venv/bin/activate
```
### Шаг 4 - Запуск скрипта
```
python main.py --input input.json
```
### Пример input.json
```
{
    "model": {
        "layers": 5,
        "activation": "relu",
        "optimizer": "adam"
    },
    "learning_rate <-": {
        "expr": ["/", 0.01, 2]
    },
    "configurations": [
        {
            "batch_size": 32,
            "epochs": 10
        },
        {
            "batch_size": 64,
            "epochs": 20
        }
    ]
}
```
### Вывод
![image](https://github.com/user-attachments/assets/2eceb003-7e15-4ba3-bb83-6f55bfda8cb0)
### Шаг 5 - Тесты
Для запуска тестов запустите test.py
```
python test.py
```
![image](https://github.com/user-attachments/assets/84af09bc-c1f3-4aa9-80c7-606bc9efeac1)

