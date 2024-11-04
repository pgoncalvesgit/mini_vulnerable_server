FROM python:3.13.0-slim

WORKDIR /app


RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
