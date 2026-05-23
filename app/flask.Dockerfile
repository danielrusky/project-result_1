FROM python:3.8

WORKDIR /usr/app/

# Копируем файл requirements.txt в контейнер и установим python зависимости
COPY requirements.txt ./app_requirements/requirements.txt
RUN pip install --no-cache-dir -r ./app_requirements/requirements.txt
# Копируем папку src в контейнер
COPY src ./src
# Запускаем Flask приложение напрямую (запускаем скрипт server.py)
CMD python ./src/server.py

# cd <project_directory>/app/
# docker build -t fin_project__app -f flask.Dockerfile .
# docker run -p 8000:8000 -it --rm --name fin_project__app fin_project__app