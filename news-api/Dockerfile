FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./news-api/ /code/
COPY ./nginx/production.env /code/news-api/config/config.env
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations api
RUN python manage.py migrate
RUN python manage.py fetch_feed
RUN python manage.py collectstatic
