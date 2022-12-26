From python:3.9.12-slim-bullseye
ENV PYTHONUNBUFFERED 1

RUN python3 --version
RUN pip3 --version

EXPOSE 5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
# CMD python3 main.py