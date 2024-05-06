FROM apache/airflow:2.9.1

COPY requirements.txt /usr/local/tmp/requirements.txt
RUN pip install --no-cache-dir -r /usr/local/tmp/requirements.txt

EXPOSE 8080 5555