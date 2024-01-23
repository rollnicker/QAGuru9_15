# Wishmaster
## Проект по автоматизации тестирования интернет-магазина

<img src="resources/wishmaster_logo.png" width="800" height="200">

### Особенности:
-  Удаленный запуск через Jenkins
-  Отчетность в allure
-  Запись логов, скриншотов и видео
-  Оповещение в Telegram
-  Время выполнения до 3 минут

### Стек проекта:
Python * Pytest * Selene * (Selenium) * Selenoid * Jenkins * Allure Report * Telegram * Intellij (PyCharm)

<p align="left">
<img align="center" src="resources/python-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/pytest-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/selenium-original.svg" width="40" height="40">
<img align="center" src="resources/jenkins-original.svg" width="40" height="40">
<img align="center" src="resources/selenoid-image.jpeg" width="40" height="40">
<img align="center" src="resources/github-original-wordmark.svg" width="40" height="40">
<img align="center" src="resources/allure.png" width="40" height="40">
<img align="center" src="resources/Telegram_logo.webp" width="40" height="40">
<img align="center" src="resources/intellij-original-wordmark.svg" width="40" height="40">
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
<img src="resources/screens/jenkins job.png" width="700" height="500">
1. Нажмите на кнопку "build with parameters" (собрать с параметрами)  
<img src="resources/screens/jenkins parameters.png" width="500" height="300">
2. Выберите версию браузера. Доступна 100 или 99 версия Google Chrome  
Также можно написать комментарий, который будет отправлен в Telegram после окончания сборки
Нажмите build 
<img src="resources/screens/building job.png" width="450" height="250">
3. Когда тест будет пройден, можно посмотреть подрбности в отчете Allure  
Для это нужно нажать на иконку allure отчета <img src="resources/allure.png" width="20" height="20">

#### Структура отчета
<img src="resources/screens/allure report.png" width="550" height="350">

- Можно раскрыть тесты и увидеть подробности сборки  
<img src="resources/screens/allure opened.png" width="800" height="500">
- Можно посмотреть дефекты прогона  
<img src="resources/screens/allure_defect.png" width="800" height="500">
- Можно посмотреть результаты сборки в графиках  
<img src="resources/screens/allure_graph.png" width="800" height="500">
- Можно посмотреть скрины сборки  
<img src="resources/screens/screen_from_allure.png" width="800" height="600">
- Можно посмотреть запись прохождения теста  
<img src="resources/screens/autotest_screenrecord.gif" width="800" height="500">

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

## Telegram: <img src="resources/Telegram_logo.webp" width="20" height="20">  

Возможна интеграция в Telegram, для более удобных оповещений.  

Нужен бот в Telegram @BotFather и чат с правами администратора.  
<img src="resources/screens/botfaher.png" width="290" height="300">

Пример отчета в Telegram   
<img src="resources/screens/telegram.png" width="290" height="300">
