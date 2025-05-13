FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git gcc g++ libxml2-dev libxslt1-dev && apt-get clean

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
