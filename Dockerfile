FROM python:3.12.5-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY .env .

EXPOSE 8017

CMD ["python", "app.py"]