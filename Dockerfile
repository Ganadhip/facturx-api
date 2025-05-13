FROM python:3.11-slim

# Installer git + dépendances système nécessaires à factur-x
RUN apt-get update && apt-get install -y \
    git \
    libxml2-dev \
    libxslt1-dev \
    gcc \
    g++ && \
    apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
