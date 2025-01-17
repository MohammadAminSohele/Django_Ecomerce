FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD ali

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn Django==5.1.1 pillow==10.4.0 django_render_partial

CMD python3 manage.py makemigrations --noinput && \
    python3 manage.py migrate --noinput && \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py createsuperuser --user admin --email admin@localhost --noinput; \
    gunicorn -b 0.0.0.0:8000 config.wsgi