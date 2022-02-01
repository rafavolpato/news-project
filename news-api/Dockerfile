FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
COPY ./config/production.env /code/config/.env
RUN pip install -r requirements.txt
RUN python manage.py makemigrations api
RUN python manage.py migrate
#RUN python manage.py fetch_feed
#RUN python manage.py collectstatic

#RUN gunicorn  --certfile=/etc/certs/localhost.crt --keyfile=/etc/certs/localhost.key news_project.wsgi:application --bind 0.0.0.0:443

#EXPOSE 8000