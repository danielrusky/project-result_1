# Прогнозирование цен на недвижимость

## Содержание
1. Описание проекта

2. Какой кейс мы решаем?

3. Обзор данных

4. Этапы проекта

5. Результаты

## Описание проекта
Нам предоставляется набор данных об объектах недвижимости в США. Целями проекта являются:
* Нахождение оптимальных гиперпараметров моделей машинного обучения с помощь фреймворка Optuna.
* Обучение моделей ML с оптимальными гиперпараметрами.
* Контейнеризация обученной модели и создание серверной части для взаимодействия модели с пользователем и обеспечения кросплатформенности.

## Какой кейс мы решаем?
Представитель крупного агентства недвижимости обратился к нам со следующей проблемой:

“Мои риэлторы тратят катастрофическое количество времени на сортировку объявлений и поиск выгодных предложений. Поэтому скорость их реакции и, откровенно говоря, качество анализа не дотягивают до уровня наших конкурентов. Это влияет на наши финансовые показатели.

Ваша задача - разработать модель, которая позволила бы нам превзойти конкурентов с точки зрения скорости и качества транзакций".

Целью проекта является разработка сервиса для прогнозирования стоимости объектов недвижимости на основе истории предложений.

## Обзор данных
Полный набор данных находится [здесь](https://drive.google.com/file/d/1JdahsdHu4N4-Xhe46VAPQFTqFVC7QTov/view?usp=share_link).

Существует 377 185 строк, представляющих различные свойства, и 18 столбцов, описывающих их особенности.

Каждое свойство обладает следующими особенностями:
1. status - статус
2. private pool - частный бассейн
3. propertyType - Тип недвижимости
4. street - улица
5. baths - бани
6. homeFacts - предметы домашнего обихода
7. fireplace - камин
8. city - город
9. schools - школы
10. sqft - кв. футы
11. zipcode - почтовый индекс
12. beds - количество комнат
13. state - штат
14. stories - количество этажей
15. mls-id - код в централизованной системе учёта предложений объектов недвижимости
16. PrivatePool - Бассеин
17. MlsId - код в централизованной системе учёта предложений объектов недвижимости
18. target - цена объекта недвижимости, прогнозируемая стоимость (целевой признак)

## Этапы проекта
Код в ноутбуках выполнялся в Google-colab с использованием соответствующих [библиотек](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/google-requirements.txt). Создание серверной части осуществлялось на локальной IDE с импортом необходимых библиотек из [google-requirements.txt](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/google-requirements.txt)
Проект состоит из следующих частей:

* I. [Обзор проекта](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud-origy/blob/main/Processing_and_baseline.ipynb)
* II. Исследовательский анализ данных - Часть 1
  * Обзор данных
* III. Предварительная обработка данных
  * target
  * status
  * private pool & PrivatePool
  * propertyType
  * street
  * baths
  * homeFacts
    * remodeled year
    * heating
    * cooling
    * parking
    * lotsize
  * fireplace
  * city
  * schools
    * schools rating
    * schools distance
  * sqft
  * beds
  * stories
  * year built
  * price/sq.ft. & lot_size & sqft
* IV. Исследовательский анализ данных - Часть 2
  * Категориальные признаки
* V. Feature Engeneering
  * Удаление выбросов
  * Корреляционная тепловая карта
  * Кодирование категориальных признаков
  * Сокращение количества признаков
  * Нормализация
* VI. Моделирование
  * Показатели оценки
  * Baseline
  * [Linear Regression](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/lr.ipynb)
  * [Light Gradient Boosted Machine Regressor](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Optuna%20-%20LGBMRegressor.ipynb)
  * [Gradient Boosting](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Optuna%20-%20Gradient%20Boosting.ipynb)
  * [Extreme Gradient Boosting](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Optuna%20-%20Extreme%20Gradient%20Boosting.ipynb)
  * [Random Forest](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Optuna%20-%20Random%20Forest.ipynb)
  * [Stacking Regressor](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Stacking%20Regressor.ipynb)
* VII. [Результаты](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/Results%20of%20model%20training.ipynb)
  * Вывод по выбору наилучшей модели.
* VIII. Создание [сервера](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/app/src/server.py) на основе Flask приложения для наилучшей обученной модели.
* IX. [Изоляция Flask приложения в docker контейнере](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/app/flask.Dockerfile).
* X. [Flask приложение + uwsgi сервер в docker контейнере](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/app/uwsgi.Dockerfile).
* XI. Docker-compose. [Flask + uwsgi приложение и nginx в двух разных контейнерах](https://github.com/AleksandrOsip/Final-project-of-the-first-year-of-stud/blob/main/docker-compose.yml)

## Результаты

1. Наилучшие результаты показывает модель регрессора случайного леса. Средняя абсолютная ошибка составила 61852.55 доллара, что довольно много. Средняя абсолютная процентная погрешность составляет 15.26%. Оценка $R^2$ (коэффициент детерминации) показывает относительно хорошие 0.85 (по шкале от -1 до 1).

2. В целом целью проекта была сериализация python объектов и контейнеризация приложений для воспроизводимости кода. Контейнеры [Flask + uwsgi](https://hub.docker.com/repository/docker/inbhktw72/fin_project_app_uwsgi/general) и [nginx](https://hub.docker.com/repository/docker/inbhktw72/fin_nginx_server/general) загружены на DockerHub.

3. Другой целью проекта была демонстрация подбора гиперпараметров для различных моделей с помощью 
платформы оптимизации гиперпараметров Optuna.