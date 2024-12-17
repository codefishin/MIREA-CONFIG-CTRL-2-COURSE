### Шаг 1 - Клонирование репозитория
Клонируйте репозиторий для запуска программы.
```
cd <INSTALL_PATH>
git clone <REPO_URL>
```
### Шаг 2 - Установка
Установите Graphviz и pytest для работы программы.
# Windows:
```
winget install graphviz
```
# Linux (Ubuntu):
```
sudo apt install graphviz
```
# PYTEST
```
pip install pytest
```
Проект выполнен на Windows, пример запуска программы доступен только на данной оперативной системе.
### Шаг 3 - Создание виртуального окружения
# Для Windows:
```
python -m venv venv
venv\Scripts\activate
```
# Для MacOs/Linux:
```
python -m venv venv
source venv/bin/activate
```
### Шаг 4 - Запуск программы
Производится при помощи вызова main.py в основной папке. Убедитесь что вы установили свой/случайный репозиторий в your_repo (см. в директории your_repo)
```
python main.py --graphviz_path "C:\Program Files\Graphviz\bin\dot.exe" --repo_path "<INSTALL_REPOSITORY_ON_YOUR_SYSTEM>" --output_file "<ANY_.DOT_FILE_ON_YOUR_SYSTEM_WHERE_YOU_WANT_TO_SAVE_DATA>" --tag_name "HEAD"
```
Если вы установили graphviz через ``` winget install graphviz ```, то у вас автоматически установится по директории ``` C:\Program Files\Graphviz\bin\dot.exe ```. 
``` --repo_path ``` требует от вас клонированый репозиторий на вашей системе (Укажите путь на папку с клонированым репозиторием).
``` --output_file ``` требует путь к любому файлу формата .dot (Укажите путь на файл формата .dot).
``` --tag_name ``` лучше оставить как "HEAD".

![image](https://github.com/user-attachments/assets/fdc7c01e-e58b-4545-969a-ab8544257013)

### Шаг 5 - Запуск тестов
```
python test_git_dep_visualizer.py
```
![image](https://github.com/user-attachments/assets/304059b3-0b9a-41cb-ac07-38168dda4696)
