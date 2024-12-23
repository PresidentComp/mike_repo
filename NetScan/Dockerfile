FROM python:3.12
RUN apt-get update && apt-get install iputils-ping -y
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ADD NetScan.py .
ENTRYPOINT ["python3", "NetScan.py", "task"]
