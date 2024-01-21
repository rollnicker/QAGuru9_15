# Wishmaster
## Проект по автоматизации тестирования интернет-магазина

<img src="readme_files/wishmaster_logo.png" width="800" height="150">

### Особенности:
-  Удаленный запуск через Jenkins
-  Отчетность в allure
-  Запись логов, скриншотов и видео
-  Оповещение в Telegram
-  Время выполнения до 3 минут

### Стек проекта:
Python * Pytest * Selene * (Selenium) * Selenoid * Jenkins * Allure Report * Telegram * Intellij (PyCharm)

<p align="left">
<img align="center" src="readme_files/python-original-wordmark.svg" width="40" height="40">
<img align="center" src="readme_files/pytest-original-wordmark.svg" width="40" height="40">
<img align="center" src="readme_files/selenium-original.svg" width="40" height="40">
<img align="center" src="readme_files/jenkins-original.svg" width="40" height="40">
<img align="center" src="readme_files/selenoid-image.jpeg" width="40" height="40">
<img align="center" src="readme_files/github-original-wordmark.svg" width="40" height="40">
<img align="center" src="readme_files/allure.png" width="40" height="40">
<img align="center" src="readme_files/Telegram_logo.webp" width="40" height="40">
<img align="center" src="readme_files/intellij-original-wordmark.svg" width="40" height="40">
</p>

### Какие проверки реализованы в тестах:
1. Функционал корзины:
   1. Добавление в корзину через каталог 
   2. Добавление в корзину через поиск 
   3. Добавление в корзину через каталог моделей в поиске 
   4. Проверка пустой корзины и очистка
2. Добавление в изрбранное:
   1. Через страницу товара
3. Выбор города:
   1. Проверка отображения выбранного города
- --
#### План развития:
- Авторизация
- Больше сценариев добавления избранное
- Рефакторинг, добавление steps
- Номер сборки в уведомлениях
#### Известные дефекты:
- товары не добавляются в избранное, если кликать на иконку сердечка на странице выбора модели через поиск

## Запуск проекта:
### Через Jenkins
Ссылка на [Job]("https://jenkins.autotests.cloud/job/Rolnik_QA_Guru_9_15/")  
<img src="readme_files/screens/jenkins job.png" width="400" height="200">
1. Нажмите на кнопку "build with parameters" (собрать с параметрами)
<img src="readme_files/screens/jenkins parameters.png" width="200" height="100">
2. Выберите версию браузера. Доступна 100 или 99 версия Google Chrome  
Также можно написать комментарий, который будет отправлен в Telegram после окончания сборки
Нажмите build 
<img src="readme_files/screens/building job.png" width="200" height="100">
3. Когда тест будет пройден, можно посмотреть подрбности в отчете Allure  
Для это нужно нажать на иконку allure отчета <img src="readme_files/allure.png" width="20" height="20">

#### Структура отчета
<img src="readme_files/screens/allure report.png" width="550" height="300">

- Можно раскрыть тесты и увидеть подробности сборки  
<img src="readme_files/screens/allure opened.png" width="550" height="300">
- Можно посмотреть дефекты прогона  
<img src="readme_files/screens/allure_defect.png" width="550" height="300">
- Можно посмотреть результаты сборки в графиках  
<img src="readme_files/screens/allure_graph.png" width="550" height="300">
- Можно посмотреть скрины сборки  
<img src="readme_files/screens/screen_from_allure.png" width="550" height="300">
- Можно посмотреть запись прохождения теста  
<img src="readme_files/screens/autotest_screenrecord.gif" width="550" height="300">

### Локально

1. Клонируйте репозиторий на свой компьютер при помощи git clone
  ```zsh
git clone
  ```
2. Создайте и активируйте виртуальное окружение
  ```zsh
  python -m venv .venv
  source venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```zsh
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команду 
  ```zsh
  pytest tests
  ```
5. Для получения allure отчета
  ```zsh
  allure serve allure-results
  ``` 

## Telegram: <img src="readme_files/Telegram_logo.webp" width="20" height="20">  

Возможна интеграция в Telegram, для более удобных оповещений.  

Нужен бот в Telegram @BotFather и чат с правами администратора. 
<img src="readme_files/screens/botfaher.png" width="100" height="100">

Пример отчета в Telegram 
<img src="readme_files/screens/telegram.png" width="100" height="100">
