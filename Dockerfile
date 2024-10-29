FROM python:3.11.5-slim

RUN pip install pipenv

WORKDIR /app                                                                

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["webapp.py", "model1.bin", "dv.bin", "./"]

EXPOSE 5555

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5555", "webapp:app"]
