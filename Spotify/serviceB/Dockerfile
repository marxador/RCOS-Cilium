FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask requests

EXPOSE 5001

CMD ["python", "serviceB.py"]
