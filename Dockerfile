FROM python:3.6

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt
#CMD ["gunicorn", "--bind", ":8080", "--chdir", "/code", "okd_cronjob_django.wsgi"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
EXPOSE 8080