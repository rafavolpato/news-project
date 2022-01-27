FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations api
RUN python manage.py migrate
RUN python manage.py fetch_feed
