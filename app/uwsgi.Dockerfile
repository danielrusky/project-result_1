FROM python:3.8

WORKDIR /usr/app/

# Копируем файл requirements.txt в контейнер и установим python зависимости
COPY requirements.txt ./app_requirements/requirements.txt
RUN pip install --no-cache-dir -r ./app_requirements/requirements.txt
# также библиотеку можно прописать в requirements.txt
RUN pip install uwsgi
# копируем папку src в контейнер
COPY src ./src
# Запускаем Flask приложение через uwsgi
CMD uwsgi --http 0.0.0.0:8000 --wsgi-file ./src/server.py --callable app --processes 2 --master

# cd <project_directory>/app/
# docker build -t fin_project_app_uwsgi -f uwsgi.Dockerfile .
# docker run -p 8000:8000 -it --rm --name fin_project_app_uwsgi fin_project_app_uwsgi