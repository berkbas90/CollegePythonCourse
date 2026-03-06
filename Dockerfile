FROM python:3.14.3-slim-trixie
RUN apt-get update && \
    apt-get install -y \
        net-tools \
        gcc \
        nano \
        curl \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*
COPY . .    
CMD python odev1.py
EXPOSE 8080