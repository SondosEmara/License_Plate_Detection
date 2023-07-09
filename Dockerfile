FROM python:3.8-slim-buster

WORKDIR /LicensePlate

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./LicensePlate.py" ]
